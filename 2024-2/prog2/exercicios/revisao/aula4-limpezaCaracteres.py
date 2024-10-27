# lista de revisão - prog2
# https://docs.python.org/3/tutorial/datastructures.html

def trimPal(palavra):
  alfaNum = "abcdefghijklmnopqrstuvxzç0123456789-"
  palavraNova = ""
  for i in alfaNum:
    x = 0
    for j in palavra:
      if i == j:
        print(j)
        palavraNova = j
        return palavraNova
      y = palavraNova
      print(y)

  # for i in range(len(palavra)):           # percorre os caracteres da palavra
  #   print(i)
  #   for j in range(len(alfaNum)):               # percorre os caracteres do alfabeto
  #     if alfaNum[j] == palavra[i]:              # verifica se as posições são iguais
  #       print(alfaNum[j])
  #       palavraNova = palavraNova + alfaNum[j]  # armazena caracteres encontrados
  #     return palavraNova                        # retorna resultado

  # print(palavraNova)

def main():
  # lixo = "~^/?°ºª][}{-_!@#$%¨&*()|+='""'"
  palavra = input("Texto a ser limpo: ")
  print("palavra original: ", palavra, "palavra com trim: ", trimPal(palavra))

main()