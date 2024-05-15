print("Seja bem-vindo ao meu quiz!")
answer_user = input("Quer começar? (S/N)")

if answer_user != "S":
    
    
   
    score = 0
###PErgunta 1
    print("Começando...")
    print("Qual o pais que sediou a primeira copa do mundo? \n (A) Uruguai \n (B) Argentina \n (C) Inglaterra \n (D) Espanha \n")
    answer_1 = input("Resposta: ")

    if answer_1 == "A":
        print("Correto!")
        score = score + 1
    else:
        print("Incorreto")
        #Pergunta 2
    print("Quem foi campeão da copa de 2002? \n (A) Alemanha \n (B) Uruguai \n (C) Brasil \n (D) Espanha \n")
    answer_2 = input("Resposta: ")

    if answer_2 == "C":
        print("Correto!")
        score = score + 1

    else:
        print("Incorreto")

        ###Pergunta 3

    print("Quem foi campeão da copa de 2006? \n (A) Italia \n (B) Uruguai \n (C) Brasil \n (D) Espanha \n")
    answer_3 = input("Resposta: ")

    if answer_3 == "A":
        print("Correto!")
        score = score + 1
    else:
        print("Incorreto")

        ###Pergunta 4
    print("Quem foi que fez o terceiro gol da argentina na copa de 2022? \n (A) Di Maria \n (B) De Paul \n (C) Messi \n (D) Dybala \n")
    answer_4 = input("Resposta: ")

    if answer_4 == "C":
        print("Correto!")
        score = score + 1
    else:
        print("Incorreto")


        print(f"Quiz acabou... pontuação: {score}/4")

















    
    