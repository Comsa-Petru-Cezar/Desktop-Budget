import os
from tkinter import *
import Budget as B
import colours as c
import Wallet as W
from math import sqrt, ceil


def clean():
    global mainRoot
    for w in mainRoot.winfo_children():
            w.grid_forget()
            w.place_forget()

Desktop_Budget_Path=os.path.join(os.path.expanduser('~'),'Documents',"Decktop_Budget")
if not os.path.exists(Desktop_Budget_Path):
    os.mkdir(Desktop_Budget_Path)
if not os.path.exists(Desktop_Budget_Path + "\\Bugete"):
    os.mkdir(Desktop_Budget_Path + "\\Bugete")

#format
mainRoot = Tk()
mainRoot.title("Desktop Budget")
mainRoot.configure(background=c.wBgCl)
try:
    iconPath = os.getcwd()
    mainRoot.iconbitmap(iconPath + "\money_100dollar.ico")
except:
    pass
mainRoot.resizable(False, False)


#this section creates elements

currentRow = 0

choseBudget = Button(mainRoot, text = "Choose Budget", width = 15, height = 5, bg = c.bBgCl,
                        command = lambda: choseBudgetClick())
newBudget = Button(mainRoot, text = "New Budget", width = 15, height = 5, bg = c.bBgCl,
                      command = lambda: newBudgetClick())

lNumeleBugetului = Label(mainRoot, text="Name the Budget", bg=c.wBgCl, )
eNumeleBugetului = Entry(mainRoot, width=20)
bCreareBuget = Button(mainRoot, text="Create Budget", width=15, height=1, bg=c.bBgCl,
                   command = lambda: creatBudgetClick(eNumeleBugetului))

buttonBackToOpen = Button(mainRoot, text="Back", width=15, height=3, bg=c.bBgCl, relief="raised",
                            command=lambda: openScreen())
cwb = None
listOfBudgetButtons = []

buttonBackToChose = Button(mainRoot, text="Back", width=15, height=3, bg=c.bBgCl, relief="raised",
                        command=lambda: choseBudgetScreen())
budgetScreenUpFrame = Frame(mainRoot, bg=c.wBgCl)
selectOO = True
selectBotton = Button(budgetScreenUpFrame, text = "Show only >", width=10,height=1,bg=c.bBgCl, relief="raised",
                      command= lambda: selectFrame())
lName = Label(budgetScreenUpFrame,text="Wallet", width=15, height=1, bg=c.bBgCl, relief="raised")
lSum = Label(budgetScreenUpFrame,text="Sum", width=20, height=1, bg=c.bBgCl, relief="raised")
lMoneda = Label(budgetScreenUpFrame,text="Currency", width=8, height=1, bg=c.bBgCl, relief="raised")
lForm = Label(budgetScreenUpFrame,text="Form", width=8, height=1, bg=c.bBgCl, relief="raised")
lStare = Label(budgetScreenUpFrame,text="State", width=8, height=1, bg=c.bBgCl, relief="raised")
listOfWallets = []
addWalletButton = Button(mainRoot, text="+Add Wallet+", width=15, height=3, bg=c.bBgCl, relief="raised",
                        command=lambda: addWalletClick())

addWalletFrame = Frame(mainRoot,bg=c.wBgCl)
sFrame = Frame(mainRoot, bg=c.wBgCl)

#but does not put them

def openScreen(): #ecranul de pornire
    clean()
    global mainRoot

    mainRoot.geometry("500x400")

    global choseBudget
    choseBudget.place(relx=0.5, rely=0.3, anchor=CENTER)

    global newBudget
    newBudget.place(relx=0.5, rely=0.7, anchor=CENTER)

def newBudgetScreen():
    clean()
    mainRoot.title("Desktop Budget - Create New Budget")

    global lNumeleBugetului
    lNumeleBugetului.place(relx=0.5, rely=0.4, anchor=CENTER)

    global eNumeleBugetului
    eNumeleBugetului.place(relx=0.5, rely=0.5, anchor=CENTER)

    global bCreareBuget
    bCreareBuget.place(relx=0.5, rely=0.6, anchor=CENTER)

    global buttonBackToOpen
    buttonBackToOpen.place(relx=0.5, rely=0.8, anchor=CENTER)

