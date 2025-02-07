import tadest as te
import tadponto as tp

def main():
	pontos = tp.loadFile("bdveiculos.txt")
	empresas = te.loadFile("bdestacionamentos.txt")
	for emp in empresas:
		print("Empresa: {:s}".format(te.get_empresa(emp)))
		print("Email: {:s}".format(te.get_email(emp)))
		print("Área: {:.2f} m2".format(te.area(emp)))
		print("Perímetro: {:.2f} m".format(te.perimetro(emp)))

		#------ verficando quantidade de carros -----#
		num = 0
		for carros in pontos:
			vaga = te.pertence(emp, carros)
			if vaga:
				num += 1
			te.set_num_carros(emp, num) 
			vaga = False
		#------ fim verifica carros -----#
		# for vagasOcupadas in emp["carros"]:
		# 	print(vagasOcupadas)
		print("Quantidade de carros: {:d} unidades".format(te.get_num_carros(emp)))
		print()


main()