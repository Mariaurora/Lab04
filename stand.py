class Stand:
    tipo='STANDARD'
    def __init__(self,codice,metriquadri,padiglione,prezzo):
       self.codice = codice
       self.metriquadri = metriquadri
       self.padiglione = padiglione
       self.prezzo =float(prezzo)
       self.espositore=None

    def disponibilita(self):
        if self.espositore is None:
            return f'DISPONIBILE'
        else:
            return f'ASSEGNATO A : {self.espositore.codice}'
    def __str__(self):
        return f'{self.disponibilita()}-->TIPO: {self.tipo} CODICE: {self.codice} MQ: {self.metriquadri} PADIGLIONE: {self.padiglione} PREZZO:{self.prezzo} '


class StandConPrese(Stand):
    tipo='PRESE EXTRA'
    def __init__(self,codice,metriquadri,padiglione,prezzo,preseextra):
        super().__init__(codice,metriquadri,padiglione,prezzo)
        self.preseextra = int(preseextra)
        self.prezzo = self.prezzo * (1 + 0.07 * self.preseextra)

    def __str__(self):
        return f'{super().__str__()} PRESE:{self.preseextra}'

class StandPremium(Stand):
    tipo='PREMIUM'
    def __init__(self,codice,metriquadri,padiglione,prezzo,posizione):
        super().__init__(codice,metriquadri,padiglione,prezzo)
        self.posizione = posizione
        self.prezzo=self.prezzo*1.30
    def __str__(self):
        return f'{super().__str__()} POSIZIONE:{self.posizione}'
