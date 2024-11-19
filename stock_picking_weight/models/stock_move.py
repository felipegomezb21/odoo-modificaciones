# Copyright 2023 ACSONE SA/NV
# Copyright 2023 Michael Tietz (MT Software) <mtietz@mt-software.de>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class StockMove(models.Model):

    _inherit = "stock.move"

    weight = fields.Float(
        compute="_compute_weight",
        readonly=False,
        store=True,
        compute_sudo=True,
        states={"done": [("readonly", True)], "cancel": [("readonly", True)]},
    )

    weight_uom_name = fields.Char(
        string="weight unit of measure label", compute="_compute_weight_uom_name"
    )

    @api.depends("product_id", "product_uom_qty", "state", "move_line_ids.product_qty")
    def _compute_weight(self):
        for move in self:
            qty = move.product_uom_qty
            if move.state in ("partially_available", "assigned"):
                qty = move.reserved_availability
            new_weight = move.product_id._get_weight_for_qty(qty, move.product_uom)
            if move.weight != new_weight:
                move.weight = new_weight

    def _compute_weight_uom_name(self):
        self.weight_uom_name = self.env[
            "product.template"
        ]._get_weight_uom_name_from_ir_config_parameter()
