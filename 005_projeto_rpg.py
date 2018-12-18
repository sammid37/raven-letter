# IFRN - Campus Caicó
# INFORMÁTICA 2M 2015.1
# 01 de setembro de 2016
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

        print(" 4 de junho de 2001 ")
        print("23h00") 
        print("""
A chuva está acabando, você está quase em casa. Pensamentos invadem sua mente, você ainda continua
brigado com seu melhor amigo. Após muito caminhar, finalmente, em frente aquela porta vermelha do
apartamento. Abre-a, entra, depois fecha-a e guarda seus pertences... Aquele ambiente reconfortante,
iluminado apenas pela luz de um poste da rua que atravessa a janela. Neste exato momento você precisa
de uma bebida quente. Na cozinha você escolhe sua caneca preferida para preparar um...""")
        
        # Opção 1 - Chá ou Café?
        op1 = input("...Chá ou Café? ")
        if (op1.upper()== "CAFÉ" or op1.upper() == "CAFE"):
            print("23h10")
            print("""
Um café será bom para lhe manter acordado por mais um tempo... O cheiro da bebida acalma tua alma.
Antes que pudesse dar mais uns goles na bebida, você ouve algo... Ao retornar para a sala, descobre
que o som pertence a janela, parecia ser uma batida. Poderia ser um galho de uma árvore, o vento ou
outra coisa...""")
            
            # Opção 2 - Ir ou não até janela
            op2 = input("...deseja ir até a janela? ('SIM' ou 'NÃO') ")
            if(op2.upper() == "S" or op2.upper() == "SIM"):
                print("23h15")
                print("""
Você ficou curioso e então decide descobrir a quem ou o quê som pertence. Ao abrí a janela, um pásaro
negro(parece um corvo) fica parado no parapeito, e aos pés da ave há um envelope. A criatura te encara
com aquela órbita negra. O corvo então lhe entrega a correspondência, permitindo ler o que há. Ele se
foi, voando na noite que agora é estrelada. A chuva se foi. O envelope está em mãos, e sua escolha é... """)
                
                # Opção 3 - Ler ou não a carta
                op3 = input("... Ler ou ignorar o envelope? ('LER' ou 'IGNORAR') ")
                if (op3.upper() == "LER" or op3.upper() == "L"):
                    print("23h20")
                    print("""
Cuidadosamente, você remove dois anexos do envelope: o primeiro trata-se de uma ilustração confusa, cheia de
rabiscos, caracteres e formas, parece um enigma, um mapa;  o segundo é a própria carta, ela possui garranchos
em toda sua estrutura, esse alguém escreveu as pressas ou então não sabia bem como segurar uma caneta. E aos
poucos você consegue compreender tudo o que há escrito... Todavia poderiam ser lorotas. O que poderia ocorrer
se tudo fosse ignorado? O que lhe ocorreria se tudo aquilo fosse real? Que dúvidas cruéis, não é mesmo? """) 

                    # Opção 4 - Acreditar ou Ignorar as palavras
                    op4 = input("Acreditar ou Ignorar as palavras? ('ACREDITAR' ou 'IGNORAR') ")
                    if (op4.upper() == "ACREDITAR" or op4.upper() == "A"):
                        print("23h21")
                        print("""
Que mal faria em acreditar? Não há nada de interessante a se fazer em casa, e ainda tem a liberdade de ir aonde
bem entender. Você está um pouco ansioso quanto a tudo isso, mas mesmo assim decide seguir sua ideia. E em direção
ao seu quarto você segue. Pega uma mochila grande o bastante para colocar alguns pertences e então...""")
                        # INÍCIO DA ATIVIDADE DE YURI
                        cojunto1 = [("caderno"), ("???"), ("ilustração"), ("carta")]
                        print("...Descrição da cidade lalalalala...")
                        print("Em desenvolvimento")
                        # FIM DA ATIVIDADE DE YURI
                        
                    else:
                    # Opção 4 - Acreditar ou Ignorar as palavras
                        print("23h20")
                        print("""
As palavras daquela carta não lhe importam, devem ser mentiras idiotas, e você já se vê cheio de problemas.
O envelope está sobre a mesa da sala, as janelas que estavam abertas estão fechadas, tudo está quieto como
desejado, e seu café agora está frio demais para desgustar. É hora de um banho bem quente antes de tomar outra
boa decisão.""")
                        print("...")
                        print("23h32")
                        print("""
Ao sair do banho e se vestir com uma roupa confortável, nota que algo está sob sua cama, lhe observando. É o
corvo novamente! Como ele poderia ter entrado? Ao se aproximar da criatura sombria, ela torna-se fumaça e vaga
pelas sombras. Talvez essa deve ter sido a maneira que encontrou para invadir o local. E agora há um bilhete
sobre a cama. E o bilhete apenas diz:

'Seja rápido, ao menos nos ajude' 

Preocupação... O que poderia ser tudo isso? E então você verifica todos os cômodos mais uma vez, algo está vai
ocorrer, as janelas agoras parecem espelhos, refletindo seu corpo pálido e do outro lado daquela superfície
refletora há algo semelhante a olhos, lhe observam, depois desaprecem. Mais um bilhete se repete:

'Saia da casa agora!'

... """)
                        
                        # Opção 5 - Ir ou não lá fora
                        op5 = input("Sair ou Ficar?")
                        if (op5.upper() == "SAIR" or op5.upper() == "S"):
                            print("23h40")
                            print ("""
No momento da saída, foi como se algo estivese puxando-lhe de volta, mas você conseguiu escapar. Agora você está no
térrio, na entrada do prédio do apartamento. E fica lá, sentado em um banco, olhando o jardim, os grilos pararam de
fazer sua música, seu coração bate forte, uma sombra muito maior do que a do corvo atravessa o salão, mas não te
percebe. Vagueia a área e depois desaparece. Os grilos retomam seu canto. Alívio...""")
                            print("24h01")
                            print("""
Teu alívio dura pouco tempo, mas você insiste em voltar. Em seu apartamento, tudo encontra-se em uma perfeita penumbra,
tudo está bagunçado, sujo de poeira e sabe-se lá mais o quê, você não toca em nada, exceto em uma mochila com alguns
pertences que levrá consigo... Agora você pretende partir e ajudar seja lá quem for. """)
                            
                            cojunto2 = [("ob1"), ("ob2"), ("ilustração"), ("carta"), ("ob3"), ("ob4")]
                            print(" 05 de junho de 2001 ")
                            print("24h12")
                            print("...Em Desenvolvimento")
                            
                        else:
                            # OpH - Ir ou não lá fora
                            print("23h45")
                            print("""
Não importa o que está para acontecer, você ficará em tua casa, segurando o que restou de seu café, as janelas sacodem.
O corvo grita do lado de fora, está preocupado contigo. E logo você é envolto nas sombras. Qualquer som agora ecoa.
Frente de ti um homem, parece já ter seus 40 anos, é alto e esguio, usa uma máscara de e uma cartola. Agora com a mão
direita remove a cartola e curva-se, continua calado. Agora volta a lhe encarar, e com a mão esquerda estrala os dedos
e magicamente uma silhueta amarrada e amordaçada aparecem em uma cadeira de madeira. O corpo daquela pessoa permanece
imóvel, inconsiente, mas você a reconhece. Agora seu coração bate mais forte, é o medo a lhe preencher com a esperança
de que aquela pessoa ainda possa ser salva.""")
                            print("""
Onde poderia estar o seu lar se as sombras a levaram? Há luz no local, tão fraca, eram velas. O homem permanecia imóvel,
ele apenas guardava por uma reação, um passo, uma setença, algo que você não poderia fazer naquele momento. Aquele que
estava na cadeira foi jogado para perto de você, ambos estavam sobre uma circunferência feita de pequenos restos de cristal.
Estão presos até segunda ordem. Um som de vidro quebrado ecoou naquele ambiente tão vazio, parecia uma janela sendo quebrada,
e com um rastro brilhante, foi-se reveledo o autor de tal ato. Era o corvo novamente. O mesmo começou a bicar o mal feitor de
toda essa barbaridade, deixando-o cego. A ave cortou o céu, levando embora todo aquele cristal, permitindo-lhe sair de lá com
seu amigo. E por fim, entregou-lhe o que parecia ser fogo, ele quer que a use.""")
                            opI = input("Deseja realmente acender uma chama? ('S' ou 'N')")
                            if (opI.upper() == "SIM" or opI.upper() == "S"):
                                print("""
Ao ascender a chama daquela pequena esfera, o corvo move sua cabeça para a direção que você deve jogar, em direção ao homem cego
e atordoado pela escuridão. Ao jogar a chama, o fogo se espalha, você tenta tirar o corvo de lá, mas ele insiste em se desfazer
nas chamas junto ao cego. Por qual razão ele havaria de fazer isto?""")
                                print("5 de junho de 2001")
                                print("00h00")
                                print("(...)")
                                print("5 de junho de 2001")
                                print("08h34")
                                print("""
NAquela madrugada, os bombeiros compareceram ao local, apagaram no incêncio no qual não havia nenhum vestígio de um corpo queimado.
O corvo e o homem sumiram? Mas eles estavam nas chamas! Essas perguntavas já não importavam mais, seus ferimentos foram tratados e
agora você está em casa agora, olhando pela janela do apartamento. A cidade permanece a mesma, com os mesmo rostos, o mesmo anúncios,
as mesmas notícias, nada mais em especial, exceto um bilhete que voa pelo ar até sua janela.""")
                                print("Obrigado")
                            else:
                                print("""
Você decide não acender, e naquela hora o malfeitor cego vem em sua direção com sede de vigança. O que fazer agora!? Correr não adianta
mais e é tarde demais para pensar em uma fuga rápida. Ao olhar pro lado você vê seu amigo já morto. O malfeitor agarra o corvo e o embrulha
na mão, deixando seu bico à mostra. Ele crava o bico do corvo no seu peito, tão forte que a dor é excruciante. Você não aguenta mais, e o
que mais deseja é morrer. Antes do fim, num último esforço para ver o que está a sua volta, você vê algo brilhante e confortante saindo
do cadáver do corvo, cujo bico está cravado em seu peito. É a alma do irmão sendo libertada para o descanso. Você conseguiu.
Dor.
Escuridão.
Fim.
""")

                                        
                else:
                    # Op3 - Abrir ou não o envelope
                    print("23h10")
                    print("""
Pouco importa o há dentro daquele envelope, tudo o que você precisa é do seu café, de um banho quente e uma noite para
afastar os problemas. Noite estrelada. Noite estrelada. O que aguarda? Apenas há uma mágoa que não se desfez na garoa.
A caneca já está vazia... O chuveiro já deixa cair o jato quente sobre os azulejos... E a cama arrumada, pronta para que
um corpo qualquer perca-se no sono. """)

                    # variáveis extras #
                    hour = 23
                    minute = 15
                    
                    for i in range(4):
                        minute = minute + 10
                        print(hour,"h",minute)
                        print("Sem sono")
                    print("""
Branco.
A luz começa a ganhar formas.
É um lugar esquisito e arrepiante, parece um cemitério. Onde estaria? O ar cheira a enxofre, é uma madrugada fria.
Qualquer barulho é notável por causa do silêncio naquele lugar. O vento bate em seu rosto, a brisa é assustadora.
Passos.
Quem estaria alí? É um cemitério, e ainda mais aquela hora da noite. Seria real? Você começa a andar entre as covas
e vê uma silhueta no escuro, ela ganha forma devido ao claro da lua, que, embora coberta por camadas finas de nuvem
ainda consegue iluminar aquela noite horrenda.
Passos.
- Olá? - Você fala, na esperança de que alguém te responda ou que seja apenas um animal assustado.
- Olá? - Você torna a dizer.
Algo surge por trás de você, a queimação em suas costas faz a dor ficar o mais real possível. O que há alí?

(...)

Você acorda, algo ensopa sua cama, o que será? Em meio aquela dor você levanta. Há sangue por todos os lados, algo
perfurou suas costas e agora a dor é quase insuportável. Ao olhar aquela cena toda você cai no chão. E tenta se arrastar
até a pequena mesinha ao lado de sua cama. Pega o telefone celular e começa a digitar 91... O último número é impedido de ser
digitado por um cara alto, parece ter uns 40 anos. Ele usa uma cartola e está com uma arma potiaguda na mão
- Quem é você e como entrou aqui? - Você se esforça para tentar levantar.
Sem mais espera, o  cara passa a faca em seu pescoço, deixando um espirro de sangue no chão.
Dor.
Nos últimos segundos você percebe que, talvez, aquela carta poderia ter ajudado a isso não acontecer.
Dor.
Agonia.
Alívio.
Escuridão.

(...)

Fim.
""")
                    
                    # break, o personagem morre
                    break 
                    
            else:
                # op2 - Abrir ou Não a Janela
                # Não importa a opção, quando entrar nesse else, significa que o jogador vai ignorar a carta!!
                print("""Você escolheu não ir até a janela e não a abriu. O corvo invade o local...""")
                print("""Após 2 minutos, a batidas na janela sessaram. Logo você retorna a beber seu café e caminha té a sala
e então retira um livro da prateleira e começa a lê-lo. O café lhe permite ficar acordado mesmo quando está ficando entediado
com o assunto do livro. Não há nenhuma TV em todo o apartamento, apenas um computador. Para por um ponto final no tédio, assistir
uma série, verificar e-mails e navegar em redes sociais é a solução.
(...)
O ambiente da sala só é ilumidado pela tela com do coputador e uma pequena luminária. Alguns ruídos percorrem o local, mas é apenas
o vento e o estabilizador da máquina oscilando. Sua caixa de e-mail está vazia, sua série favorita ainda está em hiatus, seu café
está no fim.
(...)
Aquele som irritante no vidro da janela retornou, está mais agitado do que anteriormente. O computador se desliga do nada, a luminária
começa a piscar até queimar sua lâmpada, as janelas se abrem com o sopro do vento. Uma criatura negra e alada invade a casa, bate as
asas com tamanho pavor. Atrás dela surge uma silhueta esguia, sua face é velha e seu olhar quase fatal. Um ar maquiavélico. As mãos
de dendos longos e pontudo agarra o corvo e o tira de seu caminho. E a silhueta se aproxima, é um homem. Ele estava a sua procura.
(...)
O corvo grita mais uma vez, pula em cima do homem. O homem agarra sua perna e todos juntos se desfazem na poeira.
(...)
(03h45)

// acorda num lugar louco aí, seu amigo tá lá também, você tenta fazer alguma coisa, você sai morto, mas salva seu amigo

""")
                
                # break, o personagem morreu
                break

                    
                          
            # agradecimentos
            print("---fim---")
            print("Obrigado por jogar, ", nome_jogador)
            print("Este jogo foi desenvolvido pelos alunos do IFRN - Campus Caicó")
            print("Breve em uma versão com gráficos")
            print("Todos os direitos reservados à: Samantha, Laudeíres, Yuri e José Douglas")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------            
                          
        elif(op1.upper() == "CHÁ" or op1.upper() == "CHA") :
            
            tea = input("de (informe o nome do chá, exemplo: camomila)... ")
            print("23h10")
            print("""
Confortavelmente, você senta-se a mesa e relaxa com seu chá de""", tea , """até que pequenas batidas ecoam. O som parece 
pertencer às janela da sala. 'Deve ser o vento ou as árvores da rua', o sono lhe ataca, deitar-se na cama e dormir parece
ser uma ótima ideia. Um último gole do chá. A caneca vazia está na cômoda e você encontra-se em um ambiente tão reconfortante...
Logo, os sono é quem te governa...""")
            print("...")
            print("00h10")
            print("""Grandes olhos negros estão a te observar. Com um sobresalto, você sai da cama e o corvo permanece a gritar e bica um envelope
que está sobre a cama. Poderia esta pequena criatura está te pedindo para abrir o envelope? O que deseja fazer? """)
            
            # Opção ??? - Abrir ou não o envelope
            opT = input("Deseja abrir o envelope? ('S' ou 'N')")
            if opT.upper() == "S":
                print("""Um bocejo ali e aqui, o chá ainda lhe deixa sonolento. Você abre com cuidado a correspondência entregue pelo corvo, analisa
um símbolo carimbado no papel. E logo começa a ler cada uma das palavras""")

                print("""A pequena criatura sombria permanece em seu quarto, seus olhos negros observam todo o ambiente, dá alguns passinhos, balança
as asas. Uma última olhada em você e puff! O corvo some nas sombras, vira poeira. Parece um sonho""")
                
            else:
                print("""
Você começa a ficar assustado em ver aquela criatura sombria em seu quarto. Pega o envelope, observa alguns detalhes, mas o ignora
joga no canto do quarto e espanta o corvo com tanta rispidez que, antes dele sumir, dáum grito feio, como um "eu tentei te avisar". Você
se assusta com aquela situação Mas mesmo assim volta pra cama e tenta dormir de novo.
Branco.
A luz começa a ganhar formas.
É um lugar esquisito e arrepiante, parece um cemitério. Onde estaria? O ar cheira a enxofre, é uma madrugada fria.
Qualquer barulho é notável por causa do silêncio naquele lugar. O vento bate em seu rosto, a brisa é assustadora.
Passos.
Quem estaria alí? É um cemitério, e ainda mais aquela hora da noite. Seria real? Você começa a andar entre as covas
e vê uma silhueta no escuro, ela ganha forma devido ao claro da lua, que, embora coberta por camadas finas de nuvem
ainda consegue iluminar aquela noite horrenda.
Passos.
- Olá? - Você fala, na esperança de que alguém te responda ou que seja apenas um animal assustado.
- Olá? - Você torna a dizer.
Algo surge por trás de você, a queimação em suas costas faz a dor ficar o mais real possível. O que há alí?

(...)

Você acorda, algo ensopa sua cama, o que será? Em meio aquela dor você levanta. Há sangue por todos os lados, algo
perfurou suas costas e agora a dor é quase insuportável. Ao olhar aquela cena toda você cai no chão. E tenta se arrastar
até a pequena mesinha ao lado de sua cama. Pega o telefone celular e começa a digitar 91... O último número é impedido de ser
digitado por um cara alto, parece ter uns 40 anos. Ele usa uma cartola e está com uma arma potiaguda na mão
- Quem é você e como entrou aqui? - Você se esforça para tentar levantar.
Sem mais espera, o  cara passa a faca em seu pescoço, deixando um espirro de sangue no chão.
Dor.
Nos últimos segundos você percebe que, talvez, aquela carta poderia ter ajudado a isso não acontecer.
Dor.
Agonia.
Alívio.
Escuridão.

(...)

Fim.

""")
                
            # agradecimentos
            print("---fim---")
            print("Obrigado por jogar, ", nome_jogador)
            print("Este jogo foi desenvolvido pelos alunos do IFRN - Campus Caicó")
            print("Todos os direitos reservados à: Samantha, Laudeíres, Yuri e José Douglas")
            
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
