import Tkinter
from writer import XMLWriter

class Home(object):
    def __init__(self, parent):
        self.root = parent
        self.frame = Tkinter.Frame(parent)
        self.frame.grid()
        self.initialise()

    def initialise(self):
        
        self.root.title('SS:ZS ~ Home')

        self.newEntryButton = Tkinter.Button(self.frame,text=u'Enter new Zee Story',command=self.newEntryClick)
        self.newEntryButton.grid(column=0,row=0)

    def newEntryClick(self):
        print 'test'


class InfoEntry(Tkinter.Toplevel):
    def __init__(self):
        Tkinter.Toplevel.__init__(self)
        self.root = parent
        self.initialise()

    def initialise(self):
        self.grid()
        self.root.title('SS:ZS ~ Enter Info')


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
        self.coDVariable.set('Cause of Death')

        #use text widget instead of Entry to allow for multiple lines.
        #add backend functionality & button to enable upload of a .txt file?
        self.zeeStoryVariable = Tkinter.StringVar()
        self.zeeStory = Tkinter.Entry(self, textvariable=self.zeeStoryVariable)
        self.zeeStory.grid(column=0, row=4, sticky='EW')
        self.zeeStoryVariable.set("Tell your Captain's story")

        #will be made functional after deciding on best usage
        #Use setuptools package resources for filepaths?
        """self.outFilePathVariable = Tkinter.StringVar()
        self.outFilePath = Tkinter.Entry(self, textvariable=self.outFilePathVariable)
        self.outFilePath.grid(column=0, row=5, sticky='EW')
        self.outFilePathVariable.set()"""

        submitButton = Tkinter.Button(self,text=u'Record Story',command=self.onButtonClick)
        submitButton.grid(column=0,row=5)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,anchor='w',fg='white',bg='blue')
        label.grid(column=0,row=6,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Enter your Captain's story")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,True)
        self.update()
        self.geometry(self.geometry())
        self.name.focus_set()
        self.name.selection_range(0, Tkinter.END)

    def onButtonClick(self):
        self.xml = self.writer.generateXML(self.nameVariable.get(), self.yearsVariable.get(), self.echoesVariable.get(), self.coDVariable.get(), self.zeeStoryVariable.get())
        self.writer.xMLToFile(self.xml, 'test1.xml')
        self.labelVariable.set(self.nameVariable.get()+' Clicked button yo!')
        self.name.focus_set()
        self.name.selection_range(0, Tkinter.END)

    def onPressEnter(self, event):
        #This isn't very pretty. Change generateXML to take a list?
        self.xml = self.writer.generateXML(self.nameVariable.get(), self.yearsVariable.get(), self.echoesVariable.get(), self.coDVariable.get(), self.zeeStoryVariable.get())
        self.writer.xMLToFile(self.xml, 'test1.xml')
        self.labelVariable.set(self.nameVariable.get()+' Hit enter yo!')
        self.name.focus_set()
        self.name.selection_range(0, Tkinter.END)

if __name__ == '__main__':
    root = Tkinter.Tk()
    app = Home(root)
    #app.title('SS:ZS ~ Info Entry')
    root.mainloop()