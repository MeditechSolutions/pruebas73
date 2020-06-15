# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, Warning

class ProjectTask(models.Model) :
    _inherit = 'project.task'
    
    paciente_id = fields.Many2one(comodel_name='res.partner', string='Paciente', track_visibility='onchange')
    
    def write(self, values) :
        if values.get('paciente_id') is not None :
            valor = []
            if self.paciente_id :
                if self.paciente_id.id != values.get('paciente_id') :
                    seguidor = self.message_follower_ids.filtered(lambda r: r.partner_id == self.paciente_id)
                    if seguidor :
                        valor.append((2, int(seguidor.id), 0))
            if values.get('paciente_id') :
                valor.append((0, 0, {'res_model': 'project.task', 'res_id': self.id, 'partner_id': values.get('paciente_id')}))
            if valor :
                values.update({'message_follower_ids': valor})
        res = super(ProjectTask, self).write(values)
        return res
