# IFRN - Campus Caicó
# INFORMÁTICA 2M 2015.1
# 20 de junho de 2016
# RPG - versão 3.1

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
                 seu melhor amigo de infância. Após muito caminhar, finalmente, em frente aquela porta vermelha do apartamento. 
                 Você abre a porta, entra, depois a fecha e guarda seu guarda-chuva e seu casaco... Aquele ambiente reconfortante 
                 mal iluminado pela luz de um poste da rua. Ao que parece, você precisa de uma bebida quente. Na cozinha você pega 
                 uma caneca para preparar um...""")
        
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------

        # Opção 1 - Chá ou Café?
        op1 = input("...Chá ou Café? ")
        if (op1 == "Café" or op1 == "café" or op1 == "cafe" or op1 == "Cafe"):
            print("23h10")
            print("""Um café será bom para se manter acordado por mais um tempo... O cheiro do café é reconfortante para sua alma. 
O café está pronto... 'Que som estranho é este?' Ao retornar para a sala, você ouve um barulho estranho vindo da janela, 
parecia ser uma batida. 'Poderia ser um galho de uma árvore, o vento ou outra coisa?'""")
            
            # Opção 2 - Abrir ou não a janela
            op2 = input("Deseja ir até a janela? ('S' ou 'N') ")
            if(op2 == "S" or op2 == "s"):
                print("23h15")
                print("""Para entender do que se trata o som, você abre a janela. Um pásaro negro,'parece ser um corvo', fica parado no
parapeito da janela, e aos pés da ave há uma carta com um símbolo familiar. De início, aquele ser te encara com aquele olho perturbador, 
mas em seguida, lhe permite pegar aquela carta e ao pegá-la, a criatura sai voando na noite que agora é estrelada. A chuva se foi. A carta 
está em mãos, e sua escolha é... """)
                
                # Opção 3 - Abrir ou não o envelope
                op3 = input("...Abrir ou ignorar a carta? ('Abrir' ou 'Ignorar') ")
                if (op3 == "Abrir" or op3 == "abrir"):
                    print("""Cuidadosamente, você remove dois papéis de dentro do envelope: o primeiro papel do envelope trata-se de uma
ilustração confusa, cheia de rabiscos, caracteres e formas;  o segundo é a carta que possui palavras cheias de garranchos, quase que escritas
as pressas. E aos poucos você consegue compreender tudo o que está escrito na carta: """)

                    # colocar o texto da carta aqui
                    print("""Texto da carta aqui""")
                    # colocar o texto da carta aqui
                    
                    # Opção 4 - Acreditar ou não nas palavras
                    op4 = input("Deseja realmente acreditar naquelas palavras? ('S' ou 'N')")
                    if (op4 == "S" or op4 == "s"):
                        print("23h21")
                        print("""Poderia crescer coragem em meio ao seu nervosismo? Ao que parece, sim. Em instantes você pega uma mochila e
escolhe conjuntos de obejos que lhe acompanharão na jornada...""")

                        # vetores com objetos armazenados
                        coj1 = [("caderno"), ("mapa"), ("ilustração"), ("carta")]
                        coj2 = [("celular"), ("dinheiro"), ("ilustração"), ("carta")]
                        
                        # Opção 5 - Escolher o conjunto de objetos
                        print("C1 - ", coj1)
                        print("C2 - ", coj2)
                        op5 = input("... Qual conjunto de itens você escolhe? ('C1' ou 'C2') ") 

                        if (op5 == "C1" or op5 == "c1"):
                            # Conjunto 1 - Este conjunto é para: _________. E não é bom para: __________.
                            print("Você escolheu o conjunto 1")
                            print("... Em desenvolvimento ... ") 
                        else:
                            # Conjunto 2 - Este conjunto é para: _________. E não é bom para: __________.
                            print("Você escolheu o conjunto 2")
                            print("... Em desenvolvimento ...") 
        
                    else:
                        print("23h20")
                        print("""As palavras daquela carta não lhe importam, 'que tolice'. Você deixa a carta sobre a mesa da sala e segue 
ao banheiro para um banho quente. O dia foi muito cansativo para dá atenção a meras palavras...""")
                        print("23h32")
                        print(""" 'Nada melhor do que um banho quente...' Ao sair do banho, você se sente observado, é o mesmo corvo de olhar
pertubador sob sua cama, aqueles mesmos olhos sombrios a lhe perturbar.
'O que ele estaria fazendo aqui? Por onde ele entrou?' 
Ao se aproximar na ave negra, ele se some no meio das sombras, por momento, isto soa inacreditável, é como se ele 
virasse poeira... Há um bilhete sobre sua cama, fora deixado pelo corvo, está escrito: 'ajude-me'... 'Isto soa suspeito...' 
Ao se vestir, decide verificar os outros cômodos do apartamento, até que você houve um estranho som na rua e você...""")
                        
                        # Opção ??? - Ir ou não lá fora
                        opH = input("...Decide ir lá fora ou permanecer no apartamento? ('Sair' ou 'Ficar)'")
                        if opH == "Sair" or opH == "sair":
                            print("23h37")
                            print ("""As luzes dos postes lhe permite distinguir a silhueta caída no chão, é humana. Suas pernas ficam
