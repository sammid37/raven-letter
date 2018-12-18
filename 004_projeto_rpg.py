# IFRN - Campus Caicó
# INFORMÁTICA 2M 2015.1
# 11 de julho de 2016
# RPG - versão 3.1

# menu do jogo
print("RPG_Nome_do_jogo")
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
seu melhor amigo. Após muito caminhar, finalmente, em frente aquela porta vermelha do apartamento. 
Abre-a, entra, depois fecha-a e guarda seus pertences... Aquele ambiente reconfortante, iluminado
apenas pela luz de um poste da rua que atravessa a janela. Neste exato momento você precisa de uma
bebida quente. Na cozinha você escolhe sua caneca preferida para preparar um...""")
        
        # Opção 1 - Chá ou Café?
        op1 = input("...Chá ou Café? ")
        if (op1 == "Café" or op1 == "café" or op1 == "cafe" or op1 == "Cafe"):
            print("23h10")
            print("""Um café será bom para lhe manter acordado por mais um tempo... O cheiro do café é acalma tua alma. Antes que
pudesse dar mais goles na bebida, você ouve algo... Ao retornar para a sala, descobre que o som
pertence a janela, parecia ser uma batida. Poderia ser um galho de uma árvore, o vento ou outra
coisa, mas sua decisão é...""")
            
            # Opção 2 - Ir ou não até janela
            op2 = input("Ir até a janela? ('S' ou 'N') ")
            if(op2 == "S" or op2 == "s"):
                print("23h15")
                print("""Para entender do que se trata o som, você abre a janela. Um pásaro negro, um corvo, fica parado no parapeito
da janela, e aos pés da ave há um envelope. De início, aquele ser te encara com aquele olho perturbador, mas
em seguida, lhe permite pegar aquela correspondência e ao pegá-la, a criatura sai voando na noite que agora é
estrelada. A chuva se foi. O envelope está em mãos, e decide... """)
                
                # Opção 3 - Abrir ou não o envelope
                op3 = input("... Abrir ou ignorar o envelope? ('Abrir' ou 'Ignorar') ")
                if (op3 == "Abrir" or op3 == "abrir"):
                    print("""Cuidadosamente, você remove dois papéis de dentro do envelope: o primeiro papel do envelope trata-se de
uma ilustração confusa, cheia de rabiscos, caracteres e formas;  o segundo é a carta que possui palavras cheias
de garranchos, quase que escritas as pressas. E aos poucos você consegue compreender tudo o que está escrito...""")

                    # colocar o texto da carta aqui
                    # colocar o texto da carta aqui
                    # colocar o texto da carta aqui
                    # colocar o texto da carta aqui
                    # colocar o texto da carta aqui
                    # colocar o texto da carta aqui
                    # colocar o texto da carta aqui
                    # colocar o texto da carta aqui

                    print("""Poderiam ser lorotas? O que poderia ocorrer se tudo fosse ignorado? O que lhe ocorreria se tudo aquilo fosse
real? Que dúvidas cruéis, não é mesmo? Ao serrar os punhos, sua intenção final é...""") 

                    # Opção 4 - Acreditar ou não nas palavras
                    op4 = input("Acreditar ou Rasgar as palavras? ('Acreditar' ou 'Rasgar') ")
                    if (op4 == "Acreditar" or op4 == "acreditar"):
                        print("23h21")
                        print("""Seus punhos se desfazem, você fecha os olhos e respira, solta o ar, vai em direção ao quarto e pega uma
