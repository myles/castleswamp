from google.appengine.ext import db

class Tweet(db.Model):
	created_at = db.StringProperty()
	created_at_in_seconds = db.StringProperty()
	favorited = db.BooleanProperty()
	in_reply_to_screen_name = db.StringProperty()
	in_reply_to_user_id = db.IntegerProperty()
	in_reply_to_status_id = db.IntegerProperty()
	truncated = db.BooleanProperty()
	source = db.StringProperty()
	tweet_id = db.IntegerProperty()
	text = db.StringProperty()
	relative_created_at = db.StringProperty()
	
	user_id = db.StringProperty()
	user_name = db.StringProperty()
	user_screen_name = db.StringProperty()