import unittest
import rk1

class testRk(unittest.TestCase):
    def setUp(self):
        self.test1 = [('switch/case', 10, 'Условие', 'Python'),
                      ('while', 5, 'Цикл', 'Python'),
                      ('if', 2, 'Условие', 'Python'),
                      ('Goto', 4, 'Безусловный переход', 'Pascal')]
        self.test2 = [('Python', 5.67),
                      ('C++', 4.0),
                      ('Pascal', 4.0)]
        self.test3 = [('while', 'Python'),
                      ('while', 'C++'),
                      ('while', 'Pascal'),
                      ('while', 'Java'),
                      ('while', 'C'),
                      ('while', 'Delphi')]
    def test1_rk(self):
        self.assertEqual(rk1.task1(rk1.one_to_many),self.test1)
    def test2_rk(self):
        self.assertEqual(rk1.task2(rk1.one_to_many),self.test2)
    def test3_rk(self):
        self.assertEqual(rk1.task3(rk1.many_to_many),self.test3)

if __name__=='__main__':
    unittest.main()
