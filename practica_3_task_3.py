"""
Задание №3
- Доработаем задача про студентов
- Создать базу данных для хранения информации о студентах и их оценках в
учебном заведении.
- База данных должна содержать две таблицы: "Студенты" и "Оценки".
- В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
и email.
- В таблице "Оценки" должны быть следующие поля: id, id студента, название
предмета и оценка.
📌 Необходимо создать связь между таблицами "Студенты" и "Оценки".
📌 Написать функцию-обработчик, которая будет выводить список всех
студентов с указанием их оценок.
"""
from models_practica_3_task_1 import db, Students, Faculties
from flask import Flask, render_template


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


#with app.app_context():
#    db.create_all()


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('database has been created')


@app.cli.command("add-students")
def add_students():

    count: int = 5

    for student in range(1, count + 1):
       new_students = Students(name=f'student_name_{student}',
                               surname=f'student_surname_{student}',
                               age=18,
                               gender='MALE',
                               group=student,
                               faculty_id=student)
       db.session.add(new_students)
    db.session.commit()

    for faculty in range(1, count + 1):
        new_faculty = Faculties(title_faculty=f'title_faculty_{faculty}')
        db.session.add(new_faculty)
    db.session.commit()
    print('database is full')


@app.route('/')
def index():

    students = Students.query.all()
    faculty_one = Faculties.query.get(1)

    context = {
        'title_pag': 'Вывод информации о студентах',
        'students': students,
        'faculty_one': faculty_one
    }
    return render_template('practica_3_task_1_all_students.html', **context)


if __name__ == '__main__':
    app.run()
