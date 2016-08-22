from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from random import randint, choice

from database_setup import Base, Answer


engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

nats=['Palestinian', 'Israeli', 'Other']

for i in range(1,10000):
	a1=Answer(
		pair_id = randint(1,20),
		question_id = randint(1,5),
	    selected=randint(1,5),
	    nationality = choice(nats))

	session.add(a1)


session.commit()
