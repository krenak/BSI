'''
'''

vendaBruta = 0

def main():
  vendaBruta = float(input('Valor da venda bruta na semana: ')) # valor vendido
  comissoes = [[200,299], [300,399], [400,499], [500,599], [600,699], [700,799], [800,899], [900,999], 1000] # valores de cada comissao
  pos = [0,0,0,0,0,0,0,0,0] # posicoes de bonus - 'a' ate 'i'
  bonus = 200 + (vendaBruta * 0.09)
  # for i in comissoes:
      
  print("%4.2f" % bonus)
main()