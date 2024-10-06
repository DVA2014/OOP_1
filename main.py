class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in
            self.courses_in_progress and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def avg_grade(self):
        self.avg_grades = []
        for course in self.grades:
            self.avg_grades.append((sum(self.grades[course])/
            len(self.grades[course])))
        return round(sum(self.avg_grades)/len(self.avg_grades), 1)    

    def __str__(self):
        return (f"Имя: {self.name}/n"
        f"Фамилия: {self.surname}/n"
        f"Средняя оценка за домашние задания: {self.avg_grade()}/n"
        f"Курсы в процессе изучения: {",".join(self.courses_in_progress)}/n"
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
        self.avg_grades = []
        for course in self.grades:
            self.avg_grades.append((sum(self.grades[course])/
            len(self.grades[course])))
        return round(sum(self.avg_grades)/len(self.avg_grades), 1)

    def __str__(self):
        return (f"Имя: {self.name}/n"
            f"Фамилия: {self.surname}/n"
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
        return (f"Имя: {self.name}/n"
    f"Фамилия: {self.surname}")
    
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
        and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

#if any_lecturer == some_lecturer:
    #print('any and some have the same grades')
#else:
#    print('any and some have the different grades')