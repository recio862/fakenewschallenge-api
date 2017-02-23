from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declared_attr

from app.db import Base


class NewsTable(object):

    __tablename__ = 'news'

    headline = Column(String(250), required=True)
    source = Column(String(250), required=True)
    uploader = Column(String(250), default="Unknown")
    date = Column(String(250), required=True)
    fake = Column(Boolean, required=True)

    def __repr__(self):
        return "<NewsTable(headline='%s', source='%s', uploader='%s')>" % (self.headline, self.source, self.uploader)

news_table = NewsTable
