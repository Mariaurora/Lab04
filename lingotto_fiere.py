import csv
from operator import attrgetter
from stand import *
from espositore import Espositore
class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome=nome
        self.stand=[]
        self.espositori=[]

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome=nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        #svuoto le liste perchè se viene cliccata l'opzione 2 all'interno dello stesso run carics
        #i dati 2 volte
        self.stand=[]
        self.espositori=[]
        try:
            with open(file_path,'r',encoding='utf-8') as file:
                leggofile=csv.reader(file)
                for riga in leggofile:
                   codice=riga[0]
                   iniziale=codice[0]
                   if iniziale=='S':
                       if len(riga)>4:
                           ultimoelemento=riga[-1]
                           if ultimoelemento.isdigit():
                               sprese=StandConPrese(riga[0],riga[1],riga[2],riga[3],riga[4])
                               self.stand.append(sprese)
                           elif ultimoelemento.isalpha():
                                spremium=StandPremium(riga[0],riga[1],riga[2],riga[3],riga[4])
                                self.stand.append(spremium)
                       else:
                           sstandard=Stand(riga[0],riga[1],riga[2],riga[3])
                           self.stand.append(sstandard)
                   else:
                       espositore=Espositore(riga[0],riga[1],riga[2])
                       self.espositori.append(espositore)

        except FileNotFoundError:
          raise FileNotFoundError


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        standTrovato=None
        espositoreTrovato=None
        espositoreassegnato=None
        #controllo esistenza stand
        for stand in self.stand:
            if stand.codice==codice_stand:
                standTrovato=stand

        if standTrovato is None:
            raise Exception('----Lo stand risulta inesistente----')

        #controllo assegnazione stand
        if standTrovato.espositore is not None:
            raise Exception('----Lo stand risulta essere già assegnato----')

        #controllo esistenza espositore
        for espositore in self.espositori:
            if espositore.codice==codice_espositore:
                espositoreTrovato=espositore

        if espositoreTrovato is None:
            raise Exception('----L''espositore risulta inesistente----')
        #controllo che non sia già assegnato ad uno stand
        for stand in self.stand:
            if stand.espositore is espositoreTrovato:
                espositoreassegnato=True
        if espositoreassegnato is True:
            raise Exception('----L''espositore risulta essere già assegnato ad uno stand----')

        standTrovato.espositore=espositoreTrovato
        espositoreTrovato.stand=standTrovato


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for espositore in self.espositori:
           print(espositore)
        #per lo stand ho già sistemato nella classe ESPOSITORE perchè ho deciso di salvare il riferimento a stand




    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return  sorted(self.stand, key=attrgetter('prezzo') )