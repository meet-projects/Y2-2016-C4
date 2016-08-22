#          http://127.0.0.1:5000/
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base, Picture, Answer, Question, Pair, Survey, Comment

from sqlalchemy import create_engine,or_
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
    return render_template('category.html',pics=pics, category_name=category_name)
    
@app.route('/')
def main_page():
    pics=session.query(Picture).filter_by(cover=True).all()
    return render_template('main_page.html',pics=pics)

@app.route('/<string:category_name>/pictures/<int:pic_id>')
def pictures(category_name,pic_id):
    or_condition = or_(Pair.pic1_id==pic_id, Pair.pic2_id==pic_id)
    pair=session.query(Pair).filter(or_condition).first()
    pic1=session.query(Picture).filter_by(id=pair.pic1_id).first()
    pic2=session.query(Picture).filter_by(id=pair.pic2_id).first()
    questions=session.query(Question).all()
    return render_template('picture.html', pair_id=pair.id, pic1=pic1,pic2=pic2, questions=questions, pair_discription=pic1.discription)


@app.route('/submit_answers/<int:pair_id>', methods= ['post'])
def submit_answers(pair_id):
    answers = request.form.keys()
    for i in range(len(answers)):
        if answers[i] == 'submit':
            continue
        nat = request.form[answers[i]]
        nat.split("a")[-1]
        answer_id= nat.split("a")[-1]
        question_part =nat.split("a")[0]
        question_id= question_part.split("q")[-1]
        new_answer = Answer(pair_id= pair_id,
                        question_id =i+1,
                        selected= answer_id,
                        nationality=request.form['nationality'])
        session.add(new_answer)
    session.commit()
    return redirect(url_for('answer_statistics',pair_id=pair_id))

@app.route('/statistics/<int:pair_id>/')
def answer_statistics(pair_id):
    questions=session.query(Question).all()
    statistics = {}
    for q in questions:
        question_id = q.id
        '''print
        print (question_id)
        print (pair_id)
        print'''
        answers = session.query(Answer).filter_by(pair_id=pair_id, question_id=question_id).all()
        num_answers = float(len(answers))
        #print('#######################')
        #print(len(answers))
        histogram = {'a1': 0, 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0}
        totals={'a1': 0, 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0}
        n_dic={'Israeli':{'a1': 0, 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0}, 'Palestinian':{'a1': 0, 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0}, 'Other':{'a1': 0, 'a2': 0, 'a3': 0, 'a4': 0, 'a5': 0}}
        for answer in answers:
                if answer.selected.isdigit():
                    n_dic[answer.nationality]['a'+answer.selected] += 1
                    totals['a'+answer.selected]+=1
        for nationality in n_dic.keys():
            for answer in n_dic[nationality]:
                if totals[answer]!=0:
                    n_dic[nationality][answer]*=100.0/totals[answer]
                    n_dic[nationality][answer]=round(n_dic[nationality][answer]*1000)/1000.0

        statistics[q.id] = n_dic
        #print n_dic

    pair=session.query(Pair).filter_by(id=pair_id).first()
    pic1=session.query(Picture).filter_by(id=pair.pic1_id).first()
    
    pic2=session.query(Picture).filter_by(id=pair.pic2_id).first()
    return render_template('statistics.html', q=q, pic1=pic1, pic2=pic2, questions=questions, stats=statistics)






@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/submit_survey', methods= ['post'])
def submit_survey():
    answer_nationality=request.form['nationality']
    answer_name=request.form['name']
    answer_phone=request.form['phone']
    answer_email=request.form['email']
    answer_enjoy=request.form['enjoy']
    answer_feedback=request.form['feedback']
    survey_answers=Survey(
        name=answer_name,
        nationality=answer_nationality,
        phone=answer_phone,
        email=answer_email,
        enjoy=answer_enjoy,
        feedback=answer_feedback)
    session.add(survey_answers)
    session.commit()
    pics=session.query(Picture).filter_by(cover=True).all()
    return redirect(url_for('main_page',pics=pics))

if __name__ == '__main__':
    app.run(debug=True)
