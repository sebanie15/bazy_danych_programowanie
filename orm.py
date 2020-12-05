from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    fullname = Column(String(30))
    nickname = Column(String(15))

    def __repr__(self):
        return f"User(id: {self.id}, name: {self.name}, fullname: {self.fullname}, nickname: {self.nickname}"


if __name__ == '__main__':

    # creating a object to comunicate with database
    engine = create_engine('sqlite:///:memory:', echo=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    print(Base)
    print(User)
    print(User.__dict__)

    edward = User(name='Ed', fullname='Edward Johns', nickname='big_daddy')
    adam = User(name='Adam', fullname='Edward Johns', nickname='big_daddy')
    igor = User(name='Igor', fullname='Edward Johns', nickname='big_daddy')
    session.add(edward)
    session.add(adam)
    session.add(igor)
    # session.add_all([edward, adam, igor])
    session.commit()
    # session.rollback()

    # print(edward)
    # query = session.query(User)
    print(session.query(User).all())
    # print(session.query(User).filter(text("id=2")).one())

    bob = User(name='Bob', fullname='Bob Johns', nickname='big_bob')
    session.add(bob)
    session.commit()
    bob.nickname = 'bobby42'
    print(session.dirty)
    print(session.dirty)
    print(session.query(User).all())
    print(session.dirty)

