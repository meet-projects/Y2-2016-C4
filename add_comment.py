from random import randint, choice


from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Comment 


engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

nats=['Palestinian', 'Israeli', 'Other']

for i in range(1,6):
	a1=Comment(
		pair_id = 2,
		nationality = choice(nats),
	    author='Eilon',
	    text='Comment test number '+ str(i)
	    )

	session.add(a1)


session.commit()
