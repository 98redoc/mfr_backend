""" Post ORM Module. """
import datetime
from .. import db


class Post(db.Model):
	__table_name = "post"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
	created = db.Column(db.TIMESTAMP, nullable=True, default=datetime.datetime.now())
	title = db.Column(db.Text, nullable=False)
	body = db.Column(db.Text, nullable=False)


