# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PlayerProfile(models.Model):
    _name = 'player.profile'

    name = fields.Char(string="Full Name")
    club_id = fields.Many2one("club.profile", string="Club")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    salary = fields.Float(string="Salary")
    birthday_date = fields.Date(string="Birthday Date")
    image = fields.Image(string="Upload Profile Photo", max_width=500, max_height=500)
    description = fields.Html(string="Description")
