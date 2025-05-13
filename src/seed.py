from app import app, db
from models import Users, Profiles, People, Planets, Favorites

with app.app_context():
    db.drop_all()
    db.create_all()

    # Crear usuarios y perfiles
    user1 = Users(email="alice@example.com", password="1234")
    user2 = Users(email="bob@example.com", password="5678")
    db.session.add_all([user1, user2])
    db.session.commit()

    profile1 = Profiles(bio="Soy Alice", user_id=user1.id)
    profile2 = Profiles(bio="Soy Bob", user_id=user2.id)
    #user?
    db.session.add_all([profile1, profile2])

    # People
    people1 = People(name="Luke Skywalker", birth_year="19 BBY", gender="Male", hair_color="Blond", height=77, films="A New Hope", vehicles="Snowspeeder", favorites="")
    # teacher2 = Teacher(name="Profesora Y")
    # db.session.add_all([people1, people2])
    # db.session.commit()



    # Planets
    # course1 = Course(title="Matemáticas", teacher_id=teacher1.id)
    # course2 = Course(title="Ciencias", teacher_id=teacher2.id)
    # db.session.add_all([course1, course2])
    # db.session.commit()

    # Favorites

    # enrollment1 = Enrollment(student_id=student1.id, course_id=course1.id)
    # enrollment2 = Enrollment(student_id=student2.id, course_id=course2.id)
    # db.session.add_all([enrollment1, enrollment2])

    db.session.commit()
    print("✅ Datos sembrados correctamente.")