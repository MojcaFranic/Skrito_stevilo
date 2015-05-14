#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")

class SteviloHandler(BaseHandler):
    def post(self):
        x = 19
        y = self.request.get("vnos")
        x = int(x)
        y = int(y)
        if y == x:
            rezultat = ("Bravo!")
        elif y < 19 and y > 0:
            rezultat = ("Stevilo je prenizko")
        elif y > 19 and y < 100:
            rezultat = ("Stevilo je previsoko")
        else:
            rezultat = ("Vpisano stevilo ni med 1 in 100!")

        params = {"rezultat": rezultat}
        self.render_template("stevilo.html", params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/stevilo', SteviloHandler),

], debug=True)
