# Generate a Python list of all the even numbers between 4 to 30


def even_numbers(start,end):
    even_list = []
    for i in range(start,end):
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)



even_numbers(4,30)