'''
aula 1 - dicionario
05/11/24

==== criação ====

D = {"SP": "São Paulo", "MG": "Minas Gerais", "BA": "Bahia"}    # elementos do dicionario sao chamados de 'entradas'
                                                                # cada entrada é formada por dois elementos: chave: valor
in  > D["MG"]
out > 'Minas Gerais'

in  > D["SP"]
out.> 'São Paulo'

==== consultado chaves e valores ====

in  > list(D.keys())
out > ['MG', 'SP', 'BA']

in  > list(D.values())
out > ['Minas Gerais', 'São Paulo', 'Bahia']

in  > list(D.items())
out > [('MG', 'Minas Gerais'), ('SP', 'São Paulo'), ('BA', 'Bahia')]

==== iteração ====

in  > D = {"SP": "São Paulo", "MG": "Minas Gerais", "BA": "Bahia"}
      chaves = list(D.keys())
      for k in chaves:
            print("Chave: ", k, "-", "Valores: ", D[k])

in  > D = {"SP": "São Paulo", "MG": "Minas Gerais", "BA": "Bahia"}
      for v in D.values():
            print(v)
out > São Paulo
      Minas Gerais
      Bahia
      # não podem ser chave: lista, dicionário

==== booleana ====

in  > 'SP' in D
out > True

==== dicionario de dicionario ====

in  > D = {"SP": {"nome": "São Paulo", "Pop": 5654645, "PIB": 545416}}
    > print(D["SP"]["PIB"])
out > 545416

in  > print(D["SP"])
out > {"nome": "São Paulo", "Pop": 5654645, "PIB": 545416}

in  > print(D["SP"]["Pop"])
out > 5654645

in  > popSP = D["SP"]["Pop"]
in  > popSP
out > 5654645
'''

def main():
    paises = {"Japan": "Tokyo", "France": "Paris", "Brazil": "Brasília", "India": "New Delhi", "China": "Beijing", "South Africa": "Pretoria", "Australia": "Canberra", "Russia": "Moscow", "Canada": "Ottawa", "Argentina": "Buenos Aires"}
    paisesCopia = {}
    for chaves in paises.keys():
        paisesCopia[chaves] = paises[chaves]
    print(paises)
    print()
    print(paisesCopia)
main()
