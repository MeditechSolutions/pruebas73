# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, Warning

class ProjectTask(models.Model) :
    _inherit = 'project.task'
    
    paciente_id = fields.Many2one(comodel_name='res.partner', string='Paciente', track_visibility='onchange')
    cita_id = fields.Many2one(comodel_name='medicina.cita', string='Cita', track_visibility='onchange')
    estacion_ids = fields.Many2many(related='sale_line_id.product_id.protocolo_id.estacion_ids', string='Estaciones', store=True, readonly=False, domain=[('estacion_estarbien','=',True)])
    tipo_cita = fields.Char(related='stage_id.codigo_estarbien', string='Tipo de cita')
    
    def write(self, values) :
        if not self.parent_id and not values.get('parent_id') :
            if values.get('paciente_id') is not None :
                valor = []
                if self.paciente_id :
                    if self.paciente_id.id != values.get('paciente_id') :
                        seguidor = self.message_follower_ids.filtered(lambda r: r.partner_id in self.paciente_id)
                        if seguidor :
                            valor.extend([(2, int(segui.id), 0) for segui in seguidor])
                if values.get('paciente_id') :
                    valor.append((0, 0, {'res_model': 'project.task', 'res_id': self.id, 'partner_id': values.get('paciente_id')}))
                if valor :
                    values.update({'message_follower_ids': valor})
                if self.subtask_count == 0 and self.sale_line_id.product_id.protocolo_id.estacion_ids and 'covid' not in self.sale_line_id.product_id.protocolo_id.estacion_ids.mapped('codigo_estarbien') :
                    valor = self.sale_line_id._timesheet_create_task_prepare_values(self.project_id)
                    valor.update({'parent_id': self.id})
                    del valor['sale_line_id']
                    for elemento in self.sale_line_id.product_id.protocolo_id.estacion_ids :
                        especial = dict(valor)
                        especial.update({'stage_id': elemento.id})
                        task = self.env['project.task'].sudo().create(especial)
        res = super(ProjectTask, self).sudo().write(values)
        return res

class ProjectTaskType(models.Model) :
    _inherit = 'project.task.type'
    
    estacion_estarbien = fields.Boolean(string='Estación')
    codigo_estarbien = fields.Char(string='Código Estarbien')
