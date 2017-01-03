from tkinter import *

calc = Tk()

# ************* Variables *************

global affichage
global res
global result
global chiffre
global number
global number2
global signe
global chifreold
global neg
global virg

chiffre = 0
chifreold = 0
signe = "0"
number=1
number2=0.1
neg = 0
virg = 0
affichage = StringVar ()
affichage.set(chiffre)
result = 0
res = StringVar ()
res.set(chiffre)


#************* Fonctions calcules *************

def display():
    if (signe != "0"):
        local= chifreold,signe,chiffre
        affichage.set(local)
    else :
        affichage.set(chiffre)

def ajout(nb):
    global chiffre
    global number
    chiffre=chiffre*number+nb
    number=10
    display()

def ajoutvirg(nb):
    global chiffre
    global number2
    chiffre=chiffre+nb*number2
    number2=number2*0.1
    display()

def ajoutneg(nb):
    global chiffre
    global number
    chiffre= chiffre*(-1)
    chiffre=chiffre*number+nb
    number=10
    chiffre= chiffre*(-1)
    display()

def ajoutvirgneg(nb):
    global chiffre
    global number2
    chiffre= chiffre*(-1)
    chiffre=chiffre+nb*number2
    number2=number2*0.1
    chiffre= chiffre*(-1)
    display()

def newcalc(sig):
    global chiffre
    global number
    global number2
    global signe
    global chifreold
    global neg
    global virg
    if (signe == "+"):
        chifreold = chifreold+chiffre
    elif (signe == "-"):
        chifreold = chifreold-chiffre
    elif (signe == "*"):
        chifreold = chifreold*chiffre
    elif (signe == "/"):
        chifreold = chifreold/chiffre
    chiffre= 0
    signe = sig
    neg = 0
    virg = 0
    number=1
    number2=0.1

#************* Fonctions boutons *************

def zero():
    if (virg==0 and neg==0):
        ajout(0)
    elif(virg==1 and neg==0):
        ajoutvirg(0)
    elif(virg==0 and neg==1):
        ajoutneg(0)
    elif(virg==1 and neg==1):
        ajoutvirgneg(0)

def un():
    if (virg==0 and neg==0):
        ajout(1)
    elif(virg==1 and neg==0):
        ajoutvirg(1)
    elif(virg==0 and neg==1):
        ajoutneg(1)
    elif(virg==1 and neg==1):
        ajoutvirgneg(1)

def deux():
    if (virg==0 and neg==0):
        ajout(2)
    elif(virg==1 and neg==0):
        ajoutvirg(2)
    elif(virg==0 and neg==1):
        ajoutneg(2)
    elif(virg==1 and neg==1):
        ajoutvirgneg(2)

def trois():
    if (virg==0 and neg==0):
        ajout(3)
    elif(virg==1 and neg==0):
        ajoutvirg(3)
    elif(virg==0 and neg==1):
        ajoutneg(3)
    elif(virg==1 and neg==1):
        ajoutvirgneg(3)

def quatre():
    if (virg==0 and neg==0):
        ajout(4)
    elif(virg==1 and neg==0):
        ajoutvirg(4)
    elif(virg==0 and neg==1):
        ajoutneg(4)
    elif(virg==1 and neg==1):
        ajoutvirgneg(4)

def cinq():
    if (virg==0 and neg==0):
        ajout(5)
    elif(virg==1 and neg==0):
        ajoutvirg(5)
    elif(virg==0 and neg==1):
        ajoutneg(5)
    elif(virg==1 and neg==1):
        ajoutvirgneg(5)

def six():
    if (virg==0 and neg==0):
        ajout(6)
    elif(virg==1 and neg==0):
        ajoutvirg(6)
    elif(virg==0 and neg==1):
        ajoutneg(6)
    elif(virg==1 and neg==1):
        ajoutvirgneg(6)

def sept():
    if (virg==0 and neg==0):
        ajout(7)
    elif(virg==1 and neg==0):
        ajoutvirg(7)
    elif(virg==0 and neg==1):
        ajoutneg(7)
    elif(virg==1 and neg==1):
        ajoutvirgneg(7)

def huit():
    if (virg==0 and neg==0):
        ajout(8)
    elif(virg==1 and neg==0):
        ajoutvirg(8)
    elif(virg==0 and neg==1):
        ajoutneg(8)
    elif(virg==1 and neg==1):
        ajoutvirgneg(8)