mochila, e logo começa a separar alguns pertences para levar consigo:""")

                        # vetores com objetos armazenados
                        # utilizar cojX.append("______") para adicionar algo nos conjuntos
                        coj1 = [("caderno"), ("???"), ("ilustração"), ("carta")] 
                        coj2 = [("celular"), ("dinheiro"), ("ilustração"), ("carta")]
                        
                        # Opção 5 - Escolher o conjunto de objetos
                        # Precisa de Ajustes: utilizar While para que a pergunta fique se repetindo até que o usuário digite C1 ou C2!!!
                        print("C1 - ", coj1)
                        print("C2 - ", coj2)
                        
                        op5 = input("... E após muito analisar, você decide escolher o conjunto... ('C1' ou 'C2') ") 
                        if (op5 == "C1" or op5 == "c1"):
                            # Conjunto 1 - Vantagens: Seu caderno possui já tem boas informações sobre a cidade e o seu mapa há de ser útilo em algum momento
                            # Conjunto 1 - Desvantagens: EM DESENVOLVIMENTO
                            # Vai ser mais complicado de achar o seu amigo
                            print("Você escolheu o Conjunto 1")
                            print("""Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...""")

                            # Sempre vai aparecer a pergunta: "O que deseja fazer agora?"
                            # O usuário tem apenas 3 opções sobre o que fazer, escolher o caminho já é outra coisa
                            # Precisa de ajustes!
                            def conj_1():
                                print("A - Olhar a ilustração") #A ilustração já é um mapa
                                print("B - Escolher item do inventário")
                                print("C - Desistir")
                                op_conj_1 = input("O que deseja fazer agora? ")
                                return op_conj_1
                            op_conj_1 = conj_1()
                            if op_conj_1 == "A" or op_conj_1 == "a":
                                print("Comando para abrir o arquivo do mapa")
                            elif op_conj_1 == "B" or op_conj_1 == "b":
                                print("Comando para escolher um item do inventário")
                                obj_c1 = input(coj1, "Qual item você deseja utilizar?")
                            else:
                                print("Desistir ainda não é uma opção")
                            print("""...Em Desenvolvimento...""")#isso tem que ficar fora das condicionais

                            
                        elif(op5 == "C2" or op5 == "c2"):
                            # Conjunto 2 - Vantagens: O celular possui bloco de notas, mapa e você pode usar o dinheiro com transporte e qualquer outra coisa
                            # Conjunto 2 - Desvantagem: O celular pode descarregar e não há wi-fi grátis toda hora, você pode perder seu dinheiro
                            # Vai ser mais fácil de encontrar o seu amigo
                            print("C2")
                            print("Você escolheu o Conjunto 2")
                            print("""Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...
Descrição da cidade...Descrição da cidade...""")

                            # Sempre vai aparecer a pergunta: "O que deseja fazer agora?"
                            # O usuário tem apenas 3 opções sobre o que fazer, escolher o caminho já é outra coisa
                            # Precisa de ajustes!
                            def conj_2():
                                print("A - Olhar a ilustração") # a ilustração já é um mapa
                                print("B - Escolher item do inventário")
                                print("C - Desistir")
                                op_conj_2 = input("O que deseja fazer agora? ")
                                return op_conj_2
                            op_conj_2 = conj_2()
                            if op_conj_2 == "A" or op_conj_2 == "a":
                                print("Comando para abrir o arquivo do mapa")
                            elif op_conj_2 == "B" or op_conj_2 == "b":
                                print("Comando para escolher um item do inventário")
                                obj_c2 = input(coj2, "Qual item você deseja utilizar?")
                            else:
                                print("Desistir ainda não é uma opção")
                            print("... Em desenvolvimento ...")
                            
                            
                        else:
                            print("Você tem de escolher um dos conjuntos!")
                       
                    # Não tá nem aí para as palavras da carta
                    else:
                        print("23h20")
                        print("""As palavras daquela carta não lhe importam, você acredita que são mentiras idiotas, já está cheio de
problemas, você guarda o envelope sobre a mesa da sala, fecha a janela
que abriu e logo se despe para um banho quente. Um banho quente é tudo
o que precisa nesse momento.""")
                        print("...")
                        print("23h32")
                        print("""Ao sair do banho e se vestir com um conjunto de roupas, você vê o corvo está sob sua cama, lhe observando.
As janelas estavam fechadas, todas as janelas do seu apartamento na verdade. Quando
você se aproxima da criatura sombria, ela torna-se fumaça e vaga pelas sombras.
Talvez essa deve ter sido a maneira que encontrou para invadir o local.
E agora há um bilhete sobre a cama. E o bilhete apenas diz:

