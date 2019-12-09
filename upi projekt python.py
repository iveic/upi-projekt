def Ispis():
    with open("test.txt", "r") as t:
        print(t.read())

def Izbornik():
    print("Izbornik\n(1)Kreiraj\n(2)Ažuriraj\n(3)Briši\n(4)Pregled\n(0)Izlaz")
    while True:
        try:
            zastava = 0
            izbor = int(input("Unos: "))
            if(izbor < 0 or izbor > 4):
                print("Pogrešan unos!!!")
                zastava = 1
        except ValueError:
            print("pogrešan unos!!!")
            zastava = 1
        if zastava == 0: break

    if izbor == 0:
        exit()

    if izbor == 1:
        Izbornik()
        
    if izbor == 2:
        Izbornik()

    if izbor == 3:
        Ispis()
        el_brisanja = input("Unesi ID elementa koji želite izbrisati:")
        '''
        with open("test.txt", "r") as citanje:
            with open("test.txt", "w") as pisanje:
                for line in citanje:
                    l = line.split(";")
                    if l[0] != el_brisanja:
                        pisanje.write(line + "\n")
        

        with open("test.txt", "r") as f:
            lines = f.readlines()
        with open("test.txt", "w") as f:
            for line in lines:
                l = line.strip(";")
                if l.strip("\n") != el_brisanja:
                    f.write(line)
        '''
        with open("test.txt", "r") as r:
            with open("test.txt", "w") as w:
                for l in r:
                    x = l.strip("\n")
                    x = x.split(";")
                    if x[0] != el_brisanja:
                        w.write(l)
        
        Ispis()
        Izbornik()

    if izbor == 4:
        Ispis()
        Izbornik()

Izbornik()
