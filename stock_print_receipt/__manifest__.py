# Copyright 2020 Luis Felipe Gomez Botero
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Stock Delivery Receipt Print",
    "version": "14.0.1",
    "category": "Stock",
    "summary": "Enable printing thermal receipt in delivery receipt",
    "author": "Luis Felipe Gomez Botero",
    "website": "https://github.com/felipegomezb21/odoo-modificaciones.git",
    "license": "AGPL-3",
    "depends": ["stock"],
    "data": [
        "views/report_action_deliveryslip_receipt.xml",
        "views/report_deliveryslip_receipt.xml"
    ],
    "installable": True,
}
