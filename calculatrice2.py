####################################################################
#@ calculatrice
#@ 01/02/2017
#@ Thomas LE BRUN
#####################################################################
# Module Import
from tkinter import *
calc = Tk()

tot=""
totold=""
signe="0"
affichage = StringVar ()
affichage.set(tot)
result = StringVar ()
result.set(tot)

# Function and variable creation

def display():
    global tot
    global signe
    global totold
    if (signe != "0"):
        local= totold,signe,tot
        affichage.set(local)
    else :
        affichage.set(tot)

def ajout(nb):
    global tot
    tot=tot+nb
    display()

def calcul():
    global signe
    global tot
    global totold
    global result
    calc1=eval(totold)
    calc2= eval(tot)

    if (signe == "+"):
       res= calc1+calc2
    elif (signe == "-"):
       res= calc1-calc2
    elif (signe == "*"):
       res= calc1*calc2
    elif (signe == "/"):
       res= calc1/calc2
    result.set(res)



def zero():
    ajout("0")

def un():
    ajout("1")

def deux():
    ajout("2")

def trois():
    ajout("3")

def quatre():
    ajout("4")

def cinq():
    ajout("5")

def six():
    ajout("6")

def sept():
    ajout("7")

def huit():
    ajout("8")

def neuf():
    ajout("9")

def plus():
    global signe
    global tot
    global totold
    totold=tot
    tot=""
    signe = "+"
    display()


def moins():
    global signe
    global tot
    global totold
    totold=tot
    tot=""
    signe = "-"
    display()

def multi():
    global signe
    global tot
    global totold
    totold = tot
    tot = ""
    signe = "*"
    display()

def diviser():
    global signe
    global tot
    global totold
    totold = tot
    tot = ""
    signe = "/"
    display()

def reini() :
    display()

def virgule():
    ajout(".")

def egale():
    global signe
    global tot
    global totold
    calcul()
    tot=""
    totold=""
    signe = "0"

    display()

# Body script

calcule = Label (calc, textvariable=affichage)
calcule.grid(row =0, column =0,ipady=15, sticky = W+E, columnspan=4)

resultat = Label (calc, textvariable=result)
resultat.grid(row =1, column =0,ipady=15, sticky = W+E, columnspan=2)


zero = Button(calc, text ='0', command=zero)
zero.grid(row =5, column =0, padx=5, pady=5, ipadx=15, ipady=15)

un = Button(calc, text ='1', command=un)
un.grid(row =2, column =0, padx=5, pady=5, ipadx=15, ipady=15)

deux = Button(calc, text ='2', command=deux)
deux.grid(row =2, column =1, padx=5, pady=5, ipadx=15, ipady=15)

un = Button(calc, text ='3', command=trois)
un.grid(row =2, column =2, padx=5, pady=5, ipadx=15, ipady=15)

un = Button(calc, text ='4', command=cinq)
un.grid(row =3, column =0, padx=5, pady=5, ipadx=15, ipady=15)

deux = Button(calc, text ='5', command=cinq)
deux.grid(row =3, column =1, padx=5, pady=5, ipadx=15, ipady=15)

un = Button(calc, text ='6', command=six)
un.grid(row =3, column =2, padx=5, pady=5, ipadx=15, ipady=15)

un = Button(calc, text ='7', command=sept)
un.grid(row =4, column =0, padx=5, pady=5, ipadx=15, ipady=15)

huit = Button(calc, text ='8', command=huit)
huit.grid(row =4, column =1, padx=5, pady=5, ipadx=15, ipady=15)

neuf = Button(calc, text ='9', command=neuf)
neuf.grid(row =4, column =2, padx=5, pady=5, ipadx=15, ipady=15)


plus = Button(calc, text ='+', command=plus)
plus.grid(row =1, column =3, padx=5, pady=5, ipadx=15, ipady=15)

moins = Button(calc, text ='-', command=moins)
moins.grid(row =2, column =3, padx=5, pady=5, ipadx=15, ipady=15)

multi = Button(calc, text ='*', command=multi)
multi.grid(row =3, column =3, padx=5, pady=5, ipadx=15, ipady=15)

diviser = Button(calc, text ='/', command=diviser)
diviser.grid(row =4, column =3, padx=5, pady=5, ipadx=15, ipady=15)


virgule = Button(calc, text =',', command=virgule)
virgule.grid(row =5, column =1, padx=5, pady=5, ipadx=15, ipady=15,)

reini = Button(calc, text ='C', command=reini)
reini.grid(row =1, column =2, padx=5, pady=5, ipadx=15, ipady=15)

egale = Button(calc, text ='=', command=egale)
egale.grid(row =5, column =2, padx=5, pady=5, ipadx=43, ipady=15, columnspan=2)


calc.mainloop()
