N, X = list(map(int, input().split()))
list_of_marks = []
for subject in range(X):
    list_of_marks += [list(map(float,input().split()))]
    
for student_marks in zip(*list_of_marks):    
    print(sum(student_marks)/X)