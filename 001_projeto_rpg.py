# IFRN - Campus Caicó
# INFORMÁTICA 2M 2015.1
# 23 de maio de 2016
# RPG

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
        nome_personagem = input("Informe o nome do personagem: ")
        sexo_personagem = input("Informe o sexo do personagem(F ou M): ")
        print("----------------------------------------------")

        # conferindo o sexo do personagem
        # ainda por confirmar se isto é realmente necessário
        if (sexo_personagem == "F"):
            print("São 22h32m, sua casa está vazia, escura e sombria. Há uma chuva forte lá fora, da janela começam a soar pequenas batidas. Seria o vento?")
            op1 = input("Gostaria de ir olhar? (S ou N)")
            if (op1 == "S"):
                print("...")
            else:
                  print("...")

            # agradecimentos
            print("---fim---")
            print("Obrigado por jogar, ", nome_jogador)
            print("Este jogo foi desenvolvido pelos alunos do IFRN - Campus Caicó")
            print("Todos os direitos reservados à: Samantha, Laudeíres, Caio, Yuri e José Douglas")
                  
        else:
            print("...")

            # agradecimentos
            print("---fim---")
            print("Obrigado por jogar, ", nome_jogador)
            print("Este jogo foi desenvolvido pelos alunos do IFRN - Campus Caicó")
            print("Todos os direitos reservados à: Samantha, Laudeíres, Caio, Yuri e José Douglas")
            print("----------------------------------------------")
            
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


