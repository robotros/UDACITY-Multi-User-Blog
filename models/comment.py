""" Comment

Author: Aron Roberts
Version: 1.01
Date Created: 3/4/2017
filename: comment.py

Last Update:
Date: 3/5/2017
DESC: altered code to meet pep8

"""
from google.appengine.ext import db
from models.user import User
from models.post import Post


class Comment(db.Model):
    """ Entity class for Comment """
    post = db.ReferenceProperty(Post, required=True,
                                collection_name='comments')
    author = db.ReferenceProperty(User, required=True,
                                  collection_name='comments')
    comment = db.TextProperty(required=True)
