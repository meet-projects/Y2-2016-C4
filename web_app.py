#          http://127.0.0.1:5000/
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base, Picture, Answer, Question, Pair

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route('/<string:category_name>')
def category(category_name):
	pics=session.query(Picture).filter_by(category=category_name, cover=False).all()
	return render_template('category.html',pics=pics)

@app.route('/')
def main_page():
	pics=session.query(Picture).filter_by(cover=True).all()
	return render_template('main_page.html',pics=pics)

@app.route('/<string:category_name>/pictures/<int:picture_id>')
def pictures(picture_id,category_name):
	pic1=session.query(Picture).filter_by(id=picture_id).first()
	pair=session.query(Pair).filter_by(pic1_id=pic1.id).first()
	#print(pic1.id)
	pic2=session.query(Picture).filter_by(id=pair.pic2_id).first()
	return render_template('picture.html',pic1=pic1,pic2=pic2, questions=questions)


@app.route('/submit_answers/<int:picture_id>', methods= ['post'])
def submit_answers(picture_id):
	answers = request.form.keys()
	for answer in answers:
		if answer == 'submit':
			continue 
		nat = request.form[answer]
		nat.split("a")[-1]
		answer_id= nat.split("a")[-1]
		question_part =nat.split("a")[0]
		question_id= question_part.split("q")[-1]
		new_answer = Answer(pic_id= picture_id,
						question_id =question_id,
						selected= answer_id)
		session.add(new_answer)
	session.commit()



	return str(request.form)

'''
@app.route('/questions')
def questions():
	return render_template('questions.html')
'''
@app.route('/statistics/<int:picture_id>')
def answer_statistics(picture_id):

    temp = session.query(Answer).filter_by(pic_id= picture_id).all()
    count = len(temp)
    q1 = session.query(Answer).filter_by(pic_id= picture_id,selected = 'a1').all()
    count1=len(q1)
    answer1= count1/count *100
    q2 = session.query(Answer).filter_by(pic_id= picture_id,selected = 'a2').all()
    count1=len(q2)
    answer2= count2/count *100
    q3 = session.query(Answer).filter_by(pic_id= picture_id,selected = 'a3').all()
    count1=len(q3)
    answer3= count3/count *100
    q4 = session.query(Answer).filter_by(pic_id= picture_id,selected = 'a4').all()
    count1=len(q4)
    answer4= count4/count *100
    q5 = session.query(Answer).filter_by(pic_id= picture_id,selected = 'a5').all()
    count1=len(q5)
    answer5= count5/count *100
    session.commit()
  



if __name__ == '__main__':
    app.run(debug=True)
