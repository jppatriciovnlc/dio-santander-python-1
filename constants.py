LIMITE_SAQUES = 3

opcoes_iniciais = [
    {"codigo": "d", "operacao": "Depositar"},
    {"codigo": "s", "operacao": "Sacar"},
    {"codigo": "e", "operacao": "Extrato"},
    {"codigo": "q", "operacao": "Sair"},
]

mensagens = {
    'input': '=> ',
    'titulo': ' Programa de Operações Bancárias ',
    'boas_vindas': ' Seja bem vindo(a)!',
    'escolha_opcao': ' Digite o código da opção desejada para continuar',
    'exemplo_opcao': ' Exemplo: digite d para depositar',
    'depositar_inicial': 'Digite o valor a depositar:',
    'depositar_outro': 'Deseja realizar outro deposito?',  
    'deposito_opcoes':  '[s] Sim  [n] Não',
    'saque_inicial': 'Digite o valor a sacar:',
    'erro_entrada_invalida': 'Erro: O valor informado precisa ser um número maior que zero/n',
    'erro_limite_n_saques':' Erro: O limite de saques diários foi atingido, tente novamente amanhã./n',
    'erro_saldo_insuficiente': 'Erro: O valor inserido é maior que o saldo de sua conta. Insira um valor menor./n',
    'erro_limite_saques': 'Erro: O valor inserido é maior que o limite diário. Insira um valor menor ou tente novamente amanhã./n'
    
}

