from google.appengine.ext import db

from user import User

class Comment(db.Model):
    """class that creates the basic database specifics for a comment"""
    comment = db.TextProperty(required=True)
    commentauthor = db.StringProperty(required=True)
    commentid = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)