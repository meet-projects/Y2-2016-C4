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
<<<<<<< HEAD
    pic_id = 1,
    text = 'where do you think picture nom.1 was taken ?',
=======
    #pic_id = 1,
    text = 'where do you think picture num.1 was taken ?',
>>>>>>> 2e8e2d4a1e94b480c732aa982c95f03e649e2252
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