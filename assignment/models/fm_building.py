from odoo import api, fields, models
import math

class Building(models.Model):
    _name = 'fm.building'
    _description = 'Buildings'
    _rec_name = 'building_name'

    building_id = fields.One2many('employee.building.assignment', 'building_id', string='Building')
    building_name = fields.Char(required=True)
    building_no = fields.Char(required=True)
    building_dimension = fields.Char(string='Dimension')
    construction_year = fields.Char(string='Construction Year')
    structural_system = fields.Char(string='System')
    office_area_as_mt_square = fields.Float(string='Square')
    under_root_area_as_meter = fields.Float(string='Meter')
    under_root_area_as_feet = fields.Float(string='Feet', compute='_mt_to_feet')

    active = fields.Boolean(default=True)

    @api.depends('under_root_area_as_meter')
    def _mt_to_feet(self):
        for record in self:
            record.under_root_area_as_feet = record.under_root_area_as_meter * 3.2808