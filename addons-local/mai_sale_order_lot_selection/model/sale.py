from odoo import api, fields, models, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_lot_id = fields.Many2one('stock.production.lot', 'Lot', copy=False)

    # @api.multi
    def _prepare_procurement_values(self, group_id=False):
        res = super(SaleOrderLine, self)._prepare_procurement_values(group_id=group_id)
        res['x_lot_id'] = self.x_lot_id.id
        return res
