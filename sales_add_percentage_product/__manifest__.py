# Copyright 2020 Luis Felipe Gomez Botero
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Sales Add Percentage Product",
    "summary": "Add order lines with a percentage of the total order",
    "version": "14.0.1.",
    "category": "Sales Management",
    "website": "https://github.com/felipegomezb21/odoo-modificaciones.git",
    "author": "Luis Felipe Gomez Botero",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["sale", "sale_management"],
    "data": ["views/sale_order_view.xml"],
}