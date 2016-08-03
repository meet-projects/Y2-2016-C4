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
    text = 'where do you think picture num.1 was taken ?',
    a1 = 'Israel',
    a2 = 'USA',
    a3 = 'Palestine',
    a4 = 'Syria',
	a5 = 'Other')


q2 = Question(
	text = 'Where do you think picture num.2 was taken ?',
	a1 = 'Israel',
	a2 = 'USA',
	a3 = 'Palestine',
	a4 = 'Syria',
	a5 = 'Other')

q3 = Question(
	text= 'How easy was it for you to recognize which one belongs to Palestine and which one belongs to Israel ?',
	a1 = 'Very easy',
	a2 = 'Easy',
	a3 = 'Normal',
	a4 = 'Hard',
	a5 = 'Very hard')
q4 = Question(
	text = 'Why ?',
	a1 = 'Its obvious',
	a2 = 'I have been there',
	a3 = 'I dont know it seems like it',
	a4 = 'There is no difference',
	a5 = 'Other')

q5 = Question(
	text = 'How did it make you feel ?',
	a1 = 'Happy',
	a2 = 'sad',
	a3 = 'scared',
	a4 = 'interested',
	a5 = 'not sure')


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
