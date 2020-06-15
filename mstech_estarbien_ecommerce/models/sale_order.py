# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, Warning

class SaleOrder(models.Model) :
    _inherit = 'sale.order'
    
    def _action_confirm(self) :
        """ On SO confirmation, some lines should generate a task or a project. """
        for record in self.order_line.filtered(lambda sol: sol.is_service and sol.product_id.service_tracking == 'estarbien' and sol.product_uom_qty > 1) :
            cantidad = record.product_uom_qty - 1
            while cantidad > 0 :
                linea = record.copy({'order_id': record.order_id.id})
                linea.product_uom_qty = 1
                cantidad = cantidad - 1
            record.product_uom_qty = 1
        result = super(SaleOrder, self)._action_confirm()
        return result

class SaleOrderLine(models.Model) :
    _inherit = 'sale.order.line'
    
    def _timesheet_service_generation(self):
        """ For service lines, create the task or the project. If already exists, it simply links
            the existing one to the line.
            Note: If the SO was confirmed, cancelled, set to draft then confirmed, avoid creating a
            new project/task. This explains the searches on 'sale_line_id' on project/task. This also
            implied if so line of generated task has been modified, we may regenerate it.
        """
        super(SaleOrderLine, self)._timesheet_service_generation()
        so_line_estarbien = self.filtered(lambda sol: sol.is_service and sol.product_id.service_tracking == 'estarbien')
        
        usuario = self.env.user
        project = self.env['project.project'].sudo().search([('user_id','=',usuario.id)], order='create_date desc', limit=1)
        for so_line in so_line_estarbien :
            if not project :
                if not so_line.project_id :
                    project = so_line._timesheet_create_project()
                    project.sudo().write({'user_id': usuario.id, 'sale_line_id': False, 'sale_order_id': False, 'name': so_line.order_id.partner_id.display_name})
                else :
                    project = so_line.project_id
            elif (not so_line.project_id) or so_line.project_id != project :
                so_line.project_id = project
            if not so_line.task_id :
                so_line._timesheet_create_task(project=project)
            # Portal for the client
            if so_line.order_id.partner_id not in so_line.task_id.message_follower_ids.partner_id :
                so_line.task_id.write({'message_follower_ids': [(0, 0, {'res_id':so_line.task_id.id,'res_model':'project.task', 'partner_id':so_line.order_id.partner_id.id})]})
