# Copyright 2020 Luis Felipe Gomez Botero
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Stock Custom",
    "version": "14.0.1",
    "category": "Stock",
    "summary": "Views Custom",
    "author": "Luis Felipe Gomez Botero",
    "website": "https://github.com/felipegomezb21/odoo-modificaciones.git",
    "license": "AGPL-3",
    "depends": ["stock","stock_picking_volume"],
    "data": [
        "views/stock.picking.form.custom.xml",
        "views/stock.picking.tree.custom"
    ],
    "installable": True,
}
