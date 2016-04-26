from processor import ProcessadorDeSentimentos as pds

afirmNegativas = [('A Dilma é uma vadia', 'negativo'), ('A Dilma é uma filha da puta', 'negativo'), ('A Dilma é uma corna', 'negativo'), ('A Dilma é uma corrupta', 'negativo'), ('A Dilma é uma petralha', 'negativo'),('O impeachment é golpe', 'negativo'),('O impeachment é uma coisa linda', 'negativo'),('O impeachment vai salvar o Brasil', 'negativo'),('O impeachment melhorará o Brasil', 'negativo'),('O impeachment vai fazer a gente crescer', 'negativo'),('O Lula é um corrupto', 'negativo'),('O Lula é maldito', 'negativo'),('O Lula é sem vergonha', 'negativo'),('O Lula roubou para cacete', 'negativo'),('O Lula não tem um dedo', 'negativo'),('O Lula é um infeliz', 'negativo'),('O PT é corrupto', 'negativo'),('O PT é ladrão', 'negativo'),('O PT é problemático', 'negativo'),('O PT é cheio de problemas', 'negativo'),('O PT é zuado', 'negativo')]

afirmPositivas = [('A Dilma é uma boa presidenta', 'positiva'),('A Dilma não é ladra', 'positiva'),('A Dilma não cometeu nenhum crime', 'positiva'),('A Dilma não é corrupta', 'positiva'),('O Lula salvou os pobres', 'positiva'),('O governo ajudou aos pobres', 'positiva'),('O Lula não é corrupto', 'positiva'),('O Lula ajudou o Brasil', 'positiva'),('O brasil teve ajuda do PT nos últimos anos', 'positiva'),('A TV manipula as pessoas contra o governo', 'positiva'),('o Governo ajudou a todos', 'positiva'),('O governo não cometeu nenhum crime', 'positiva'),('Os criminosos não estão no governo', 'positiva'),('Como podem acusar a dilma sem nem terem provas?', 'positiva'),('O PT criou o bolsa família, deixe eles no poder', 'positiva'),('Sou governista e ponto, sou feliz assim', 'positiva'),('O governo não é corrupto', 'positiva'),('Não temos nenhuma prova para mostrar que nossa presidenta cometeu crime', 'positiva'),('O esquema da Petrobrás é uma farça', 'positiva')]

amostras = pds.tokenize(afirmNegativas + afirmPositivas)

#print(str(amostras))

processor = pds(amostras)

print(processor.classifica("o Brasil é bom"))
