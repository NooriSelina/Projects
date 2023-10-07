#Noori Selina

import random
import readquiz
from tkinter import *

#setting the initial values of the score
correct = 0
total = 0

#defining the function for new question
def getNewQuestion():
    chosen = random.choice(readquiz.loadQuestions())
    print(chosen)
    Question['text'] = chosen[0] #setting text for the 'Question' label 
    if chosen[1]: #setting the good and bad answer for yes/no function
        buttonYes['command'] = goodAnswer
        buttonNo['command'] = badAnswer
    else:
        buttonNo['command'] = goodAnswer
        buttonYes['command'] = badAnswer

#providing function to update score
def scoreupdate():
    score['text'] = 'Score: {0}/{1}' .format(correct,total)

def badAnswer(): #defining bad answer function
    global total, correct
    correct += 0
    total += 1 
    status['bg'] = 'pink' #changing background color
    status['text'] = 'Your answer was incorrect'
    scoreupdate() #updating score
    getNewQuestion() #obtaining new question

def goodAnswer(): #defining good answer function
    global total, correct
    correct += 1
    total += 1
    status['bg'] = 'light Green' #changing background color
    status['text'] = 'Your answer was correct' 
    scoreupdate() 
    getNewQuestion()

root = Tk() #creating the window

#crearing label
Question = Label(root)
Question['text'] = 'Question'
Question.pack()

#creating no button
buttonNo = Button(root, width=12)
buttonNo['text'] = 'No'
buttonNo.pack(side=RIGHT, fill=X)

#creating yes button
buttonYes = Button(root, width=12)
buttonYes['text'] = 'Yes'
buttonYes.pack(side=LEFT, fill=X)

status = Label(root)
status.pack(expand=YES, fill=BOTH)

#creating the Score label
score = Label(root)
score.pack(side=RIGHT)

status = Label(root)
status.pack(side=LEFT)
status['text'] = 'Status'

#getting new question, and creating score update
getNewQuestion()
scoreupdate()
mainloop() #starting the mainloop

            
 



