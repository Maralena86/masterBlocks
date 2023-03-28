'''GROUPS OF STUDENTS:
In one of the courses a class has been divided into two groups A and B. In order to mix the students as well as possible, all the girls with names beginning with the letter E to M were assigned to group A and the rest to group B. The boys with names starting with the letter A through H and R through Z have been assigned to group A as well, the rest are in group B.
Create a script that asks the user if it is a girl or a boy and the name. The script must show on the screen the group that corresponds to that student.
'''
groupA = []
groupB = []

nameStudent = input("What's your name? ")
sexeStudent = input("Make the choice: women, men:  ")

if  nameStudent.lower() == range(ord("a"), ord("z")):
    if ((ord(nameStudent[0].lower()) >= ord("a") or ord(nameStudent[0].lower()) <= ord("m")) and sexeStudent == "women") or (sexeStudent == "men" and (nameStudent[0].lower() == range(ord("a"), ord("h")) or nameStudent[0].lower() == range(ord("r"), ord("z")))):
        groupA.append(nameStudent)
        print("You're in group A")
    else:
        groupB.append(nameStudent)
        print("You're in group B")
print(nameStudent[0].lower()+ range(chr(97),chr(109)))