'Seja rápido, ao menos nos ajude' 

Você logo começa a ficar mais preocupado, verifica todos os cômodos mais uma vez,
algo está para ocorrer, as janelas agoras parecem espelhos, refletem olhos que
estão a lhe observar, mas eles logo somem... Mais um bilhete aparece:

'Saia da casa agora!'

... """)
                        
                        # Opção H - Ir ou não lá fora
                        opH = input("Sair ou Ficar?")
                        if opH == "Sair" or opH == "sair":
                            print("23h40")
                            print ("""No momento da saída, foi como se algo estivese puxando-lhe de volta, mas você conseguiu escapar.
Agora você está no térrio, na entrada do prédio do apartamento. E fica lá, sentado em um banco, olhando o jardim,
os grilos pararam de fazer sua música, seu coração bate forte, uma sombra muito maior do que a do corvo atravessa
o salão, mas não te percebe. Vagueia a área e depois desaparece. Os grilos retomam seu canto. Alívio...""")
                            print("24h00")
                            print("""Teu alívio dura pouco tempo, mas você insiste em voltar. Em seu apartamento, tudo encontra-se
em uma perfeita penumbra, tudo está bagunçado, sujo de poeira e sabe-se lá mais o quê, você não toca em nada, exceto
em uma mochila com alguns pertences que levrá consigo... Agora você pretende partir e ajudar seja lá quem for. """)
                            # A partir de agora, torna-se claro que você deseja seguir o que a carta diz, está claro de que você precisa tomar uma providência
                            
                            # vetores com objetos armazenados
                            # utilizar cojX.append("______") para adicionar algo nos conjuntos
                            coj3 = [("ob1"), ("ob2"), ("ilustração"), ("carta"), ("ob3"), ("ob4")]
                            print("...Em Desenvolvimento")
                            

                        else:
                            # Op 4.1 - Ir ou não lá fora
                            print("23h45")
                            print("""Não importa o que está para acontecer, você ficará em tua casa, segurando o que restou de seu
café, as janelas sacodem. O corvo grita do lado de fora, está preocupado contigo. E logo você é envolto nas sombras.
Qualquer som agora ecoa. Frente de ti um homem, parece já ter seus 40 anos, é alto e esguio, usa uma máscara de e uma
cartola. Agora com a mão direita remove a cartola e curva-se, continua calado. Agora volta a lhe encarar, e com a mão
esquerda estrala os dedos e magicamente uma silhueta amarrada e amordaçada aparecem em uma cadeira de madeira. O corpo
daquela pessoa permanece imóvel, incosiente, mas você a reconhece. Agora seu coração bate mais forte, é o medo a lhe
preencher com a esperança de que aquela pessoa ainda possa ser salva.""")
                            print("... Em desenvolvimento ...")

                
                else:
                    # Op3 - Abrir ou não o envelope
                    # O que ocorre caso não abrir o envelope?
                    # Vai acontecer umas coisas bem doida e você morre :v
                    print("Você decidiu não abrir a carta")
                    print("... Algumas ações ...")
                    print("... Algumas ações ...")
                    print("... Algumas ações ...")
                    break # sempre que usar break, significa que o personagem morre
                    
            else:
                # op2 - Abrir ou Não a Janela
                # Não importa a opção, quando nesse else, significa que o jogador vai ignorar a carta!!
                print("""Você escolheu não ir até a janela e não a abriu. O corvo invade o local...""")
                print("... Em desenvolvimento ...")

                    
                          
            # agradecimentos
            print("---fim---")
            print("Obrigado por jogar, ", nome_jogador)
            print("Este jogo foi desenvolvido pelos alunos do IFRN - Campus Caicó")
            print("Breve em uma versão com gráficos")
            print("Todos os direitos reservados à: Samantha, Laudeíres, Caio, Yuri e José Douglas")

#           ---------------------------------------------------------------------------------------            
                          
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
        # ações alternativas ????
        # Acabar com o jogo agora ????
        else:
            print("Escolha inválida, tente novamente")
            option = menu()

            
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
