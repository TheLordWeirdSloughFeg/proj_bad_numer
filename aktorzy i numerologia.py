import requests
from bs4 import BeautifulSoup

import pandas as pd


# Etap 1 szukanie ludzi filmu

linki_text = []
linki_cale = []
aktorzy=[]
urodz = []


def DaneLudziFilmu():
    wybor = input("Podaj ranking ludzi filmu, ktory chcesz wczytac:\n1 to aktorzy\n2 to aktorki\n3 to reżyserzy\n4 to kompozytorzy:\n")
    
    if wybor == "1":
        npliku = "aktorzy"
        link = 'https://www.filmweb.pl/ranking/person/actors/male?page='
    elif wybor == "2":
        npliku = "aktorki"
        link = 'https://www.filmweb.pl/ranking/person/actors/female?page='
    elif wybor == "3":
        npliku = "reżyserzy"
        link = 'https://www.filmweb.pl/ranking/person/director?page='
    elif wybor == "4":
        npliku = "kompozytorzy"
        link = 'https://www.filmweb.pl/ranking/person/music?page='
    else:
        print("blad, wpisz [1,2,3, lub 4]")
    
    
    for i in range(1,21):
        link_skl = link+str(i)
        tekst = requests.get(link_skl).text
        #print(odpowiedz.text)
        
        
        
        
        soup = BeautifulSoup(tekst, 'lxml')
        osoby = soup.find_all("h2",class_  ="rankingTypePerson__header")
        
        #print(osoby)
        
            
        for osoby_ze_str in osoby:
            akt = osoby_ze_str.find("a", class_="rankingTypePerson__title").text
            #link = osoby_ze_str.find("a",href_.startswith("person"))
            aktorzy.append(akt)
            #print(akt)
            for a in osoby_ze_str.find_all('a', href=True): 
                linki_text.append(a['href'])
        #print(linki_text)
        #print(linki_text[0])
        #for a in soup.find_all('a', href=True):
            #if a.startswith('''a href="//person'''):
            #print( a)
    
    
    
    
    
        # Etap 1.5 - zamiana linkow na pelne filmwebowe
    for j in linki_text:
        l = j.replace("/person/","https://www.filmweb.pl/person/")
        linki_cale.append(l)
        
        
    count=0       
    # Etap 2 uzycie linkow i wydobycie danych    
    for k in linki_cale:
        cala_strona = requests.get(k).text
        s = BeautifulSoup(cala_strona, 'lxml')
        #ur = s.find("span", itemprop="birthDate").text
        try:
            ur = s.find("span", itemprop="birthDate").text
        except (AttributeError):
            pass
        oss=aktorzy[count]
        osoba = oss.replace(" ","_")
        if len(ur) == 6:
            ur=" 0"+" 0"+ur 
        urodz.append(ur)
        count+=1
        #Pasek postepu
        proc = round((linki_cale.index(k)/len(aktorzy))*100,2)
        print("----------"+str(proc)+"%"+"----------")
        #########################################################################
        nazwa_pliku = npliku+".txt"
        with open(nazwa_pliku, 'a', encoding='utf-8') as urodzeni_aktorzy:
            urodzeni_aktorzy.write(osoba)
            urodzeni_aktorzy.write(ur)
    print("Zrobione!")

#DaneLudziFilmu()



# Etap 3 teraz mamy wszystko w plikach

def TabelkaLudziFilmu():
    wyborA = input("Podaj ranking ludzi filmu, ktory chcesz zanalizowac:\n1 to aktorzy\n2 to aktorki\n3 to reżyserzy\n4 to kompozytorzy:\n")
    if wyborA == "1":
        npliku = "aktorzy"

    elif wyborA == "2":
        npliku = "aktorki"
        
    elif wyborA == "3":
        npliku = "reżyserzy"
        
    elif wyborA == "4":
        npliku = "kompozytorzy"
        
    else:
        print("blad, wpisz [1,2,3, lub 4]")
        
    nazwa_pliku = npliku+".txt"
    
# surowa lista po kolei po spacji, ostatnia nadmiarowa spacja jest usunieta  
    
    with open(nazwa_pliku, 'r', encoding='utf-8') as tf:
            surowa = tf.read().split(' ')
    surowa = surowa[:-1]
    #print(surowa)
    len(surowa)

