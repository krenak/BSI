'''
desafio proposto

interpretar dados da mega sena e identificar quais os numeros
mais frequentes nos sorteios vencedores

base de dados utilizada:
download de resultados
https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx
'''
import loadFile as lf
import ordenaMatriz as om
import imprimeTela as it

def main():
    #sorteios = lf.carregaArquivo("megaTeste.txt")
    sorteios = lf.carregaArquivo("mega.txt")
    sorteioOrdenado = om.ordenaMatriz(sorteios)

    #it.imprimeTela(sorteios)

main()

