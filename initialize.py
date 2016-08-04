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
session.query(QuestAndPic).delete()
################################################
#   MAJD YOU WORK ON THIS   #


q1 = Question(

    text = 'where do you think picture num.1 was taken ?',
    pic_id=6,
    a1 = 'Israel',
    a2 = 'USA',
    a3 = 'Palestine',
    a4 = 'Syria',
	a5 = 'Other')


q2 = Question(

	text = 'Where do you think picture num.2 was taken ?',
	pic_id=6,
	a1 = 'Israel',
	a2 = 'USA',
	a3 = 'Palestine',
	a4 = 'Syria',
	a5 = 'Other')

q3 = Question(
	text= 'How easy was it for you to recognize which one belongs to Palestine and which one belongs to Israel ?',
	pic_id=6,
	a1 = 'Very easy',
	a2 = 'Easy',
	a3 = 'Normal',
	a4 = 'Hard',
	a5 = 'Very hard')
q4 = Question(
	text = 'Why ?',
	pic_id=6,
	a1 = 'Its obvious',
	a2 = 'I have been there',
	a3 = 'I dont know it seems like it',
	a4 = 'There is no difference',
	a5 = 'Other')

q5 = Question(
	text = 'How did it make you feel ?',
	pic_id=6,
	a1 = 'Happy',
	a2 = 'sad',
	a3 = 'scared',
	a4 = 'interested',
	a5 = 'not sure')

q1= question(
	text= 'o you see a difference between the two pictures?',
	pic_id=5,
	a1='yes',
	a2='no',
	a3='maybe')

q2 =question(
	text= 'why ?',
	pic_id=5,
	a1='Picture 2 looks better',
	a2='There is a big difference',
	a3='Picture 1 looks luxurious',
	a4='There is no differences',
	a5='other')
q3= question(
	text='where do you think the two pictures were taken ?',
	pic_id=5,
	a1='Palestine and USA')

x = QuestAndPic(
	question_id = q1.id,
	pic_id = 1)

questions=[q1,q2,q3,q4]
for question_to_add in questions:
	session.add(question_to_add)
###############################################
answer_chosen='a3'
a1=Answer(
	question_id = 1,
    selected=answer_chosen,
    nationality = 'Palastinian')

answers=[a1]
for question_to_add in questions:
	session.add(question_to_add)
############################################## PIC ----- FOOD
p1=Picture(
	path='pic/food/israeldessert.jpg',
	category= 'food',
	cover=False)

p2=Picture(
	path='pic/food/israelfood.jpg',
	category= 'food',
	cover=False)
p3=Picture(
	path='pic/food/palestinedessert.jpg',
	category= 'food',
	cover=False)

p4=Picture(
	path='pic/food/Palestinefood.jpg',
	category= 'food',
	cover=False)

############################################## PIC ----- ACTIVITY
p5=Picture(
	path= 'pic/activities/israelbowling.jpg',
	category= 'activity',
	cover=False)
p6=Picture(
	path= 'pic/activities/israelcinema.jpg',
	category= 'activity',
	cover=False)
p7=Picture(
	path= 'pic/activities/palestinebowling.jpg',
	category= 'activity',
	cover=False)
p8=Picture(
	path= 'pic/activities/palestinecinema.jpg',
	category= 'activity',
	cover=False)
############################################## PIC ----- EDUCATION
p9=Picture(
	path= 'pic/education/israelreligion.jpg',
	category= 'education',
	cover=False)
p10=Picture(
	path= 'pic/education/Israelschool.jpg',
	category= 'education',
	cover=False)
p11=Picture(
	path= 'pic/education/palestinereligion.jpg',
	category= 'education' , 
	cover=False)
p12=Picture(
	path= 'pic/education/palestineschool.jpg',
	category= 'education',
	cover=False)
############################################# PIC ----- Meaningful
p13=Picture(
	path= 'pic/meaningful/I.jpg',
	category= 'meaningful',
	cover=False)
p14=Picture(
	path= 'pic/meaningful/we.jpg',
	category= 'meaningful',
	cover=False)
p15=Picture(
	path= 'pic/meaningful/us.jpg',
	category= 'meaningful',
	cover=False)
p16=Picture(
	path= 'pic/meaningful/goals.jpg',
	category= 'meaningful',
	cover=False)
############################################# PIC ----- COVER
p17=Picture(
	path= 'pic/palestineschool.jpg',
	category= 'education',
	cover=True)
p18=Picture(
	path= 'pic/cover.jpg',
	category= 'food',
	cover=True)
p19=Picture(
	path= 'pic/activities.jpg',
	category= 'activity',
	cover=True)
p20=Picture(
	path='pic/meaningful.jpg',
	category= 'meaningful',
	cover=True)
pics=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]
for pic_to_add in pics:
	session.add(pic_to_add)

##############################################

picquestion = QuestAndPic()
picquestion.picture = p1
picquestion.question = q1
picquestionw = QuestAndPic()
picquestionw.picture=p1
picquestionw.question=q2

session.add(picquestion)
session.add(picquestionw)

session.commit()