#take two inputs
a = input()
b = input()


for i in range(5):
    #sum those numbers
    c = int(a) + int(b)
    print(c)

    #swap those numbers
    a = b
    b = c
