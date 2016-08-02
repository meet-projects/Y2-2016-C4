from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
@app.route('/food')
def food():
	return render_template('category_food.html')

@app.route('/activity')
def activity():
	return render_template('category_activity.html')
@app.route('/education')
def education():
	return render_template('category_education.html')


@app.route('/')
def main():
    return render_template('main_page.html')


if __name__ == '__main__':
    app.run(debug=True)
