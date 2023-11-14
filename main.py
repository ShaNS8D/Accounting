import sys
import datetime
sys.path.insert(1, 'C:\\Users\\shalaevskiyns\\Documents\\Доки по учебе\\Homework\\Accounting\\application')
import salary
from db.people import get_employees


if __name__ == '__main__':
    time = datetime.date.today()
    print(time)
    sal = salary.calculate_salary()
    print(sal)
    peo = get_employees()
    print(peo)
