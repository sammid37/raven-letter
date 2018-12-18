# IFRN - Campus Caicó
# INFORMÁTICA 2M 2015.1
# 14 de junho de 2016
# RPG - versão 2

# menu do jogo
print("Nome_do_jogo")
def menu():
    print("1 - Iniciar")
    print("2 - Instruções")
    print("3 - Sair")

    # inserindo a opção
    option = int(input("Informe sua opção: "))
    return option

option = menu()

print("Você informou a opção", option)
while option != 3:

    # inciando o jogo
    if (option == 1):
        print("INICIAR")
        print("----------------------------------------------")
        nome_jogador = input("Informe seu nome: ")
        print("----------------------------------------------")
        
        print("23h00") 
        print("""A chuva está acabando, você está quase em casa. Pensamentos invadem sua mente, você ainda continua brigado com
seu melhor amigo de infância. Após muito caminhar, finalmente, está em frente aquela porta vermelha do apartamento. Você abre a porta,
entra, depois a fecha e guarda seu guarda-chuva e seu casaco... Aquele ambiente reconfortante mal iluminado pela luz de um poste
da rua. Ao que parece, você precisa de uma bebida quente. Na cozinha você pega uma caneca para preparar...""")
        
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Opção 1 - Chá ou Café?
        op1 = input("...Chá ou Café? ")
        if (op1 == "Café" or op1 == "café" or op1 == "cafe" or op1 == "Cafe"):
            # se escolher café: você terá mais disposição para permanecer acordado
            print("""Um café será bom para se manter acordado por mais um tempo... O cheiro do café é reconfortante para sua alma. O café
está pronto... 'Que som estranho é este?' Ao retornar para a sala, você ouve um barulho estranho vindo da janela, parecia ser uma batida.
'Poderia ser um galho de uma árvore, o vento ou outra coisa?'""")
            
            # Opção 2 - Abrir ou não a janela
            op2 = input("Deseja ir até a janela? ('S' ou 'N') ")
            if(op2 == "S" or op2 == "s"):
                print("23h15")
                print("""Para entender do que se trata o som, você abre a janela. Um páasaro negro,'parece ser um corvo', fica parado no
parapeito da janela, e aos pés da ave há uma carta de um símbolo familiar. De início, aquele ser te encara com aquele olho perturbador, mas
em seguida, lhe permite pegar aquela carta e ao pegá-la, a criatura sai voando na noite que agora é estrelada. A chuva se foi. A carta está
em mãos, e sua escolha é... """)
                
                # Opção 3 - Abrir ou não o envelope
                op3 = input("...Abrir a carta? ('S' ou 'N')")
                if (op3 == "S" or op3 == "s"):
                    print("""Cuidadosamente, você remove dois papéis de dentro do envelope: o primeiro papel do envelope trata-se de uma
ilustração confusa, cheia de rabiscos, caracteres e formas;  o segundo é a carta que possui palavras cheias de garranchos, quase que escritas
as pressas. E aos poucos você consegue compreender tudo o que está escrito na carta: """)

                    # colocar o texto da carta aqui
                    print("""Texto da carta aqui""")
                    # colocar o texto da carta aqui
                    
                    # Opção 4 - Acreditar ou não nas palavras
                    op4 = input("Deseja realmente acreditar naquelas palavras? ('S' ou 'N')")
                    if (op4 == "S" or op4 == "s"):
                        print("23h31")
                        print("""Poderia crescer coragem em meio ao seu nervosismo? Ao que parece, sim. Em instantes você pega uma mochila e
escolhe conjuntos de obejos que lhe acompanharão na jornada...""")
                        # cada um dos objetos vai influenciar na trama
                        # precisa configurar esses vetores!!
                        # os objetos dos vetores são muito inportantes
                        coj1 = [("caderno"), ("mapa"), ("ilustração"), ("carta")]
                        coj2 = [("celular"), ("dinheiro"), ("ilustração"), ("carta")]
                        
                        # Opção 5 - Escolher o conjunto de objetos
                        print("C1 - ", coj1)
                        print("C2 - ", coj2)
                        op5 = input("... Qual conjunto de itens você escolhe? ('C1' ou 'C2') ") 

                        if (op5 == "C1" or op5 == "c1"):
                            # Conjunto 1 - Este conjunto é para: _________. E não é bom para: __________.
                            print("Você escolheu o conjunto 1")
                            print("...") #continua a história
                        else:
                            # Conjunto 2 - Este conjunto é para: _________. E não é bom para: __________.
                            print("Você escolheu o conjunto 2")
                            print("...") #continua a história
        
                    else:
                        print("23h34")
                        print("""Você logo coloca a carta em cima da mesinha ao seu lado e sobe para tomar um banho quente. O dia foi muito cansativo para
dá atenção a palavras como essas. Ao sair do banho, você se depara com o corvo em sua cama lhe observando atentamente. 'O que ele estaria fazendo aqui? Por onde
entrou?' Você se aproxima e ele voa pelo basculante (janela de vidro) do banheiro. Ao olhar melhor, você percebe que há um bilhete em sua cama escrito 'Ajude-me'.
Você suspeita, veste a roupa e olha a casa toda, nem mais uma pista desse 'joguinho' mental. Lá de fora, ouve-se um estrondo de algo pesado caindo no chão, você...""")
                        
                        # Opção ??? - Ir ou não lá fora
                        opH = input("...Vai até lá olhar ou fica ali mesmo? ('S' ou 'N') ")
                        if opH == "S" or opH == "s":
                            print (""" Você se dirige até a porta dos fundos e abre-a, está escuro, apenas alguns feixes de luz revelam uma silhueta no chão do seu
quintal, parece ser humana, você se aproxima e ver que é um corpo. Quase cai para trás de susto e resolve ligar para a polícia. Ao pegar o celular, você começa a
encaixar tudo, o corvo, o bilhete, a carta, as ilustrações. 'E se tudo for parte disso? Este corpo realmente tem algo a ver com todo o resto?'. Você desiste de ligar
para a polícia e pega um lençol preto para cobrir o corpo. Você pode pegar uma lanterna para ver seu rosto...""")

                            # Opção ??? - Iluminar ou não o rosto da vítima
                            opK = input("Você deseja iluminar o rosto da vítima? ('S' ou 'N') ")
                            if opK == "S" or opK == "s":
                                print(""" Ao pegar a lanterna você levanta o lençol e ilumina o rosto da vítima e nota que é familiar. É um homem.
Mas mesmo assim, é difícil rechonhecê-lo pelo seu estado físico atual. O rosto dele está muito ferido, cheio de cortes e arranhões, sangue por todos os lados e
seus olhos não parecem estar no lugar. Os globos oculares parecem terem sido arrancados. Você se assusta com a visão daquele corpo e resolve...""")
                                
                                # Opção ??? - Levar o corpo para dentro de casa
                                opR = input("O que fará a seguir? Levar o corpo consigo para dentro de casa? ('S' ou 'N') ")
                                if (opR == "S" or opR == "s"):
                                    # escolheu levar o corpo para dentro de casa para examinar
                                    print("...")
                                else:
                                    # escolheu ir para dentro de casa e deixar o corpo lá fora
                                    print("...")
                            else:
                                print("...")
                                
                        else:
                            print("""Mesmo na curiosidade/medo do que poderia estar lá fora, você se mantém e volta para o quarto. Alguns minutos depois
10 mais ou menos) seu celular toca, é a polícia. """)

                            # Opção ??? - Atender ou não o telefonema da polícia
                            opL = input("Você atende? ('S' ou 'N') ")
                            if opL == "S" or opL == "s":
                                print("""- Alô? (Você fala)
- Preciso que saia da casa imediatamente residente""", nome_jogador)
                                print("""Você sai, há duas viaturas de polícia lá fora. Você se pergunta o que está acontecendo e ao acompanhar o policial até o teu
quintal, você se depara com um corpo em uma maca.
- Você está sendo acusado por crime""" , nome_jogador, "Infelizmente teremos que te levar...")
                                
                                # Opção ??? - Entrar ou não no carro da polícia
                                opM = input("...Você entra dentra do carro ou sai correndo? 'Entrar' 'Correr'")
                                if (opM == "Entrar" or opM == "entrar"):
                                    print("...")
                                    #Entra no carro e vai à delegacia (Continuar)
                                else:
                                    print("Estamos trabalhando...")
                                    
                            else:
                                # não atende o telefonema
                                print("...")
                                    
                else:
                    print("Algumas ações aê :v ")
                    
            # caso você não escolher abir a janela
            else:
                print(""" o corvo invade a sala """)


            # agradecimentos
            print("---fim---")
            print("Obrigado por jogar, ", nome_jogador)
            print("Este jogo foi desenvolvido pelos alunos do IFRN - Campus Caicó")
            print("Todos os direitos reservados à: Samantha, Laudeíres, Caio, Yuri e José Douglas")
            
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

        else:
            # se escolher chá: você estará mais sonolento
            # cole aqui os outros códigos
            tea = input("Digite o chá que você quer beber: ")
            print("""
Você toma o chá de""", tea,""" e senta-se na cadeira da sua mesa de jantar. Na cozinha ecoa pequenas batidas vindas da janela da sala, tomar o chá te deixou mais sonolento,
o sono lhe impede de ir descobrir a fonte das batidas, logo você levanta e se dirige ao seu quarto. Chegando lá, sena-se na cama e adormece... """)
            print("23h45")
            print("""
Depois de dormir quase meia hora, você acorda com algo lhe incomodando em cima de sua barriga. Automaticamente você tem um susto. O corvo te encara e você nota que
ele tem um pequeno envelope envolvido em sua pata. Você pega a carta e...""")
            
            # Opção ??? - Abrir ou não o envelope
            opT = input("Abrir ou Não? 'S' ou 'N' ")
            if opT == "S":
                print("...")
                # coloque o texto da carta 
                print("Texto da Carta")
                # coloque o texto da carta
                
            else:
                print("....")
                
            # agradecimentos
            print("---fim---")
            print("Obrigado por jogar, ", nome_jogador)
            print("Este jogo foi desenvolvido pelos alunos do IFRN - Campus Caicó")
            print("Todos os direitos reservados à: Samantha, Laudeíres, Caio, Yuri e José Douglas")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------                 
       
            
    # apresentando as instruções do jogo ao usuário
    elif (option == 2):
        print("INSTRUÇÕES")
        print("Caro jogador(a), este é um RPG(jogo de interpretação de personagens)onde você desempenhará o papel do personagem na realidade em que ele ou ela vive.")
        print("A seguir, segue algumas informações úteis a respeito do jogo, leia e, em seguida, aproveite o nosso jogo!")
        print("----------------------------------------------")
        print("1 - Analise bem sua alternativa, verificando se o que digitou coincide com o que se pede;")
        print("2 - Atenção aos detalhes de cada descrição da história, eles serão importantes;")
        print("3 - Escolha com sabedoria suas ações, cada uma delas terá uma consequência e influenciará o destino do seu personage")
        print("----------------------------------------------")

    # opção inválida
    else:
        print("Opção inválida")

    option = menu()


# FIM DO CÓDIGO!
