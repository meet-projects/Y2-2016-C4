from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Question, Answer

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.

###############################################
#   MAJD YOU WORK ON THIS   #
q1 = Question(
    #pic_id = 1,
    text = 'where do you think picture nom.1 was taken ?',
    a1 = 'Israel',
    a2 = 'USA',
    a3 = 'Palestine',
    a4 = 'Syria',
	a5 = 'other')


q2 = Question(
	text = 'where do you think picture nom.2 was taken ?',
	a1 = 'Israel',
	a2 = 'USA',
	a3 = 'Palestine',
	a4 = 'Syria',
	a5 = 'other')

q3 = Question(
	text= 'How easy for you to recognize which one belongs to Palestine and which one belongs to Israel ?',
	a1 = 'very easy',
	a2 = 'easy',
	a3 = 'normal',
	a4 = 'hard',
	a5 = 'very hard')
q4 = Question(
	text = 'why ?',
	a1 = 'its obvious',
	a2 = 'i have been there',
	a3 = 'i dont know it seems like it',
	a4 = 'other',
	a5 = 'something')


###############################################
a1=Answer(
	question_id = 1,
    selected='a3',
    text=session.query(Question).filter_by(id=1).one().a3,
    nationality = 'Palastinian')
# This deletes everything in your database.
session.query(Question).delete()
session.query(Answer).delete()
session.commit()

# This adds some rows to the database. Make sure you `commit` after `add`ing!
session.add(q1)
session.add(a1)
session.commit()
