#/bin/python
# -*- coding: utf-8 -*-

__author__    = 'Gerrit Giehl <ggiehl@piratenfraktion-nrw.de>'
__contact__   = 'it@piratenfraktion-nrw.de'
__date__      = '09 November 2014'

from jinja2 import Environment, FileSystemLoader
import tornado.ioloop
import tornado.web
from pyactiveresource.activeresource import ActiveResource
from pyactiveresource import formats
from models.top import Top
import os.path
import operator

APPDIR = os.path.dirname(os.path.abspath(__file__))
CONFIGFILE = os.path.join(APPDIR, 'server.conf')

class MainHandler(tornado.web.RequestHandler):

    def get(self):

        tops = []

        issues = Issue.find(query_id = 67)
        for i, v in enumerate(issues):
            t = Top()
            #print('issue [',i,']',' =', v)
            for item in issues[i].attributes:
                #print(item, " = ", issues[i].attributes[item])
                if item == 'custom_fields':
                    for j, cf in enumerate(issues[i].attributes[item]):
                        #print(cf, " = ", cf.attributes['name'])
                        if cf.attributes['name'] == 'Abstimmungsempfehlung':
                            t.abstimmungsempfehlung = cf.attributes['value']
                            if t.abstimmungsempfehlung == 'Dafür':
                                t.btn = 'btn-success'
                            elif t.abstimmungsempfehlung == 'Dagegen':
                                t.btn = 'btn-danger'
                            elif t.abstimmungsempfehlung == 'Zustimmung zur Überweisung':
                                t.btn = 'btn-warning'
                            elif t.abstimmungsempfehlung == 'Enthaltung':
                                t.btn = 'btn-primary'
                            else:
                                t.btn = 'btn-default'

                        elif cf.attributes['name'] == 'Top':
                            t.nummer = int(cf.attributes['value'])

                elif item == 'id':
                    t.ticketid = issues[i].attributes[item]
                elif item == 'subject':
                    t.beschreibung = issues[i].attributes[item]
            tops.append(t)
            del t

        tops.sort(key=operator.attrgetter("nummer"), reverse=False)
        
        template = templateEnv.get_template('index.html')        
        self.write(template.render(tops=tops))

class Issue(ActiveResource):
    _site = 'https://redmine.piratenfraktion-nrw.de/projects/plenum'
    _format = formats.XMLFormat 

templateLoader = FileSystemLoader(searchpath="templates/")
templateEnv = Environment(loader=templateLoader)

application = tornado.web.Application([
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
    (r"/", MainHandler),
], debug=False)

def main():
    application.listen(8080)
    #tornado.options.parse_config_file(CONFIGFILE)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
