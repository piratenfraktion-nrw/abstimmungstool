from controllers.basehandler import BaseHandler
from models.top import Top

from pyactiveresource.activeresource import ActiveResource
from pyactiveresource import formats
import tornado.ioloop
import tornado.web

import operator

class Issue(ActiveResource):
    _site = 'https://redmine.piratenfraktion-nrw.de/projects/plenum'
    _format = formats.XMLFormat

class MainHandler(BaseHandler):

    #@tornado.web.authenticated
    def get(self):

        #name = tornado.escape.xhtml_escape(self.current_user)
        #self.write("Hello, " + name)

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

        template = self.templateEnv.get_template('index.html')
        self.write(template.render(tops=tops))

