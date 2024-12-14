import sqlite3 as sqlite
import os

#print(os.listdir())



class StudentsDB:

    def __init__(self, file):
        self.file = file
        
        self.connection = sqlite.connect(self.file)
        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):
        with self.connection:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS students_data (
                      firstname TEXT,
                      secondname TEXT,
                      lastname TEXT,
                      age INTEGER,
                      s_class TEXT
                ) 
            """)

    def add_student(self, f_name:str=None, s_name:str=None,lastname:str=None, age:int=None, s_class:str=None):
        # use the with keyword so as to close the db authomatically after the code block
        # is executed otherwise, you will explicitly close like this -> self.connection.close()
        with self.connection:
            self.cursor.execute("INSERT INTO students_data (firstname, secondname, lastname, age, s_class) VALUES (?, ?, ?, ?, ?)",
                                (f_name.lower(), s_name.lower(), lastname.lower(), age, s_class.lower()))
        return f_name + ' added'

    def get_students_by_firstname(self, first_name:str):
        '''
        :param
          -  first_name(str): first name of students to be returned.
        :return list of tuples of students bearing the specified first_name if there is else []
        '''
        self.cursor.execute("SELECT * FROM students_data WHERE firstname=:first",
                            {'first':first_name.lower()})
        return self.cursor.fetchall()

    def get_students_by_secondname(self, second_name:str):
        '''
        :param
          -  second_name(str): second name of students to be returned.
        :return list of tuples of students bearing the specified second_name if there is else []
        '''
        self.cursor.execute('SELECT * FROM students_data WHERE secondname=:second',
                            {'second': second_name.lower()})
        return self.cursor.fetchall()

    def get_students_by_lastname(self, lastname:str):
        '''
        :param
          -  lastname(str): lastname name of students to be returned.
        :return list of tuples of students bearing the specified lastname if there is else []
        '''
        self.cursor.execute('SELECT * FROM students_data WHERE lastname=:lastname',
                            {'lastname': lastname.lower()})
        return self.cursor.fetchall()

    def get_students_by_age(self, age:int=0):
        '''
        :param
          -  age(int): age of students to be returned.
        :return list of tuples of students having the specified age if there is else []
        '''
        self.cursor.execute('SELECT * FROM students_data WHERE age=:age', {'age': age})
        return self.cursor.fetchall()

    def get_students_by_class(self, s_class):
        '''
        :param
          -  s_class(str): class of students to be gotten.
        :return list of tuples of students in the specified class if there is else []
        '''
        self.cursor.execute('SELECT * FROM students_data WHERE s_class=:s_class',
                            {'s_class': s_class.lower()})
        return self.cursor.fetchall()

    def update_student_age(self, lastname:str=None, new_age:int=1):
        '''
         update student bearing the specified firstname or secondn_name age
        :param
          -  new_age(int): new age to replace old age with.
          - lastname(str): lastname of the student to be updated.
        :return None
        '''
        # search if surname is in table of students in the database
        is_valid = self.get_students_by_lastname(lastname)
        if len(is_valid) <= 0: return 'Student not found!'
        with self.connection:
            self.cursor.execute("UPDATE students_data SET age=:age WHERE lastname=:lastname",
                            {'age':new_age, 'lastname':lastname.lower()})
            return 'Updated!'

    def update_student_class(self, lastname:str, new_class:str):
        '''update the class of student'''
        # search if surname is in table of students in the database
        is_valid = self.get_students_by_lastname(lastname)
        if len(is_valid) <= 0: return '{} not found!'.format(lastname)
        with self.connection:
            self.cursor.execute('UPDATE students_data SET s_class=:new_class WHERE lastname=:lastname',
                                {'new_class': new_class, 'lastname': lastname})
            return 'Updated!'
 
    def remove_student(self, lastname:str):
        '''remove specific student with the given name'''
        with self.connection:
            self.cursor.execute('DELETE FROM students_data WHERE lastname=:lastname',
                                {'lastname': lastname.lower()})


if __name__ == '__main__':
    s1 = StudentsDB('dbfile1.db')
    #print(s1.add_student(f_name='Daniel', s_name='Olatunde', lastname='Fatokun', age=18, s_class='ss3'))
    #print(s1.get_students_by_lastname("fatokun"))
    #a = s1.get_students_by_age(20)
    #print(s1.update_student_age('fatokun', 20))
    #print(s1.update_student_class('fatokun', 'ss2'))
    #s1.remove_student('fatokun')     


    