def newBudgetClick():
    newBudgetScreen()

def creatBudgetClick(e):
     n = e.get()


     #path = os.getcwd() + "\\Bugete"

     l = os.listdir(Desktop_Budget_Path + "\\Bugete")

     for i in range(len(l)):
         l[i] = l[i].upper()

     if n != '' and l.count(n.upper()) == 0 :
         global  cwb
         cwb = B.Budget(n)
         budgetScreen()
     else:
         e.delete(0,len(n))

def choseBudgetClick():
    global mainRoot
    mainRoot.geometry("800x600")
    choseBudgetScreen()

def choseBudgetScreen():
    clean()

    path = Desktop_Budget_Path + "\\Bugete"



    global listOfBudgetButtons
    global buttonBackToOpen
    global mainRoot

    mainRoot.title("Desktop Budget - Choose Budget")
    buttonBackToOpen.place(relx=0.9, rely=0.1, anchor=CENTER)
    listOfBudgetButtons = []

    for bud in os.listdir(path):
        but = Button(mainRoot, text=bud, width=15, height=5, bg=c.bBgCl,
                         command= lambda n = bud: chosenBudgetClick(n))
        listOfBudgetButtons.append(but)

    n = ceil(sqrt(len(listOfBudgetButtons)))
    i = 0
    j = 0
    for bud in listOfBudgetButtons:

        bud.grid(row = i, column = j, padx = 5, pady = 5)
        if j == n - 1:
            j = 0
            i = i + 1
        else:
            j = j + 1

def chosenBudgetClick(n):
    global cwb
    cwb = B.Budget(n, take = True)
    budgetScreen()

def budgetScreen():
    global cwb
    global mainRoot
    global addWalletButton

    clean()
    mainRoot.title("Desktop Budget - " + str(cwb.name))
    mainRoot.geometry("1100x650")

    buttonBackToChose.place(relx=0.9, rely=0.1, anchor=CENTER)

    global lName
    global lSum
    global lMoneda
    global lForm
    global lStare
    global budgetScreenUpFrame
    r = 1

    lName.grid(row=r, column=0, padx=2, pady=2,sticky="w")
    lMoneda.grid(row=r, column=1, padx=2, pady=2,sticky="w")
    lForm.grid(row=r, column=2, padx=2, pady=2,sticky="w")
    lStare.grid(row=r, column=3, padx=2, pady=2,sticky="w")
    lSum.grid(row=r, column=4, padx=2, pady=2,sticky="w")
    selectBotton.grid(row=0, column=0, padx=2, pady=2, sticky="w", columnspan=2)
    budgetScreenUpFrame.grid(pady=(5,15),padx=(5,1), columnspan=5,sticky="w")
    listTheWallets()

def listTheWallets(filter = None):
    global currentRow
    currentRow = 1
    global cwd
    for w in cwb.listOfWallets:
        try:
            w.walletOfScreen()
        except:
            pass
    if filter != None and filter != []:


        for w in cwb.listOfWallets:

            for ch in w.listOfChoses:
                if w.listOfChoses[ch] in filter:
                    w.walletOnScreen(mainRoot, currentRow, cwb, sFrame)
                    currentRow = currentRow + 1
                    break
    else:
        for w in cwb.listOfWallets:
            w.walletOnScreen(mainRoot, currentRow, cwb, sFrame)
            currentRow = currentRow + 1


    addWalletButtonShow(currentRow)

def addWalletButtonShow(r):
    addWalletButton.grid_forget()
    addWalletButton.grid(row=r + 2,column=0,  padx=10, pady=(50, 5), columnspan=3, sticky="NW")

