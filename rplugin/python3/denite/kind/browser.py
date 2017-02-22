# -*- coding: utf-8 -*-
# FILE: browser.py
# AUTHOR: pocari <caffelattenonsugar at gmail.com>
# License: MIT license

from .base import Base


class Kind(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'browser'
        self.default_action = 'open'


    def action_open(self, context):
        for x in context['targets']:
            self.vim.command("OpenBrowser {}".format(x['url']))

