from jinja2 import Environment, FileSystemLoader
import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    templateLoader = FileSystemLoader(searchpath="templates/")
    templateEnv = Environment(loader=templateLoader)

    def get_current_user(self):
        return self.get_secure_cookie("user")
