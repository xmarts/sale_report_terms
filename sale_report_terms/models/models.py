# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


# from odoo.exceptions import UserError

class res_company(models.Model):
    _inherit = 'res.company'

    sale_report_terms = fields.Html(store=True,translate=True)
