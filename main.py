class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(
                lecturer, Lecturer
        ) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_1:
                lecturer.grades_1[course] += [grade]
            else:
                lecturer.grades_1[course] = [grade]
        else:
            return 'Ошибка'

    def __middle__(self):
        sum = 0
        count = 0
        for i in self.grades.values():
            for j in i:
                sum += j
                count += 1
        return sum / count

    def __str__(self):
        r = f'Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания: {round(self.__middle__(), 2)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return r

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        n = self.__middle__() > other.__middle__()
        if n == True:
            return f'Средняя оценка выше у студента {self.name}'
        else:
            return f'Средняя оценка выше у студента {other.name}'


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_lecturer(self):
        return super().rate_lecturer


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_1 = {}

    def __middle__(self):
        sum = 0
        count = 0
        for i in self.grades_1.values():
            for j in i:
                sum += j
                count += 1
        return sum / count

    def __str__(self):
        rounding = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{round(self.__middle__(), 2)}\n'
        return rounding

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        n = self.__middle__() > other.__middle__()
        if n == True:
            return f'Средняя оценка выше у лектора {self.name} '
        else:
            return f'Средняя оценка выше у лектора {other.name}'


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        inf = f'Имя: {self.name}\nФамилия: {self.surname}'
        return inf


student_1 = Student('Albert', 'Einstein', 'man')
student_2 = Student('Nikola', 'Tesla', 'man')
student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']
student_2.finished_courses += ['Git']
cool_reviewer = Reviewer('Childish', 'Gambino')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(student_1, 'Python', 10)
cool_reviewer.rate_hw(student_1, 'Python', 9)
cool_reviewer.rate_hw(student_1, 'Python', 10)
cool_reviewer.rate_hw(student_2, 'Python', 8)
cool_reviewer.rate_hw(student_2, 'Python', 9)
cool_reviewer.rate_hw(student_2, 'Python', 10)

print(student_1.grades)
print(student_2.grades)

lecturer_1 = Lecturer('Eric', 'Xavier')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Eric', 'Cartman')
lecturer_2.courses_attached += ['Python']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Python', 8)

student_2.rate_lecturer(lecturer_2, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 8)

print(lecturer_1.grades_1)
print(lecturer_2.grades_1)

print("")
print(cool_reviewer)

print("")
print(lecturer_1)
print(lecturer_2)

print(student_1)
print("")
print(student_2)
print("")
print(student_1 > student_2)
print(lecturer_1 < lecturer_2)
print("")


def average_student(list, name_course):
    sum = 0
    count = 0
    for i in list:
        for j in i.grades[name_course]:
            sum += j
            count += 1
    return round(sum / count, 2)


def average_lecturer(list, name_course):
    sum = 0
    count = 0
    for i in list:
        for j in i.grades_1[name_course]:
            sum += j
            count += 1
    return round(sum / count, 2)


# print(average_student([student_1, student_2], 'Python'))
# print(average_lecturer([lecturer_1, lecturer_2], 'Python'))

result_1 = average_student([student_1, student_2], 'Python')
result_2 = average_lecturer([lecturer_1, lecturer_2], 'Python')

print(f'Средняя оценка у студентов: {result_1}')
print(f'Средняя оценка у лекторов: {result_2}')