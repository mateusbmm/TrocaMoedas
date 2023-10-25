class Moeda:
    
    def __init__(self, valInjet, qtdCircular):

        self.liquidez = valInjet or 0
        self.qtdCircular = qtdCircular

    def __str__(self):

        return "\n------------------\nvalInjet: " + str(self.liquidez) + "\nqtdCircular:" + str(self.qtdCircular) + "\n------------------\n"
       