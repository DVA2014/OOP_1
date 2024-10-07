class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def add_courses_in_progress(self, course_name):
        self.courses_in_progress.append(course_name)
    
    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if grade in range(11):
            if (isinstance(lecturer, Lecturer) and course in
            self.courses_in_progress and course in lecturer.courses_attached):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            print('Некорректная оценка')

    def avg_grade(self):
        avg_grades = []
        for course in self.grades:
            avg_grades.append((sum(self.grades[course])/
            len(self.grades[course])))
        if len(avg_grades) > 0: 
            return round(sum(avg_grades)/len(avg_grades), 1)
        else:
            return f'Оценок нет'
        
    def __str__(self):
        return (f"Имя: {self.name}\n"
        f"Фамилия: {self.surname}\n"
        f"Средняя оценка за домашние задания: {self.avg_grade()}\n"
        f"Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n"
        f"Завершенные курсы: {",".join(self.finished_courses)}")
    
    def __eq__(self, student):
        return self.avg_grade() == student.avg_grade()
    
    def __lt__(self, student):
        return self.avg_grade() < student.avg_grade()
    
    def __ge__(self, student):
        return self.avg_grade() >= student.avg_grade()
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def avg_grade(self):
        avg_grades = []
        for course in self.grades:
            avg_grades.append((sum(self.grades[course])/
            len(self.grades[course])))
        if len(avg_grades) > 0: 
            return round(sum(avg_grades)/len(avg_grades), 1)
        else:
            return f'Оценок нет'


    def __str__(self):
        return (f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.avg_grade()}")
    
    def __eq__(self, lecturer):
        return self.avg_grade() == lecturer.avg_grade()
    
    def __lt__(self, lecturer):
        return self.avg_grade() < lecturer.avg_grade()
    
    def __ge__(self, lecturer):
        return self.avg_grade() >= lecturer.avg_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f"Имя: {self.name}\n"
    f"Фамилия: {self.surname}")
    
    def rate_hw(self, student, course, grade):
        if grade in range(11):
            if (isinstance(student, Student) and course in self.courses_attached
            and course in student.courses_in_progress):
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            print('Некорректная оценка') 

lecturer_a = Lecturer('Jason', 'Statham')
lecturer_a.courses_attached += ['Python']

lecturer_2 = Lecturer('Sylvester', 'Stallone')
lecturer_2.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.add_courses_in_progress('Python')
best_student.add_finished_courses('Git')
best_student.rate_lecture(lecturer_a, 'Python', 10)
best_student.rate_lecture(lecturer_2, 'Python', 9)

student_2 = Student('Roy', 'Jones', 'male')
student_2.add_courses_in_progress('Python')
student_2.add_courses_in_progress('Git')
student_2.add_finished_courses('1C')
student_2.rate_lecture(lecturer_a, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Python', 9)

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(student_2, 'Python', 10)
print(cool_mentor)

reviewer_2 = Reviewer('Dolph', 'Lundgren')
reviewer_2.courses_attached += ['Python']
reviewer_2.rate_hw(best_student, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 8)
print(reviewer_2)

if lecturer_a == lecturer_2:
    print(f'{lecturer_a.name} have the same grades as {lecturer_2.name}')
elif lecturer_a < lecturer_2:
    print(f'{lecturer_a.name} have the less grade than {lecturer_2.name}')
else:
    print(f'{lecturer_a.name} have the better grade than {lecturer_2.name}')

print(lecturer_a)

print(lecturer_2)

#print(best_student)

#print(student_2)
#if any_lecturer == some_lecturer:
    #print('any and some have the same grades')
#else:
#    print('any and some have the different grades')