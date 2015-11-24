import webapp2
import os
import jinja2
import logging
from src.albumLists.listData import getAlbumListData

jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class ListsHandler(webapp2.RequestHandler):
	def get(self):

		template_values = {'data':getAlbumListData()}
		template = jinja_environment.get_template('templates/lists.html')
		self.response.out.write(template.render(template_values))