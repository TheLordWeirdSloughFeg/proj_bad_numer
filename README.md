<sub><sup>Autor zaznacza, że nie wierzy w pseudonaukę oraz teorie dotyczące prekognicji. Stara się jedynie poddać numerologię analizie naukowej, by móc jednoznacznie stwierdzić wiarygodność (lub jej BRAK ) pseudonauki jaką jest numerologia.</sup></sub>
# Ludzie filmu i numerologia - Czy Twój los jest przesądzony?

# Wstęp
Numerologia to pseudonauka badająca mistyczne lub magiczne właściwości liczb oraz opierająca się na przekonaniu, że numer przyporządkowany danemu obiektowi (data urodzenia, numer domu, samochodu, telefonu, zakodowane pod postacią liczby imię i nazwisko, itp.) ma związek z jego losem. Na podstawie takich zależności według numerologów można przewidywać przyszłość.</br>
Pitagoras oraz jego szkoła pitagorejska jako jedni z pierwszych zajmowali się numerologią. Byli oni przekonani, że porządek Wszechświata jest oparty na liczbach, regułach matematycznych i geometrycznych. Można zatem przypuszczać, że dla pitagorejczyków numerologia i zależności między liczbami były utożsamiane z bóstwem. Szkoła pitagorejska z kolei wpłynęła na platonizm, który zaś wpłynął na powstanie gematrii, która jest podobna do numerologii. W gematrii słowa przekształca się na liczby, zwykle przez przypisanie każdej litery alfabetu hebrajskiego do liczby, następnie w zależności od wyniku przypisywany jest sens słowu. Gematria jest obecnie szeroko praktykowana w judaizmie i stanowi ważne źródło biblijnej interpretacji ([ciekawy przykład na stronie uniwersytetu Yale](https://web.library.yale.edu/cataloging/hebraica/about-gematria#:~:text=Gematria%20is%20a%20Jewish%20form,ten%20from%2020%20to%2090.)). Przyjmowana przez pitagorejczyków symbolika liczb z kolei była kontynuowana m.in. w chrześcijańskiej analizie biblijnej liczby Bestii. W późniejszych wiekach podczas kształtowania się nauki, dzięki sięganiu do wiedzy starożytnych kultur, numerologia wpłynęła także na rozwój matematyki.</br>
Przedmiotem numerologii są nie tylko liczby, lecz również nazwy własne, które są zamieniane na liczby poprzez ponumerowanie liter alfabetu, a następnie ich sumowanie. Przyporządkowanie liczb literom polega na zapisaniu alfabetu w pionowych słupkach (9 liter w słupku). Ten sam wyraz zapisany w różnych językach lub alfabetach może dawać inną sumę. Numerologia posługująca się alfabetem łacińskim ma identyczne wartości liter w każdym kraju i języku na świecie, pod warunkiem, że używanym alfabetem jest alfabet łaciński.</br>
Według numerologów nic nie dzieje się przypadkowo ani to, że ktoś urodził się w jakimś kraju, ani, że posiada takie, a nie inne imiona i nazwiska, datę urodzenia itp. Podstawową procedurą numerologii jest sumowanie cyfr danej liczby. W związku z tym można określić tzw. liczbę drogi życia lub tzw. liczba urodzenia. Według numerologów liczba drogi życia determinuje cechy danej osoby, a także zawiera program, do którego człowiek powinien dążyć. Aby uzyskać te cechy, sumuje się cyfry daty urodzenia, aż do uzyskania jednej cyfry, będącej „liczbą urodzenia” lub liczbą drogi życia danej osoby. Działanie to nazywa się redukcją teozoficzną. Przykładowo osoba urodzona 23-08-1979 r.: 2+3+8+1+9+7+9 = 39 ⇒ 3+9 = 12 ⇒ 1+2 = 3 (taka osoba jest numerologiczną jedynką). Jest to tzw. metoda horyzontalna.</br>
Dalsze teorie numerologiczne wiążą się z interpretacją liczbami takimi jak liczba drogi życia lub liczba urodzenia. Przykładowo osoba urodzona 23-08-1979 r. jako numerologiczna trójka ma odznaczać się: charyzmą, elokwencją, artystyczną duszą, pozytywnym myśleniem.

# Cel
Moim teoretycznym założeniem w tym badaniu było to, że numerologia pozwala na przewidywanie przyszłości, a analiza daty urodzenia oraz liczby imienia i nazwiska umożliwiają przewidzenie, czy dana osoba, jedynie na podstawie daty urodzenia oraz imienia i nazwiska, jest np. sławnym aktorem, kompozytorem lub reżyserem. Przez określenie "sławny" rozumie się osobę związaną z przemysłem filmowym, która znajduje się na liście top 500 najlepszych aktorów, aktorek, kompozytorów i reżyserów z portalu [Filmweb.pl](https://www.filmweb.pl/). Analizując liczbę drogi życia i liczbę urodzenia osób z tej listy staram się znaleźć zależność tych obliczonych liczb z wykonywanym zawodem związanym z filmem (o ile taka istnieje). Zawody związane z filmem zostały przeze mnie wybrane z uwagi na zweryfikowaną datę urodzenia oraz to, że dla wielu osób w społeczeństwie zawód aktora, bądź filmowca jest postrzegany jako prestiżowy i kojarzy się z bogactwem, popularnością oraz ogólnym spełnieniem.

# Wyniki badań
## Pobranie i wstępna analiza danych
### I) Pobranie danych z portalu Filmweb

<b>Etap 1 - szukanie ludzi filmu</b></br>
Najpierw pobieram dane z serwisu Filmweb, korzystając z modułu beautifulsoup.
Wyciągam imię i nazwisko z rankingu 500 najlepiej ocenianych aktorów, aktorek, kompozytorów i reżyserów z nagłówków.

<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/etap_1.JPG" />
</p>
Daty urodzenia są na konkretnej stronie osoby. Po wyciągnięciu imienia i nazwiska tworzę link, aby pobrać datę urodzenia.
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/etap_1.5.JPG" />
</p>
<b>Etap 2 – pobranie dat  urodzeń</b></br>
Pobieram datę urodzenia, następnie obrabiam ją wstępnie. Pobieranie przedstawiam graficznie paskiem stanu.

<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/etap_2.JPG" />
</p>
Dane zapisuję do pliku txt dla łatwiejszego dostępu. Przykładowo pobrane dane aktorek wyglądają one następująco:

<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/etap_2plik.JPG" />
</p>
Imię i nazwisko jest oddzielone znakiem podkreślenia, a dzień, miesiąc i rok spacją. Kolejnym etapem jest przygotowanie tabelki do analizy.
### II) Wstępna obróbka danych
Usuwam nadmiarową spację między kolejnymi rekordami. W przypadku braku daty urodzenia, domyślnie wstawiane jest 0 do dnia, miesiąca i roku urodzenia.</br>
W dacie urodzenia na stronie miesiąc jest w postaci pełnej nazwy (string). Do obliczeń zamieniam kolejno nazwy miesięcy na liczby:

<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/mies.JPG" />
</p>
<b>a) obliczenie liczby urodzenia </b></br>
Do analizy potrzebuję liczbę urodzenia, znak zodiaku oraz liczbę imienia i nazwiska. Liczbę urodzenia obliczam metodą horyzontalną  (dla przypomnienia, dodaję kolejno cyfry  daty urodzenia, a następnie dodaję kolejno cyfry w wyniku jeśli suma kolejnych cyfr daty urodzenia nie jest równa 11, 22 lub 33, bądź nie jest cyfrą od 1 do 9).
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/liczba_ur.JPG" />
</p>
<b>b) obliczenie liczby imienia i nazwiska </b></br>

Kolejnym etapem jest obliczenie liczby imienia i nazwiska. Zamieniam kolejne litery alfabetu na odpowiednią cyfrę według tabelki systemu pitagorejskiego opartej na alfabecie łacińskim:
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/numerologia-alfabet.JPG" />
</p>
W przypadku imion i nazwisk ze znakami innych alfabetów, np. polskiego czy hiszpańskiego przyporządkowuję cyfrę tej literze na której jest oparta, czyli do <i>ą,à,á</i> przyporządkowuję tę samą cyfrę co do litery <i>a</i>, litery <i>ç, ć</i> do cyfry litery <i>c</i> itd. </br>
Po zamianie postępuję w taki sam sposób jak przy obliczaniu liczby urodzenia, czyli dodaję kolejne cyfry i jeśli wynik nie jest równy 11, 22 lub 33, bądź nie jest cyfrą od 1 do 9, dodaję cyfry z wyniku aż do otrzymania wyniku 11, 22, 33, 1, 2, 3, 4, 5, 6, 7, 8 lub 9.
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/liczba_im_naz.JPG" />
</p>
<b>c) dodanie znaku zodiaku </b></br>
Na podstawie analizy miesiąca i dnia urodzenia określam znak zodiaku. Znaki zodiaku zgodnie z są określane według dat z tabelki:
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/znaki_zodiaku.JPG" />
</p>
Przy analizie wykorzystuję sekwencję logiczną:
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/zodiak.JPG" />
</p>
<b>d) Stworzenie ramki danych </b></br>
Z dotychczasowych danych tworzę ramkę danych do analizy.



