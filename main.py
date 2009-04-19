import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext import db

import twitter
from models import Tweet

class MainHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write('Hello world!')

class TwitterHandler(webapp.RequestHandler):
	def get(self):
		from settings import TWITTER_USERNAME, TWITTER_PASSWORD
		api = twitter.Api(username=TWITTER_USERNAME, password=TWITTER_PASSWORD)
		
		try:
			last_tweet_processes = db.Query(Tweet).all().order('tweet_id').fetch(limit=1)[0]
			replies = api.GetReplies(since_id=last_tweet_processes.tweet_id)
		except IndexError:
			replies = api.GetReplies()
		
		

def main():
	application = webapp.WSGIApplication([
		('/', MainHandler),
		('/twitter', TwitterHandler),
	], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
	main()