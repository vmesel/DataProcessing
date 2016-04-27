from processor import ProcessadorDeSentimentos as pds

afirmNegativas = [('Vivemos em um país lixo!', "negativo"),('O país é horrível!', "negativo"),('A Dilma é uma vadia', 'negativo'), ('A Dilma é uma filha da puta', 'negativo'), ('A Dilma é uma corna', 'negativo'), ('A Dilma é uma corrupta', 'negativo'), ('A Dilma é uma petralha', 'negativo'),('O impeachment é uma coisa linda', 'negativo'),('O impeachment vai salvar a nós', 'negativo'),
('O impeachment melhorará a situação', 'negativo'),('O impeachment vai fazer a gente crescer', 'negativo'),('O Lula é um corrupto', 'negativo'),('O Lula é maldito', 'negativo'),('O Lula é sem vergonha', 'negativo'),('O Lula roubou para cacete', 'negativo'),('O Lula não tem um dedo', 'negativo'),('O Lula é um infeliz', 'negativo'),('O PT é corrupto', 'negativo'),('O juiz Sergio Moro está complicando as situações', 'negativo'),
('O PT é ladrão', 'negativo'),('O PT é problemático', 'negativo'),('O PT é cheio de problemas', 'negativo'),('O PT é zuado', 'negativo'),('A crise é por causa do PT', 'negativo'),('A crise é uma coisa que ninguém entende', 'negativo'),('Os comunistas estão chegando no Brasil', 'negativo'),('Os cubanos estão chegando no Brasil', 'negativo'),('Os coxinhas vão derrubar os comunistas', 'negativo')]


afirmPositivas = [('Impeachment não vai tirar o Cunha e nenhum deputado!', "positiva"),('Impeachment não levantará a econômia!', "positiva"),('Impeachment não ajudará a gente!', "positiva"),('Vivemos em um país ótimo!', "positiva"),('O país é bom!', "positiva"),('A Dilma é uma boa presidenta', 'positiva'),('A Dilma não é ladra', 'positiva'),('A Dilma não cometeu nenhum crime', 'positiva'),('A Dilma não é corrupta', 'positiva'),
('O Lula salvou os pobres', 'positiva'),('O governo ajudou aos pobres', 'positiva'),('O Lula não é corrupto', 'positiva'),('O Lula ajudou a todos', 'positiva'),('Tivemos ajuda do PT nos últimos anos', 'positiva'),('A TV manipula as pessoas contra o governo', 'positiva'),('o Governo ajudou a todos', 'positiva'),('O governo não cometeu nenhum crime', 'positiva'),('Os criminosos não estão no governo', 'positiva'),('Como podem acusar a dilma sem nem terem provas?', 'positiva'),
('O PT criou o bolsa família, deixe eles no poder', 'positiva'),('Sou governista e ponto, sou feliz assim', 'positiva'),('O governo não é corrupto', 'positiva'),('Não temos nenhuma prova para mostrar que nossa presidenta cometeu crime', 'positiva'),('O esquema da Petrobrás é uma farça', 'positiva'),('O impeachment é golpe', 'positiva'),
('A crise foi criada pela mídia', 'positiva'), ('A mídia influência a cabeça', 'positiva')]

amostras = pds.tokenize(afirmNegativas + afirmPositivas)

processor = pds(amostras)

valorPositivas = 0
Positivas = []
valorNegativas = 0
Negativas = []

print("""
                       _ _             _____            _   _                      _        _ 
     /\               | (_)           / ____|          | | (_)                    | |      | |
    /  \   _ __   __ _| |_ ___  ___  | (___   ___ _ __ | |_ _ _ __ ___   ___ _ __ | |_ __ _| |
   / /\ \ | '_ \ / _` | | / __|/ _ \  \___ \ / _ \ '_ \| __| | '_ ` _ \ / _ \ '_ \| __/ _` | |
  / ____ \| | | | (_| | | \__ \  __/  ____) |  __/ | | | |_| | | | | | |  __/ | | | || (_| | |
 /_/    \_\_| |_|\__,_|_|_|___/\___| |_____/ \___|_| |_|\__|_|_| |_| |_|\___|_| |_|\__\__,_|_|
                                                                                              
                                                                                              
Script criado por: Vinicius Mesel, Renan Palmeira e Eduardo Mendes
Disponível em: http://github.com/vmesel/
""")

print("Iniciando o script, Aguarde os resultados...\n")

for linha in open("dbs/saida1-sl.txt"):
    if processor.classifica(linha) is "positiva":
        valorPositivas = valorPositivas + 1
        Positivas.append(linha)
    else:
        valorNegativas = valorNegativas + 1
        Negativas.append(linha)


print("Análise Concluída:\n\nNeste arquivo existem {} tweets contra o governo e {} tweets pró-governo!\n\n\n".format(valorNegativas,valorPositivas))
