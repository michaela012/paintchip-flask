from app import app, db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    # mixin provides default implementations for the methods that Flask-Login expects user objects to have.
    __tablename__ = 'users'
    userID = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)

    email = db.Column(db.Text,
                      index=False,
                      unique=True,
                      nullable=False)
    password_hash = db.Column(db.Text,
                              index=False,
                              unique=False)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Feed(db.Model):
    # model for single newsfeed
    __tablename__ = 'feeds'
    feedID = db.Column(db.Integer,
                   primary_key=True)
    title = db.Column(db.Text,
                     index=False,
                     unique=True,
                     nullable=False)
    subtitle = db.Column(db.Text,
                         index=False,
                         unique=False,
                         nullable=True)
    url = db.Column(db.Text,
                    index=False,
                    unique=True,
                    nullable=False)
    def __repr__(self):
        return 'Feed Title: {}'.format(self.title)


class Article(db.Model):
    # model for individual article
    __tablename__ = 'articles'
    articleID = db.Column(db.Integer,
                          primary_key=True)
    title = db.Column(db.Text,
                      index=False,
                      unique=False,
                      nullable=False)
    subtitle = db.Column(db.Text,
                         index=False,
                         unique=False,
                         nullable=True)
    author = db.Column(db.Text,
                       index=False,
                       unique=False,
                       nullable=True)
    pub_date = db.Column(db.DateTime,
                         index=False,
                         unique=False,
                         nullable=False)
    url = db.Column(db.Text,
                    index=False,
                    unique=True,
                    nullable=False)


class readArticle(db.Model):
    __tablename__ = 'readArticles'
    entryID = db.Column(db.Integer,
                        primary_key=True)
    articleID = db.Column(db.Integer, db.ForeignKey('articles.articleID'))
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'))
    read_date = db.Column(db.DateTime, default=datetime.now())