# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from jsonm import Field, Model


class Offer(Model):
    offerid = Field()
    admin_id = Field()
    category = Field()
    converts_at = Field()
    lead_rate = Field()
    merchant_id = Field()
    merchant_paying = Field()
    name = Field()
    name_private = Field()
    note = Field()
    preview = Field()
    requirements = Field()
    textlink_url = Field()
