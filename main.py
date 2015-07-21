#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainPage(Handler):
	def get(self):
		self.render('intro.html', title='')

class MediaPage(Handler):
	def get(self):
		self.render('media.html', title=' - Media')	

class ReflectionPage(Handler):
	def get(self):
		self.render('reflection.html', title=' - Reflection')	

class ActivitiesPage(Handler):
	def get(self):
		self.render('activities.html', title=' - Activities')	

class Act1Page(Handler):
	def get(self):
		self.render('act1.html', title=' - 1. Motto')		

class Act2Page(Handler):
	def get(self):
		self.render('act2.html', title=' - 2. Capitol City')	

class Act3Page(Handler):
	def get(self):
		self.render('act3.html', title=' - 3. Myth')	

class Act4Page(Handler):
	def get(self):
		self.render('act4.html', title=' - 4. Sport')	

class Act5Page(Handler):
	def get(self):
		self.render('act5.html', title=' - 5. Food')

class Act6Page(Handler):
	def get(self):
		self.render('act6.html', title=' - 6. Flag')	

class Act7Page(Handler):
	def get(self):
		self.render('act7.html', title=' - 7. Daily Life')	

class Act8Page(Handler):
	def get(self):
		self.render('act8.html', title=' - 8. Celebration')	


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/media', MediaPage),
    ('/reflection', ReflectionPage),
    ('/activities', ActivitiesPage),
    ('/act1', Act1Page),
    ('/act2', Act2Page),
    ('/act3', Act3Page),
    ('/act4', Act4Page),
    ('/act5', Act5Page),
    ('/act6', Act6Page),
    ('/act7', Act7Page),
    ('/act8', Act8Page)


], debug=True)
