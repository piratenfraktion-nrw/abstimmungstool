from controllers.basehandler import BaseHandler

import tornado

class LoginHandler(BaseHandler):
    
    def get(self):
        template = self.templateEnv.get_template('login.html')
        self.write(template.render())

    def post(self):
        self.set_secure_cookie("user", tornado.escape.xhtml_escape(self.get_argument("username")))
        self.redirect("/")
