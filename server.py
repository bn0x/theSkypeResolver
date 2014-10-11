#!/usr/bin/python2
#! -*- coding: utf-8 -*-
#
# ---------------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 43.5):
# @__akiaki wrote this file. As long as you retain this notice you can do whatever
# you want with this stuff. If we meet some day, and you think this stuff is worth
# it, you can buy me a beer (or caffeinated beverage) in return. --aki
# ---------------------------------------------------------------------------------

import web
import json
import time
import glob
import logparse
import skypeapi


urls = (
  '/', 'index',
  '/api/(.*)', 'api'
)

app = web.application(urls, globals())
render = web.template.render('templates/')
skypeapi.init()

class api:
    def GET(self, username):
        skypeapi.activateSkype(username)
        time.sleep(3) # because skype is ew
        buf = []
        for logfile in glob.glob('*.log'):
            buf += logparse.search(logfile, username)
        return json.dumps(buf)

class index:
    def GET(self):
        return render.index()

if __name__ == "__main__":
    app.run()
