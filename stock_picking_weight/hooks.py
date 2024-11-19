# Copyright 2023 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from odoo.tools.sql import column_exists, create_column

_logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    """Pre init create weight column on stock.picking and stock.move"""
    if not column_exists(cr, "stock_move", "weight"):
        create_column(cr, "stock_move", "weight", "double precision")
        # First we compute the reserved qty by move_id
        # the reserved qty is the sum of the reserved qty of the move lines
        # linked to the move
        # Then we update the weight of the moves not in state done or cancel
        # If the move is in state partially available, or assigned, the weight
        # is the reserved qty * the product weight
        # else the weight is the move quantity * the product weight
        cr.execute(
            """
            with reserved_qty_by_move as (
                select
                    move_id,
                    product_id,
                    sum(product_qty) as product_qty
                from stock_move_line
                group by move_id, product_id
            )
            update stock_move
                set weight =
                    CASE
                        WHEN stock_move.state in ('partially_available', 'assigned') THEN
                            reserved_qty_by_move.product_qty * pp.weight
                        ELSE
                            stock_move.product_uom_qty * pp.weight
                    END
            from reserved_qty_by_move
            join product_product pp on pp.id = reserved_qty_by_move.product_id
            where
                stock_move.id = reserved_qty_by_move.move_id
                and stock_move.state not in ('done', 'cancel')
            """
        )
        _logger.info(f"{cr.rowcount} rows updated in stock_move")

    if not column_exists(cr, "stock_picking", "weight"):
        create_column(cr, "stock_picking", "weight", "double precision")
        # we recompute the weight of the pickings not in state done or cancel
        # the weight is the sum of the weight of the moves linked to the picking
        # that are not in state done or cancel
        cr.execute(
            """
            update stock_picking
                set weight = (
                    select sum(weight)
                    from stock_move
                    where
                        stock_move.picking_id = stock_picking.id
                        and state not in ('done', 'cancel')
                )
            where state not in ('done', 'cancel')
            """
        )
        _logger.info(f"{cr.rowcount} rows updated in stock_picking")
