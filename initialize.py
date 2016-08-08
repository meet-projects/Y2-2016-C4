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

    text = 'Which nationality do you support ?',
    a1 = 'Israel',
    a2 = 'Not against palestine but not with them',
    a3 = 'Palestine',
    a4 = 'Not against israel but nt with them ',
	a5 = 'I am with both of them')


q2 = Question(

	text = 'Have you ever communicat with people from other nationalities ?',
	a1 = 'No, never',
	a2 = 'Rarly',
	a3 = 'Sometimes',
	a4 = 'Yes, alot',
	a5 = 'often')

q3 = Question(
	text = 'Why ?',
	a1 = 'I am afraid of them',
	a2 = 'They are racist' ,
	a3 = 'I have never had the chance to meet them',
	a4 = 'There is no difference between us',
	a5 = 'Other')
	
q4 = Question(
	text= 'If you se people from other nationalities would you recognize them ?',
	a1 = 'No, we are all human being',
	a2 = 'yes, they will look diffient',
	a3 ='we are the same',
	a4 = 'Other')


q5 = Question(
	text = 'How did it make you feel ?',
	a1 = 'Happy',
	a2 = 'Excited',
	a3 = 'Scared',
	a4 = 'Interested',
	a5 = 'Not sure')
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