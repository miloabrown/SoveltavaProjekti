import sortingAlgo
import searchAlgo
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import time
#100k satunnaisia numeroita väliltä 1-100
satunnainenLista = np.random.randint(low = -100, high = 100, size = 100000)
#luvut 1-100k järjestyksessä
jarjestettyLista = np.arange(100000)



def lajittelut(lista):
    #fiksu ihminen säikeistäis nää lajittelut, ettei menis aikaa niimm birusti

    aloitus = time.time()
    #algoritmi 1
    lopetus1 =  time.time() - aloitus

    aloitus = time.time()
    #algoritmi2
    lopetus2 = time.time() - aloitus
    
    nimet = [sortingAlgo.algoritmi1(), sortingAlgo.algoritmi2()]
    
    arvot = [lopetus1, lopetus2]

    plt.figure(figsize = (8, 9))

    plt.subplot(131)
    plt.bar(nimet, arvot)
    plt.suptitle("Lajittelualgoritmien erot")
    plt.show()

    


def haut(lista):
     #fiksu ihminen säikeistäis nääkin
     #Koska haussa listat on järjestetty, täytyy hakea listan _viimeinen_ alkio, kompleksisuuksien erojen korostamiseksi. 

    aloitus1 = time.time()
    #algoritmi 1
    lopetus1 = aloitus1 - time.time()

    aloitus2 = time.time()
    #algoritmi2
    lopetus2 = aloitus2 - time.time()

    nimet = [searchAlgo.algoritmi1(), searchAlgo.algoritmi2()]
    
    arvot = [lopetus1, lopetus2]

    plt.figure(figsize = (8, 9))

    plt.subplot(131)
    plt.bar(nimet, arvot)
    plt.suptitle("Hakualgoritmien erot")
    plt.show()
    

def kayttoliittyma():
    #Setit
    root = Tk()
    root.title("Soveltava Proju fre$$hh")
    root.geometry('550x150')
    frame1 = Frame(root, relief = RAISED, borderwidth = 1)
    frame1.pack(fill = BOTH, expand = True)
    frame2 = Frame(root)
    frame2.pack(side = TOP)

    #Widgetit
    searchButton = Button(frame2, text = "Hakualgoritmi", padx = 25, pady = 15, command = lambda: haut(jarjestettyLista)).pack(side = LEFT)
    sortingButton = Button(frame2, text = "Lajittelualgoritmi", padx = 15, pady = 15, command = lambda: lajittelut(satunnainenLista)).pack(side = RIGHT)
    teksti = Label(frame1, text = "Napit demonstroivat nimensämukaisten algoritmien aikakompleksien eroja")
    teksti.pack()

    #Ikkuna näytölle
    root.mainloop()

def main():
    kayttoliittyma()
    

if __name__ == "__main__":
    main()