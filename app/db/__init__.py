from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE = {
    'default': {
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'ADDRESS': os.environ.get('DB_ADDRESS')
    }
}

engine = create_engine('mysql://{user}:{password}@{address}/{database}'.format(
    user=DATABASE['default']['USER'],
    password=DATABASE['default']['PASSWORD'],
    address=DATABASE['default']['ADDRESS'],
    database=DATABASE['default']['NAME']))

Base = declarative_base()


class FakeNewsChallengeDB(object):
    _session = None

    @property
    def session(self):
        if not self._session:
            self.session = sessionmaker(bind=engine)()
        return self._session

    @session.setter
    def session(self, val):
        self._session = val


fnc_db = FakeNewsChallengeDB()

Base.metadata.create_all(engine)
