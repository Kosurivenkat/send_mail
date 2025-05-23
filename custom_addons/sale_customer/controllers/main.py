from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class SaleCustomerController(http.Controller):

    @http.route('/sale_order/accept/<int:order_id>', type='http', auth='public', website=True)
    def accept_sale_order(self, order_id, **kwargs):
        order = request.env['sale.order'].sudo().browse(order_id)

        if not order.exists():
            _logger.warning("Sale order with ID %s does not exist.", order_id)
            return request.not_found()

        _logger.info("Customer accessed accept URL for order ID: %s", order_id)

        if order.state == 'sent':
            order.write({'state': 'customer_accepted'})
            _logger.info("Order ID %s state updated to 'customer_accepted'.", order_id)
        else:
            _logger.info("Order ID %s already processed. Current state: %s", order_id, order.state)

        return request.render('sale_customer.accept_quotation_template', {'order': order})
