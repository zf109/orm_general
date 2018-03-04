from db_models.models import Employee, Engineer, Manager, Company
from db_models.backend_db import db_session

def main():
    with db_session() as sess:
        techservice = Company(name="247TechService")
        engineer = Engineer(name="techy1", specialty="IT service", grade="senior peasant")
        manager = Manager(name="manager1", industry="financial service", grade="peasant master")
        employee = Employee(name="somebody", grade="peasant")
        employee.company = techservice
        engineer.company = techservice
        manager.company = techservice
        sess.add(techservice)
        sess.add(employee)
        sess.add(manager)
        sess.add(engineer)
        sess.commit()
        print("commited")

if __name__ == "__main__":
    main()
