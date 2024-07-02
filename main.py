import time

V=[]
R=[]
C=[]
broj_poteza=0
konverzija=False
recnik={}
popunjena_polja = []
while True:

    print("Izaberite jednu od sledecih opcija:")
    print("1:Stvaranje praznog talona za igru")
    print("2:Ispis talona uz ispis trenutnog broja bodova")
    print("3:Odigravanje jednog poteza slucajnim generisanjem vrednosti kockica")
    print("4:Odabir opcije \"pomoc prijatelja\" za odigravanje sledeceg poteza")
    print("5:Zavrsi igranje igre")
    a=int(input())
    if (a==1):
        V = []
        C = []
        R = []
        broj_poteza=0
    if (a==2):
        popunjena_polja.sort(key=lambda x: (x[1], x[0]))
        V=[]
        R = []
        C=[]
        for item in range(int(popunjena_polja[len(popunjena_polja) - 1][0]) + 1):
            C.append(0)

        for i in range(len(popunjena_polja)):
            C[popunjena_polja[i][1]] += 1
        for i in range(len(C) - 1):
            if (C[i + 1]): C[i + 1] += C[i]
            else: C[i + 1] = C[i]
        C.insert(0, 0)
        for i in range(len(C) - 1):
            for j in range(C[i], C[i + 1], 1):
                R.append(popunjena_polja[j][0])
        #for i in range(len(V)):
        #    if (V[i]==0): V[i]="X"

        for item in popunjena_polja:
            if(recnik[str(item)]):V.append(recnik[str(item)])
            else: V.append('X')

        #velicinastandardmatrice=popunjena_polja[len(popunjena_polja)-1][0]*popunjena_polja[len(popunjena_polja)-1][1]
        #OVO JE REALNA VREDNOST STANDARDNE MATRICE KOJA JE NEOPHODNA ZA ISPISIVANJE RELEVANTNIH PODATAKA O TALONU

        velicinastandardmatrice=33 #OVO JE FIKSNA VREDNOST AKO MORAJU DA SE ISPISUJU POLJA KOJA NISU POPUNJENA

        if ((len(V)+len(C)+len(R))>velicinastandardmatrice):
            konverzija=True
            matrica=[]
            br = 0
            for i in range(max(popunjena_polja)[0] + 1):
                tmp = []
                tmp2 = []
                for j in range(max(map(lambda x: x[1], popunjena_polja)) + 1):
                    tmp = []
                    tmp.append(i)
                    tmp.append(j)
                    if (tmp in popunjena_polja):
                        tmp2.append(V[br])
                        br += 1
                    else:
                        tmp2.append('')
                for i in range(3-len(tmp2)):
                    tmp2.append('')
                # ZA ISPISIVANJE PRAZNIH MESTA U STANDARD MATRICI
                matrica.append(tmp2)

        if (konverzija):
            suma1=[0,0,0]
            for item in matrica:
                print(item[:])
            print("UKUPNA SUMA SVIH:")
            sumasvih = 0

            for item in matrica:
                for i in range(len(item)):
                    if (str(item[i]).isnumeric()): suma1[i]+=item[i]

            print("Suma kolone \"Na dole\" je {}".format(suma1[0]))
            print("Suma kolone \"Na gore\" je {}".format(suma1[1]))
            print("Suma kolone \"Rucna\" je {}".format(suma1[2]))
            for item in V:
                if (str(item).isnumeric()):sumasvih += item
            print(sumasvih)

        else:
            print("VREDNOSTI:")
            print(V[:])
            print("KOLONE")
            print(C[:])
            print("REDOVI")
            print(R[:])
            print("UKUPNA SUMA: ")
            sumasvih=0
            for item in V:
                if (str(item).isnumeric()):sumasvih+=item
            print(sumasvih)
    if (a==3):
        broj_poteza=0
        trenutne_kockice=[]
        ostale_kockice=[]
        Niz=[]
        Niz.append(float(time.time()))#prvi seed

        p=71
        q=79
        M=p*q
        konacanbroj=""
        for j in range(5):
            konacanbroj = ""
            time.sleep(0.1)
            for i in range(1,10,1):
                Niz.append((Niz[i-1]**2)%M)
                if (int(format(int(Niz[i]),'b').count("1"))%2==0):
                    konacanbroj+="0"
                    #paran broj jedinica
                else:konacanbroj+="1"
            trenutne_kockice.append((int(konacanbroj)%6)+1)
            Niz.clear()
            Niz.append(float(time.time()))
        print(trenutne_kockice[:])
        print("Koje kockice zelite da ostavite? (indeksi 1->5)")
        print("npr(1,3,5)")
        print("Ukoliko ne zelite ostaviti ni jednu kockicu, pritisnite samo \"Enter\"")
        broj_poteza+=1
        c=input().split(',')
        if (c[0]==''): c.clear()
        while(broj_poteza!=3):
            if(len(c)):
                for i in range(len(c)):
                    ostale_kockice.append(trenutne_kockice[int(c[i])-1])
            trenutne_kockice=[]
            print(ostale_kockice[:])
            Niz.clear()
            Niz.append(float(time.time()))

            for j in range(5-len(ostale_kockice)):
                konacanbroj = ""
                time.sleep(0.1)
                for i in range(1,10,1):
                    Niz.append((Niz[i-1]**2)%M)
                    if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                        konacanbroj += "0"
                        # paran broj jedinica
                    else:
                        konacanbroj += "1"

                trenutne_kockice.append((int(konacanbroj) % 6) + 1)
                Niz.clear()
                Niz.append(float(time.time()))
            print(trenutne_kockice[:])
            if (len(trenutne_kockice)==0): break
            print("Koje kockice zelite da ostavite? (indeksi 1->{})".format(len(trenutne_kockice)))
            print("Ukoliko ne zelite ostaviti ni jednu kockicu, pritisnite samo \"Enter\"")
            c=input().split(',')
            if (c[0]==''):c.clear()
            broj_poteza+=1
        if (len(trenutne_kockice)!=0):
            for i in range(len(c)):
                ostale_kockice.append(trenutne_kockice[int(c[i]) - 1])
        upis=False
        while(upis==False):
            print("Vase kockice za ovaj potez su:")
            print(ostale_kockice[:])
            print("Koje polje zelite popuniti sa Vasim kockicama?")
            print("1: 1\tKenta: Kenta")
            print("2: 2\tFul: Ful")
            print("3: 3\tPoker: Poker")
            print("4: 4\tJamb: Jamb")
            print("5: 5\tBack: 0")
            print("6: 6")
            prvi=input()
            if (prvi=="0"): break
            print("Izaberite jednu od sledecih opcija:")
            print("Na dole: 1")
            print("Na gore: 2")
            print("Rucna: 3")
            drugi=input()


            while(drugi=="3" and broj_poteza!=1):
                print("Ne mozete upisati u kolonu rucna, zato sto vam nije prvi potez")
                print("Izaberite jednu od sledecih opcija:")
                print("Na dole: 1")
                print("Na gore: 2")
                drugi=input()

            if (prvi == "1"):
                if (drugi=="1"):
                    tmp=[0,0]
                    if not(tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        suma=(ostale_kockice.count(1))
                        recnik["[0, 0]"]=suma
                        #V.append(suma)
                        upis = True
                    else: print("Postoji vrednost koja je vec upisana na to polje!")
                elif (drugi=="2"):
                    tmp=[0,1]
                    tmp_prethodno=[1,1]
                    if not(tmp in popunjena_polja):
                        if (tmp_prethodno in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma=ostale_kockice.count(1)
                            recnik["[0, 1]"] = suma
                            #V.append(suma)
                            upis = True
                        else: print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="3"):
                    tmp=[0,2]
                    if not(tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        suma=ostale_kockice.count(1)
                        recnik["[0, 2]"] = suma
                        #V.append(suma)
                        upis = True
                    else: print("Postoji vrednost koja je vec upisana na to polje!")
            elif (prvi == "2"):
                    if (drugi=="1"):
                        tmp_prethodno=[0,0]
                        tmp=[1,0]
                        if (tmp_prethodno in popunjena_polja):
                            if not(tmp in popunjena_polja):
                                popunjena_polja.append(tmp)
                                suma=ostale_kockice.count(2)*2
                                #V.append(suma)
                                recnik["[1, 0]"] = suma

                                upis=True


                            else:print("Postoji vrednost koja je vec upisana na to polje!")
                        else: print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                    elif (drugi=="2"):
                        tmp_prethodno = [2, 1]
                        tmp = [1, 1]
                        if (tmp_prethodno in popunjena_polja):
                            if not (tmp in popunjena_polja):
                                popunjena_polja.append(tmp)
                                suma = ostale_kockice.count(2) * 2
                                recnik["[1, 1]"] = suma
                                #V.append(suma)

                                upis = True


                            else:
                                print("Postoji vrednost koja je vec upisana na to polje!")
                        else:
                            print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                    elif (drugi=="3"):
                        tmp=[1,2]
                        if not(tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma = ostale_kockice.count(2) * 2
                            recnik["[1, 2]"] = suma
                            #V.append(suma)
                            upis = True
                        else: print("Postoji vrednost koja je vec upisana na to polje!")
            elif(prvi=="3"):
                if (drugi=="1"):
                    tmp=[2,0]
                    tmp_prethodno=[1,0]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma=ostale_kockice.count(3)*3
                            #V.append(suma)
                            recnik["[2, 0]"] = suma

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="2"):
                    tmp=[2,1]
                    tmp_prethodno=[3,1]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma = ostale_kockice.count(3) * 3
                            recnik["[2, 1]"] = suma
                            #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif(drugi=="3"):
                    tmp=[2,2]
                    if not (tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        suma = ostale_kockice.count(3) * 3
                        recnik["[2, 2]"] = suma
                        #V.append(suma)
                        upis = True
                    else:
                        print("Postoji vrednost koja je vec upisana na to polje!")
            elif(prvi=="4"):
                if (drugi=="1"):
                    tmp=[3,0]
                    tmp_prethodno=[2,0]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma=ostale_kockice.count(4)*4
                            #V.append(suma)
                            recnik["[3, 0]"] = suma

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="2"):
                    tmp=[3,1]
                    tmp_prethodno=[4,1]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma = ostale_kockice.count(4) * 4
                            recnik["[3, 1]"] = suma
                            #V.append(suma)
                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif(drugi=="3"):
                    tmp=[3,2]
                    if not (tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        suma = ostale_kockice.count(4) * 4
                        recnik["[3, 2]"] = suma
                        #V.append(suma)
                        upis = True
                    else:
                        print("Postoji vrednost koja je vec upisana na to polje!")
            elif(prvi=="5"):
                if (drugi=="1"):
                    tmp=[4,0]
                    tmp_prethodno=[3,0]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma=ostale_kockice.count(5)*5
                            #V.append(suma)
                            recnik["[4, 0]"] = suma

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="2"):
                    tmp=[4,1]
                    tmp_prethodno=[5,1]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma = ostale_kockice.count(5) * 5
                            recnik["[4, 1]"] = suma
                            #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif(drugi=="3"):
                    tmp=[4,2]
                    if not (tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        suma = ostale_kockice.count(5) * 5
                        recnik["[4, 2]"] = suma
                        #V.append(suma)
                        upis = True
                    else:
                        print("Postoji vrednost koja je vec upisana na to polje!")
            elif (prvi=="6"):
                if (drugi=="1"):
                    tmp=[5,0]
                    tmp_prethodno=[4,0]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma = ostale_kockice.count(6) * 6
                            recnik["[5, 0]"] = suma
                            #V.append(suma)
                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="2"):
                    tmp=[5,1]
                    tmp_prethodno=[6,1]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            suma = ostale_kockice.count(6) * 6
                            recnik["[5, 1]"] = suma
                            #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="3"):
                    tmp=[5,2]
                    if not (tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        suma = ostale_kockice.count(6) * 6
                        recnik["[5, 2]"] = suma
                        #V.append(suma)
                        upis = True
                    else:
                        print("Postoji vrednost koja je vec upisana na to polje!")
            elif (prvi=="Kenta"):
                if (drugi=="1"):
                    tmp=[6,0]
                    tmp_prethodno=[5,0]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            if ((ostale_kockice.count(1) == 1 and ostale_kockice.count(2) == 1 and ostale_kockice.count(3) == 1 and ostale_kockice.count(4) == 1 and ostale_kockice.count(5) == 1) or (ostale_kockice.count(2) == 1 and ostale_kockice.count(3) == 1 and ostale_kockice.count(4) == 1 and ostale_kockice.count(5) == 1 and ostale_kockice.count(6) == 1)):
                                if (broj_poteza == 1):suma = 66
                                elif (broj_poteza == 2):suma = 56
                                elif (broj_poteza == 3):suma = 46
                                recnik["[6, 0]"] = suma
                                #V.append(suma)
                            else:
                                print("Nemate povoljnu kombinaciju kockica za Kentu! Polje je precrtano.")
                                suma = 0
                                recnik["[6, 0]"] = suma
                                #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="2"):
                    tmp=[6,1]
                    tmp_prethodno=[7,1]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            if ((ostale_kockice.count(1) == 1 and ostale_kockice.count(2) == 1 and ostale_kockice.count(3) == 1 and ostale_kockice.count(4) == 1 and ostale_kockice.count(5) == 1) or (ostale_kockice.count(2) == 1 and ostale_kockice.count(3) == 1 and ostale_kockice.count(4) == 1 and ostale_kockice.count(5) == 1 and ostale_kockice.count(6) == 1)):
                                if (broj_poteza == 1):suma = 66
                                elif (broj_poteza == 2):suma = 56
                                elif (broj_poteza == 3):suma = 46
                                recnik["[6, 1]"] = suma
                                #V.append(suma)
                            else:
                                print("Nemate povoljnu kombinaciju kockica za Kentu! Polje je precrtano.")
                                suma=0
                                recnik["[6, 1]"] = suma
                                #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="3"):
                    tmp=[6,2]
                    if not (tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        if ((ostale_kockice.count(1)==1 and ostale_kockice.count(2)==1 and ostale_kockice.count(3)==1 and ostale_kockice.count(4)==1 and ostale_kockice.count(5)==1) or (ostale_kockice.count(2)==1 and ostale_kockice.count(3)==1 and ostale_kockice.count(4)==1 and ostale_kockice.count(5)==1 and ostale_kockice.count(6)==1)):
                            if (broj_poteza == 1):    suma = 66
                            elif (broj_poteza == 2):  suma = 56
                            elif (broj_poteza == 3):  suma = 46
                            recnik["[6, 2]"] = suma
                            #V.append(suma)
                        else:
                            print("Nemate povoljnu kombinaciju kockica za Kentu! Polje je precrtano.")
                            suma=0
                            recnik["[6, 2]"] = suma
                            #V.append(suma)

                        upis = True
                    else:
                        print("Postoji vrednost koja je vec upisana na to polje!")
            elif(prvi=="Ful"):
                if (drugi=="1"):
                    suma=0
                    nije=False
                    tmp=[7,0]
                    tmp_prethodno=[6,0]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            for i in range(1,7,1):
                                if (ostale_kockice.count(i)==1 or ostale_kockice.count(i)>3):
                                    suma=0
                                    nije=True
                                    break
                            if (nije):
                                print("Nemate povoljnu kombinaciju kockica za Ful! Polje je precrtano.")
                                recnik["[7, 0]"] = suma
                                #V.append(suma)
                            else:
                                for i in range(1,7,1):
                                    if (ostale_kockice.count(i)!=0):
                                        suma+=ostale_kockice.count(i)*i
                                suma+=30
                                recnik["[7, 0]"] = suma
                                #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="2"):
                    suma=0
                    nije=False
                    tmp=[7,1]
                    tmp_prethodno=[8,1]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            for i in range(1,7,1):
                                if (ostale_kockice.count(i)==1 or ostale_kockice.count(i)>3):
                                    suma=0
                                    nije=True
                                    break
                            if (nije):
                                print("Nemate povoljnu kombinaciju kockica za Ful! Polje je precrtano.")
                                recnik["[7, 1]"] = suma
                                #V.append(suma)
                            else:
                                for i in range(1,7,1):
                                    if (ostale_kockice.count(i)!=0):
                                        suma+=ostale_kockice.count(i)*i
                                suma+=30
                                recnik["[7, 1]"] = suma
                                #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="3"):
                    suma=0
                    nije=False
                    tmp=[7,2]
                    if not (tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        for i in range(1, 7, 1):
                            if (ostale_kockice.count(i) == 1 or ostale_kockice.count(i) > 3):
                                suma = 0
                                nije = True
                                break
                        if (nije):
                            print("Nemate povoljnu kombinaciju kockica za Ful! Polje je precrtano.")
                            recnik["[7, 2]"] = suma
                            #V.append(suma)
                        else:
                            for i in range(1, 7, 1):
                                if (ostale_kockice.count(i) != 0):
                                    suma += ostale_kockice.count(i) * i
                            suma+=30
                            recnik["[7, 2]"] = suma
                            #V.append(suma)
                        upis = True
                    else:
                        print("Postoji vrednost koja je vec upisana na to polje!")
            elif (prvi=="Poker"):
                suma=0
                nije=False
                if (drugi=="1"):
                    tmp=[8,0]
                    tmp_prethodno=[7,0]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            for i in range(1,7,1):
                                if (ostale_kockice.count(i)==2 or ostale_kockice.count(i)==3 or ostale_kockice.count(i)==5):
                                    nije=True
                                    suma=0
                                    break
                            if (nije):
                                print("Nemate povoljnu kombinaciju kockica za Poker! Polje je precrtano.")
                                recnik["[8, 0]"] = suma
                                #V.append(suma)
                            else:
                                for i in range(1,7,1):
                                    suma+=ostale_kockice.count(i)*i
                                suma+=40
                                recnik["[8, 0]"] = suma
                                #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="2"):
                    suma=0
                    tmp=[8,1]
                    tmp_prethodno=[9,1]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            for i in range(1,7,1):
                                if (ostale_kockice.count(i)==2 or ostale_kockice.count(i)==3 or ostale_kockice.count(i)==5):
                                    nije=True
                                    suma=0
                                    break
                            if (nije):
                                print("Nemate povoljnu kombinaciju kockica za Poker! Polje je precrtano.")
                                recnik["[8, 1]"] = suma
                                #V.append(suma)
                            else:
                                for i in range(1,7,1):
                                    suma+=ostale_kockice.count(i)*i
                                suma+=40
                                recnik["[8, 1]"] = suma
                                #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="3"):
                    suma=0
                    tmp=[8,2]
                    if not (tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        for i in range(1, 7, 1):
                            if (ostale_kockice.count(i) == 2 or ostale_kockice.count(i) == 3 or ostale_kockice.count(
                                    i) == 5):
                                nije = True
                                suma = 0
                                break
                        if (nije):
                            print("Nemate povoljnu kombinaciju kockica za Poker! Polje je precrtano.")
                            recnik["[8, 2]"] = suma
                            #V.append(suma)
                        else:
                            for i in range(1, 7, 1):
                                suma += ostale_kockice.count(i) * i
                            suma += 40
                            recnik["[8, 2]"] = suma
                            #V.append(suma)
                        upis = True
                    else:
                        print("Postoji vrednost koja je vec upisana na to polje!")
            elif(prvi=="Jamb"):
                nije=False
                suma=0
                if (drugi=="1"):
                    tmp=[9,0]
                    tmp_prethodno=[8,0]
                    if (tmp_prethodno in popunjena_polja):
                        if not (tmp in popunjena_polja):
                            popunjena_polja.append(tmp)
                            for i in range(1,7,1):
                                if (ostale_kockice.count(i)>0 and ostale_kockice.count(i)<5):
                                    nije=True
                                    suma=0
                                    break
                            if (nije):
                                print("Nemate povoljnu kombinaciju kockica za Jamb! Polje je precrtano.")
                                recnik["[9, 0]"] = suma
                                #V.append(suma)
                            else:
                                for i in range(1,7,1):
                                    suma+=ostale_kockice.count(i)*i
                                suma+=50
                                recnik["[9, 0]"] = suma
                                #V.append(suma)

                            upis = True


                        else:
                            print("Postoji vrednost koja je vec upisana na to polje!")
                    else:
                        print("Ne mozete u ovo polje upisati jer prethodno polje nije popunjeno")
                elif (drugi=="2"):
                    tmp=[9,1]
                    if not (tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        for i in range(1, 7, 1):
                            if (ostale_kockice.count(i) > 0 and ostale_kockice.count(i) < 5):
                                nije = True
                                suma = 0
                                break
                        if (nije):
                            print("Nemate povoljnu kombinaciju kockica za Jamb! Polje je precrtano.")
                            recnik["[9, 1]"] = suma
                            #V.append(suma)
                        else:
                            for i in range(1, 7, 1):
                                suma += ostale_kockice.count(i) * i
                            suma += 50
                            recnik["[9, 1]"] = suma
                           # V.append(suma)

                        upis = True
                    else:
                        print("Postoji vrednost koja je vec upisana na to polje!")
                elif (drugi=="3"):
                    tmp=[9,2]
                    if not (tmp in popunjena_polja):
                        popunjena_polja.append(tmp)
                        for i in range(1, 7, 1):
                            if (ostale_kockice.count(i) > 0 and ostale_kockice.count(i) < 5):
                                nije = True
                                suma = 0
                                break
                        if (nije):
                            print("Nemate povoljnu kombinaciju kockica za Jamb! Polje je precrtano.")
                            recnik["[9, 2]"] = suma
                            #V.append(suma)
                        else:
                            for i in range(1, 7, 1):
                                suma += ostale_kockice.count(i) * i
                            suma += 50
                            recnik["[9, 2]"] = suma
                            #V.append(suma)
                        upis = True
                    else:
                        print("Postoji vrednost koja je vec upisana na to polje!")


    if (a == 4):
        vrednost_praga=0.35

        broj_poteza = 1
        trenutne_kockice = []
        ostale_kockice = []
        Niz = []
        suma=0
        Niz.append(float(time.time()))  # prvi seed
        p = 71
        q = 79
        M = p * q
        konacanbroj = ""
        for j in range(5):
            konacanbroj = ""
            time.sleep(0.01)
            for i in range(1, 10, 1):
                Niz.append((Niz[i - 1] ** 2) % M)
                if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                    konacanbroj += "0"
                    # paran broj jedinica
                else:
                    konacanbroj += "1"
            trenutne_kockice.append((int(konacanbroj) % 6) + 1)
            Niz.clear()
            Niz.append(float(time.time()))
        print(trenutne_kockice[:])
        for i in range(10):
            if ([i,2] not in popunjena_polja and trenutne_kockice.count(i+1)>0 and i<6):
                suma+=trenutne_kockice.count(i+1)*(i+1)
                popunjena_polja.append([i,2])
                broj_poteza+=1
                recnik["[{}, 2]".format(i)] = suma
                popunjena_polja.append([i, 2])

                break
            elif (i==6 and ([i,2] not in popunjena_polja)):
                if ((trenutne_kockice.count(1) == 1 and trenutne_kockice.count(2) == 1 and trenutne_kockice.count(
                        3) == 1 and trenutne_kockice.count(4) == 1 and trenutne_kockice.count(5) == 1) or (
                        trenutne_kockice.count(2) == 1 and trenutne_kockice.count(3) == 1 and trenutne_kockice.count(
                        4) == 1 and trenutne_kockice.count(5) == 1 and trenutne_kockice.count(6) == 1)):
                    if (broj_poteza == 1):
                        suma = 66
                    elif (broj_poteza == 2):
                        suma = 56
                    elif (broj_poteza == 3):
                        suma = 46
                    recnik["[6, 2]"] = suma
                    broj_poteza += 1
                    popunjena_polja.append([6, 2])
                    break
                    # V.append(suma)
            elif (i==7 and ([i,2] not in popunjena_polja)):
                for i in range(1, 7, 1):
                    if (trenutne_kockice(i) == 1 or trenutne_kockice(i) > 3):
                        suma = 0
                        nije = True
                        break
                if not(nije):
                    for i in range(1, 7, 1):
                        if (trenutne_kockice.count(i) != 0):
                            suma += trenutne_kockice.count(i) * i
                    suma += 30
                    popunjena_polja.append([7, 2])
                    recnik["[7, 2]"] = suma
                    broj_poteza += 1
                    break
            elif (i==8 and ([i,2] not in popunjena_polja)):
                for i in range(1, 7, 1):
                    if (trenutne_kockice.count(i) == 2 or trenutne_kockice.count(i) == 3 or trenutne_kockice.count(i) == 5):
                        nije = True
                        suma = 0
                        break
                if not (nije):
                    for i in range(1, 7, 1):
                        suma += trenutne_kockice.count(i) * i
                    suma += 40
                    recnik["[8, 2]"] = suma
                    broj_poteza += 1
                    popunjena_polja.append([8, 2])
                    # V.append(suma)
            elif (i==9 and ([i,2] not in popunjena_polja)):
                for i in range(1, 7, 1):
                    if (trenutne_kockice.count(i) > 0 and trenutne_kockice.count(i) < 5):
                        nije = True
                        suma = 0

                        break
                if not (nije):
                    for i in range(1, 7, 1):
                        suma += trenutne_kockice.count(i) * i
                    suma += 50
                    recnik["[9, 2]"] = suma
                    popunjena_polja.append([9,2])
                    broj_poteza+=1
                    break
        #Racunanje Verovatnoce
        max=-1
        najvisekockica=-1
        for item in trenutne_kockice:
            if (trenutne_kockice.count(item)>max):
                najvisekockica=item
                max=trenutne_kockice.count(item)

        #za Kentu
        kockice=[]
        kockicekojetrazimo=[]
        for item in sorted(trenutne_kockice):
            if (item not in kockice):
                kockice.append(item)
        brojac=0
        for i in range(len(kockice)-1):
            if (kockice[i]+1!=kockice[i+1]):
                brojac+=1

        for i in range(len(kockice)-1):
            if (kockice[i] + 1 != kockice[i + 1]):
                kockicekojetrazimo.append(kockice[i]+1)
        privremene=[]
        brojuspelih=0
        for k in range(100):
            privremene=[]
            for j in range(brojac):
                konacanbroj = ""
                time.sleep(0.01)
                for i in range(1, 10, 1):
                    Niz.append((Niz[i - 1] ** 2) % M)
                    if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                        konacanbroj += "0"
                        # paran broj jedinica
                    else:
                        konacanbroj += "1"
                privremene.append((int(konacanbroj) % 6) + 1)
                Niz.clear()
                Niz.append(float(time.time()))
            if (sorted(privremene)==sorted(kockicekojetrazimo)):
                brojuspelih+=1
        verovatnocazakentu=brojuspelih/100
        #Verovatnoca za ful
        brojac=0
        kockice=[]
        trenutne_kockice.sort()
        recnik2={}
        for item in trenutne_kockice:
            recnik2[item]=0

        for i in range(len(trenutne_kockice)-1):
            for j in range(i+1,len(trenutne_kockice),1):
                if (trenutne_kockice[i]==trenutne_kockice[j]):
                    recnik2[trenutne_kockice[i]]+=1
        for i in recnik2.keys():
            if (recnik2[i]==2 or recnik2[i]==3):
                for j in range(recnik2[i]):
                    kockice.append(i)
        brojuspelih=0
        for k in range(100):
            privremene=[]
            brojac=0
            for j in range(5-len(kockice)):
                konacanbroj = ""
                time.sleep(0.01)
                for i in range(1, 10, 1):
                    Niz.append((Niz[i - 1] ** 2) % M)
                    if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                        konacanbroj += "0"
                        # paran broj jedinica
                    else:
                        konacanbroj += "1"
                privremene.append((int(konacanbroj) % 6) + 1)
                Niz.clear()
                Niz.append(float(time.time()))
            for l in range(len(privremene)-1):
                if (privremene[l]==privremene[l+1]):
                    brojac+=1
            if (brojac==len(privremene)-1):
                brojuspelih+=1
        verovatnocazaful=brojuspelih/100
        #verovatnoca za poker
        kockicekojetrazimo=[]
        kockicekojetrazimo.append(najvisekockica)
        namatreba=4-max
        brojuspelih=0
        for k in range(100):
            privremene=[]
            brojac=0
            for j in range(5-max):
                konacanbroj = ""
                time.sleep(0.01)
                for i in range(1, 10, 1):
                    Niz.append((Niz[i - 1] ** 2) % M)
                    if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                        konacanbroj += "0"
                        # paran broj jedinica
                    else:
                        konacanbroj += "1"
                privremene.append((int(konacanbroj) % 6) + 1)
                Niz.clear()
                Niz.append(float(time.time()))
            for l in range(len(privremene)-1):
                if (privremene[l]==privremene[l+1] and privremene[l]==kockicekojetrazimo[0]):
                    brojac+=1
            if (brojac>=namatreba-1):
                brojuspelih+=1
        verovatnocazapoker=brojuspelih/100
        #verovatnocazajamb
        namatreba=5-max
        kockicekojetrazimo=[]
        brojuspelih=0
        kockicekojetrazimo.append(najvisekockica)
        for k in range(100):
            privremene = []
            brojac = 0
            for j in range(namatreba):
                konacanbroj = ""
                time.sleep(0.01)
                for i in range(1, 10, 1):
                    Niz.append((Niz[i - 1] ** 2) % M)
                    if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                        konacanbroj += "0"
                        # paran broj jedinica
                    else:
                        konacanbroj += "1"
                privremene.append((int(konacanbroj) % 6) + 1)
                Niz.clear()
                Niz.append(float(time.time()))
            for l in range(len(privremene) - 1):
                if (privremene[l] == privremene[l + 1] and privremene[l]==kockicekojetrazimo[0]):
                    brojac += 1
            if (brojac >= namatreba-1):
                brojuspelih += 1
        verovatnocazajamb=brojuspelih/100

        while(broj_poteza!=3):
            if ([5,0]  in popunjena_polja and [6,1] in popunjena_polja):
                verovatnoca=verovatnocazajamb+verovatnocazapoker+verovatnocazaful+verovatnocazakentu
                if (verovatnoca>vrednost_praga):
                    maksimalan=max(verovatnocazajamb,verovatnocazaful,verovatnocazapoker,verovatnocazakentu)
                    if (maksimalan==verovatnocazajamb):
                        namatreba = 5 - max
                        kockicekojetrazimo = []
                        brojuspelih = 0
                        kockicekojetrazimo.append(najvisekockica)
                        privremene = []
                        brojac = 0
                        for j in range(namatreba):
                            konacanbroj = ""
                            time.sleep(0.01)
                            for i in range(1, 10, 1):
                                Niz.append((Niz[i - 1] ** 2) % M)
                                if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                                    konacanbroj += "0"
                                    # paran broj jedinica
                                else:
                                    konacanbroj += "1"
                            privremene.append((int(konacanbroj) % 6) + 1)
                            Niz.clear()
                            Niz.append(float(time.time()))
                        broj_poteza += 1
                        for l in range(len(privremene) - 1):
                            if (privremene[l] == privremene[l + 1] and privremene[l] == kockicekojetrazimo[0]):
                                brojac += 1
                        if (brojac >= namatreba - 1):
                            for i in range(1, 7, 1):
                                suma += privremene.count(i) * i
                            suma += 50
                            recnik["[9, 0]"] = suma
                            break


                    elif(maksimalan==verovatnocazaful):
                        brojac = 0
                        kockice = []
                        trenutne_kockice.sort()
                        recnik2 = {}
                        for item in trenutne_kockice:
                            recnik2[item] = 0

                        for i in range(len(trenutne_kockice) - 1):
                            for j in range(i + 1, len(trenutne_kockice), 1):
                                if (trenutne_kockice[i] == trenutne_kockice[j]):
                                    recnik2[trenutne_kockice[i]] += 1
                        for i in recnik2.keys():
                            if (recnik2[i] == 2 or recnik2[i] == 3):
                                for j in range(recnik2[i]):
                                    kockice.append(i)
                        privremene = []
                        brojac = 0
                        for j in range(5 - len(kockice)):
                            konacanbroj = ""
                            time.sleep(0.01)
                            for i in range(1, 10, 1):
                                Niz.append((Niz[i - 1] ** 2) % M)
                                if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                                    konacanbroj += "0"
                                    # paran broj jedinica
                                else:
                                    konacanbroj += "1"
                            privremene.append((int(konacanbroj) % 6) + 1)
                            Niz.clear()
                            Niz.append(float(time.time()))
                        broj_poteza += 1
                        for l in range(len(privremene) - 1):
                            if (privremene[l] == privremene[l + 1]):
                                brojac += 1
                        if (brojac == len(privremene) - 1):
                            for i in range(1, 7, 1):
                                if (ostale_kockice.count(i) != 0):
                                    suma += ostale_kockice.count(i) * i
                            suma += 30
                            recnik["[7, 0]"] = suma
                            break

                    elif(maksimalan==verovatnocazapoker):
                        kockicekojetrazimo = []
                        kockicekojetrazimo.append(najvisekockica)
                        namatreba = 4 - max
                        brojuspelih = 0
                        privremene = []
                        brojac = 0
                        for j in range(5 - max):
                            konacanbroj = ""
                            time.sleep(0.01)
                            for i in range(1, 10, 1):
                                Niz.append((Niz[i - 1] ** 2) % M)
                                if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                                    konacanbroj += "0"
                                    # paran broj jedinica
                                else:
                                    konacanbroj += "1"
                            privremene.append((int(konacanbroj) % 6) + 1)
                            Niz.clear()
                            Niz.append(float(time.time()))
                        broj_poteza += 1
                        for l in range(len(privremene) - 1):
                            if (privremene[l] == privremene[l + 1] and privremene[l] == kockicekojetrazimo[0]):
                                brojac += 1
                        if (brojac >= namatreba - 1):
                            for i in range(1, 7, 1):
                                suma += ostale_kockice.count(i) * i
                            suma += 40
                            recnik["[8, 0]"] = suma
                            break


                    elif(maksimalan==verovatnocazakentu):
                        kockice = []
                        kockicekojetrazimo = []
                        for item in sorted(trenutne_kockice):
                            if (item not in kockice):
                                kockice.append(item)
                        brojac = 0
                        for i in range(len(kockice)):
                            if (kockice[i] + 1 != kockice[i + 1]):
                                brojac += 1

                        for i in range(len(kockice)):
                            if (kockice[i] + 1 != kockice[i + 1]):
                                kockicekojetrazimo.append(kockice[i] + 1)
                        privremene = []
                        brojuspelih = 0
                        privremene = []
                        for j in range(brojac):
                            konacanbroj = ""
                            time.sleep(0.01)
                            for i in range(1, 10, 1):
                                Niz.append((Niz[i - 1] ** 2) % M)
                                if (int(format(int(Niz[i]), 'b').count("1")) % 2 == 0):
                                    konacanbroj += "0"
                                    # paran broj jedinica
                                else:
                                    konacanbroj += "1"
                            privremene.append((int(konacanbroj) % 6) + 1)
                            Niz.clear()
                            Niz.append(float(time.time()))
                        broj_poteza+=1
                        if (sorted(privremene) == sorted(kockicekojetrazimo)):
                            if (broj_poteza == 1):
                                suma = 66
                            elif (broj_poteza == 2):
                                suma = 56
                            elif (broj_poteza == 3):
                                suma = 46
                            recnik["[6, 0]"] = suma
                            break
            else:
                print("prosao sam ovde")
                tmp=[0,0]
                popunjena_polja.append(tmp)
                suma=trenutne_kockice.count(1)
                recnik["[0, 0]"] = suma
                break

        print("Upisano je polje od strane pomoci prijatelja!")

            

    if (a == 5):
        print("Suma svih poena dobijenih u talonu je:{}".format(int(sum(V))))
        break
