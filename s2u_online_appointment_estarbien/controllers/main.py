# -*- coding: utf-8 -*-

from odoo.addons.s2u_online_appointment.controllers.main import OnlineAppointment
from odoo.addons.s2u_online_appointment.helpers import functions

from odoo import api, fields, models, _, SUPERUSER_ID
from odoo import http, modules, tools
from odoo.http import request

import pytz
from pytz import timezone
import datetime

DEFAULT_TIMEZONE = 'America/Lima'

class OnlineAppointmentCustom(OnlineAppointment) :
    def prepare_values(self, form_data=False, default_appointee_id=False, criteria='default', default_appointment_option_id=False):
        values = super(OnlineAppointmentCustom, self).prepare_values(form_data, default_appointee_id, criteria)
        values.update({'external_appointment_option_id': False})
        if not form_data :
            try :
                default_appointment_option_id = int(default_appointment_option_id)
            except :
                default_appointment_option_id = False
            if default_appointment_option_id and default_appointment_option_id in values['appointment_options'].ids :
                values['appointment_option_id'] = default_appointment_option_id
                values['external_appointment_option_id'] = True
        return values
    
    @http.route()
    def online_appointment(self, **kw) :
        #res = super(OnlineAppointmentCustom, self).online_appointment(kw)
        if request.env.user._is_public() :
            param = request.env['ir.config_parameter'].sudo().search([('key', '=', 's2u_online_appointment')], limit=1)
            if not param or param.value.lower() != 'public' :
                return request.render('s2u_online_appointment.only_registered_users')
        
        param = kw.get('appointment_option', False)
        values = self.prepare_values(default_appointee_id=kw.get('appointee', False), default_appointment_option_id=param)
        
        return request.render('s2u_online_appointment.make_appointment', values)
    
    @http.route()
    def online_appointment_confirm(self, **post) :
        error = {}
        error_message = []
        
        if request.env.user._is_public() :
            param = request.env['ir.config_parameter'].sudo().search([('key', '=', 's2u_online_appointment')], limit=1)
            if not param or param.value.lower() != 'public' :
                return request.render('s2u_online_appointment.only_registered_users')
            if not post.get('name', False) :
                error['name'] = True
                error_message.append(_('Please enter your name.'))
            if not post.get('email', False) :
                error['email'] = True
                error_message.append(_('Please enter your email address.'))
            elif not functions.valid_email(post.get('email', '')) :
                error['email'] = True
                error_message.append(_('Please enter a valid email address.'))
            if not post.get('phone', False) :
                error['phone'] = True
                error_message.append(_('Please enter your phone number.'))
        
        try :
            appointee_id = int(post.get('appointee_id', 0))
        except :
            appointee_id = 0
        if not appointee_id :
            error['appointee_id'] = True
            error_message.append(_('Please select a valid appointee.'))
        
        option = request.env['s2u.appointment.option'].sudo().search([('id', '=', int(post.get('appointment_option_id', 0)))])
        if not option :
            error['appointment_option_id'] = True
            error_message.append(_('Please select a valid subject.'))
        
        slot = request.env['s2u.appointment.slot'].sudo().search([('id', '=', int(post.get('timeslot_id', 0)))])
        if not slot :
            error['timeslot_id'] = True
            error_message.append(_('Please select a valid timeslot.'))
        
        try :
            date_start = datetime.datetime.strptime(post['appointment_date'], '%d/%m/%Y').strftime('%Y-%m-%d')
            day_slot = date_start + ' ' + functions.float_to_time(slot.slot)
            start_datetime = self.ld_to_utc(day_slot, appointee_id)
        except :
            error['appointment_date'] = True
            error_message.append(_('Please select a valid date.'))
        
        values = self.prepare_values(form_data=post)
        if error_message :
            values['error'] = error
            values['error_message'] = error_message
            return request.render('s2u_online_appointment.make_appointment', values)
        
        if not self.check_slot_is_possible(option.id, post['appointment_date'], appointee_id, slot.id) :
            values['error'] = {'timeslot_id': True}
            values['error_message'] = [_('Slot is already occupied, please choose another slot.')]
            return request.render('s2u_online_appointment.make_appointment', values)
        
        appointee_partner_id = self.appointee_id_to_partner_id(appointee_id)
        partner = request.env.user.partner_id
        if request.env.user._is_public() :
            partner = request.env['res.partner'].sudo().search(['|', ('phone','ilike',values['phone']), ('email','ilike',values['email'])])
            if not partner :
                partner = request.env['res.partner'].sudo().create({'name': values['name'],
                                                                    'phone': values['phone'],
                                                                    'email': values['email']})
        partner_ids = [appointee_partner_id, partner[0].id]
        
        appointment = {'name': option.name,
                       'description': post.get('remarks', ''),
                       'start': start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                       'stop': (start_datetime + datetime.timedelta(minutes=round(option.duration * 60))).strftime("%Y-%m-%d %H:%M:%S"),
                       'duration': option.duration,
                       'categ_ids': [(6, 0, request.env.ref('s2u_online_appointment_extra.calendar_event_type_s2u_online_appointment').ids)],
                       'partner_ids': [(6, 0, partner_ids)]}
        # set detaching = True, we do not want to send a mail to the attendees
        appointment = request.env['calendar.event'].sudo().with_context(detaching=True).create(appointment)
        # set all attendees on 'accepted'
        appointment.attendee_ids.write({'state': 'accepted'})
        
        ##inherited automated action for telemedicine
        #venta = [('partner_id','in',partner_ids), ('state','in',['sale']), ('order_line.product_id.website_published','=',True)]
        #venta = request.env['sale.order'].sudo().search(venta, limit=1, order='create_date desc')
        #if venta and not request.env['sinerkia_jitsi_meet.jitsi_meet'].sudo().search([('order_id','=',venta.id)]) :
        #    local_start_datetime = start_datetime.astimezone(timezone(request.env.user.tz or DEFAULT_TIMEZONE))
        #    #partners = request.env['res.partner'].sudo().search([('id', 'in', partner_ids)])
        #    jitsi = {'name': 'Reunión del paciente ' + partner[0].name + ' el ' + local_start_datetime.strftime('%d/%m/%Y') + ' a las ' + local_start_datetime.strftime('%H:%M:%S'),
        #             'date': start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        #             'date_delay': option.duration,
        #             'external_participants': [(0,0,{'name': partner[0].email})],
        #             'event_id': appointment.id,
        #             'order_id': venta.id}
        #    jitsi = request.env['sinerkia_jitsi_meet.jitsi_meet'].sudo().create(jitsi)
        #    patient = request.env['medical.patient'].sudo().search([('id','=',partner[0].id)])
        #    if not patient :
        #        patient = request.env['medical.patient'].sudo().create({'patient_id': partner[0].id})
        #    doctor = request.env['medical.physician'].sudo().search([('partner_id','=',appointee_partner_id)],limit=1)
        #    if not doctor :
        #        doctor = request.env['medical.physician'].sudo().create({'partner_id': appointee_partner_id})
        #    cita = {'patient_id': patient.id,
        #            'doctor_id': doctor.id,
        #            'appointment_date': start_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        #            'appointment_end': (start_datetime + datetime.timedelta(minutes=round(option.duration * 60))).strftime("%Y-%m-%d %H:%M:%S"),
        #            'duration': option.duration * 60,
        #            'no_invoice': True,
        #            'consultations_id': venta.order_line[0].product_id.id}
        #    cita = request.env['medical.appointment'].create(cita)
        
        # registered user, we want something to show in his portal
        if not request.env.user._is_public() :
            registration = {'partner_id': request.env.user.partner_id.id,
                            'appointee_id': self.appointee_id_to_partner_id(appointee_id),
                            'event_id': appointment.id}
            registration = request.env['s2u.appointment.registration'].create(registration)
        
        return request.redirect('/online-appointment/appointment-scheduled?appointment=%d' % appointment.id)
