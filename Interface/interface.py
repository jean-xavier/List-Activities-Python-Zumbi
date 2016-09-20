try:
    from Tkinter import *  #Python2
except ImportError:
    from tkinter import *  #Python3

def apertei_botao():
    print("Apertei o botão!")

app = Tk()
app.title("Massa")
app.geometry('300x100+200+100')

b1 = Button(app, text = "Certo", width = 10)
b1.pack(side = "left", padx = 10, pady = 10)

b2 = Button(app, text = "Errado", width = 10)
b2.pack (side = "right", padx = 10, pady = 10)

# b = Button(app, text = "Aperte-me", width = 10, command = apertei_botao)
# b.pack(side = "top", padx = 10, pady = 10)

app.mainloop()
