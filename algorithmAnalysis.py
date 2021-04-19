
#Kirjastot sekä moduulit
import sortingAlgo
import searchAlgo
import nopee
import hidas
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import time

#100k satunnaisia numeroita väliltä -100 - 100
satunnainenLista = np.random.randint(low = -100, high = 100, size = 100000)
#luvut 1-10m
jarjestettyLista = np.arange(10000000)


#Funktio, jossa suoritetaan kaksi lajittelualgoritmia
#-Bubblesort
#-Quicksort
#Sekä visualisoidaan niiden suoritukseen mennyt aika Matplotlibllä
def lajittelut():
    lista1 = satunnainenLista
    lista2 = satunnainenLista

    aloitus = time.time()
    sortingAlgo.algoritmi1(lista1)
    lopetus1 = (time.time() - aloitus) 

    aloitus = time.time()
    sortingAlgo.algoritmi2(lista2)
    lopetus2 =  (time.time() - aloitus)


    nimet = ["Bubblesort", "Quicksort"]
    arvot = [lopetus1, lopetus2]

    plt.figure(figsize = (9, 10))

    plt.subplot(131)
    plt.bar(nimet, arvot)
    plt.ylabel("Aika sekunteina")
    plt.suptitle("Lajittelualgoritmien erot")
    plt.show()

#Funktio, jossa suoritetaan kaksi hakualgoritmia
#-Binäärihaku
#-Lineaarihaku
#Sekä visualisoidaan niiden suorituksen käyttämä aika Matplotlibillä
def haut():
    #Koska haussa listat on järjestetty, täytyy hakea listan _viimeinen_ alkio, kompleksisuuksien erojen korostamiseksi. 
    
    aloitus = time.time()
    searchAlgo.algoritmi1(jarjestettyLista, 9999999)
    ero1 = (time.time() - aloitus)

    

    aloitus = time.time()
    searchAlgo.algoritmi2(jarjestettyLista, 9999999)
    ero2 = (time.time() - aloitus) * 10000 # kerrotaan kymmenellätuhannella, sillä ero2 oli jatkuvasti n. 3.719329833984375e-05, joten se oli kerrottava e-x-1:n määrällä nollia, että luku olisi ns. totuudenmukainen. 

    nimet = ["Linear Search", "Binary Search"]
    print(ero1, ero2)
    arvot = [ero1, ero2]

    plt.figure(figsize = (9, 10))

    plt.subplot(131)
    plt.bar(nimet, arvot)
    plt.ylabel("Aika sekunteina")
    plt.suptitle("Hakualgoritmien erot")
    plt.show()
    
#Funktio, joka käynnistää graafisen Tkinter-käyttöliittymän
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
    searchButton = Button(frame2, text = "Hakualgoritmi", padx = 25, pady = 15, command = lambda: haut()).pack(side = LEFT)
    sortingButton = Button(frame2, text = "Lajittelualgoritmi", padx = 15, pady = 15, command = lambda: lajittelut()).pack(side = RIGHT)
    teksti = Label(frame1, text = "Napit demonstroivat nimensämukaisten algoritmien aikakompleksien eroja")
    teksti.pack()

    #Ikkuna näytölle
    root.mainloop()

#getterit testiluokalle
def getUnsorted():
    return satunnainenLista
def getSorted():
    return jarjestettyLista
def main():
    kayttoliittyma()
    

if __name__ == "__main__":
    main()