# robimy oddzielne listy dla kazdego aktora oraz daty urodzenia
    ImieNazwisko =[]
    dzien = []
    miesiac = []
    rok = []
        
    for a in surowa:
        ImieNazwisko=surowa[0::4]
        dzien = surowa[1::4]
        miesiac = surowa[2::4]
        rok = surowa[3::4]
        miesiac_n=[]
    for b in miesiac:
        if b.startswith('sty'):
            mm = b.replace(b,"1")
            miesiac_n.append(mm)
        elif b.startswith('lut'):
            mm = b.replace(b,"2")
            miesiac_n.append(mm)
        elif b.startswith('mar'):
            mm = b.replace(b,"3")
            miesiac_n.append(mm)
        elif b.startswith('kwi'):
            mm = b.replace(b,"4")
            miesiac_n.append(mm)
        elif b.startswith('maj'):
            mm = b.replace(b,"5")
            miesiac_n.append(mm)
        elif b.startswith('cze'):
            mm = b.replace(b,"6")
            miesiac_n.append(mm)
        elif b.startswith('lip'):
            mm = b.replace(b,"7")
            miesiac_n.append(mm)
        elif b.startswith('sie'):
            mm = b.replace(b,"8")
            miesiac_n.append(mm)
        elif b.startswith('wrz'):
            mm = b.replace(b,"9")
            miesiac_n.append(mm)
        elif b.startswith('paź'):
            mm = b.replace(b,"10")
            miesiac_n.append(mm)
        elif b.startswith('lis'):
            mm = b.replace(b,"11")
            miesiac_n.append(mm)
        elif b.startswith('gru'):
            mm = b.replace(b,"12")
            miesiac_n.append(mm)
        else:
            miesiac_n.append(b)
            
    
    #Kolejna rzecz dodajemy liste bedaca suma liczby urodzenia
    
    Liczba_Ur = []
    
    count = 0
    for a in ImieNazwisko:
        s=dzien[count] + miesiac_n[count] + rok[count]
        l_ur=0
        for j in s:
            l_ur+=int(j)
        count+=1
        if l_ur == 11 or l_ur == 22 or l_ur == 33:
            Liczba_Ur.append(l_ur)
        else:
            l_ur=str(l_ur)
            ur_ost=0
            for j in l_ur:
                ur_ost+=int(j)
            if ur_ost == 11 or l_ur == 22 or l_ur == 33 or ur_ost < 10:
                Liczba_Ur.append(ur_ost)
            else:
                ur_ost=str(ur_ost)
                ur_ost_ost=0
                for j in ur_ost:
                    ur_ost_ost+=int(j)
                Liczba_Ur.append(ur_ost_ost)

    #Kolejna rzecz dodajemy liczbe imienia i nazwiska zamieniajac odpowiednio litere na cyfre:
    L_Imienia_I_Nazwiska = []
    # trzeba po kazdym elemencie listy i go przeliterować (for w for) i wtedy w zaleznosci od litery (znaki specjalne uwazac) nadac wartosc zgodnie z tabelka
    
    for m in ImieNazwisko:
        im=m.lower()
        l_count = 0
        for li in im:
            if li == "à" or li == "á" or li =="â" or li =="ã" or li =="ä" or li =="å" or li =="ă" or li =="ā" or li =="ą" \
            or li == "æ" or li == "a" or li == "j"  or li == "s"  or li == "ś"  or li == "ĵ"  or li == "ş" or li == "š" or li =="ŝ":
                l_count +=1
            if li == "ß" or li == "b" or li =="k" or li =="t" or li =="þ" or li =="ķ" or li =="ĸ" or li =="ţ" or li =="ť" or li =="ŧ":
                l_count +=2
            if li == "ç" or li == "č" or li =="ĉ" or li =="ċ" or li =="c" or li =="ć" or li =="ù" or li =="ú" or li =="û" or li =="ü"\
            or li == "ĺ" or li =="ļ" or li =="ľ" or li =="ŀ" or li =="ł" or li =="ũ" or li =="ū" or li =="ŭ" or li =="ů" \
            or li =="ű" or li =="ų" or li == "u" or li == "l":
                l_count +=3
            if li == "ð" or li == "d" or li == "m" or li == "v":
                l_count +=4
            if li == "è" or li == "é" or li == "ê" or li == "ë" or li == "ñ" or li == "e" or li == "ē" or li == "ĕ" or li == "ė" or li == "ę"\
            or li == "ě" or li == "ń" or li == "ņ" or li == "ň" or li == "ŉ" or li == "ŋ" or li =="n" or li =="ŵ" or li == "w":
                l_count +=5
            if li == "f" or li == "ò" or li == "ø" or li == "ô" or li == "ó" or li == "õ" or li == "ö" or li == "ō" or li == "ŏ" or li == "ő"\
            or li == "œ" or li == "o" or li == "x":
                l_count +=6    
            if li == "ý" or li == "ÿ" or li == "ĝ" or li == "ğ" or li == "ġ" or li == "ģ" or li == "ŷ" or li == "g" or li == "p" or li == "y":
                l_count +=7   
            if li == "ĥ" or li == "ħ" or li =="ź" or li =="ż" or li =="ž" or li =="h" or li =="q" or li =="z":
                l_count +=8
            if li == "ì" or li == "í" or li =="î" or li =="ï" or li =="ĩ" or li =="ī" or li =="ĭ" or li =="į" or li =="ı"\
            or li =="i"  or li =="ŕ"  or li =="ŗ"  or li =="ř" or li =="r":
                l_count +=9
            else:
                l_count +=0
        if l_count == 11 or l_count == 22 or l_count == 33:
            L_Imienia_I_Nazwiska.append(l_count)
        else:
            l_count=str(l_count)
            li_li=0
            for j in l_count:
                li_li+=int(j)
            if li_li == 11 or li_li == 22 or li_li == 33 or li_li < 10:
                L_Imienia_I_Nazwiska.append(li_li)
            else:
                li_li=str(li_li)
                li_li_li=0
                for j in li_li:
                    li_li_li+=int(j)
                L_Imienia_I_Nazwiska.append(li_li_li)

    
    '''1 – A, Ą, J, S, Ś

    2 – B, K, T

    3 – C, Ć, L, Ł, U

    4 – D, M, V

    5 – E, Ę, N, Ń, W

    6 – F, O, Ó, X

    7 – G, P, Y

    8 – H, Q, Z, Ź, Ż

    9 – I, R
    
    znaki
    ß,à,á,â,ã,ä,å,æ,ç,è,é,ê,ë,ì,í,î,ï,ð,ñ,ò,ó,ô,õ,ö,,ø,ù,ú,û,ü,ý,þ,
    ÿ,ā,ă,ā,ą,,ć,ĉ,ċ,č,ď,đ,ē,ĕ,ė,ę,ě,ĝ,ğ,ġ,ģ,ĥ,ħ,ĩ,ī,ĭ,į,ı,ĵ,ķ,ĸ,ĺ,ļ,ľ
    ,ŀ,ł,ń,ņ,ň,ŉ,ŋ,ō,ŏ,ő,œ,ŕ,ŗ,ř,ś,ŝ,ş,š,ţ,ť,ŧ,ũ,ū,ŭ,ů,ű,ų,ŵ,ŷ,ź,ż,ž'''
    
    
    Profesja = []

    for a in ImieNazwisko:
        if wyborA == "1":
            Profesja.append(1)
        elif wyborA == "2":
            Profesja.append(1)
        elif wyborA == "3":
            Profesja.append(2)
        elif wyborA == "4":
            Profesja.append(3)


    #Kolejna rzecz znaki zodiaku
    Znak_zodiaku = []
    ct = 0
    
    for a in ImieNazwisko:
        mies=int(miesiac_n[ct])
        dn=int(dzien[ct])
        if mies == 1:
            if dn <=19:
                Znak_zodiaku.append("koziorozec")
            else:
                Znak_zodiaku.append("wodnik")
        if mies == 2:
            if dn <=18:
                Znak_zodiaku.append("wodnik")
            else:
                Znak_zodiaku.append("ryby")        
        if mies == 3:
            if dn <=20:
                Znak_zodiaku.append("ryby")
            else:
                Znak_zodiaku.append("baran")
        if mies == 4:
            if dn <=19:
                Znak_zodiaku.append("baran")
            else:
                Znak_zodiaku.append("byk")
        if mies == 5:
            if dn <=20:
                Znak_zodiaku.append("byk")
            else:
                Znak_zodiaku.append("bliznieta")
        if mies == 6:
            if dn <=20:
                Znak_zodiaku.append("bliznieta")
            else:
                Znak_zodiaku.append("rak")
        if mies == 7:
            if dn <=22:
                Znak_zodiaku.append("rak")
            else:
                Znak_zodiaku.append("lew")
        if mies == 8:
            if dn <=22:
                Znak_zodiaku.append("lew")
            else:
                Znak_zodiaku.append("panna")
        if mies == 9:
            if dn <=22:
                Znak_zodiaku.append("panna")
            else:
                Znak_zodiaku.append("waga")
        if mies == 10:
            if dn <=22:
                Znak_zodiaku.append("waga")
            else:
                Znak_zodiaku.append("skorpion")
        if mies == 11:
            if dn <=21:
                Znak_zodiaku.append("skorpion")
            else:
                Znak_zodiaku.append("strzelec")
        if mies == 12:
            if dn <=21:
                Znak_zodiaku.append("strzelec")
            else:
                Znak_zodiaku.append("koziorozec")
        if mies == 0:
            Znak_zodiaku.append("brak")
        ct+=1


    #Dataframe


    dict = {'Imie_i_Nazwisko': ImieNazwisko, 'dzien': dzien, 'miesiac': miesiac_n, "rok": rok, "liczba urodzenia":Liczba_Ur, "znak zodiaku":Znak_zodiaku, "liczba imienia i nazwiska": L_Imienia_I_Nazwiska, "profesja": Profesja} 
    df = pd.DataFrame(dict)
    print(df)
    nazwa_do_zapisu = npliku+"_tabelka"+".txt" 
    df.to_csv(nazwa_do_zapisu)


TabelkaLudziFilmu()


#Operacje

'''wybor = input("Podaj ranking ludzi filmu, ktory chcesz zanalizowac:\n1 to aktorzy\n2 to aktorki\n3 to reżyserzy\n4 to kompozytorzy:\n")
if wybor == "1":
    npliku = "aktorzy"
        
elif wybor == "2":
    npliku = "aktorki"
        
elif wybor == "3":
    npliku = "reżyserzy"
        
elif wybor == "4":
    npliku = "kompozytorzy"     
else:
    print("blad, wpisz []")
        

nazwa = npliku+"_tabelka"+".txt"
data = pd.read_csv(nazwa)  

print(data)'''

#dalej mozna dodac przelicznik liter na cyfry (uwaga na unicode)






#TESTY