def addWalletClick():
    global cwb
    global addWalletFrame
    global currentRow
    global addWalletButton
    global sFrame
    global selectOO
    selectOO = True
    sFrame.grid_forget()
    for v in addWalletFrame.winfo_children():
        try:
            v.destroy()
        except:
            pass
    for w in cwb.listOfWallets:
        try:
            w.newTransFrame.destroy()
        except:
            pass

    addWalletButton.grid_forget()
    addWalletFrame.grid(row = currentRow, column=0)

    Label(addWalletFrame, text="Wallet", width=20, height=1, bg=c.wBgCl, pady=5).grid(row=currentRow,
                                                                column=0,padx=1,  pady=(10, 5), columnspan=2)
    n = Entry(addWalletFrame, width=20)
    n.grid(row=currentRow + 1, column=0, padx=1, pady=3, columnspan=2)

    # set suma initiala
    Label(addWalletFrame, text="Sum", width=20, height=1, bg=c.wBgCl, pady=5).grid(row=currentRow,
                                                                       column=2, padx=1, pady=(10, 5), columnspan=2)
    s = Entry(addWalletFrame, width=20)
    s.grid(row=currentRow + 1, column=2,padx=1,  pady=3, columnspan=2)



    newWalletButton = Button(addWalletFrame, text="New Wallet", width=15, height=3, bg=c.bBgCl, relief="raised",
                             command=lambda: newWalletClick(addWalletFrame, n, s))
    newWalletButton.grid(row=currentRow + 2, column=9, pady=5, columnspan=2,rowspan=3)

    backButton = Button(addWalletFrame, text="Back", width=15, height=3, bg=c.bBgCl, relief="raised",
                             command=lambda:  backClick(addWalletFrame))
    backButton.grid(row=currentRow + 4, column=9, pady=5, columnspan=2, rowspan=3)

    newW = W.Wallet(cwb.name, root=addWalletFrame, cr=currentRow)

    def backClick(r):
        nonlocal newW
        for v in r.winfo_children():
            try:
                v.deselect()
            except:
                pass
        for v in addWalletFrame.winfo_children():
            try:
                v.destroy()
            except:
                pass
        r.grid_forget()
        del newW
        addWalletButtonShow(len(cwb.listOfWallets))

    def newWalletClick(r,n,s):
        nonlocal newW
        o = True


        for a in newW.listOfChoses:
            if a == None:
                o = False

        na = n.get()
        su_int = 0

        if na == '':
            o = False
            n.delete(0, len(na))
        try:
            su = s.get()
            su_int = int(su)
            if su_int < 0:
                o = False
                s.delete(0, len(su))
        except:
            o = False
            s.delete(0, len(su))

        if o:
            newW.newWalletClick(na, su_int)
            cwb.listOfWallets.append(newW)
            for v in r.winfo_children():
                try:
                    v.deselect()
                except:
                    pass

            for v in addWalletFrame.winfo_children():
                try:
                    v.destroy()
                except:
                    pass
            r.grid_forget()
            r.grid_forget()
            listTheWallets()

def selectFrame():
    global addWalletFrame
    global cwb
    global sFrame
    global  selectOO

    for wall in cwb.listOfWallets:
        try:
            wall.newTransFrame.destroy()
        except:
            pass

    addWalletFrame.grid_forget()
    sFrame.grid_forget()
    for es in sFrame.winfo_children():
        es.grid_forget()

    if selectOO:
        selectOO = False
        global addWalletButtonShow
        addWalletButtonShow(len(cwb.listOfWallets))
        for w in cwb.listOfWallets:
            try:
                w.destroy()
            except:
                pass


        i = 2
        listOfS = []
        for cs in W.Wallet.listOfLists:
            for cc in W.Wallet.listOfLists[cs]:
                l = Checkbutton(sFrame,text=cc,bg=c.wBgCl, command=lambda s=cc: select(s))
                l.deselect()
                l.grid(row=0,column=i,sticky="NW")
                i = i + 1

        def select(s):

            global sFrame
            nonlocal listOfS
            if s in listOfS:
                listOfS.remove(s)
            else:
                listOfS.append(s)
            listTheWallets(listOfS)

        clearB= Button(sFrame, text="Clear Filter",width=10,height=1,bg=c.bBgCl, relief="raised",
                          command= lambda: clearCommand())
        clearB.grid(row=0, column=10,sticky="NW")

        def clearCommand():

            global sFrame
            nonlocal listOfS
            listOfS = None
            listTheWallets()
            for eee in sFrame.winfo_children():
                try:
                    eee.deselect()
                except:
                    pass



        sFrame.grid(row=0,column=2,padx=100,pady=5, sticky="N")
    else:
        selectOO = True

openScreen()


mainRoot.mainloop()




