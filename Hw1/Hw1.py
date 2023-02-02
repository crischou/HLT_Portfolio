#Homework 1
#Cris Chou

import sys
import os
import pickle
import re
import pathlib


#person class
class Person: 
    #initializtion
    def __init__(self, lastName, firstName, middleInitial, id, officePhone):
        self.lastName = lastName
        self.firstName = firstName
        self.middleInitial = middleInitial
        self.id = id 
        self.officePhone =  officePhone
    
    #display method
    def display(self):
        print("Employee ID: " + self.id)
        print(self.firstName, self.middleInitial, self.lastName)
        print("Office Phone: " + self.officePhone)

#employees dictionary
employees = {}

#process lines method
def process_lines(lines):
    #parse through lines
    for line in lines:
        #split line into parts on ','
        parts = line.split(',')
        #create new person object for every employee
        person = Person(parts[0], parts[1], parts[2], parts[3], parts[4])
        #add person object to employees dict using ID as key
        employees[parts[3]] = person
        #print(parts)



if __name__ == '__main__':
    #check sys.argsv
    if len(sys.argv) < 2:
        print('Please use valid file path: ')
        quit()
    
    fp = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(fp), 'r') as f:
        #split text by lines
        text_in = f.read().splitlines()

        #refer to process_lines method
        process_lines(text_in[1:])   

        #print
        for key in employees:
            print(employees[key].display())
        





