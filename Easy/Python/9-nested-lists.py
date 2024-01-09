if __name__ == '__main__':
    students_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_score.append([name, score])

    second_grade = sorted((set([score for name, score in students_score])))[1]

    second_students = sorted([name for name, score in students_score if score == second_grade])

    for student in second_students:
        print(student)