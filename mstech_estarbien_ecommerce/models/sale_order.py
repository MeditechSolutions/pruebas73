# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, Warning

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    def _timesheet_service_generation(self):
        """ For service lines, create the task or the project. If already exists, it simply links
            the existing one to the line.
            Note: If the SO was confirmed, cancelled, set to draft then confirmed, avoid creating a
            new project/task. This explains the searches on 'sale_line_id' on project/task. This also
            implied if so line of generated task has been modified, we may regenerate it.
        """
        super(SaleOrderLine, self)._timesheet_service_generation()
        so_line_estarbien = self.filtered(lambda sol: sol.is_service and sol.product_id.service_tracking == 'no')
        
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
    
    @api.model_create_multi
    def create(self, vals_list):
        #raise UserError(_(str(vals_list)))
        copiado = False
        if isinstance(vals_list, list) :
            copiado = vals_list[:]
            copia_list = vals_list[:]
            i = 0
            for vals in vals_list :
                if vals.get('product_uom_qty', 0) > 1 :
                    producto = self.env['product.template'].browse(vals['product_template_id'])
                    if producto.type == 'service' and producto.service_tracking == 'no' :
                        copia_list[i]['product_uom_qty'] = 1
                        copia_list.extend([copia_list[i]]*(vals.get('product_uom_qty', 0)-1))
                i = i + 1
            vals_list = copia_list[:]
        else :
            copiado = dict(vals_list)
            copia = [vals_list]
            if vals_list.get('product_uom_qty', 0) > 1 :
                producto = self.env['product.template'].browse(vals_list['product_template_id'])
                if producto.type == 'service' and producto.service_tracking == 'no' :
                    copia[0]['product_uom_qty'] = 1
                    copia.extend([copia[0]]*(vals_list.get('product_uom_qty', 0)-1))
            vals_list = len(copia)==1 and copia[0] or copia
        raise UserError(_(str(vals_list) + '\n---------------------------------\n' + str(copiado)))
        return super(SaleOrderLine, self).create(vals_list)
    #################################################
