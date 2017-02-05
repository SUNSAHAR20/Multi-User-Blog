from google.appengine.ext import db

from user import User

		#Class that creates a comment object
class Comment(db.Model):
	comment = db.TextProperty(required=True)
	commentauthor = db.StringProperty(required=True)
	commentid = db.IntegerProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)