from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('customer_accepted', 'Customer Accepted'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
    ], string='Status', readonly=True, copy=False, index=True, default='draft')


    def action_confirm_from_customer(self):
        for order in self:
            if order.state == 'customer_accepted':
                order.state = 'draft'
                order.action_confirm()





