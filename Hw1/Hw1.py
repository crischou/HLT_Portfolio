#Homework 1
#Cris Chou

import sys
import os
import pickle
import re
import pathlib


#person class
class Person: 
    #initialization
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
        print("\n")

#employees dictionary
employees = {}

#process lines method
def process_lines(lines):
    #parse through lines
    for line in lines:
        #split line into parts on ','
        parts = line.split(',')
        #check if name is capital case
        if not parts[0].istitle() : #lastname
            
            parts[0] = parts[0].capitalize()

        if not parts[1].istitle(): #firstname
            
            parts[1] = parts[1].capitalize()

        #Checking middle initial
        if not parts[2].isupper(): 

            parts[2] = parts[2].upper()

        if parts[2] == "":

            parts[2] = "X"
        
        #check id
        regCheck = False
        #interate until valid input
        while not regCheck:
            regCheck = re.match('([a-zA-Z]{2})''([0-9]{4})$', parts[3])
            #get new id if invalid
            if not regCheck:
                print("ID invalid: " + parts[3])
                print("ID is two letters followed by 4 digits: ")
                parts[3] = input("Enter new ID: ")

        #check phone number
        regCheck = False 
        #iterate until valid input
        while not regCheck:
            regCheck = re.match('([0-9]{3})''-''([0-9]{3})''-''([0-9]{4})$', parts[4])
            if not regCheck:
                print("Phone " + parts[4] + " is invalid")
                print("Enter phone number in format: 123-456-7890")
                parts[4] = input("Enter new phone number: ")

        #create new person object for every employee
        newPerson = Person(parts[0], parts[1], parts[2], parts[3], parts[4])
        #add person object to employees dict using ID as key
        employees[parts[3]] = newPerson




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

        #print using display method
        for key in employees:
            employees[key].display()
        





