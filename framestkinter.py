from tkinter import *
from PIL import ImageTk, Image
import os

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #label = Label(self, text="This is page 1")
       img = Image.open("/home/moy/Escritorio/tkinter_amaretos/amaretos.png")
       img = img.resize((300, 300), Image.ANTIALIAS)
       img = ImageTk.PhotoImage(img)
       panel = Label(self, image = img)
       panel.image = img
       E1 = Entry(self, bd = 1)
       E2 = Entry(self, bd = 1,show='*')
       L1 = Label (self, text = "Recuperar contraseña")
       #panel.pack(side = "bottom")
       panel.pack(side="top", fill="both", expand=True)
       c = Button(self, text="Iniciar sesión")       
       E1.place(relx=0.85, rely=0.20, anchor=SE)
       E2.place(relx=0.85, rely=0.30, anchor=SE)
       L1.place(relx=0.85, rely=0.40, anchor=SE)
       c.place(relx=0.85, rely=0.50, anchor=SE)
       #E1.pack(side="top")

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       E1 = Entry(self, bd = 1) #Centavos
       E2 = Entry(self, bd = 1) #Peso
       E3 = Entry(self, bd = 1) #2 Peso
       E4 = Entry(self, bd = 1) #5 Pesos
       E5 = Entry(self, bd = 1) #10 Pesos
       E6 = Entry(self, bd = 1) #20 Pesos
       E7 = Entry(self, bd = 1) #50 Pesos
       E8 = Entry(self, bd = 1) #100 Pesos
       E9 = Entry(self, bd = 1) #200 Pesos
       E10 = Entry(self, bd = 1) #500 Pesos
       E11 = Entry(self, bd = 1) #1000 Pesos
       c = Button(self, text="Recibir caja")   

       E1.place(relx=0.35,rely=0.1,width=50,anchor=SE)
       E2.place(relx=0.35,rely=0.2,width=50,anchor=SE)
       E3.place(relx=0.35,rely=0.3,width=50,anchor=SE)
       E4.place(relx=0.35,rely=0.4,width=50,anchor=SE)
       E5.place(relx=0.35,rely=0.5,width=50,anchor=SE)
       E6.place(relx=0.35,rely=0.6,width=50,anchor=SE)
       E7.place(relx=0.65,rely=0.1,width=50,anchor=SE)
       E8.place(relx=0.65,rely=0.2,width=50,anchor=SE)
       E9.place(relx=0.65,rely=0.3,width=50,anchor=SE)
       E10.place(relx=0.65,rely=0.4,width=50,anchor=SE)
       E11.place(relx=0.65,rely=0.5,width=50,anchor=SE)

       L1 = Label (self, text = "Centavos")
       L2 = Label (self, text = "Peso")
       L3 = Label (self, text = "$2")
       L4 = Label (self, text = "$5")
       L5 = Label (self, text = "$10")
       L6 = Label (self, text = "$20")
       L7 = Label (self, text = "$50")
       L8 = Label (self, text = "$100")
       L9 = Label (self, text = "$200")
       L10 = Label (self, text = "$500")
       L11 = Label (self, text = "$1000")       

       L1.place(relx=0.2, rely=0.1,anchor=SE)
       L2.place(relx=0.2, rely=0.2,anchor=SE)
       L3.place(relx=0.2, rely=0.3,anchor=SE)
       L4.place(relx=0.2, rely=0.4,anchor=SE)
       L5.place(relx=0.2, rely=0.5,anchor=SE)
       L6.place(relx=0.2, rely=0.6,anchor=SE)
       L7.place(relx=0.5, rely=0.1,anchor=SE)
       L8.place(relx=0.5, rely=0.2,anchor=SE)
       L9.place(relx=0.5, rely=0.3,anchor=SE)
       L10.place(relx=0.5, rely=0.4,anchor=SE)
       L11.place(relx=0.5, rely=0.5,anchor=SE)

       c.place(relx=0.70, rely=0.60, anchor=SE)

       
       #label = Label(self, text="This is page 2")
       #label.pack(side="top", fill="both", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class Page4(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 4")
       label.pack(side="top", fill="both", expand=True)

class MainView(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
               

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Autenticación", command=p1.lift)
        b2 = Button(buttonframe, text="Caja", command=p2.lift)
        b3 = Button(buttonframe, text="Comanda", command=p3.lift)
        b4 = Button(buttonframe, text="Inventarios", command=p4.lift)
        
        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")     
        b4.pack(side="left")  
       
        p1.show()

if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()