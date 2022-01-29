<sub><sup>Autor zaznacza, że nie wierzy w pseudonaukę oraz teorie dotyczące prekognicji. Stara się jedynie poddać numerologię analizie naukowej, by móc jednoznacznie stwierdzić wiarygodność (lub jej BRAK) pseudonauki jaką jest numerologia.</sup></sub>
# Ludzie filmu i numerologia - Czy Twój los jest przesądzony?

# Wstęp
Numerologia to pseudonauka badająca mistyczne lub magiczne właściwości liczb oraz opierająca się na przekonaniu, że numer przyporządkowany danemu obiektowi (data urodzenia, numer domu, samochodu, telefonu, zakodowane pod postacią liczby imię i nazwisko, itp.) ma związek z jego losem. Na podstawie takich zależności według numerologów można przewidywać przyszłość.</br>
Pitagoras oraz jego szkoła pitagorejska jako jedni z pierwszych zajmowali się numerologią. Byli oni przekonani, że porządek Wszechświata jest oparty na liczbach, regułach matematycznych i geometrycznych. Można zatem przypuszcać, że dla pitagorejczyków numerologia i zależności między liczbami były utożsamiane z bóstwem. Szkoła pitagorejska z kolei wpłynęła na platonizm, który zaś wpłynął na powstanie gematrii, która jest podobna do numerologii. W gematrii słowa przekształca się na liczby, zwykle przez przypisanie każdej litery alfabetu hebrajskiego do liczby, następnie w zależności od wyniku przypisywany jest sens słowu. Gematria jest obecnie szeroko praktykowana w judaizmie i stanowi ważne źródło biblijnej interpretacji ([ciekawy przykład na stronie uniwersytaetu Yale](https://web.library.yale.edu/cataloging/hebraica/about-gematria#:~:text=Gematria%20is%20a%20Jewish%20form,ten%20from%2020%20to%2090.)). Przyjmowana przez pitagorejczyków symbolika liczb z kolei była kontynuowana m.in. w chrześcijańskiej analizie biblijnej liczby Bestii. W późniejszych wiekach podczas kształtowania się nauki, dzięki sięganiu do wiedzy starożytnych kultur, numerologia wpłynęła także na rozwój matematyki.</br>
Przedmiotem numerologii są nie tylko liczby, lecz również nazwy własne, które są zamieniane na liczby poprzez ponumerowanie liter alfabetu, a następnie ich sumowanie. Przyporządkowanie liczb literom polega na zapisaniu alfabetu w pionowych słupkach (9 liter w słupku). Ten sam wyraz zapisany w różnych językach lub alfabetach może dawać inną sumę. Numerologia posługująca się alfabetem łacińskim ma identyczne wartości liter w każdym kraju i języku na świecie, pod warunkiem, że używanym alfabetem jest alfabet łaciński.</br>
Według numerologów nic nie dzieje się przypadkowo ani to, że ktoś urodził się w jakimś kraju, ani, że posiada takie, a nie inne imiona i nazwiska, datę urodzenia itp. Podstawową procedurą numerologii jest sumowanie cyfr danej liczby. W związku z tym można określić tzw. liczbę drogi życia lub tzw. liczba urodzenia. Według numerologów liczba drogi życia determinuje cechy danej osoby, a także zawiera program, do którego człowiek powinien dążyć. Aby uzyskać te cechy, sumuje się cyfry daty urodzenia, aż do uzyskania jednej cyfry, będącej „liczbą urodzenia” lub liczbą drogi życia danej osoby. Działanie to nazywa się redukcją teozoficzną. Przykładowo osoba urodzona 23-08-1979 r.: 2+3+8+1+9+7+9 = 39 ⇒ 3+9 = 12 ⇒ 1+2 = 3 (taka osoba jest numerologiczną jedynką). Jest to tzw. metoda horyzontalna.</br>
Dalsze teorie numerologiczne wiążą się z interpretacją liczbami takimi jak liczba drogi życia lub liczba urodzenia. Przykładowo osoba urodzona 23-08-1979 r. jako numerologiczna trójka ma odznaczać się: charyzmą, elokwencją, artystyczną duszą, pozytywnym myśleniem.

# Cel
Moim teoretycznym założeniem w tym badaniu było to, że numerologia pozwala na przewidywanie przyszłości, a analiza daty urodzenia oraz liczby imienia i nazwiska umożliwiają przewidzenie, czy dana osoba, jedynie na podstawie daty urodzenia oraz imienia i nazwiska, zostanie np. sławnym aktorem, kompozytorem lub reżyserem. Przez określenie "sławny" rozumie się osobę związaną z przemysłem filmowym, która znajduje się na liście top 500 najlepszych aktorów, aktorek, kompozytorów i reżyserów z portalu [Filmweb.pl](https://www.filmweb.pl/). Analizując liczbę drogi życia i liczbę urodzenia osób z tej listy staram się znaleźć zależność tych obliczonych liczb z wykonywanym zawodem związanym z filmem (o ile taka istnieje). Zawody związane z filmem zostały przeze mnie wybrane z uwagi na zweryfikowaną datę urodzenia oraz to, że dla wielu osób w społeczeństwie zawód aktora, bądź filmowca jest postrzegany jako prestiżowy i kojarzy się z bogactwem, popularnością oraz ogólnym spełnieniem.

# Wyniki badań
## Wstępna analiza danych
I) Pobranie danych z portalu Filmweb

Etap 1 szukanie ludzi filmu
Najpierw pobieram dane z serwisu Filmweb, korzystając z modułu beautifulsoup.



Etap 1.5 - zamiana linkow na pelne filmwebowe

Etap 2 uzycie linkow i wydobycie danych  

Etap 3 teraz mamy wszystko w plikach

surowa lista po kolei po spacji, ostatnia nadmiarowa spacja jest usuniet
robimy oddzielne listy dla kazdego aktora oraz daty urodzenia
Kolejna rzecz dodajemy liste bedaca suma liczby urodzenia
Kolejna rzecz dodajemy liczbe imienia i nazwiska zamieniajac odpowiednio litere na cyfre:
trzeba po kazdym elemencie listy i go przeliterować (for w for) i wtedy w zaleznosci od litery (znaki specjalne uwazac) nadac wartosc zgodnie z tabelka
#Kolejna rzecz znaki zodiaku
mamy dataframe
analiza przeprowadzona w jupiterze


## Badanie zależności


# Wnioski
