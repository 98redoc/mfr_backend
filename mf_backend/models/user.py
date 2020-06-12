""" User ORM model. """
from .. import db


class User(db.Model):
	__table__name = "user"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, nullable=False)

	def save(self):
		db.session.add(self)
		db.session.commit()
