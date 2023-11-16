import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    time = datetime.date.today()
    print(time)
    sal = calculate_salary()
    peo = get_employees()

