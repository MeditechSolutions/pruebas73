# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class MedicinaFiliacion(models.Model) :
    _name = 'medicina.filiacion'
    _description = 'Filiación'
    
    paciente_id = fields.Many2one(comodel_name='''medical.patient''', string='''Paciente''')
    paciente_empresa_id = fields.Many2one(comodel_name='''res.partner''', string='''Empresa''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    paciente_perfil_id = fields.Many2one(comodel_name='''medicina.paciente.perfil''', string='''Protocolo''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    
    @api.depends('paciente_id')
    def _compute_paciente_datos(self):
        for record in self :
            record.paciente_empresa_id = record.paciente_id.partner_address_id
            record.paciente_perfil_id = record.paciente_id.perfil_id
    
    fecha_cita = fields.Date(string='''Fecha de atención''')
    tipo_cita = fields.Selection(string='''Tipo''',selection=[("diagnostico","Diagnóstico"),
                                                              ("triaje","Triaje"),
                                                              ("antecedentes_personales","Antecedentes Personales"),
                                                              ("historia_ocupacional","Historia Ocupacional"),
                                                              ("medicina","Medicina general"),
                                                              ("dermatologia","Dermatología"),
                                                              ("grandes_alturas","Anexo N°16 A"),
                                                              ("altura","Certificación de trabajo en altura"),
                                                              ("confinados","Trabajo en espacios confinados"),
                                                              ("electrocardiograma","Electrocardiograma"),
                                                              ("oftalmologia","Oftalmología"),
                                                              ("audiometria","Audiometría"),
                                                              ("psicologia","Psicología"),
                                                              ("odontograma","Odontograma"),
                                                              ("musculo_esqueletico","Músculo Esquelético"),
                                                              ("radiologia","Radiología"),
                                                              ("espirometria","Espirometría"),
                                                              ("tsr","Test de Sintomático Respiratorio"),
                                                              ("laboratorio","Laboratorio"),
                                                              ("consentimiento","Consentimiento"),
                                                              ("interconsultas","Interconsultas"),
                                                              ("encuesta","Encuesta")])
    atencion_inicio = fields.Datetime(string='''Inicio de la atención''')
    atencion_fin = fields.Datetime(string='''Fin de la atención''')
    
    #paciente_apellidos_nombres = fields.Char(string='''Apellidos y nombres''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    #paciente_cargo = fields.Char(string='''Cargo''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    #paciente_dni = fields.Char(string='''DNI''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    #paciente_edad = fields.Char(string='''Edad''', compute='''_compute_paciente_datos''', store=True, readonly=True)
    #paciente_sexo = fields.Selection(string='''Sexo''',selection='''[('m', 'Male'), ('f', 'Female')]''', compute='''_compute_paciente_datos''', store=True, readonly=True)

    auditado = fields.Boolean(string='''Auditado''')
    auditor = fields.Many2one(comodel_name='''res.partner''', string='''Auditor''')
    responsable = fields.Many2one(comodel_name='''res.partner''', string='''Responsable''')
    revisado = fields.Boolean(string='''Revisado''')
    medico = fields.Many2one(comodel_name='''res.partner''', string='''Médico''')
    evaluador = fields.Many2one(comodel_name='''res.partner''', string='''Evaluador''')
    
    diagnostico_ids = fields.One2many(comodel_name='''medicina.cita.diagnostico''', inverse_name='''cita_id''', string='''Diagnóstico''', domain=[('tipo_diagnostico_oido','=','bilateral')])
    diagnostico_oido_derecho_ids = fields.One2many(comodel_name='''medicina.cita.diagnostico''', inverse_name='''cita_id''', string='''Diagnóstico del oido derecho''', domain=[('tipo_diagnostico_oido','=','derecho')])
    diagnostico_oido_izquierdo_ids = fields.One2many(comodel_name='''medicina.cita.diagnostico''', inverse_name='''cita_id''', string='''Diagnóstico del oido izquierdo''', domain=[('tipo_diagnostico_oido','=','izquierdo')])
    historial_paciente = fields.Many2many(comodel_name='''medicina.cita''', relation='''medicina_filiacion_medicina_cita_rel''', column1='''filiacion_id''', column2='''cita_id''', string='''Historial del paciente''')
    
    name = fields.Char(string='''Filiación''')
