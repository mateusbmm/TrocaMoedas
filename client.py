from xmlrpc.client import ServerProxy as rpc

class Cliente:
    def __init__(self) -> None:
        self.con = rpc("http://localhost:1000")

    def consultaPrecoEmBRL(self, qtdAtivoSaida):
        return self.con.consultaPrecoEmBRL(qtdAtivoSaida)
    
    def fazerCompraMTcomBrl(self, valorEntradaEmBRL):
        return self.con.fazerCompraMTcomBrl(valorEntradaEmBRL)


    
Cliente = Cliente()


print(Cliente.consultaPrecoEmBRL(1))
Cliente.fazerCompraMTcomBrl(500)