def neuf():
    if (virg==0 and neg==0):
        ajout(9)
    elif(virg==1 and neg==0):
        ajoutvirg(9)
    elif(virg==0 and neg==1):
        ajoutneg(9)
    elif(virg==1 and neg==1):
        ajoutvirgneg(9)

def plus():
    global chifreold
    global signe
    global chiffre
    global neg
    global virg
    global number
    global number2
    if (signe == "0"):
        chifreold = chiffre
        chiffre=0
        signe ="+"
        neg= 0
        virg=0
        number=1
        number2=0.1
    else:
        newcalc("+")

    display()

def moins():
    global chifreold
    global signe
    global chiffre
    global neg
    global virg
    global number
    global number2
    if (signe == "0"):
        chifreold = chiffre
        chiffre=0
        signe ="-"
        neg= 0
        virg=0
        number=1
        number2=0.1
    elif (chiffre!=0):
        newcalc("-")
    else:
         neg=1

    display()

def multi():
    global chifreold
    global signe
    global chiffre
    global neg
    global virg
    global number
    global number2
    if (signe == "0"):
        chifreold = chiffre
        chiffre=0
        signe ="*"
        neg= 0
        virg=0
        number=1
        number2=0.1
    else:
        newcalc("*")

    display()

def diviser():
    global chifreold
    global signe
    global chiffre
    global neg
    global virg
    global number
    global number2
    if (signe == "0"):
        chifreold = chiffre
        chiffre=0
        signe ="/"
        neg= 0
        virg=0
        number=1
        number2=0.1
    else:
        newcalc("/")

    display()

def reini() :
    global chiffre
    global number
    global number2
    global signe
    global chifreold
    global neg
    global virg
    chiffre= 0
    chifreold = 0
    signe = "0"
    number=1
    number2=0.1
    neg = 0
    virg = 0
    display()

def virgule():
    global virg
    global chiffre
    virg=1
    chiffre=float(chiffre)

def egale():
    global chiffre
    global signe
    global chifreold
    global result
    global res
    global virg
    global neg
    if (signe == "+"):
       chiffre= chifreold+chiffre
    elif (signe == "-"):
       chiffre= chifreold-chiffre
    elif (signe == "*"):
       chiffre= chifreold*chiffre
    elif (signe == "/"):
       chiffre= chifreold/chiffre
    neg=0
    virg=0
    chifreold = 0
    signe = "0"
    result = chiffre
    display()
    res.set(chiffre)

# ************* Resultat *************

calcule = Label (calc, textvariable=affichage)
calcule.grid(row =0, column =0,ipady=15, sticky = W+E, columnspan=4)

resultat = Label (calc, textvariable=res)
resultat.grid(row =1, column =0,ipady=15, sticky = W+E, columnspan=2)


# ************* Bouton numeros *************

zero = Button(calc, text ='0', command=zero)
zero.grid(row =5, column =0, padx=5, pady=5, ipadx=15, ipady=15)

un = Button(calc, text ='1', command=un)
un.grid(row =2, column =0, padx=5, pady=5, ipadx=15, ipady=15)

deux = Button(calc, text ='2', command=deux)
deux.grid(row =2, column =1, padx=5, pady=5, ipadx=15, ipady=15)

un = Button(calc, text ='3', command=trois)
un.grid(row =2, column =2, padx=5, pady=5, ipadx=15, ipady=15)

un = Button(calc, text ='4', command=quatre)
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

# ************* Bouton calcules *************

plus = Button(calc, text ='+', command=plus)
plus.grid(row =1, column =3, padx=5, pady=5, ipadx=15, ipady=15)

moins = Button(calc, text ='-', command=moins)
moins.grid(row =2, column =3, padx=5, pady=5, ipadx=15, ipady=15)

multi = Button(calc, text ='*', command=multi)
multi.grid(row =3, column =3, padx=5, pady=5, ipadx=15, ipady=15)

diviser = Button(calc, text ='/', command=diviser)
diviser.grid(row =4, column =3, padx=5, pady=5, ipadx=15, ipady=15)

# ************* Bouton specifique *************

virgule = Button(calc, text =',', command=virgule)
virgule.grid(row =5, column =1, padx=5, pady=5, ipadx=15, ipady=15,)

reini = Button(calc, text ='C', command=reini)
reini.grid(row =1, column =2, padx=5, pady=5, ipadx=15, ipady=15)

egale = Button(calc, text ='=', command=egale)
egale.grid(row =5, column =2, padx=5, pady=5, ipadx=43, ipady=15, columnspan=2)


# ************* start *************
calc.mainloop()
