#/bin/python
# -*- coding: utf-8 -*-

__author__    = 'Gerrit Giehl <ggiehl@piratenfraktion-nrw.de>'
__contact__   = 'it@piratenfraktion-nrw.de'
__date__      = '09 November 2014'

import tornado.ioloop
import tornado.web
from controllers.mainhandler import MainHandler
from controllers.loginhandler import LoginHandler
import os.path

APPDIR = os.path.dirname(os.path.abspath(__file__))
CONFIGFILE = os.path.join(APPDIR, 'server.conf')

application = tornado.web.Application([
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    (r"/", MainHandler),
    (r"/login", LoginHandler),
], debug=False, cookie_secret="__TODO:__", login_url="/login")

def main():
    application.listen(8080)
    #tornado.options.parse_config_file(CONFIGFILE)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
