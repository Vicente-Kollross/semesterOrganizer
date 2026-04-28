import pickle
import os

db = "database.pkl"

login_g = "admin"
senha_g = "123"

tentativa = 0

if not os.path.exists(db):
    with open(db, 'wb') as f:
        pickle.dump({}, f)
else:
    try:
        with open(db, 'rb') as f:
            dados = pickle.load(f)
        if not isinstance(dados, dict):
            raise ValueError("Banco de dados não é um dicionário!")
    except Exception:
        with open(db, 'wb') as f:
            pickle.dump({}, f)

print ("Bem-vindo ao sistema bancario")

while True:

  escolha = input("Selecione uma opcao:\n1 - Cliente\n2 - Gerente\n3 - Salvar alteracoes em disco\n0 - Sair\n")

## ------------ MODO CLIENTE ------------ ##

  if escolha == "1": 
    cliente_opcoes = input("Selecione uma opcao:\n1 - Consultar saldo\n2 - Depositar valor\n3 - Sacar valor\n4 - Simular rendimento\n5 - Listar ultimas transacoes (extrato)\n6 - Sair\n")
    
    if cliente_opcoes == "1": 
      valor_deposito = int(input("Informe o valor a ser depositado: "))

      if valor_deposito != 0:
        print(f"Valor depositado: {valor_deposito}")
    elif cliente_opcoes == "3":
      print("Sacar valor")
    elif cliente_opcoes == "4":
      print("Simular rendimento")
    elif cliente_opcoes == "5":
      print("Listar ultimas transacoes (extrato)")
    elif cliente_opcoes == "6":
      continue
    else:
      print("Opcao invalida")

## ------------ MODO GERENTE ------------ ##

  elif escolha == "2":
    login_gerente = input("Informe o login:\t")
    senha_gerente = input("Informe a senha:\t")
    while login_gerente != login_g or senha_gerente != senha_g:
      print("Senha incorreta")
      login_gerente = input("Informe o login:\t")
      senha_gerente = input("Informe a senha:\t")
      tentativa += 1
      if tentativa == 3:
        print("Senha inválida...\tTente Novamente")
        break

  if login_gerente == login_g and senha_gerente == senha_g:
    print("Login bem-sucedido!")
    
    gerente_opcoes = input("Selecione uma opcao:\n1 - Cadastrar ou alterar o nome de um cliente\n2 - Corrigir Saldo\n3 - Consultar Dados de um Cliente\n4 - Listar ultimas transacoes (extrato)\n0 - Sair\n")
    
    if gerente_opcoes == "1":
        nome_cliente = input("Informe o nome do cliente:\t")
        print("Cadastrar ou alterar o nome de um cliente")
    elif gerente_opcoes == "2":
        print("Corrigir Saldo")
    elif gerente_opcoes == "3":
        print("Consultar Dados de um Cliente")
    elif gerente_opcoes == "4":
        print("Listar ultimas transacoes (extrato)")
    elif gerente_opcoes == "0":
        continue
    else:
        print("Opcao invalida")

## ------------ SALVAR OS DADOS, GARANTINDO A PERSISTÊNCIA DOS DADOS ------------ ##

  elif escolha == "3": 
    salvar_alteracoes = input("Deseja salvar as alteracoes em disco? (s/n)")
    if salvar_alteracoes == "s":
      with open(db, 'wb') as f:
        pickle.dump(dados, f)
      print("Alteracoes salvas com sucesso")
    else:
      print("Alteracoes nao salvas")

  elif escolha == "0": ## SAIR
    break
  else:
    print("Opcao invalida")
