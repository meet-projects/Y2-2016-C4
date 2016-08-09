from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


'''
class QuestAndPair(Base):
    __tablename__ = 'quest_and_pair'
    id = Column(Integer, primary_key=True)
    pair_id = Column(Integer, ForeignKey('pair.id'))
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship('Question')
    pair = relationship('Pair')
'''
class Question(Base):
    __tablename__ = 'question'
    id = Column(Integer, primary_key=True)
    text = Column(String(15))
    a1 = Column(String(30))
    a2 = Column(String(60))
    a3 = Column(String(30))
    a4 = Column(String(30))
    a5 = Column(String(30))


class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    pair_id = Column(Integer, ForeignKey('pair.id'))
    question_id = Column(Integer, ForeignKey('question.id'))
    selected=Column(String)
    nationality = Column(String(15))


class Picture(Base):
    __tablename__ = 'picture'
    id = Column(Integer, primary_key=True)
    path = Column(String)
    category = Column(String)
    cover = Column(Boolean)
    discription=Column(String)

class Pair(Base):
    __tablename__ = 'pair'
    id=Column(Integer, primary_key=True)
    pic1_id =Column(Integer, ForeignKey('picture.id'))
    pic2_id=Column(Integer, ForeignKey('picture.id'))


class Survey(Base):
    __tablename__ = 'survey'
    id=Column(Integer, primary_key=True)
    name=Column(String)
    nationality=Column(String)
    email=Column(String)
    phone=Column(String)
    enjoy=Column(String)
    feedback=Column(String)


class Comment(Base):
    __tablename__ = 'comment'
    id=Column(Integer, primary_key=True)
    pair_id=(Integer, ForeignKey('pair.id'))
    nationality=(String)
    author=Column(String)
    text=Column(String)

        
