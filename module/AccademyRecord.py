# Academic Performance Tracker


# Global variable to store student records
students = {}

def add_course(student_id, course_name, credits, earned_points):
    if student_id not in students:
        students[student_id] = {'courses': []}
    
    students[student_id]['courses'].append({
        'course_name': course_name,
        'credits': credits,
        'earned_points': earned_points
    })
    print(f'Course {course_name} added for student ID {student_id}.')

def drop_course(student_id, course_name):
    if student_id in students:
        initial_count = len(students[student_id]['courses'])
        students[student_id]['courses'] = [
            course for course in students[student_id]['courses'] if course['course_name'] != course_name
        ]
        if len(students[student_id]['courses']) < initial_count:
            print(f'Course {course_name} dropped for student ID {student_id}.')
        else:
            print(f'Course {course_name} not found for student ID {student_id}.')
    else:
        print('Student not found!')

def calculate_cgpa(student_id):
    if student_id in students:
        total_credits = sum(course['credits'] for course in students[student_id]['courses'])
        if total_credits == 0:
            return 0
        total_points = sum(course['earned_points'] * course['credits'] for course in students[student_id]['courses'])
        return total_points / total_credits
    else:
        print('Student not found!')
        return None

def print_academic_record(student_id):
    if student_id in students:
        record = f"Academic Record for Student ID {student_id}:\n"
        for course in students[student_id]['courses']:
            record += f"Course: {course['course_name']}, Credits: {course['credits']}, Earned Points: {course['earned_points']}\n"
        record += f"Current CGPA: {calculate_cgpa(student_id):.2f}\n"
        print(record)
    else:
        print('Student not found!')
