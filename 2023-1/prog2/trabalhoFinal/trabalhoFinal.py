'''
entrada:
 {'matricula do aluno' : (nome,(2023,1),(p1, nt, nM, bonus), faltas)}

formato de saida:
    2023/1 BSI0381767 Ana Ferreira - 100 (29+40+29 +2P = 100)
    2023/1 BSI0791174 Jo~ao Jesus - 100 (28+42+30 +2P = 102)
    2023/1 BSI0473077 Maria Albuquerque - 100 (27+42+30 +1E +2P = 102)
    2023/1 BSI1858432 Afonso Coimbra - 98 (29+42+26 +1E = 98)
    2023/1 BSI0878237 Ana Jesus - 98 (30+37+29 +2E = 98)
    2023/1 BSI1718106 Beatriz Gomes - 87 (30+33+23 +1E = 87)
'''
import pickle

def ordenacao(pauta):
    ordemSemestre = []
    semestre = 1
    ano = 0
    for i in range(len(pauta)):
        print(i)
        if pauta[i][1][0] > ano:
            ano = anos
            if pauta[i][1][1] > semestre:
                semestre = sems
            return ordemSemestre.append(ano, semestre)
        else:
            if pauta[i][1][1] > semestre:
                semestre = sems
            return ordemSemestre.append(ano, semestre)

def mat(pauta):
    matricula= []
    for mat in pauta: 
        matricula.append(mat)
    return matricula

def main(args):
    # interpretacao do arquivo binario
    with open('entrada10.bin', 'rb') as matriculas:
        m = pickle.load(matriculas)
    # print(m)

    # teste de saída das matrículas
    print('matriculas: ', mat(m))
    print('teste de ordenacao\n', ordenacao(m))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
