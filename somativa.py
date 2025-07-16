x = input("Olá, obrigado por escolher CineRay,  Você gostaria de comprar um ingresso? (sim/não) ")

while x not in ("sim", "não"):
    print("Resposta incorreta, por favor digite 'sim' ou 'não'.")
    x = input("Olá, você gostaria de comprar um ingresso? (sim/não) ")

if x == "não":
    print("Sistema encerrado")
else:
    print("Ok, vou te direcionar para a lista de filmes😁.")

    lista_filmes = ["sonic", "mario", "titanic", "divergente"]
    for filme in lista_filmes:
        print(filme)

    lista_ingresso = []

    adicionar = input("Você deseja adicionar um ingresso? (sim/não) ")
    while adicionar not in ("sim", "não"):
        print("Resposta incorreta, por favor digite 'sim' ou 'não'.")
        adicionar = input("Você deseja adicionar um ingresso? (sim/não) ")

    if adicionar == "não":
        print("Sistema encerrado")
    else:
        print("Ok, vamos continuar.")

        ingressos = 0 

        while adicionar == "sim" and ingressos < 2:
            ingresso = input("Digite o nome do filme que você deseja adicionar: ")
            if ingresso not in lista_filmes:
                print("Filme não encontrado, tente novamente :(")
                continue

            lista_ingresso.append(ingresso)
            ingressos += 1
            print("Ingresso adicionado com sucesso❤:", lista_ingresso)

            if ingressos == 2:
                print("Você já adicionou 2 ingressos, não é possível adicionar mais.")
                break

            adicionar = input("Você gostaria de comprar outro ingresso? (sim/não) ")
            while adicionar not in ("sim", "não"):
                print("Resposta incorreta, por favor digite 'sim' ou 'não'.")
                adicionar = input("Você gostaria de comprar outro ingresso? (sim/não) ")

        excluir = input("Você deseja excluir algum ingresso? (sim/não) ")
        while excluir not in ("sim", "não"):
            print("Resposta incorreta, por favor digite 'sim' ou 'não'.")
            excluir = input("Você deseja excluir algum ingresso? (sim/não) ")

        if excluir == "sim":
            print("Ingressos adicionados na lista:", lista_ingresso)
            ingresso_excluir = input("Digite o nome do ingresso que deseja excluir: ")
            if ingresso_excluir in lista_ingresso:
                lista_ingresso.remove(ingresso_excluir)
                print("Ingresso excluído com sucesso:", lista_ingresso)
            else:
                print("Ingresso não encontrado. Nenhuma exclusão realizada.")

        print("Muito obrigado por escolher a gente!")
        avaliacao = input("Poderia nos avaliar de 1 a 10? ")
        print("Esse foi o seu feedback de CineRay:", avaliacao)
        feedback = input("Poderia nos dizer se algo no sistema deve melhorar? ")
        print("Obrigado pelo seu feedback! 😊 CineRay agradece!")
