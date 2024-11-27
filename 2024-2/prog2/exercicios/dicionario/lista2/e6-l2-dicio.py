def media(d):
    mediaFinal = {}
    for i in d.keys():
        media = 0
        soma = 0
        for notas in d[i]:
            soma += notas
        media = soma/len(d[i])
        mediaFinal[i] = int(media)
    return mediaFinal

def mediaMaior(d):
    mediaMaior = {}
    for aluno in d:
        if d[aluno] >= 7:
             mediaMaior[aluno] = d[aluno]
    return mediaMaior

def main():
    d = {"pedro": [4, 8, 7], "maria": [8, 10, 9], "carla": [7, 8, 7]}
    mf = media(d)
    mMaior = mediaMaior(mf)
    print(mf)
    print(mMaior)

main()
