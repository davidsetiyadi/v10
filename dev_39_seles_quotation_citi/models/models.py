# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class dev_39_seles_quotation_citi(models.Model):
#     _name = 'dev_39_seles_quotation_citi.dev_39_seles_quotation_citi'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100