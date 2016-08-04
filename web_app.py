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
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/<string:category_name>')
def category(category_name):
	pics=session.query(Picture).filter_by(category=category_name, cover=False).all()
	return render_template('category.html',pics=pics)

@app.route('/')
def main_page():
	pics=session.query(Picture).filter_by(cover=True).all()
	return render_template('main_page.html',pics=pics)

@app.route('/<string:category_name>/pictures/<int:pair_id>')
def pictures(category_name,pair_id):
	pair=session.query(Pair).filter_by(id=pair_id).first()
	pic1=session.query(Picture).filter_by(id=pair.pic1_id).first()
	questions=session.query(Question).all()
	pic2=session.query(Picture).filter_by(id=pair.pic2_id).first()
	return render_template('picture.html', pair_id=pair_id, pic1=pic1,pic2=pic2, questions=questions)


@app.route('/submit_answers/<int:pair_id>', methods= ['post'])
def submit_answers(pair_id):
	answers = request.form.keys()
	for answer in answers:
		if answer == 'submit':
			continue
		nat = request.form[answer]
		nat.split("a")[-1]
		answer_id= nat.split("a")[-1]
		question_part =nat.split("a")[0]
		question_id= question_part.split("q")[-1]
		new_answer = Answer(pair_id= pair_id,
						question_id =question_id,
						selected= answer_id)
		session.add(new_answer)
	session.commit()
	return str(request.form)

@app.route('/statistics/<int:picture_id>/<int:question_id>/')
def answer_statistics(pair_id, question_id):

    answers = session.query(Answer).filter_by(pic_id= picture_id, question_id=question_id).all()
    q = session.query(Question).filter_by(id = question_id).one()
    num_answers = len(answers)
    histogram = {'a1': 0, 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0}
    for answer in answers:
        selected_answer = answer.selected
        histogram[selected_answer] += 1
    for answer in histogram.keys():
        histogram[answer] /= num_answers * 100
    return render_template('statistics.html', q=q, answer1=histogram['a1'], answer2=histogram['a2'],answer3=histogram['a3'],answer4=histogram['a4'],answer5=histogram['a5'])





@app.route('/survey')
def survey():
	return render_template('survey.html')
if __name__ == '__main__':
    app.run(debug=True)
