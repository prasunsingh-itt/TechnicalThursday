studentList = []
N=int(input())
for _ in range(N): 
     studentList.append([input(),float(input())])

print(studentList)

studentList.sort(key=lambda x: x[1])
print(studentList)

print(studentList[1])
