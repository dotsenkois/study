

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

        if self.grades.keys():
            for i in self.grades.values():
                self.total += sum(i)
                self.count = len(i)
            self.tc = self.total / self.count
        else:
            self.tc = 'оценок нет'
        str_started_courses = ', '.join(self.started_courses)
        if self.finished_courses:
            str_fin_cour = ', '.join(self.finished_courses)
        else:
            str_fin_cour = 'Студент не окончил ни одного курса'

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
        if isinstance(student, Student) and (course in student.started_courses or course in student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка.'.format())

    def __str__(self):
        return 'Имя: {}\nФамилия: {}\n'.format(self.name, self.surname)

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        total = 0
        count = 0
        if self.grades:
            for i in self.grades.values():
                total += sum(i)
                count = len(i)
            tc = total / count
        else:
            tc = 'оценок нет'
        return 'Имя: {}\nФамилия: {}\nСредняя оценка за лекции {}'.format(self.name, self.surname, tc)

def middle_grade(course, *args):
    total = 0
    count = 0
    msg = ''
    for arg in args:
        if isinstance(arg, Student):
            msg = 'Средний балл за домашнее задание по курсу {} составляет - {} баллов'
        else:
            msg = 'Средний балл за лекции по курсу {} составляет - {} баллов'

        if course in arg.grades:
            total += sum(arg.grades[course])
            count += 1

    if count > 0:
        print(msg.format(course, total/count))
    return

student1 = Student('Iosif', 'Dzhugashvily', 'm')
student2 = Student('Vladimir', 'Ulianov', 'm')

student1.started_courses.append('Python')
student1.started_courses.append('Web')
student1.finished_courses.append('Frontend')
student1.finished_courses.append('C#')

student2.started_courses.append('Frontend')
student2.started_courses.append('C#')
student2.finished_courses.append('Frontend')
student2.finished_courses.append('Pyhon')

lectourer1 = Lecturer('Karl', 'Marx')
lectourer2 = Lecturer('Nikina', 'Khrushchov')
lectourer1.coureses_attached.append('Python')
lectourer1.coureses_attached.append('Frontend')

lectourer2.coureses_attached.append('Web')
lectourer2.coureses_attached.append('C#')

student1.rate_a_lecturer(lectourer1, 'Python', 5)
student1.rate_a_lecturer(lectourer2, 'Web', 5)
student2.rate_a_lecturer(lectourer1, 'Python', 4)
student2.rate_a_lecturer(lectourer2, 'C#', 4)

reviewer1 = Reviewer('Friedrich', 'Engels')
reviewer2 = Reviewer('Leonid', 'Brezhnev')
reviewer1.rate_sudent(student1, 'Python', 3)
reviewer2.rate_sudent(student1, 'C#', 10)
reviewer1.rate_sudent(student1, 'C#', 3)
reviewer2.rate_sudent(student2, 'Python', 10)

reviewer1.rate_sudent(student1, 'Web', 3)
reviewer2.rate_sudent(student2, 'Frontend', 10)
reviewer1.rate_sudent(student1, 'Frontend', 3)
reviewer2.rate_sudent(student2, 'Web', 10)

print(student1.grades)
print(student2.grades)

print()
print(reviewer1)
print()
print(lectourer1)
print()
print(reviewer2)
print()
print(lectourer2)
print()
print(student1)
print()
print(student2)
print()

middle_grade('Web', student1, student2)
middle_grade('C#', lectourer1, lectourer2)
