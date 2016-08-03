from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


from database_setup import Base, Question, Answer, QuestAndPic, Picture


engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.

# This deletes everything in your database.
session.query(Question).delete()
session.query(Answer).delete()
session.query(Picture).delete()
################################################
#   MAJD YOU WORK ON THIS   #


q1 = Question(

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

'''x = QuestAndPic(
	question_id = q1.id,
	pic_id = 1)
'''
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
############################################## PIC ----- FOOD
p1=Picture(
	path='pic/food/israeldessert.jpg',
	category= 'food')

p2=Picture(
	path='pic/food/israelfood.jpg',
	category= 'food')
p3=Picture(
	path='pic/food/palestinedessert.jpg',
	category= 'food')
p4=Picture(
	path='pic/food/Palestinefood.jpg',
	category= 'food')

############################################## PIC ----- ACTIVITY
p5=Picture(
	path= 'pic/activities/israelbowling.jpg',
	category= 'activity')
p6=Picture(
	path= 'pic/activities/israelcinema.jpg',
	category= 'activity')
p7=Picture(
	path= 'pic/activities/palestinebowling.jpg',
	category= 'activity')
p8=Picture(
	path= 'pic/activities/palestinecinema.jpg',
	category= 'activity')
############################################## PIC ----- EDUCATION
p9=Picture(
	path= 'pic/education/israelreligion.jpg',
	category= 'education')
p10=Picture(
	path= 'pic/education/Israelschool.jpg',
	category= 'education')
p11=Picture(
	path= 'pic/education/palestinereligion.jpg',
	category= 'education')
p12=Picture(
	path= 'pic/education/palestineschool.jpg',
	category= 'education')
############################################# PIC ----- COVER
p13=Picture(
	path= 'pic/palestineschool.jpg',
	category= 'cover')
p14=Picture(
	path= 'pic/cover.jpg',
	category= 'cover')
p15=Picture(
	path= 'pic/activities.jpg',
	category= 'cover')

pics=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]
for pic_to_add in pics:
	session.add(pic_to_add)

##############################################


session.commit()