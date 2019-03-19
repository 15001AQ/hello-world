from appJar import gui

level = 0
x = level
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
    
    def correctOrNot(self):
        userAnswer = app.getOptionBox("Your Answer:")
        x = level
        if userAnswer == self.cans:
            if x == 0:
                x = x + 1
                app.setLabel("Questions",questionList[x].show())
                changingQ()
            elif x == 1:
                x = x + 1
                app.setLabel("Questions",questionList[x].show())
                changingQ()
        else: 
            app.stop()
        
  
#main routine
def launch(win):
    if win == "Start":
        app.showSubWindow("questions")
        app.setLabel("Questions",questionList[x].show())        
    elif win == "Exit":
        app.stop()

    
def check(button):
    if button == "Enter Answer":
        questionList[x].correctOrNot()
    elif button == "Go back":
        app.stop()

def changingQ():
    if x == 1:
        app.changeOptionBox("Your Answer:",["7","3","2","5"])
    elif x == 2:
        app.changeOptionBox("Your Answer:",["5","3","2","5"])
        
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
app.addLabelOptionBox("Your Answer:",["sewage, oil spills", "people swimming","people driving boats","climate change"])

app.addButtons(["Enter Answer", "Go back"],check)
app.stopSubWindow()

app.startSubWindow("correct",modal=True)
app.setBg("red")
app.setSize(400,400)
app.addLabel("titl", x)
app.stopSubWindow()


questionList.append(Question("What is water pollution caused by?","sewage, oil spills", "people swimming","people driving boats","climate change"))
questionList.append(Question("What is causing global warming?","7","3","2","5"))
questionList.append(Question("What is causing eghioehogbewogglobal warming?","5","3","2","5"))


app.go()