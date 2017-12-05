import tkinter as tk
import globalVars
from tableModification import dbMod

LARGE_FONT = ("Verdana", 12)

global db

class tkTest(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, dbConfig, btLogger):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, stick="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def exit(self):
        app.quit()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        controller.minsize(width=300, height=300)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="dbConfig", command=lambda: controller.show_frame(dbConfig))
        button1.pack()
        button2 = tk.Button(self, text="Bluetooth", command=lambda: controller.show_frame(btLogger))
        button2.pack()

        exitButton = tk.Button(self, text="Exit", command=lambda: tkTest.quit(self))
        exitButton.pack()

class dbConfig(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="User: ", font = LARGE_FONT).grid(row=0)
        tk.Label(self, text="Password: ", font = LARGE_FONT).grid(row=1)
        tk.Label(self, text="Host: ", font = LARGE_FONT).grid(row=2)
        tk.Label(self, text="Database Name: ", font = LARGE_FONT).grid(row=3)
        tk.Label(self, text="Port: ", font = LARGE_FONT).grid(row=4)
        e0 = tk.Entry(self)
        e0.insert(0, 'alwayskamin')
        e0.grid(row=0, column=1)
        e1 = tk.Entry(self, show="*")
        e1.grid(row=1, column=1)
        e2 = tk.Entry(self)
        e2.insert(0, 'db4free.net')
        e2.grid(row=2, column=1)
        e3 = tk.Entry(self)
        e3.insert(0, 'btlogger')
        e3.grid(row=3, column=1)
        e4 = tk.Entry(self)
        e4.insert(0, '3307')
        e4.grid(row=4, column=1)

        tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage)).grid(row=5, column=1, sticky="w")
        tk.Button(self, text="Connect", command=lambda: self.getInput(e0, e1, e2, e3, e4)).grid(row=5, column=2, sticky="w")

    def getInput(self, e0, e1, e2, e3, e4):
        print("Show data")
        globalVars.username = e0.get()
        globalVars.password = e1.get()
        globalVars.hostname = e2.get()
        globalVars.db = e3.get()
        globalVars.port = int(e4.get())
        db = dbMod()
        print(dbMod.showVersion(db))

class btLogger(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Button(self, text="Start", command=lambda: self.startScanning()).grid(row=0, column=1, sticky="w")
        tk.Button(self, text="Stop", command=lambda: self.stopScanning()).grid(row=0, column=2, sticky="w")
        tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage)).grid(row=0, column=3, sticky="w")



    def startScanning(self):
        print("Scanning")

    def stopScanning(self):
        print("Done Scanning")


app = tkTest()
app.mainloop()