# Copyright 2020 Luis Felipe Gomez Botero
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Receipt Print",
    "version": "14.0.1",
    "category": "Accounting & Finance",
    "summary": "Enable printing thermal receipt in invoice",
    "author": "Luis Felipe Gomez Botero",
    "website": "https://github.com/felipegomezb21/odoo-modificaciones.git",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": [
        "views/report_invoice_with_payments_custom_receipt.xml"
    ],
    "installable": True,
}
