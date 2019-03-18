from appJar import gui

questionList = []

app = gui("Environment Quiz","500x200") 

class Question:
    def __init__(self,quesText,cans,pans1,pans2,pans3):
        self.quesText = quesText
        self.cans = cans
        self.pans1 = pans1
        self.pans2 = pans2
        self.pans3 = pans3
        
    def show(self):
        app.setLabel("Questions",self.quesText)
        
  
#main routine
def launch(win):
    if win == "Start":
        app.showSubWindow("question 1")
        app.setLabel("Questions",questionList[0].show())
        app.getEntry("Your Answer:")
        
    elif win == "Exit":
        app.stop()
    
def check(button):
    if button == "Enter Answer":
        correct()
    elif button == "Go back":
        app.stop()
    
        
#main routine - setting up the GUI
app.addLabel("title", "Welcome to my Environment Quiz")
app.addLabel("belowtitle", "In this quiz, you will be asked various questions\n        on the problems with our environment")
app.addLabel("belowbelowtitle", "Press Start to begin.")
app.setBg("light green")
app.addButtons(["Start", "Exit"],launch)

#CREATING SUB WINDOW FOR QUESTIONS
app.startSubWindow("question 1", modal=True)
app.setBg("light green")
app.setSize(400,400)
app.addLabel("Questions", "")
app.addLabelEntry("Your Answer:")
app.addButtons(["Enter answer", "Go back"],check)
app.stopSubWindow()

app.startSubWindow("correct")
app.setBg("red")
app.addLabel("f", "f")
app.stopSubWindow()


questionList.append(Question("What is water pollution caused by?","sewage","oil spills","acid rain","rubbish"))
questionList.append(Question("How high?","7","3","2","5"))

questionList[0].show()

app.go()