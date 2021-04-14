# 실전 6-3 성적이 낮은 순서로 학생 출력하기

n = int(input())

students = []
for i in range(n):
    data = input().split()
    name = data[0]
    score = int(data[1])
    students.append((name, score))

students.sort(key=lambda x: x[1])

for student, score in students:
    print(student, end=" ")