bambas ao notar as pequenas manchas de sangue sobre a calçada. Antes de fazer qualquer coisa, você percebe 
que tudo começa a ficar claro: o corvo, o envelope, o bilhete...""")
                            print("... Em desenvolvimento ...")

                        else:
                            print("""A curiosidade está a te matar, 'O que pode haver lá fora?', agora que deita-se na cama, olhando
para o teto, seu celular vibra sobre a cômodo, é um telefonema. Alguém da polícia está a te ligar...""")

                            # Opção ??? - Atender ou não o telefonema da polícia
                            opL = input("Atender ou ignorar a chamada? ('Atender' ou 'Ignorar') ")
                            if opL == "Atender" or opL == "atender":
                                print("""- Alô?
                                         - Preciso que se retire da residência, imediatamente""", nome_jogador)
                                print("23h42")
                                print("""Ao sair, há duas viaturas de polícia lá fora. 'O que pode estar ocorrendo?'
Um policial te guia até a maca onde o corpo caído se encontra e lhe diz:
- Você é um dos suspeitos do crime""" , nome_jogador, """Te levaremos para a delagacia para seguir
com interregações. """)
                                
                                # Opção ??? - Entrar ou não no carro da polícia
                                opM = input("...Você entra dentra do carro ou sai correndo? ('Entrar' ou 'Correr')")
                                if (opM == "Entrar" or opM == "entrar"):
                                    print("... Em desenvolvimento ...")
                                else:
                                    print("... Em desenvolvimento ...")
                                    
                            else:
                                # ignorar o telefonema
                                print("... Em desenvolvimento ...")
                                    
                else:
                    print("Você decidiu não abrir a carta")
                    print("... Em desenvolvimento ...")
                    
            else:
                print("""Você escolheu não ir até a janela e não a abriu. O corvo invade o local...""")
                print("... Em desenvolvimento ...")


            # agradecimentos
            print("---fim---")
            print("Obrigado por jogar, ", nome_jogador)
            print("Este jogo foi desenvolvido pelos alunos do IFRN - Campus Caicó")
            print("Todos os direitos reservados à: Samantha, Laudeíres, Caio, Yuri e José Douglas")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif(op1 == "Chá" or op1 == "chá" or op1 == "cha" or op1 == "Cha") :
            
            tea = input("de (informe o nome do chá, exemplo: hibisco)... ")
            print("23h10")
            print("""Confortavelmente, você senta-se a mesa e relaxa com seu chá de""", tea , """até que pequenas batidas ecoam. O som parece 
pertencer às janela da sala. 'Deve ser o vento ou as árvores da rua', o sono lhe ataca, deitar-se na cama e dormir parece ser uma
ótima ideia. Um último gole do chá. A caneca vazia está na cômoda e você encontra-se em um ambiente tão reconfortante... Logo, os
sono é quem te comanda...""")
            print("...")
            print("23h40")
            print("""Grandes olhos negros estão a te observar. Com um sobresalto, você sai da cama e o corvo permanecer a gritar e bica um envelope
que está sobre a cama. Poderia esta pequena criatura está te pedindo para abrir o envelope? O que deseja fazer? """)
            
            # Opção ??? - Abrir ou não o envelope
            opT = input("Deseja abrir o envelope? ('S' ou 'N')")
            if opT == "S":
                print("...Em desenvolvimento...")
                
                # coloque o texto da carta 
                print("Texto da Carta")
                # coloque o texto da carta
                
            else:
                print("...Em desenvolvimento...")
                
            # agradecimentos
            print("---fim---")
            print("Obrigado por jogar, ", nome_jogador)
            print("Este jogo foi desenvolvido pelos alunos do IFRN - Campus Caicó")
            print("Todos os direitos reservados à: Samantha, Laudeíres, Caio, Yuri e José Douglas")
            
        # caso o usuário não digitar nem café nem chá
        else:
            print("Escolha inválida, tente novamente")
            option = menu()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------                 
       
            
    # apresentando as instruções do jogo ao usuário
    elif (option == 2):
        print("INSTRUÇÕES")
        print("Caro jogador(a), este é um RPG(jogo de interpretação de personagens)onde você desempenhará o papel do personagem na realidade em que ele vive.")
        print("A seguir, segue algumas informações úteis a respeito do jogo, leia e, em seguida, aproveite o nosso jogo!")
        print("----------------------------------------------")
        print("1 - Analise bem sua alternativa, verificando se o que digitou coincide com o que se pede;")
        print("2 - Atenção aos detalhes da história, eles são importantes;")
        print("3 - Escolha com sabedoria suas ações, talvez, qualquer coisa posso mudar seu destino no jogo.")
        print("----------------------------------------------")

    # opção inválida
    else:
        print("Opção inválida")
        
    option = menu()


# FIM DO CÓDIGO!
