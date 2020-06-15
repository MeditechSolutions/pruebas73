# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, Warning

class ProjectTask(models.Model) :
    _inherit = 'project.task'
    
    paciente_id = fields.Many2one(comodel_name='res.partner', string='Paciente')
