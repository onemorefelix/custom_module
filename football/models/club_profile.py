# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FootballClub(models.Model):
    _name = 'club.profile'

    name = fields.Char(string="Club Name")
    site = fields.Char(string="Site")
    # players_count = fields.Integer(string="Number of player")
    players_count = fields.Integer(string="Number of player")
    image = fields.Image(string="Upload Club Photo", max_width=500, max_height=500)
    description = fields.Html(string="Description")
    player_list = fields.One2many("player.profile", "club_id", string="Player List")


