class Espositore:
    def __init__(self,codice,nome,cognome):
        self.codice = codice
        self.nome = nome
        self.cognome= cognome
        self.stand=None
    def __str__(self):
        if self.stand is None:
          return f'CODICE: {self.codice} NOME: {self.nome} COGNOME: {self.cognome}--> NESSUNO STAND ASSEGNATO'
        else:
            return f'CODICE: {self.codice} NOME: {self.nome} COGNOME: {self.cognome}--> STAND ASSEGNATO : {self.stand.codice}'

