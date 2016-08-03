from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Question, Answer, QuestsAndPics

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.

# This deletes everything in your database.
session.query(Question).delete()
session.query(Answer).delete()

###############################################
#   MAJD YOU WORK ON THIS   #


q1 = Question(
    pic_id = 1,
    text = 'where do you think picture nom.1 was taken ?',
    a1 = 'Israel',
    a2 = 'USA',
    a3 = 'Palestine',
    a4 = 'Syria',
	a5 = 'other')


q2 = Question(
	pic_id = 2,
	text = 'where do you think picture nom.2 was taken ?',
	a1 = 'Israel',
	a2 = 'USA',
	a3 = 'Palestine',
	a4 = 'Syria',
	a5 = 'other')

q3 = Question(
	pic_id = 3,
	text= 'How easy for you to recognize which one belongs to Palestine and which one belongs to Israel ?',
	a1 = 'very easy',
	a2 = 'easy',
	a3 = 'normal',
	a4 = 'hard',
	a5 = 'very hard')

q4 = Question(
	pic_id = 4,
	text = 'why ?',
	a1 = 'its obvious',
	a2 = 'i have been there',
	a3 = 'i dont know it seems like it',
	a4 = 'other',
	a5 = 'something')

x = QuestsAndPics(
	question_id = q1.id,
	pic_id = 1)

questions=[q1,q2,q3,q4]
for question_to_add in questions:
	session.add(question_to_add)
###############################################
question = session.query(Question).filter_by(id=1).one()
print (question)
answer_chosen='a3'
a1=Answer(
	question_id = 1,
    selected=answer_chosen,
    text=getattr(question, answer_chosen),
    nationality = 'Palastinian')

answers=[a1]
for question_to_add in questions:
	session.add(question_to_add)
##############################################
session.commit()