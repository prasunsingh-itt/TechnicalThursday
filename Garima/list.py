emptylist = []
n = int(input("Enter number of elements : "))
def Sort(emptylist):
    return(sorted(emptylist , key = lambda x: x[0]))

for i in range(0, n):
    studentlist = [input(), float(input())]
    emptylist.append(studentlist)

minimum = min(emptylist, key=lambda x: x[1])[1]
list_of_min = [emptylist.pop(emptylist.index(element)) if element[1] == minimum else None for element in emptylist]
second_min = min(emptylist, key=lambda x: x[1])[1]
name_sorted_list = Sort(emptylist)
for element in name_sorted_list:
    if element[1] == second_min:
        print(element[0])







