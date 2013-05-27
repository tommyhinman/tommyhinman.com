import webapp2
import os
import jinja2
import logging

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):

	def get(self):
		logging.info("test")
		template_values = {}

		template = jinja_environment.get_template('templates/resume.html')
		self.response.out.write(template.render(template_values))

application = webapp2.WSGIApplication([
	('/', MainHandler),
	('/resume', ResumeHandler),
], debug=True)
