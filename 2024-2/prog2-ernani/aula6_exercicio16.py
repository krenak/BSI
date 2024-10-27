'''
https://wiki.python.org.br/ExerciciosListas
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
'''

vendaBruta = 0
def qtdBonus(salario):
    comissoes = [[200,299], [300,399], [400,499], [500,599], [600,699], [700,799], [800,899], [900,999], [1000,9999]] # valores de cada comissao
    pos = [['a. ', 0],['b. ', 0],['c. ', 0],['d. ', 0],['e. ', 0],['f. ', 0],['g. ', 0],['h. ', 0],['i. ', 0]] # posicoes de bonus - 'a' ate 'i'
    cont = 0 # contagem para acesso as posicoes de 'pos'
    for i in comissoes:
        if salario > i[0] and salario <= i[1]:
            cont = cont + 1
            pos.insert(0, cont)
            return pos
        

def main():
    qtdVendedores = []
    vendaBruta = float(input('Valor da venda bruta na semana: ')) # valor vendido
    while vendaBruta != 0:
        bonus = 200 + (vendaBruta * 0.09)
        qtdVendedores = qtdBonus(bonus)
        print("%4.2f" % bonus)
        vendaBruta = float(input('Valor da venda bruta na semana: ')) # valor vendido
    print("A quantidade de vendedores que receberam bonus em cada categoria foi:", qtdVendedores)

main()
