from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()



class QuestAndPic(Base):
    __tablename__ = 'quest_and_pic'
    id = Column(Integer, primary_key=True)
    pic_id = Column(Integer, ForeignKey('picture.id'))
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship('Question')
    picture = relationship('Picture')

class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    pic_id = Column(Integer, ForeignKey('picture.id'))
    text = Column(String(15))
    a1 = Column(String(30))
    a2 = Column(String(60))
    a3 = Column(String(30))
    a4 = Column(String(30))
    a5 = Column(String(30))


class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    pic_id = Column(Integer)
    question_id = Column(Integer, ForeignKey('question.id'))
    selected=Column(String)
    nationality = Column(String(15))


class Picture(Base):
    __tablename__ = 'picture'
    id = Column(Integer, primary_key=True)
    pic_name = Column(String)
    path = Column(String)
    category = Column(String)
    cover = Column(Boolean)
    questions = relationship('Question', secondary='quest_and_pic', uselist=True)
