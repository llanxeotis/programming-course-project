import sys
import csv

studentnames = ['Ahmed', 'Ali', 'Adham']
studentgrades = [43, 98, 50]
successfulstudents = []

combinelists = list(zip(studentnames, studentgrades)) #put two lists in one

def displaylist():
    i = 1
    for i, (name, grade) in enumerate(zip(studentnames, studentgrades)):
        i = i+1
        print(i, name, ", grade: ", grade)

def add(): #adding member to the enrolled course list
        name = input("\nPlease enter the new student's full name to add it: ")
        studentnames.append(name)
        print("NAME HAS BEEN ADDED")
        while True:
            confirm = input("Would you like to add another? [Y/N]:").lower()
            if confirm in ("yes", "y"):
                add()
            elif confirm not in ("yes", "y", "no", "n"):
                print("Please answer with y/n.")
                continue
            elif confirm in ("no", "n"):
                pause()
            break
                            
def show(): #show members of the course list
    print("\n --- LIST OF NAME OF CURRENT STUDENTS:---")
    index = 1
    for value in studentnames:
        print(index ,":",value)
        index = index+1
    if len(studentnames) < 1:
        print ("This student list is empty.\n")
  

def delete(): #delete member from the course list
    show()
    name = input("\nPlease enter the FULL NAME from the list of members to remove: ").lower()
    if name in studentnames:
        studentnames.remove(name)
    else:
        print('\nPLEASE NOTE: This name is not on the list.')
    pause()
    
def update():#change member`s name from the course list
    show()
    index = int(input("Please enter the number from the list of members that you want to change: "))
    if index > len(studentnames):
        print('\nPLEASE NOTE: This number is not on the list.')
        update()
        return
    name = input("Please enter the student's NEW name:\n")
    studentnames[index-1] = name
    show()
    pause()
    
def adddegree():
    show()
    ind = int(input("Please enter the number from the list of students that you want to add a grade to: "))
    if ind > len(studentnames):
        print('\nPLEASE NOTE: This number is not on the list.')
        adddegree()
        return
    while True:
        grade = int(input("Please enter the student's grade:\n"))
        if grade > 100:
            print('\nPLEASE ENTER VALUE FROM 0 - 100')
            continue
        else:
            studentgrades.insert(ind, grade)
            displaylist()
            pause()
        break

def interpretdegree():
    print("\nList of student grades based on degree:\n")
    combinedict = dict(zip(studentnames, studentgrades))
    interpret = {
        key:('Excellent' if value >= 86 and value <= 100 else
             "Very good PLUS" if value>= 75 and value <= 85 else
             "Very good" if value >= 65 and value <= 74 else
             "Good" if value >= 50 and value <= 64 else
             "Weak" if value >= 35 and value <= 49
             else 'Very weak') for (key, value) in combinedict.items()}
    for k, v in interpret.items():
        print(f'{k:<8} {v}') #format string
   
def displaysuccess():
    for w in range(len(studentnames)):
        if studentgrades[w] >= 50:
            successfulstudents.append(studentnames[w])
    print("\n --- LIST OF SUCCESSFUL STUDENTS:---")
    inde = 1
    for v in successfulstudents:
        print(inde ,":",v)
        inde = inde+1
    print("\nTotal number of successful students: ", len(successfulstudents))
    if len(successfulstudents) < 5:
        while True:
            compconfirm = input("Would you like to add compensatory grades to failed students? [Y/N]:").lower()
            if compconfirm in ("yes", "y"):
                for i, value in enumerate(studentgrades):
                    if value < 50:
                        studentgrades[i] = value+16;
            elif compconfirm not in ("yes", "y", "no", "n"):
                print("Please answer with y/n.")
                continue
            elif compconfirm in ("no", "n"):
                pause()
            break

def pause():
    wait = input("\nOPERATION DONE SUCCESSFULLY.\nPRESS ENTER KEY TO CONTINUE . . .\n")

def mainmenu():
    while True:
        print("\n-- Please choose a list to work on: \n1 - Student names\n2 - Student grades\n3 - QUIT THE PROGRAM.")
        worklist = input("--- SELECTING: ")
        if worklist == "1":
            print("\n-- WORKING ON: STUDENT NAMES LIST --")
            namesmenu()
        elif worklist == "2":
            print("\n-- WORKING ON: STUDENT GRADES LIST --")
            gradesmenu()
        elif worklist == "3":
            print("\nQUITTING THE PROGRAM . . .\n")
            sys.exit()    
        else:
            print("\n[INVALID! Please enter a valid command!]\n")
            
def namesmenu():
        while(True):
            print("\n[Please choose an action from 1 - 6:")
            print("1 - SHOW the list of enrolled members in the course\n2 - ADD new member to the list\n3 - DELETE  member from the list\n4 - UPDATE  a member's name from the list\n5 - Go Back\n6 - QUIT THE PROGRAM.]")
            number = input("--- SELECTING: ")
            if number == "1" :
                show()
            elif number == "2" :
                add()
            elif number == "3" :
                delete()
            elif number == "4":
                update()
            elif number == "5":
                print("\nReturning to main menu . . .\n")
                mainmenu()
            elif number == "6":
                print("\nQUITTING THE PROGRAM . . .\n")
                sys.exit()
            else:
                print("\n[INVALID! Please enter a valid command!]\n")

def gradesmenu():
        while(True):
            print("\n[Please choose an action from 1 - 6:")
            print("1 - SHOW the grades of enrolled students\n2 - ADD new degree to a student\n3 - SHOW GRADES of students \n4 - DISPLAY successful students\n5 - Go Back\n6 - QUIT THE PROGRAM.]")
            number = input("--- SELECTING: ")
            if number == "1" :
                displaylist()
            elif number == "2" :
                adddegree()
            elif number == "3" :
                interpretdegree()
            elif number == "4":
                displaysuccess()
            elif number == "5":
                print("\nReturning to main menu . . .\n")
                mainmenu()
            elif number == "6":
                print("\nQUITTING THE PROGRAM . . .\n")
                sys.exit()
            else:
                print("\n[INVALID! Please enter a valid command!]\n")
  
print ("-- Welcome to the Student grades program. --")

with open('studentnames2023.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(studentnames)

file = open('studentdegreelist2023.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(combinelists) 
file.close()

mainmenu()



        
