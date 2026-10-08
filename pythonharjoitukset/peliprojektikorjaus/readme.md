## Vapaapäivä
Aapo Hannikainen

Pelin rakenne

Pelin pääohjelma, main.py sisältää pelin etenemisen. Tiedostossa käynnistetään peli ja käsitetellään pelaajan valintoja. Tieodstossa käyetään muiden tiedostojen luokkia ja
funktioita. Tiedostossa käsitellään myös pelin eri vaiheita. Eteneminen pelissä tallennetaan tallennus.txt tiedostoon, jolloin voi jatkaa peliä myöhemmin.


pelaaja.py: sisältää Pelaaja-luokan, joka käsittelee pelaajan liittyvää tietoa, esim. nimi, ikä, sekä havisit-method. Pelaaja-luokalla luodaan pelaajaolio. Jos tekee väärän valinnan pelissä, metodi tulostaa, että hävisit sekä syyn häviämiselle

huone.py sisältää Huone-luokan jolla voi luoda erilaisia paikkoja peliin, esim koti, hesburger, puisto. Luokan avulla voi käsitellä pelin paikkoja, ettei jokaista paikka varten tarvitse luoda omaa luokkaa.

valikko.py sisältää valinta-funktion, jolla näytetään valintavaihtoehdot ja kysytään valinta.  Funktio käsittelee valinnan ja palauttaa pääohjelmaan pelaajan valitsemasta vaihtoehdosta.

init.py tekee kansiosta paketin, jotta voidaan käyttää import-komentoa.

saavutukset.py:ssä määritellään pelin saavutukset ja kuvaukset. Saavutukset tallennetaan saavutukset.json-tiedostoon, jotta ne säiliyisi.

lataa-funktio lukee json-tiedostosta pelaajan saavuttamat saavutukset. (tai palauttaa tyhjän listan jos saavutuksia ei ole.)

avaa-funktiolla annetaan pelaajalle uusi saavutus. Ensin tarkistetaan, onko saavutusta vielä ja jos ei, saavutus lisätään ja tallennetaan json-tiedostoon.

tallennus.txt sisältää pelin tallennustiedot, jotta pelaaja voi myöhemmin jatkaa samasta kohdasta.
intro.txt sisältää pelin aloitustekstin
ohjeet.txt sisältää pelinohjeet


__pycache__ en osaa selittää, se vaan ilmesty tuonne.


