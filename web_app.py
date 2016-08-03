#          http://127.0.0.1:5000/
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base, Picture, Answer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route('/category/<string:category_name>')
def category(category_name):
	pics=session.query(Picture).filter_by(category=category_name).all()
	return render_template('category.html',pics=pics)

@app.route('/')
def main_page():
	pics=session.query(Picture).filter_by(category='cover').all()
	return render_template('main_page.html',pics=pics)

@app.route('/pictures/<int:picture_id>')
def pictures(picture_id):
	pic=session.query(Picture).filter_by(id=picture_id).first()
	return render_template('questions.html',pic=pic)


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

@app.route('/questions')
def questions():
	return render_template('questions.html')
	


if __name__ == '__main__':
    app.run(debug=True)
