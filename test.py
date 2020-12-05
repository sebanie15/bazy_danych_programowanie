from sqlalchemy import  create_engine


def add_users(engine, users):
    results = []
    for (user_id, name, nick) in users:
        result = engine.execute(
            f"Insert Into Users values('{user_id}', '{name}', '{nick}')"
        )
        results.append(result)

    return results


def add_department(engine, name, manager):
    return engine.execute(
        f"Insert Into Departments ('name', 'manager') values('{name}', '{manager}')"
    )


def add_position(engine, name, manager):
    return engine.execute(
        f"Insert Into Departments ('name', 'manager') values('{name}', '{manager}')"
    )


if __name__ == '__main__':

    # creating a object to comunicate with database
    engine = create_engine('sqlite:///:memory:', echo=True)

    create_users = engine.execute("CREATE TABLE Users(id int, name varchar, nickname varchar)")
    print(create_users)

    users = [
        (1, "Roman", "magneton_bora"),
        (2, "Sam", "big_daddy"),
        (3, "Sara", "lovely_kitty"),
       ]

    add_users(engine, users)

    result = engine.execute("Select * from Users").fetchall()

    for user in result:
        print(f"{user.id}, {user.name}, {user.nickname}")

    employees = """
    CREATE TABLE Employees(
    id int  unique , 
    first_name varchar(30) not null,
    last_name varchar(30) not null,
    position_id int not null,
    salary_id int not null,
    PRIMARY KEY (id),
    FOREIGN KEY (position_id) REFERENCES Positions(id),
    FOREIGN KEY (salary_id) REFERENCES Salaries(id)
    );
    """
    positions = """
    CREATE TABLE Positions(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name varchar(30) not null,
    department_id int not null,
    FOREIGN KEY (department_id) REFERENCES Departments(id));
    """
    salaries = """
    CREATE TABLE Salaries(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    amount double not null
    );
    """
    departments = """
    CREATE TABLE Departments(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name varchar(30) not null,
    manager varchar(30)
    );
    """
    engine.execute(departments)
    engine.execute(salaries)
    engine.execute(positions)
    engine.execute(employees)

    add_department(engine, "Departament spraw trudnych", "Adam Harmasz")
    add_department(engine, "Departament spraw trudnych", "Adam Harmasz")

    department_result = engine.execute("SELECT * FROM Departments").fetchall()
    print(department_result)
