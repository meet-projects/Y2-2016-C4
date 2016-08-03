#          http://127.0.0.1:5000/
from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
### Add your tables here!
# For example:
# from database_setup import Base, Potato, Monkey
from database_setup import Base, Picture

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

if __name__ == '__main__':
    app.run(debug=True)
