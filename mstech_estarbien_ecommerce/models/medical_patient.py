# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, Warning

class MedicalPatientProtocolo(models.Model) :
    _name = 'medical.patient.protocolo'
    _description = 'Protocolo de atención'
    
    name = fields.Char(string='Protocolo')
    estacion_ids = fields.Many2many(comodel_name='project.task.type', string='Estaciones', domain=[('estacion_estarbien','=',True)])

class medical_patient(models.Model) :
    _inherit = 'medical.patient'
    
    protocolo_id = fields.Many2one(comodel_name='medical.patient.protocolo',string='Perfil')
