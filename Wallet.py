import os
from tkinter import *
import colours as C
import csv

class Wallet:


    listOfFields = ["in/out", "sum", "date","repeat"]
    listOfCurency = ["Euro", "Ron", "Dolar"]


    listOfForms = ["Physical", "Virtual"]


    listOfStates = ["Current", "Debt", "Loan"]

    listOfLists = {}
    listOfLists["Currency"] = listOfCurency
    listOfLists["Form"] = listOfForms
    listOfLists["State"] = listOfStates

    def walletOfScreen(self):
        self.onScreen.grid_forget()

    def walletOnScreen(self, root, r, cwb, f1):
        self.onScreen = Frame(root, bg = C.wBgCl)

        lName = Label(self.onScreen, text=self.name, width=15, height=1)
        self.lSum = Label(self.onScreen, text=self.sumaActuala, width=20, height=1)
        lMoneda = Label(self.onScreen, text=self.listOfChoses["Currency"], width=8, height=1 )
        lForm = Label(self.onScreen, text=self.listOfChoses["Form"], width=8, height=1)
        lStare = Label(self.onScreen, text=self.listOfChoses["State"], width=8, height=1,)
        Plas = Button(self.onScreen, text="+", width=4, height=1, bg=C.bBgCl, relief="raised",
                                   command=lambda: self.newTrans(r, root, cwb, f1))
        History = Button(self.onScreen, text="=", width=4, height=1, bg=C.bBgCl, relief="raised",
                        command=lambda: self.showTrans(cwb))


        lName.grid(row=r, column=0, padx=2, pady=2,sticky="w")
        lMoneda.grid(row=r, column=1, padx=2, pady=2,sticky="w")
        lForm.grid(row=r, column=2, padx=2, pady=2,sticky="w")
        lStare.grid(row=r, column=3, padx=2, pady=2,sticky="w")
        self.lSum.grid(row=r, column=4, padx=2, pady=2,sticky="w")
        History.grid(row=r, column=5, padx=2, pady=2,sticky="w")
        Plas.grid(row=r, column=6, padx=2, pady=2, sticky="w")

        (self.onScreen).grid(row=r,column=0,columnspan=5, padx=(5,1), sticky="w")

    def chs(self, lcds, set, ch):
        for b in lcds:
            if b["text"] != ch:
                b.deselect()
        self.listOfChoses[set] = ch

    def newWalletScreen(self, r, cr, set, col):

        self.listOfChoses[set] = None



        rf = 2

        lf = Label(r, text=set, width=15, height=1, bg=C.wBgCl,  anchor =  W)
        lf.grid(row=cr + rf, column=col, pady=(50, 2), sticky = "W", columnspan=2)


        i = 0
        lcb = []
        for a in self.listOfLists[set]:
            cb = Checkbutton(r, text=a, width=15, height=1, bg=C.wBgCl, anchor =  W,
                                 command=lambda al=a,lcds=lcb,s=self: self.chs(lcds,set, al))
            lcb.append(cb)
            lcb[i].deselect()
            lcb[i].grid(row=cr + rf + i + 1, column=col,pady=2, sticky = "W", columnspan = 2)
            i = i + 1
        r.grid(row=cr, columnspan=7)

    def creatFile(self):
        fileName = self.name + "_" + str(self.sumaInitiala)
        fileName = fileName + "_" + self.listOfChoses["Currency"] + "_" + self.listOfChoses["Form"] + "_" + self.listOfChoses["State"]
        self.path = os.path.join(os.path.expanduser('~'),'Documents',"Decktop_Budget") + "\\Bugete" + "\\" + self.budgetName + "\\" + fileName
        f = open(self.path, "w")
        for fi in self.listOfFields:
            if fi != self.listOfFields[-1]:
                f.write(fi + ",")
            else:
                f.write(fi+"\n")

    def newWalletClick(self, n, s):
        self.name = n
        self.sumaInitiala = s
        self.sumaActuala = float(s)
        self.creatFile()

    def newTrans(self, r, root, cwb, f1):
        for w in cwb.listOfWallets:
            try:
                w.newTransFrame.destroy()
            except:
                pass

        f1.grid_forget()

        self.newTransFrame = Frame(root,  bg = C.wBgCl)

        sumE = Entry(self.newTransFrame, width=15)
        In = None
        Out = None
        inout = None
        sad = 0
        sex = 0
        sre = 0

        In = Checkbutton(self.newTransFrame, text="+in+", bg=C.wBgCl, command=lambda: inCheck(),foreground='#004a0a')
        Out = Checkbutton(self.newTransFrame, text="-out-", bg=C.wBgCl, command=lambda: outCheck(),foreground='#960202')
        lLink = Label(self.newTransFrame, text="to/from", width=6, height=1,bg=C.bBgCl,relief="raised")
        lLinkEx = Label(self.newTransFrame, text="to/from", width=6, height=1, bg=C.bBgCl, relief="raised")
        linkE = Entry(self.newTransFrame, width=15)
        exchange = Checkbutton(self.newTransFrame, text="exchange", bg=C.wBgCl, command=lambda: exchangeCheck())
        repeat = Checkbutton(self.newTransFrame, text="repeat", bg=C.wBgCl, command=lambda: repeatCheck())
        repeat.deselect()

        In.deselect()
        Out.deselect()
        exchange.deselect()
        ex = Entry(self.newTransFrame, width=5)
        linKEx = Entry(self.newTransFrame, width=5)

        anotherday = Checkbutton(self.newTransFrame, text="another day", bg=C.wBgCl, command=lambda: anotherCheck())

        In.grid(row=r-1, column=8, padx=0, pady=0, sticky="w")
        Out.grid(row=r-1, column=9, padx=0, pady=0, sticky="w")
        lLink.grid(row=r, column=10,columnspan=1, padx=0, pady=0, sticky="n")
        linkE.grid(row=r, column=11, columnspan=1, padx=10, pady=0, sticky="w")
        anotherday.grid(row=r+3, column=8, columnspan=2, padx=0, pady=0, sticky="w")
        exchange.grid(row=r+2, column=8, columnspan=2, padx=0, pady=0, sticky="w")
        repeat.grid(row=r+7, column=8, columnspan=2, padx=0, pady=0, sticky="w")

        sumE.grid(row=r, column=8,columnspan=2, padx=5, pady=0, sticky="w")
        addTrans = Button(self.newTransFrame,text="Do", width=5, height=1, bg=C.bBgCl, relief="raised",
                                   command=lambda: verTrans(self))
        addTrans.grid(row=r-1, column=7,rowspan=2, padx=2, pady=0, sticky="w")

        noAddTrans = Button(self.newTransFrame, text="Cancel", width=5, height=1, bg=C.bBgCl, relief="raised",
                          command=lambda: no(self))
        noAddTrans.grid(row=r+1, column=7,rowspan=2, padx=2, pady=0, sticky="nw")

        self.newTransFrame.grid(row=r, column=7, columnspan=11,rowspan=9, padx=(10,1), sticky="n")

        d = Entry(self.newTransFrame, width=5)
        dd = Label(self.newTransFrame, text="day", width=4, height=1, bg=C.wBgCl)
        m = Entry(self.newTransFrame, width=5)
        mm = Label(self.newTransFrame, text="month", width=4, height=1, bg=C.wBgCl)
        y = Entry(self.newTransFrame, width=7)
        yyyy = Label(self.newTransFrame, text="year", width=4, height=1, bg=C.wBgCl)
        every = Label(self.newTransFrame, text="every", width=4, height=1, bg=C.wBgCl)
        number = Entry(self.newTransFrame, width=5)
        period = Entry(self.newTransFrame, width=8)

        def anotherCheck():
            nonlocal sad
            if sad == 0:
                sad = 1
                d.grid(row=r+5, column=8, padx=0, pady=0, sticky="w")
                dd.grid(row=r+6, column=8, padx=0, pady=0, sticky="w")
                m.grid(row=r+5, column=9, padx=0, pady=2, sticky="w")
                mm.grid(row=r+6, column=9, padx=0, pady=0, sticky="w")
                y.grid(row=r+5, column=10, padx=0, pady=2, sticky="w")
                yyyy.grid(row=r+6, column=10, padx=0, pady=0,sticky="n")
            else:
                sad = 0
                d.grid_forget()
                dd.grid_forget()
                m.grid_forget()
                mm.grid_forget()
                y.grid_forget()
                yyyy.grid_forget()

        def exchangeCheck():
            nonlocal ex
            nonlocal sex
            if sex == 0:
                sex = 1
                ex.grid(row=r+1, column=9,columnspan=1, padx=5, pady=5, sticky="w")
                lLinkEx.grid(row=r+1, column=10,columnspan=1, padx=0, pady=5, sticky="n")
                linKEx.grid(row=r+1, column=11,columnspan=1, padx=10, pady=5, sticky="w")
            else:
                sex = 0
                ex.grid_forget()
                lLinkEx.grid_forget()
                linKEx.grid_forget()

        def inCheck():
            nonlocal inout

            if inout == "out" or inout == None:
                inout = "in"
                Out.deselect()
            elif inout == "in" :
                inout = None

        def outCheck():
            nonlocal inout
            if inout == "in" or inout == None:
                inout = "out"
                In.deselect()
            elif inout == "out":
                inout = None


        def repeatCheck():
            nonlocal sre
            nonlocal every
            nonlocal number
            nonlocal period
            if sre == 0:
                every.grid(row=r+8, column=8, padx=0, pady=2, sticky="e")
                number.grid(row=r+8, column=9, padx=0, pady=2, sticky="n")
                period.grid(row=r+8, column=10, padx=0, pady=2, sticky="w")


                sre = 1
            else:
                sre = 0
                every.grid_forget()
                number.grid_forget()
                period.grid_forget()

        def no(self):
            self.newTransFrame.grid_forget()

        def verTrans(self):
            nonlocal cwb
            nonlocal sumE
            nonlocal ex
            nonlocal sex
            nonlocal d
            nonlocal m
            nonlocal y
            nonlocal linkE
            nonlocal linKEx
            nonlocal sre





            try:

                sumECon = sumE.get()
                sumECon_int = float(sumECon)
                #sumLCon_int = 0
                inw = None
                if sumECon_int < 0:
                    sumE.delete(0, len(sumECon))
                elif inout != None :
                    link = linkE.get()


                    if link != "":
                        if link == self.name:
                            raise Exception()

                        for www in cwb.listOfWallets:
                            if link == www.name:
                                linkWallet = w
                                inw = www
                        if inw == None:
                            raise Exception()
                    repeat_par = None
                    if sre == 1:
                        nonlocal number
                        nonlocal period
                        periodset = {"year", "years", "day", "days", "month", "months"}
                        number_n = number.get()

                        if float(number_n) <= 0 or float(number_n) % 1 != 0:# or (number_n - float(int(number_n))) > 0:
                            number.delete(0,len(number_n))
                            raise Exception()

                        period_w = period.get()
                        if not(period_w in periodset):
                            period.delete(0,len(number_n))
                            raise Exception()
                        repeat_par=number_n + period_w[0]

                    if sex == 1:
                        trece = False
                        lexT = linKEx.get()
                        if lexT != '' and inw != None:
                            lex_f = float(lexT)
                            if lex_f > 0:
                                sumLCon_int = sumECon_int * lex_f

                                sumLCon = str(sumLCon_int)
                                trece = True

                        exT = ex.get()
                        if exT != '':
                            ex_f = float(exT)
                            if ex_f > 0:
                                sumECon_int = sumECon_int * ex_f

                                sumECon = str(sumECon_int)
                                trece = True

                        if not trece:
                            raise Exception()
                    date_var = None
                    if sad == 1:
                        dt = d.get()
                        di = int(dt)
                        mt = m.get()
                        mi = int(mt)
                        yt = y.get()
                        yi = int(yt)
                        if not(di > 0 and mi > 0 and yi > 0) or (mi > 12) or (di > 28 and mi == 2 and yi % 4 != 0)\
                                or (di > 29 and mi == 2 and yi % 4 == 0) or (mi in [1, 3, 5, 7, 8, 10, 12] and di > 31) \
                                or (mi in [4, 6, 9, 11] and di > 30):

                            print("w")
                            raise Exception

                        else:
                            date_var = dt + "-" + mt + "-" + yt
                            '''
                            self.trans(inout=inout, sum=sumECon, date = dt + "-" + mt + "-" + yt)
                            if inw != None:
                                inoutlink = None
                                if inout == "out":
                                    inw.trans(inout="in", sum=sumLCon, date=dt + "-" + mt + "-" + yt)
                                else:
                                    inw.trans(inout="out", sum=sumLCon, date = dt + "-" + mt + "-" + yt)

                            In.deselect()
                            Out.deselect()
                            anotherday.deselect()
                            self.newTransFrame.destroy()'''

                    self.trans(inout=inout, sum=sumECon, date = date_var, repeat = repeat_par)
                    if inw != None:
                        inoutlink = None
                        if inout == "out":
                            inw.trans(inout="in", sum=sumLCon, date = date_var, repeat = repeat_par)
                        else:
                            inw.trans(inout="out", sum=sumLCon, date = date_var, repeat = repeat_par)

                    In.deselect()
                    Out.deselect()
                    anotherday.deselect()
                    self.newTransFrame.destroy()



            except:
                pass

    def trans(self, inout, sum, date=None, repeat=None):
        if date == None:
            from datetime import date
            date = (date.today()).strftime("%d-%m-%Y")
        with open(self.path, "a",newline='') as csvf:
            csvw = csv.writer(csvf)

            row = []
            row.append(inout)
            row.append(sum)
            row.append(date)
            row.append(repeat)
            csvw.writerow(row)
        self.setSumaActuala()
        self.lSum.config(text=self.sumaActuala)

    def setSumaActuala(self):
        self.sumaActuala=float(self.sumaInitiala)
        self.nrTrans = 0
        import csv
        with open(self.path, "r") as csvf:
            csvr = csv.reader(csvf)
            next(csvr)

            for row in csvr:
                self.nrTrans = self.nrTrans + 1
                from datetime import datetime, date
                today = date.today()
                day = (datetime.strptime(row[2],'%d-%m-%Y')).date()
                repeat = row[3]

                nor = 1
                if today >= day:
                    if len(repeat) >1:
                        per = repeat[-1]

                        num = 0
                        if per == "d":
                            delta = (today-day)
                            num = delta.days

                        elif per == "m":
                           num = today.month - day.month + 12 * (today.year - day.year)
                        else:
                            num = today.year - day.year
                        repeat = int(repeat[0:-1])
                        nor = num // repeat + 1



                    if row[0] == "in":
                        self.sumaActuala = self.sumaActuala + float(row[1]) * nor
                    else:
                        self.sumaActuala = self.sumaActuala - float(row[1]) * nor

    def showTrans(self, cwb):
        self.showTransRoot = Tk()
        self.showTransRoot.title("Transaction: " + self.name)
        self.showTransRoot.configure(background=C.wBgCl)
        iconPath = os.getcwd()
        self.showTransRoot.iconbitmap(iconPath + "\money_100dollar.ico")
        self.showTransRoot.resizable(False, False)
        self.showTransRoot.geometry("200x450")



        if self.nrTrans > 0:
            scrollbar = Scrollbar(self.showTransRoot)
            scrollbar.pack(side=RIGHT, fill=Y)
            transList = Listbox(self.showTransRoot, yscrollcommand=scrollbar.set, bg=C.wBgCl, height=30, width=30, bd=0)

            inout = []
            day = []
            sum = []
            rep = []
            import csv
            with open(self.path, "r") as csvf:
                csvr = csv.reader(csvf)
                next(csvr)

                transList.insert(END, "")
                transList.insert(END, ' ' + str(self.sumaActuala) + "  =  " + str(float(self.sumaActuala)-float(self.sumaInitiala)) +
                                                                                 "  +  " +self.sumaInitiala )
                transList.insert(END, "")

                transList.itemconfig(1,foreground='#05004a')
                for row in csvr:
                    if row[0] == "in":
                        inout.append("+")
                    else:
                        inout.append("-")

                    sum.append(float(row[1]))
                    day.append(row[2])
                    num = 0
                    repeat = row[3]
                    nor = 1
                    if len(repeat) > 1:
                        from datetime import datetime, date
                        today = date.today()
                        aday = (datetime.strptime(row[2], '%d-%m-%Y')).date()
                        per = repeat[-1]
                        num = 0
                        if per == "d":
                            delta = (today - aday)
                            num = delta.days

                        elif per == "m":
                            num = today.month - aday.month + 12 * (today.year - aday.year)
                        else:
                            num = today.year - aday.year
                        repeat = int(repeat[0:-1])
                        nor = num // repeat + 1

                        rep.append(" X " + str (nor))

                    else:
                        rep.append("")

                    transList.insert(END, " "*10 + inout[-1] + "  " + str(sum[-1]) + rep[-1] + " "*(15-(len(str(sum[-1])) + len(rep[-1])) ) + day[-1])

                    if row[0] == "in":
                        transList.itemconfig(END, foreground='#004a0a')
                    else:
                        transList.itemconfig(END, foreground='#960202')

                    transList.insert(END, "-" * 30)



            transList.pack()
            scrollbar.config(command=transList.yview)

    def __init__(self, budget, walldir=None, root=None, cr=None):
        self.budgetName = budget
        self.name=""
        self.sumaInitiala=0
        self.sumaActuala=0
        self.nrTrans = 0
        if walldir == None:
            self.listOfChoses = {}
            self.newWalletScreen(root, cr, "Currency",0)
            self.newWalletScreen(root, cr, "Form",1)
            self.newWalletScreen(root, cr, "State",2)
        else:
            self.path=walldir
            self.listOfChoses={}
            n = walldir.rfind("\\")
            inf = walldir[n + 1:]
            self.name = inf[:inf.find("_")]
            inf = inf[inf.find("_") + 1:]

            self.sumaInitiala = inf[:inf.find("_")]
            self.setSumaActuala()
            inf = inf[inf.find("_") + 1:]

            self.listOfChoses["Currency"] = inf[:inf.find("_")]
            inf = inf[inf.find("_") + 1:]

            self.listOfChoses["Form"] = inf[:inf.find("_")]
            inf = inf[inf.find("_") + 1:]

            self.listOfChoses["State"] = inf
