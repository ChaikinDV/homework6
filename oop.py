class Student:
    def __init__(self, name, surname, gender):
        self.grade_student = []
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle(self):
        for v in self.grades.values():
            self.grade_student.extend(v)
        middle_grade = round(sum(self.grade_student) / len(self.grade_student), 2)
        return middle_grade

    def __str__(self):
        conclusion = f'Имя студента: {self.name}\nФамилия студента: {self.surname}\nСредняя оценка: {self.middle()}\n' \
                     f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
                     f'Завершенные курсы: {self.finished_courses}'
        return conclusion

    def __lt__(self, next):
        if self.middle() > next.middle():
            print(f'Лучший студент - {self.name} {self.surname}')
        else:
            print(f'Лучший студент - {next.name} {next.surname}')
        return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_lecturer = []
        self.grades = {}

    def middle(self):
        for v in self.grades.values():
            self.grade_lecturer.extend(v)
        middle_grade = round(sum(self.grade_lecturer) / len(self.grade_lecturer), 2)
        return middle_grade

    def __str__(self):
        conclusion = f'Имя лектора: {self.name}\nФамилия лектора: {self.surname}\nСредняя оценка за лекции: {self.middle()}'
        return conclusion

    def __lt__(self, next):
        if self.middle() > next.middle():
            print(f'Лучший лектор - {self.name} {self.surname}')
        else:
            print(f'Лучший лектор - {next.name} {next.surname}')
        return


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        conclusion = f'Имя проверяющего: {self.name}\nФамилия проверяющего: {self.surname}'
        return conclusion


first_student = Student('Александр', 'Иванов', 'мужчина')
second_student = Student('Полина', 'Зуева', 'женщина')
first_student.courses_in_progress += ['Python', 'Git']
second_student.courses_in_progress += ['Python', 'Git']
first_student.finished_courses += ['Введение в программирование']
second_student.finished_courses += ['Основы языка']

first_mentor = Mentor('Олег', 'Сидоров')
second_mentor = Mentor('Ольга', 'Петрова')
first_mentor.courses_attached += ['Python', 'Git']
second_mentor.courses_attached += ['Python', 'Git']

first_lecturer = Lecturer('Иван', 'Сусанин')
second_lecturer = Lecturer('Андрей', 'Евдокимов')
first_lecturer.courses_attached += ['Python', 'Git']
second_lecturer.courses_attached += ['Python', 'Git']

first_reviewer = Reviewer('Михаил', 'Польский')
second_reviewer = Reviewer('Вениамин', 'Рубашкин')
first_reviewer.courses_attached += ['Python', 'Git']
second_reviewer.courses_attached += ['Python', 'Git']

first_student.rate_hw(first_lecturer, 'Python', 8.9)
first_student.rate_hw(first_lecturer, 'Python', 7)
first_student.rate_hw(first_lecturer, 'Python', 5.5)
first_student.rate_hw(first_lecturer, 'Git', 9.9)
first_student.rate_hw(first_lecturer, 'Git', 4.3)
first_student.rate_hw(first_lecturer, 'Git', 6.1)
second_student.rate_hw(second_lecturer, 'Python', 5.2)
second_student.rate_hw(second_lecturer, 'Python', 10)
second_student.rate_hw(second_lecturer, 'Python', 3.8)
second_student.rate_hw(second_lecturer, 'Git', 7.4)
second_student.rate_hw(second_lecturer, 'Git', 9.2)
second_student.rate_hw(second_lecturer, 'Git', 8.4)

first_reviewer.rate_hw(first_student, 'Python', 0)
first_reviewer.rate_hw(first_student, 'Python', 1)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Git', 2.9)
first_reviewer.rate_hw(first_student, 'Git', 9.3)
first_reviewer.rate_hw(first_student, 'Git', 4.4)
second_reviewer.rate_hw(second_student, 'Python', 7.8)
second_reviewer.rate_hw(second_student, 'Python', 8.5)
second_reviewer.rate_hw(second_student, 'Python', 4.3)
second_reviewer.rate_hw(second_student, 'Git', 6.8)
second_reviewer.rate_hw(second_student, 'Git', 7.5)
second_reviewer.rate_hw(second_student, 'Git', 9.3)

print(first_student)
print(second_student)
first_student.__lt__(second_student)

print(first_lecturer)
print(second_lecturer)
first_lecturer.__lt__(second_lecturer)

print(first_reviewer)
print(second_reviewer)


def middle_grade_student(first_student, second_student, course):
    overall_grades = 0
    count_grades = 0
    if course in first_student.grades.keys():
        for grades in first_student.grades[course]:
            overall_grades += grades
        count_grades += len(first_student.grades[course])
        if course in second_student.grades.keys():
            for grades in second_student.grades[course]:
                overall_grades += grades
            count_grades += len(second_student.grades[course])
    print(f'Средняя оценка по курсу "{course}" у студентов составляет: {overall_grades / count_grades: .2f}')
    return


middle_grade_student(first_student, second_student, 'Python')
middle_grade_student(first_student, second_student, 'Git')


def middle_grade_lecturer(first_lecturer, second_lecturer, course):
    overall_grades = 0
    count_grades = 0
    if course in first_lecturer.grades.keys():
        for grades in first_lecturer.grades[course]:
            overall_grades += grades
        count_grades += len(first_lecturer.grades[course])
        if course in second_lecturer.grades.keys():
            for grades in second_lecturer.grades[course]:
                overall_grades += grades
            count_grades += len(second_lecturer.grades[course])
    print(f'Средняя оценка по курсу "{course}" у лекторов составляет:{overall_grades / count_grades: .2f}')


middle_grade_lecturer(first_lecturer, second_lecturer, 'Python')
middle_grade_lecturer(first_lecturer, second_lecturer, 'Git')
