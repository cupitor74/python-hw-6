from datetime import date, datetime, timedelta
from university import Course, Mentor, Teacher, Student, University

python_course = Course("Python", datetime.now(), datetime.now() + timedelta(days=30))
js_course = Course("JavaScript", datetime.now() - timedelta(days=60), datetime.now() - timedelta(days=5))

alex_student = Student("Alex", "Stp", date(1995, 7, 8))
nik_student = Student("Nik", "Fial", date(1998, 10, 22))

bred_teacher = Teacher("Bred", "Cmp", date(1974, 6, 25), 2000, python_course)

koli_mentor = Mentor("Koli", "Key", date(1987, 3, 13), 1200, [python_course, js_course])

harvard_university = University(
    "Harvard",
    [python_course, js_course],
    [bred_teacher, koli_mentor],
    [alex_student, nik_student],
)
# print(koli_mentor.answer_question(python_course, 'Яка домашка?'))
# """-> True # на перше питання відповіли"""
# print(koli_mentor.answer_question(python_course, 'Чи можу я здати пізніше?') )
# """-> False # на друге питання НЕ відповіли"""
# print(koli_mentor.answer_question(python_course, 'Чи можу я здати пізніше?'))
# """ -> True # теж саме питання, але вже знайшли час відповісти"""
# print(koli_mentor.answer_question(python_course, 'Яка оцінка?'))
# """ -> False # не вистачило часу відповісти на це питання """

# print(koli_mentor.answer_question(js_course, 'Чи можу я здати пізніше?'))
# """ -> False
#         # питання на яке відповідали, і є час відповісти, але питання стосується курсу який вже закінчився
# """
# print( koli_mentor.answer_question(python_course, 'Що було на уроці?'))
# """ -> True
#         # так як на минуле питання ми не відповідали, на наступне питання є можливість відповісти"""

nik_student.add_mark(2)
nik_student.add_mark(4)
nik_student.add_mark(12)
nik_student.add_mark(10)
# print(nik_student.get_all_marks())
# print(nik_student.get_average_by_last_n_marks(3))
# print(nik_student.get_average_from_date(datetime(2022, 7, 25)))
# print(bred_teacher.answer_question(python_course, 'Яка домашка?'))
print(bred_teacher.get_yearly_salary())
print(bred_teacher.answer_question(python_course, 'sdgdsfdg'))
print(harvard_university.get_average_salary())
print(harvard_university.get_active_courses())
print(harvard_university.get_average_mark())
"""-> True # на перше питання відповіли"""
print(bred_teacher.answer_question(python_course, 'Чи можу я здати пізніше?') )
"""-> False # на друге питання НЕ відповіли"""
print(bred_teacher.answer_question(python_course, 'Чи можу я здати пізніше?'))
""" -> True # теж саме питання, але вже знайшли час відповісти"""
print(bred_teacher.answer_question(python_course, 'Яка оцінка?'))
""" -> False # не вистачило часу відповісти на це питання """

print(bred_teacher.answer_question(js_course, 'Чи можу я здати пізніше?'))
""" -> False
        # питання на яке відповідали, і є час відповісти, але питання стосується курсу який вже закінчився
"""
print( bred_teacher.answer_question(python_course, 'Що було на уроці?'))
""" -> True
        # так як на минуле питання ми не відповідали, на наступне питання є можливість відповісти"""

# print(koli_mentor.answer_question(some_course, 'Що було на уроці?'))
# """ -> True
#         # не дивлячись на те що ми дуже зайняті, але маємо змогу відповісти на питання, на яке вже відповідали.
# """
# print(koli_mentor.answer_question(some_course, 'Як мені виконати ДЗ?'))
# """ -> False"""


# print(koli_mentor.answer_question(python_course, 'Rfrafsdf'))
# print(koli_mentor.answer_question(js_course, 'Rfrafsdf'))
# print(koli_mentor.answer_question(js_course, 'werwerw'))
# print(koli_mentor.answer_question(js_course, '56hryhtyh'))