from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Employees(Base):
    __tablename__ = 'Employees'
    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    position_id = Column(Integer, ForeignKey("Positions.position_id"), nullable=False)
    salary_id = Column(Integer, ForeignKey("Salaries.salary_id"), nullable=False)

    def __repr__(self):
        return f"Employee(" \
               f"ID: {self.employee_id}," \
               f"Full name: {self.first_name} {self.last_name})"


class Positions(Base):
    __tablename__ = 'Positions'
    position_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    department_id = Column(Integer, ForeignKey("Departments.department_id"), nullable=False)

    def __repr__(self):
        return f"Position(" \
               f"ID: {self.position_id}, " \
               f"Name: {self.name})"


class Salaries(Base):
    __tablename__ = 'Salaries'
    salary_id = Column(Integer, primary_key=True)
    amount = Column(Numeric, nullable=False)

    def __repr__(self):
        return f"Salary(" \
               f"ID: {self.salary_id}," \
               f"Amount: {self.amount})"


class Departments(Base):
    __tablename__ = 'Departments'
    department_id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    manager_id = Column(Integer, ForeignKey("Employees.employee_id"), nullable=True)

    def __repr__(self):
        return f"Department(" \
               f"ID: {self.department_id}," \
               f"Name: {self.name}," \
               f"Manager ID: {self.manager_id}"


if __name__ == '__main__':

    engine = create_engine('sqlite:///:memory:', echo=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    department = Departments(name="Departament spraw trudnych")
    position = Positions(name="Trener", department_id=1)
    salary = Salaries(amount=15000.0)
    employee = Employees(first_name="Adam", last_name="Harmasz", position_id=1, salary_id=1)
    session.add_all([department, position, salary, employee])
    session.commit()
    print(session.query(Departments).all())
    print(session.query(Employees).all())
    print(session.query(Positions).all())
    print(session.query(Salaries).all())
