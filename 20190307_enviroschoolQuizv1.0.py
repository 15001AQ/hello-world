from appJar import gui

level = 0
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
        app.showSubWindow("questions")
        x = level
        app.setLabel("Questions",questionList[x].show())        
    elif win == "Exit":
        app.stop()

    
def check(button):
    if button == "Enter Answer":
        correctOrNot()
    elif button == "Go back":
        app.stop()

def correctOrNot():
    app.getOptionBox("Your Answer:")
    if app.getOptionBox("Your Answer:") == "sewage":
        app.showSubWindow("correct")
    else:
        pass
        
#main routine - setting up the GUI
app.addLabel("title", "Welcome to my Environment Quiz")
app.addLabel("belowtitle", "In this quiz, you will be asked various questions\n        on the problems with our environment")
app.addLabel("belowbelowtitle", "Press Start to begin.")
app.setBg("light green")
app.addButtons(["Start", "Exit"],launch)

#CREATING SUB WINDOW FOR QUESTIONS
app.startSubWindow("questions", modal=True)
app.setBg("light green")
app.setSize(400,400)
app.addLabel("Questions", "")
app.addLabelOptionBox("Your Answer:",["sewage","oil spills","acid rain","rubbish"])

app.addButtons(["Enter answer", "Go back"],check)
app.stopSubWindow()

app.startSubWindow("correct",modal=True)
app.setBg("red")
app.addLabel("titl", "fgrehsd")
app.stopSubWindow()


questionList.append(Question("What is water pollution caused by?","sewage","oil spills","acid rain","rubbish"))
questionList.append(Question("What is causing global warming?","7","3","2","5"))

app.go()