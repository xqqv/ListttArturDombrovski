nimed=["Mati","Kati"]
while True:
    valik=input("Andmete lisamine-add\nAndmete nätamine-show\nAndmete kustutamine-del\n")
    if valik=="add":
        valik=input("Kas lisame mitu inimest(mitu) või positsioonile(pos)")   
        if valik=="mitu":
            mitu=int(input("Mitu inimest lisame?"))
            for i in range(mitu):
                nimi=input("Sisesta nimi:")
                nimed.append(nimi)
        else:
            indeks=int(input("kuhu lisamine?"))
            nimi==input("Mis nimi:")
            nimed.insert(indeks -1,nimi)
    elif valik=="del":
        valik=input("Kas kustutame nimi(nimi) või indeksi järgi(ind)?")
        if valik=="nimi":
            nimi=input("Mis nimi in vaja kustuta?")
            kogus=nimed.count(nimi)
            if kogus>0:
                for i in range(kogus):
                    nimed.remove(nimi)
            else:
                print(f"Nimi {nimi} ei ole nimekirjas")
        else:
            indeks=int(input("Mis on järjekorranumber?"))
            nimed.pop(indeks-1)
    elif valik=="show":    
            print(nimed)
    elif valik=="rev":
        print(nimed.reverse())
    elif valik=="sort":
        print(nimed.sort())
    elif valik=="clear":
        print(nimed.clear())
    elif valik=="ots":
        int=i 
        nimi=input("Mis nimi otsime?")
        if nimed.count(nimi)>0:
            for nim in nimed:
                if nim=nimi:

    

#1
def draw_towers(n):
    i = 1
    while i <= n:
        spaces = " " * (n - i)
        print(spaces + "Ä" + spaces)
        print(spaces + "/ \\" + spaces)
        print(spaces + "| |" + spaces)
        i += 1


number_of_towers = int(input("Sisestage tornide arv (1 kuni 9): "))
draw_towers(number_of_towers)           #переходим к следующей башне


#2
