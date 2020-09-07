# Copyright 2020 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class WizardOrderpointImportExportStepTwo(models.Model):

    _name = 'wizard.orderpoint.import.export.steptwo'
    _description = 'Wizard Orderpoint Import Export'

    filename = fields.Char()
    file = fields.Binary()
