import sys
from Crypto4Christmas import Crypto4Christmas

student_id = sys.argv[1] # "1231023"
c = Crypto4Christmas(student_id)

c.at_position(1)

c.task1()
c.task2()
c.task3()
c.task4()
c.task5()
c.task6()

