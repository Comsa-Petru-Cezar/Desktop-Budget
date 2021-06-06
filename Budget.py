import os
from tkinter import *
import Wallet as W



class Budget:
    name = ""
    listOfWallets = []
    dirAddres = None

    def createDir(self):
        path = os.path.join(os.path.expanduser('~'),'Documents',"Decktop_Budget") + "\\Bugete\\" + self.name
        try:
            os.makedirs(path)
        except:
            pass


    def adListOfWallets(self):
        self.listOfWallets = []
        for w in os.listdir(self.dirAddres):
            self.listOfWallets.append(W.Wallet(self.name, walldir=self.dirAddres + "\\" + w))


    def __init__(self, name, take = False):
        self.name = name
        self.dirAddres = os.path.join(os.path.expanduser('~'),'Documents',"Decktop_Budget") + "\\Bugete\\" + self.name

        if take:
            self.adListOfWallets()

        else:
            self.createDir()