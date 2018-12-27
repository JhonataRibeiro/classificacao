from sklearn.naive_bayes import MultinomialNB

#nome [gordinho, perna_curta, late]
porco1 = [1, 1, 0]
porco2 = [0, 1, 0]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 1, 1]
cachorro3 = [0, 0, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]

animalDesconhecido = [0, 0, 0]
animalDesconhecido2 = [1, 1, 0]
animalDesconhecido3 = [0, 1, 0]
animalDesconhecido4 = [0, 0, 1]

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)
print(modelo.predict(
    [animalDesconhecido, animalDesconhecido2, animalDesconhecido3, animalDesconhecido4]))
