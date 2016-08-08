from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine


from database_setup import Base, Question, Answer, Picture, Pair, Survey#, QuestAndPair


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
session.query(Pair).delete()
#session.query(QuestAndPic).delete()
################################################
#   MAJD YOU WORK ON THIS   #


q1 = Question(

    text = 'Where do you think the left picture was taken ?',
    a1 = 'Israel',
    a2 = 'USA',
    a3 = 'Palestine',
    a4 = 'Syria',
	a5 = 'Other')


q2 = Question(

	text = 'Where do you think the right picture was taken ?',
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
'''
qp = QuestAndPic(
	question_id = q1.id,
	pair_id = 1)
'''
questions=[q1,q2,q3,q4,q5]
for question_to_add in questions:
	session.add(question_to_add)
###############################################
a1=Answer(
	question_id = 1,
    selected='a3',
    nationality = 'Palastinian')

answers=[a1]
for question_to_add in questions:
	session.add(question_to_add)
############################################## PIC ----- FOOD
p1=Picture(
	path='pic/food/israeldessert.jpg',
	category= 'food',
	cover=False,
	discription=''' Stereotype:  Israel only serves Palestinian sweets/desserts.
The first thing you notice is that both desserts look delicious, and each one of them is unique on its own way. Alot of people think that the only good and delicious sweets Israel are Palestinian/Arabian sweets, which is wrong and you can see that by looking at the Israeli sweet shown in the picture.'''
	)

p2=Picture(
	path='pic/food/israelfood.jpg',
	category= 'food',
	cover=False,
	discription='''Stereotype:  Israelis can’t cook even the easiest stuff.
The first thing you notice is how hungry you are, and then you realize that you can’t actually recognize which pizza belongs to Israel or Palestine because they look really similar, and this also can be used as a metaphor to how people are really similar from the inside even if there is a wall between them'''
	)
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
	cover=False,
	discription= '''Stereotype:  All the places that Israel builds are more beautiful than the places that Palestine builds.
The first thought that comes into your mind when you see the pictures is WHICH ONE BELONGS TO WHICH because the two pictures show two beautiful places! So you have to use your luck and answer, if you lucky enough you’ll get it right, if not... well you won’t.'''
	)
p6=Picture(
	path= 'pic/activities/israelcinema.jpg',
	category= 'activity',
	cover=False,
	discription='''Stereotype:  People in Palestine don’t have places to spend time in/have fun.
The first thing you notice about the pictures is that they’re not taken in the same place/rooms, the Israel one is taken in the waiting room but the one in Palestine is taken in the film room. The first thing you think of when you hear Palestine is that they live in camps/ don’t have electricity/ don’t have fun activities but the truth is that they aren’t all like this, of course there are people who live in camps, suffer, don’t have places to spend time in, but there is also people who have these stuff. 
'''
	)
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
	cover=False ,
	 discription='''Stereotype:  Religious people from Israel and Palestine are racist people.
	This stereotype is popular, and alot of people think its true, but the truth is religious people - real religious people who love god and follow everything he said- love all people from all religions! racism is NOT  connected to religion.'''
	)
p10=Picture(
	path= 'pic/education/Israelschool.jpg',
	category= 'education',
	cover=False,
	 discription='''Stereotype:  People in Palestine don’t have appropriate places to learn in/schools.
	The first thing you notice about the pictures is that they’re both taken in classrooms but in different countries. Alot of people believe that in Palestine the schools are horrible and really bad unlike Israel where schools are really good with high education system, but this stereotype is not entirely true because there are alot of good schools in Palestine and we can take the schools in east Jerusalem as an example. '''
	)
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
pair1=Pair(pic1_id =1,
	pic2_id=3
	)
pair2=Pair(pic1_id =2,
	pic2_id=4
	)
pair3=Pair(pic1_id =5,
	pic2_id=7

	)
pair4=Pair(pic1_id =6,
	pic2_id=8 
	)
pair5=Pair(pic1_id =9,
	pic2_id=11
	)
pair6=Pair(pic1_id =10,
	pic2_id=12
	)
pair7=Pair(pic1_id =13,
	pic2_id=15
	)
pair8=Pair(pic1_id =14,
	pic2_id=16
	)
pair9=Pair(pic1_id =17,
	pic2_id=19
	)
pair10=Pair(pic1_id =18,
	pic2_id=20
	)
pairs=[pair1,pair2,pair3,pair4,pair5,pair6,pair7,pair8,pair9,pair10]##############################################################Continu
for pair_to_add in pairs:
	session.add(pair_to_add)
##############################################
'''picquestion = QuestAndPic()
picquestion.picture = p1
picquestion.question = q1
picquestionw = QuestAndPic()
picquestionw.picture=p1
picquestionw.question=q2

session.add(picquestion)
session.add(picquestionw)'''

session.commit()