# -*- coding: utf-8 -*-
# FILE: gists.py
# AUTHOR: pocari <caffelattenonsugar at gmail.com>
# License: MIT license

import urllib.request
import urllib.parse
import json

from denite import util
from .base import Base


GIST_BASE_URL = "https://api.github.com/users/{}/gists"


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'gists'
        self.kind = 'browser'


    def gather_candidates(self, context):
        gists_url = self._build_url(context)
        params = {
            "direction": "desc",
            "sort": "updated"
        }

        gists = self._get_gists(gists_url, params)
        if gists:
            return [self._convert(r) for r in gists]


    def _build_url(self, context):
        args = dict(enumerate(context['args']))
        arg = args.get(0)
        if arg:
            user_name = arg
        else:
            u = self.vim.call('denite_gists#util#github_user')
            if u:
                user_name = u
            else:
                user_name = util.input(self.vim, context, 'Gist User: ')

        return GIST_BASE_URL.format(user_name)


    def _get_gists(self, url, params):
        encoded_params = urllib.parse.urlencode(params)
        url = "{}?{}".format(url, encoded_params)
        try:
          with urllib.request.urlopen(url) as res:
              return json.loads(res.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            util.error(self.vim, "Error {} api url:{}".format(e.reason, url))


    def _convert(self, gist_info):
        return {
            "word": "{} ({})".format(gist_info["description"], gist_info["updated_at"]),
            "url": gist_info["html_url"]
        }

