

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.grades = {}
        self.started_courses = []
        self.finished_courses = []

    def rate_a_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.started_courses or course in self.finished_courses) and course in lecturer.coureses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        self.total = 0
        self.count = 0

        if '' in self.grades.keys() != False:
            for i in self.grades.values():
                self.total += sum(i)
                self.count = len(i)
            self.tc = self.total / self.count
        else:
            self.tc = 'оценок нет'
        str_started_courses = ', '.join(self.started_courses)
        str_fin_cour = ', '.join(self.finished_courses)

        return 'Имя: {}\nФамилия: {}\nСредняя оценка: {}\nСписок начатых курсов: {}\nЗавершены курсы: {}'.format(self.name, self.surname, self.tc, str_started_courses, str_fin_cour)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.coureses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_sudent(self, student, course, grade):
        if isinstance(student, Student) and course in student.started_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        return 'Имя: {}\nФамилия: {}\n'.format(self.name, self.surname)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        total = 0
        count = 0
        if self.grades != None:
            for i in self.grades.values():
                total += sum(i)
                count = len(i)
            tc = total / count
        else:
            tc = 'оцено нет'

        return 'Имя: {}\nФамилия: {}\nСредняя оценка за лекции {}'.format(self.name, self.surname,tc )

student1 = Student('Iosif', 'Dzhugashvily', 'm')
student2 = Student('Vladimir', 'Ulianov', 'm')
student1.started_courses.append('Python')
student2.started_courses.append('web')
student2.started_courses.append('Python')
student2.finished_courses.append('Введение в программирование')
print(f'Курсы студента {student1.started_courses}')
print(f'Оценки лектора {student1.surname} {student1.grades}')

lectourer1 = Lecturer('Karl', 'Marx')
lectourer1.coureses_attached.append('Python')
print(f'Курсы лектора {lectourer1.coureses_attached}')


student1.rate_a_lecturer(lectourer1, 'Python', 5)
student2.rate_a_lecturer(lectourer1, 'Python', 4)
student2.rate_a_lecturer(lectourer1, 'web', 4)
print(f'Оценки лектора {lectourer1.surname} {lectourer1.grades}')
reviewer1 = Reviewer('Friedrich', 'Engels')
reviewer1.rate_sudent(student1, 'Python', 3)
print(student1.grades)
print()
print(reviewer1)
print()
print(lectourer1)
print()
print(student1)
print()
print(student2)