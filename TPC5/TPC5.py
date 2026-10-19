def criarTurma():
    turma = []
    nometurma = input("Que nome queres dar à tua turma?")
    print(f"Turma {nometurma} criada com sucesso!")
    return turma

def verificar_id(id, turma):
    repetido = False
    for aluno in turma:
        if aluno[1] == id:
            repetido = True
    return repetido

def validar_nota(texto):
    nota = float(input(texto))
    while nota < 0 or nota > 20:
        nota = float(input("Valor Inválido! Introduza uma nota de 0 a 20: "))
    return nota

def inserirAluno(turma):
    nome = input("Introduz o nome do aluno/a: ")
    id_aluno = input("Introduz o id do aluno/a: ")

    while verificar_id(id_aluno,turma):
        id_aluno = input("Já existe um aluno com esse id! Tenta novamente: ")

    nota_tpc = validar_nota("Insere a nota do TPC do aluno/a: ")
    nota_proj = validar_nota("Insera a nota do Projeto do aluno/a: ")
    nota_teste = validar_nota("Insere a nota do Teste do aluno/a: ")

    aluno = (nome, id_aluno, [nota_tpc, nota_proj, nota_teste])
    turma.append(aluno)
    print(f"Aluno/a {aluno} inserido com sucesso!")
    return turma

def listarTurma(turma):
    if turma == []:
        print("A sua turma não tem alunos de momento. Insira primeiro na opção 2.")
        principal()
    else:
        for aluno in turma:
            print(f"Nome: {aluno[0]} \nId: {aluno[1]} \nNota do TPC: {aluno[2][0]} \nNota do Projeto: {aluno[2][1]} \nNota do Teste: {aluno[2][2]}")

def consultarAluno(turma):
    encontrado = False
    id_cons = input("Introduza o id do aluno7a que pretende consultar: ")
    for aluno in turma:
        if aluno[1] == id_cons:
            print(F"Estas são as informações do aluno/a que consultou com id {id_cons}: \nNome: {aluno[0]} \nNota do TPC: {aluno[2][0]} \nNota do Projeto: {aluno[2][1]} \nNota do Teste: {aluno[2][2]}")
            encontrado = True
    if encontrado == False:
        print("O id que indicou não corresponde a nenhum aluno7a da turma. Tente novamente!")

def guardarTurma(turma):
    nomefile = input("Indica o nome que queres dar ao teu ficheiro: ")
    file = open(f"{nomefile}.txt", "w")
    for aluno in turma:
        file.write(f"{aluno[0]}|{aluno[1]}|{aluno[2][0]}|{aluno[2][1]}|{aluno[2][2]}\n")
    file.close()
    print(f"A sua turma foi guardada com sucesso no ficheiro {nomefile}")

def carregarTurma():
    nomefile = input("Indica o nome do ficheiro a abrir: ")
    turma = []
    file = open(f"{nomefile}.txt", "r")
    for line in file:
        dados = line.split ("|")
        nome = dados [0]
        id = dados [1]
        notas = [float(dados [2]), float(dados [3]), float(dados[4])]
        aluno = (nome, id, notas) 
        turma.append (aluno)
    file.close()
    return turma

def mostrar_menu():
    print("\n===== MENU: GESTÃO DE ALUNOS =====")
    print("(1) Criar uma turma")
    print("(2) Inserir um aluno na turma")
    print("(3) Listar a turma")
    print("(4) Consultar um aluno por id")
    print("(5) Guardar uma turma num ficheiro")
    print("(6) Carregar uma turma dum ficheiro")
    print("(0) Sair\n")

def principal():
    turma = []
    opcao = -1
    while opcao != 0:
            mostrar_menu()
            opcao = int(input("Escolha uma opção para a operação que pretende efetuar: "))
    
            if opcao == 0:
                print("\nA terminar a aplicação. Até à próxima!")
            elif opcao == 1:
                criarTurma()
            elif opcao == 2:
                inserirAluno(turma)
            elif opcao == 3:
                listarTurma(turma)
            elif opcao == 4:
                consultarAluno(turma)
            elif opcao == 5:
                guardarTurma (turma)
            elif opcao == 6:
                carregarTurma()
                print(turma)
            else:
                print("\nOpção inválida! Tente novamente.")

principal()