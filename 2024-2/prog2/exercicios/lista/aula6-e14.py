def main():
  quiz = ['Telefonou para a vítima?', 'Esteve no local do crime?', 'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']
  
  veredito = ['Inocente', 'Inocente', 'Suspeito', 'Cúmplice', 'Assassino']
  cTotal = 0
  for i in quiz:
    count = 0 # contados de respostas
    resp = input(i + ' ')
    if resp in ['sim', 'Sim', 's']:
      count = count + 1
    cTotal = cTotal + count
  print('Veredito: ' + veredito[cTotal])
  
main()