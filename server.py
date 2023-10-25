from xmlrpc.server import SimpleXMLRPCServer as rpc
from moeda import Moeda

endereco = ('localhost', 1000)
server = rpc(endereco)

MTP = Moeda(2000, 500)

usuario = {
    "id": 1,
    "BRL": 2000,
    "MTP": 0

}

print(MTP)


# dado um valor de entrada de um ativo e um par de reservas, retorna o valor máximo de saída do outro ativo
# qtdEntrada é o valor em BRL que voce quer pagar e a função retorna a quantidade de MTP que vai retornar
def getAmountOut(qtdEntrada, liquidezAtivoSaida, reservaAtivoSaida):
    qtdEntradaComTaxa = qtdEntrada
    numerator = qtdEntradaComTaxa * reservaAtivoSaida
    denominator = liquidezAtivoSaida + qtdEntradaComTaxa
    quantSaida = numerator / denominator
    return quantSaida


#retorna p "preço" de um ativo dada a liquidez e a qunatidade disponivel no mercado de outro
#dado um valor de saída de um ativo e um par de reservas, retorna um valor de entrada necessário do outro ativo
def getAmountIn(quantidadeSaida, liquidezAtivoSaida, reservaAtivoSaida):
    numerator = liquidezAtivoSaida * quantidadeSaida
    denominator = reservaAtivoSaida - quantidadeSaida
    precoSaida = numerator / denominator
    return precoSaida


def consultaPrecoEmBRL(qtdSaida):
    return getAmountIn(qtdSaida, MTP.liquidez, MTP.qtdCircular)

def fazerCompraMTcomBrl(valorEntradaEmBRL):
    #valorEntradaEmBRL = int(valorEntradaEmBRL)
    total = getAmountOut(valorEntradaEmBRL, MTP.liquidez, MTP.qtdCircular)

    if( usuario["BRL"] > valorEntradaEmBRL ):
       #print(usuario["BRL"], valorEntradaEmBRL )



        if(int( MTP.qtdCircular) >= total):
            usuario["BRL"] = usuario["BRL"] - valorEntradaEmBRL
            MTP.liquidez = MTP.liquidez + valorEntradaEmBRL

            usuario["MTP"] = total
            MTP.qtdCircular =  MTP.qtdCircular - total

            print( "\n\nCompra finalizada: valores Atuais MTP: ")
            print(MTP)
            return True
            

        else:
            print("\nerror 2\n")
            print("\nerror 2: Não exite saudo de moedas\n")
            print(MTP)
            return 2

    else: 
        print("\nerror 3: O usuário não tem saldo\n")
        print(type(usuario["BRL"]))
        return 3

def fazerCompraMTP(qtdMoedasMTP):



   




print(getAmountIn(1, MTP.liquidez, MTP.qtdCircular))

server.register_function(consultaPrecoEmBRL)
server.register_function(getAmountIn)
server.register_function(getAmountOut)
server.register_function(fazerCompraMTcomBrl)





server.serve_forever()