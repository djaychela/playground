import tkinter


class App:
    def __init__(self, master):

        frame = tkinter.Frame(master)
        frame.pack()

        self.button = tkinter.Button(
            frame, text='QUIT', fg='red', command=frame.quit
        )
        self.button.pack(side=tkinter.RIGHT)

        self.hi_there = tkinter.Button(frame, text='Hello', command=self.say_hi)
        self.hi_there.pack(side=tkinter.LEFT)

        self.oi = tkinter.Button(frame, text='oi', command=self.oi_noise)
        self.oi.pack(side=tkinter.RIGHT)

    @staticmethod
    def say_hi():
        print('hi there')

    @staticmethod
    def oi_noise():
        print('noise!')


root = tkinter.Tk()

app = App(root)

root.mainloop()
root.destroy()
