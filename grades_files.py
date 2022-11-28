# Name: Mike Vance
# Prog Purpose: This program computes grades for students using a python LIST
#	of data in Pythin DICTIONARIES (as student records)
#   Each Student has 3 graded items: Homework, Midterms, and Finals
#   Each item is worth 100 points
#   The student's final grade is the average of the three graded items

############## define global variables & constants ##############
import datetime
stu = []
student_file = "students.csv"
out_file = 'stu_report.txt'

############## define program functions ##############
def main():
    read_data_file()
    calculate_grades()
    create_report_file()

def read_data_file():
    datafile = open(student_file,"r") #the 'r' indicates this is a READ file
    lines = datafile.readlines() #Read the entire file into a variable called lines
    for i in lines:
        stu.append(i.split(',')) #Split the data by commas and add each sectionto the list
    datafile.close()

def calculate_grades():
    global average, totA, totB, totC, totD, totF
    totA = totB = totC= totD = totF = 0
    gradestotal = 0

    for i in range(len(stu)):
        hw = int(stu[i][2]) #Last name pos. 0, forst name is pos.1, so homework is pos. 
        midex = int(stu[i][3]) #Midterm exam is in position 3
        stu[i][4] = stu[i][4][:-1] #Removes the \n from the final exam string (end of the input line)
        finex = int(stu[i][4]) #Final exam is in position 4
        sum_grades = hw + midex + finex
        finalgr = sum_grades / 3
        gradestotal += finalgr #Add the grade to the total for calculating the average
        stu[i].append(finalgr) 

        if finalgr >= 90:
            lettergrade = 'A'
            totA += 1
        elif finalgr >= 80:
            lettergrade = 'B'
            totB += 1
        elif finalgr >= 70:
            lettergrade = 'C'
            totC += 1
        elif finalgr >= 60:
            lettergrade = 'D'
            totD += 1
        else:
            lettergrade = 'F'
            totF += 1
        stu[i].append(lettergrade)
    
    average = gradestotal / len(stu)




def create_report_file():
    line = '\n*******************************************'
    repfile = open(out_file, 'w')
    repfile.write('\n***************** CSC 230 Grade Report *****************')
    repfile.write('\nReport Date/Time        : ' + str(datetime.datetime.now()))
    repfile.write('\nTotal number of students: ' + str(len(stu)))
    repfile.write('\nAverage student grade   : ' + format(average, '5,.2f'))
    repfile.write('\nTotal number of A grades: ' + str(totA))
    repfile.write('\nTotal number of B grades: ' + str(totB))
    repfile.write('\nTotal number of C grades: ' + str(totC))
    repfile.write('\nTotal number of D grades: ' + str(totD))
    repfile.write('\nTotal number of F grades: ' + str(totF))
    repfile.write(line)
    for i in range(len(stu)):
        sname = '{0:<18}'.format(stu[i][0]+', '+stu[i][1])
        hw = str(stu[i][2])
        midex = str(stu[i][3])
        finex = str(stu[i][4])
        fingrade = format(stu[i][5], '6,.2f')
        repfile.write('\n' + sname + '\t' + hw + '\t' + midex + '\t' + finex + '\t' + fingrade + ' '+ stu[i][6])
    repfile.write(line)
    repfile.close()
    print('Open this file to view the Grade Report: ' + out_file)

############## Call on main program to execute ##############
main()