import Tkinter
#from pubsub import pub
import os
from writer import XMLWriter

#TODO:
#Resize home and into entry windows
#Create view stories window
#improve descriptions/auto select etc for info entry screen

size = '400x400'

class Home(object):
    
    def __init__(self, parent, size):
        self.root = parent
        self.frame = Tkinter.Frame(parent)
        self.frame.grid()
        self.initialise(size)
        

    def initialise(self, size):
        self.root.title('SS:ZS ~ Home')
        self.root.geometry(size)
        self.newEntryButton = Tkinter.Button(self.frame,text=u'Enter new Zee Story',command=self.newEntryClick)
        self.newEntryButton.grid(column=0,row=0,sticky='EW')

        self.viewStoriesButton = Tkinter.Button(self.frame, text=u'View recorded Stories',command=self.viewStoriesClick)
        self.viewStoriesButton.grid(column=0,row=1,sticky='EW')

    def newEntryClick(self):
        self.root.withdraw()
        entryFrame = InfoEntry(size)

    def viewStoriesClick(self):
        print 'recorded stories test'

class InfoViewer(Tkinter.Toplevel):
    def __init__(self):
        Tkinter.Toplevel.__init__(self)
        self.initialise()

    def initialise(self):
        pass

class InfoEntry(Tkinter.Toplevel):
    def __init__(self, size):
        Tkinter.Toplevel.__init__(self)
        self.initialise(size)

    def initialise(self, size):
        self.grid()
        self.geometry(size)
        self.title('SS:ZS ~ Add Entry')
        self.protocol("WM_DELETE_WINDOW", root.destroy)

        self.writer = XMLWriter()
        self.xml = None

        self.nameVariable = Tkinter.StringVar()
        self.name = Tkinter.Entry(self, textvariable=self.nameVariable)
        self.name.grid(column=0, row=0, sticky='EW')
        self.name.bind('<Return>',self.onPressEnter)
        self.nameVariable.set('Enter name here')

        self.yearsVariable = Tkinter.StringVar()
        self.years = Tkinter.Entry(self,textvariable=self.yearsVariable)
        self.years.grid(column=0, row=1, sticky='EW')
        self.years.bind('<Return>',self.onPressEnter)
        self.yearsVariable.set('Enter # of years at Zee')

        self.echoesVariable = Tkinter.StringVar()
        self.echoes = Tkinter.Entry(self, textvariable=self.echoesVariable)
        self.echoes.grid(column=0, row=2, sticky='EW')
        self.echoes.bind('<Return>',self.onPressEnter)
        self.echoesVariable.set('Enter # of echoes')

        self.coDVariable = Tkinter.StringVar()
        self.coD = Tkinter.Entry(self, textvariable=self.coDVariable)
        self.coD.grid(column=0, row=3, sticky='EW')
        self.coD.bind('<Return>',self.onPressEnter)
        self.coDVariable.set('Cause of Death')

        #use text widget instead of Entry to allow for multiple lines.
        #Text widget needs work around as it cannot take textvariable by default
        self.zeeStoryVariable = Tkinter.StringVar()
        self.zeeStory = Tkinter.Entry(self, textvariable=self.zeeStoryVariable)
        self.zeeStory.grid(column=0, row=4, sticky='EW')
        self.zeeStory.bind('<Return>',self.onPressEnter)
        self.zeeStoryVariable.set("Tell your Captain's story")

        self.outFilePathVariable = Tkinter.StringVar()
        self.outFilePath = Tkinter.Entry(self, textvariable=self.outFilePathVariable)
        self.outFilePath.grid(column=0, row=5, sticky='EW')
        currentPath = os.path.dirname(os.path.abspath(__file__))
        self.outFilePath.bind('<Return>',self.onPressEnter)
        self.outFilePathVariable.set(currentPath)

        submitButton = Tkinter.Button(self,text=u'Record Story',command=self.onButtonClick)
        submitButton.grid(column=0,row=6)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,anchor='w',fg='white',bg='blue')
        label.grid(column=0,row=7,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Enter your Captain's story")

        #self.rowconfigure(5, weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)
        self.update()
        #self.geometry(self.geometry())
        self.name.focus_set()
        self.name.selection_range(0, Tkinter.END)

    def storyToFile(self):
        self.storyList = [self.nameVariable.get(), self.yearsVariable.get(), self.echoesVariable.get(), self.coDVariable.get(), self.zeeStoryVariable.get()]
        self.xml = self.writer.generateXML(self.storyList)
        self.writer.xmlToFile(self.outFilePathVariable.get(), self.xml)
        self.labelVariable.set(self.nameVariable.get()+"'s story has been recorded")
        self.name.focus_set()
        self.name.selection_range(0, Tkinter.END)

    def onButtonClick(self):
        self.storyToFile()       

    def onPressEnter(self, event):
        self.storyToFile()

if __name__ == '__main__':
    root = Tkinter.Tk()
    app = Home(root, size)
    #app.title('SS:ZS ~ Info Entry')
    root.mainloop()