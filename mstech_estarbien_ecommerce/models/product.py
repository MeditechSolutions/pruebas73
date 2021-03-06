# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError, Warning

class ProductTemplateProtocolo(models.Model) :
    _name = 'product.template.protocolo'
    _description = 'Protocolo de atención'
    
    name = fields.Char(string='Protocolo')
    estacion_ids = fields.Many2many(comodel_name='project.task.type', string='Estaciones', domain=[('estacion_estarbien','=',True)])

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    service_tracking = fields.Selection(selection_add=[('estarbien', 'Estarbien')])
    subproducto_ids = fields.Many2many(comodel_name='product.template', relation='tabla_bom_extra', column1='prod1', column2='prod2', string='Subproductos')
    protocolo_id = fields.Many2one(comodel_name='product.template.protocolo',string='Perfil')
    
    @api.constrains('project_id', 'project_template_id')
    def _check_project_and_template(self) :
        """ NOTE 'service_tracking' should be in decorator parameters but since ORM check constraints twice (one after setting
            stored fields, one after setting non stored field), the error is raised when company-dependent fields are not set.
            So, this constraints does cover all cases and inconsistent can still be recorded until the ORM change its behavior.
        """
        super(ProductTemplate, self)._check_project_and_template()
        for product in self :
            if product.service_tracking == 'estarbien' and (product.project_id or product.project_template_id) :
                raise ValidationError('El producto %s no debería tener un proyecto o una plantilla de proyecto ya que no generará un proyecto.' % (product.name,))
    
    @api.onchange('service_tracking')
    def _onchange_service_tracking(self) :
        super(ProductTemplate, self)._onchange_service_tracking()
        if self.service_tracking == 'estarbien' :
            self.project_id = False
            self.project_template_id = False
        else :
            self.subproducto_ids = False
            self.protocolo_id = False

class ProductProduct(models.Model):
    _inherit = 'product.product'
    
    @api.onchange('service_tracking')
    def _onchange_service_tracking(self) :
        super(ProductProduct, self)._onchange_service_tracking()
        if self.service_tracking == 'estarbien' :
            self.project_id = False
            self.project_template_id = False
        else :
            self.subproducto_ids = False
            self.protocolo_id = False
