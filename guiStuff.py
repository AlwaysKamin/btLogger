import Tkinter as tk

LARGE_FONT = ("Verdana", 12)

class tkTest(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, dbConfig):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, stick="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        controller.minsize(width=300, height=300)
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font = LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="dbConfig", command=lambda: controller.show_frame(dbConfig))
        button1.pack()

class dbConfig(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="User: ", font = LARGE_FONT).grid(row=0)
        tk.Label(self, text="Password: ", font = LARGE_FONT).grid(row=1)
        tk.Label(self, text="Host: ", font = LARGE_FONT).grid(row=2)
        tk.Label(self, text="Database Name: ", font = LARGE_FONT).grid(row=3)
        e0 = tk.Entry(self)
        e0.grid(row=0, column=1)
        e1 = tk.Entry(self, show="*")
        e1.grid(row=1, column=1)
        e2 = tk.Entry(self)
        e2.grid(row=2, column=1)
        e3 = tk.Entry(self)
        e3.grid(row=3, column=1)

        tk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage)).grid(row=4, column=1, sticky="w")
        tk.Button(self, text="Show", command=lambda: self.getInput(e0, e1, e2, e3)).grid(row=4, column=2, sticky="w")

    def getInput(self, e0, e1, e2, e3):
        print("Show data")
        Username = e0.get()
        Password = e1.get()
        HostName = e2.get()
        Database = e3.get()
        print("User: " + Username + " pass: " + Password + " host: " + HostName + " databaseName: " + Database)


app = tkTest()
app.mainloop()