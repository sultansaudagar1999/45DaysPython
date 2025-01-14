# Assign a different name to function and call it through the new name

def display_student(name,age):
    print("Student Name :",name)
    print("Student Age :",age)

show_student = display_student

show_student("Sultan Saudagar",25)