<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/dict.JPG" />
</p>
## Analiza EDA
Analiza została przeprowadzona w Jupiter notebook. </br>
Na początku sprawdzam, czy tabelka została dobrze wczytana.
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/top_10_aktorow.JPG" />
</p>
<div align="center">
<b><h3>Top 10 aktorów według użytkowników serwisu Filmweb</h3></b>
</div>
Sprawdzam jaki jest rozkład odpowiednich kolumn dla aktorów, aktorek, reżyserów i kompozytorów.
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/aktorzy_wykr.JPG" />
</p>
<div align="center">
<b><h3>Rozkład kolumn dla aktorów</h3></b>
</div>

<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/ aktorki_wykr.JPG" />
</p>
<div align="center">
<b><h3>Rozkład kolumn dla aktorek</h3></b>
</div>

<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/rezyserzy_wykr.JPG" />
</p>
<div align="center">
<b><h3>Rozkład kolumn dla reżyserów</h3></b>
</div>
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/kompozytorzy_wykr.JPG" />
</p>
<div align="center">
<b><h3>Rozkład kolumn dla kompozytorów</h3></b>
</div>

W przypadku aktorów i aktorek najczęstszym miesiącem urodzenia jest kwiecień (znak zodiaku baran), a najczęstszą liczbą urodzenia jest 9.
W przypadku reżyserów najczęstszą liczbą urodzenia jest 7, miesiącem urodzenia marzec (znak zodiaku ryby), a najczęstszą liczbą imienia i nazwiska 11 oraz 9.
W przypadku kompozytorów najczęstszą liczbą urodzenia jest również 9, a najczęstsza liczba imienia i nazwiska to 1 i 11. Najwięcej kompozytorów urodziło się w marcu i kwietniu (znak zodiaku baran oraz byk).</br>

