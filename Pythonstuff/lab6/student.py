#Daniel Kolodziej
#3/21/2018
#Lab 6  ITMD-413

import time
class Student:

         Scores={} 

         def __init__(self, name, grade): # Initializing constructor method
                self.name = name
                self.grade = grade

         def getScores(self):

                answer_key=[]
                #read into answer_key list, the answer key from file
                answer_key = [line.strip() for line in open("answers.txt", 'r')]
                 
                student_answers=[]
                #read into student_answers list, student answers from file
                student_answers = [line.strip().split(',') for line in open("data.txt", 'r')]
                
                total_score=100

                #---start your loop processing logic here---#
                #studAns var to index through student answers
                studAns = 1
                #loop through each student in the list
                for student in student_answers:
                    #check name with object
                    if student[0] == self.getName():
                        #loop through each answer in the answer list
                        for answer in answer_key:
                            #compare answer key to student answer, deduct 10 per wrong
                            if answer!= student[studAns]:
                                total_score -= 10
                            studAns+=1
                                            
                #---end your loop processing logic here---#
                                
                Student.Scores[self.getName()]=total_score;
                
         def getName(self):
                return self.name;
         @staticmethod
         def sortDict():
                return sorted(Student.Scores.items());
             
student_objs = [
        Student('Sammy Student',65),
        Student('Betty sanchez', 45),
        Student('Alice brown', 100),
        Student('tom Schulz', 50),
        Student('Daniel Kolodziej', 90),
        ]

#student_objs.append(Student("Daniel Kolodziej", 90))  -> another option to add in name and grade

for index in range(len(student_objs)):
    student_objs[index].getScores();

sortList=Student.sortDict();

#added title method to names in list to uppercase first char in both names
for k,v in sortList:
      print (k.title(), "has score:", v)

#author, date, time, lab number
print('Daniel Kolodziej',time.strftime("%m/%d/%Y"),time.strftime("%H:%M:%S"),'Lab6')
