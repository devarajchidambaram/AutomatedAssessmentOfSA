#!/usr/bin/env python

import webapp2
import jinja2
import os
from proj import main_algo

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class TestHandler(BaseHandler):
    def get(self):
        q1 = "What is OOPS?"
        q2 = "What are the basic concepts of OOPS?"
        q3 = "What is encapsulation?"
        self.render("TakeTest.html", q1=q1, q2=q2, q3=q3)

    def post(self):
        # self.response.out.write()
        a1 = self.request.get("a1")
        a2 = self.request.get("a2")
        a3 = self.request.get("a3")
        params = {}

        params["a1_ans"] = a1
        params["a2_ans"] = a2
        params["a3_ans"] = a3

        no_of_spell_errors, words_dup_stop_removd = main_algo(a1)
        params["a1_error"] = str(no_of_spell_errors)
        params["a1_tokens"] = words_dup_stop_removd

        no_of_spell_errors, words_dup_stop_removd = main_algo(a2)
        params["a2_error"] = str(no_of_spell_errors)
        params["a2_tokens"] = words_dup_stop_removd

        no_of_spell_errors, words_dup_stop_removd = main_algo(a3)
        params["a3_error"] = str(no_of_spell_errors)
        params["a3_tokens"] = words_dup_stop_removd

        self.render("Result.html", **params)

app = webapp2.WSGIApplication([
    ('/taketest', TestHandler)
], debug=True)