Po wstępnej analizie poszczególnych profesji, wszystkie tabelki zostały połączone w jedną, co umożliwia dalszą analizę oraz sklasyfikowanie za pomocą algorytmów uczenia maczynowego.</br>
Do danych dodałem kolumnę zawierającą zakodowane profesje:</br>
* 1 to aktorzy i aktorki
* 2 to reżyserzy
* 3 to kompozytorzy


<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/ludzie_filmu_wykr.JPG" />
</p>
<div align="center">
<b><h3>Rozkład kolumn dla ludzi filmu</h3></b>
</div>

Ogółem najczęstszą liczbą urodzenia jest 9, miesiącem urodzenia marzec lub kwiecień, a najpopularniejszym znakiem baran.

Przed analizą zamieniam również znaki zodiaku na dane numeryczne według schematu:</br>
* 0 - brak
* 1 - baran
* 2 - byk
* 3 - bliźnięta
* 4 - rak
* 5 - lew
* 6 - panna
* 7 - waga
* 8 - skorpion
* 9 - strzelec
* 10 - koziorożec
* 11 - wodnik
* 12 - ryby

Następnie usuwam id oraz imię i nazwisko.</br>
Stosunek liczby urodzenia do imienia i nazwiska w zależności od profesji:

<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/l_ur_do_l_im_naz.JPG" />
</p>
W przypadku liczbie imienia i nazwiska 33 oraz 22 przeważają aktorzy i aktorki.
## XGBoost
Dzielę dane na zbiór testowy i treningowy w stosunku 1:3. W kolejnym kroku trenuję model XGBoost:
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/train_XGB.JPG" />
</p>


Sprawdzam jeszcze jakie czynniki mają wpływ na profesję (o ile jakiekolwiek).
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/shap.JPG" />
</p>

<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/shap_1.JPG" />
</p>
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/shap_2.JPG" />
</p>
Według grafów największy wpływ na profesję ma rok urodzenia, dopiero w dalszej kolejności liczby obliczone metodami zgodnymi z numerologią. Wynik ma sens, gdyż z analizy EDA wynika, że porównując wszystkie tabele top 500, stosunkowo najmłodsze są aktorki, następnie aktorzy, a na samym końcu reżyserzy oraz kompozytorzy. Także dzień urodzenia wydaje się mieć wpływ, mimo, że we wcześniejszych analizach trudno było stwierdzić, który dzień urodzenia jest najbardziej charakterystyczny dla danej profesji/.</br>

Wybieram algorytm klasyfikacyjny XGBoost.
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/xgb_fit.JPG" />
</p>
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/xgb_score.JPG" />
</p>

Po zastosowaniu modelu XGBoost jego dokładność wyniosła <b>0,68</b>, co jest przeciętnym wynikiem. Następnie dla porównania zastosowałem jeszcze algorytm k-najbliższych sąsiadów.

## Algorytm k-najbliższych sąsiadów
Na początku sprawdzam który parametr k jest najbardziej optymalny.
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/knn_fit.JPG" />
</p>

Wybrałem k=16 jako że, przy wyższych współczynnikach k wzrost dokładności jest niewielki. Trenuję model.
<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/knn_train.JPG" />
</p>

<p align="center">
  <img src="https://github.com/TheLordWeirdSloughFeg/proj_bad_numer/blob/main/obrazki/knn_score.JPG" />
</p>
Wynik modelu k-najbliższych sąsiadów to <b>0,76</b>, biorąc pod uwagę rozkład poszczególnych profesji względem roku urodzenia, prawdopodobnie miało to największy wpływ na wyższy wynik tego modelu.

# Wnioski
Numerologia jako paranauka na pewno w dalszym ciągu będzie służyła do przewidywania przyszłości, jednak w przypadku zawodów związanych z przemysłem filmowym, nie wydaje się zdawać egzaminu. Dokładność algorytmu XGBoost wyniosła <b>0,68</b>, natomiast dokładność algorytmu k-najbliższych sąsiadów wynosi <b>0,76</b>.
