from datetime import datetime
from utils import filtrar_numeros
from constants import LIMITE_SAQUES, mensagens, opcoes_iniciais


class Operacoes:

    def __init__(self):  

        self.saldo = 0.00
        self.limite = 500.00
        self.extrato = []
        self.numero_saques = 0       

    def print_mensagem_inicial(self):
        print(mensagens['titulo'].upper().center(len(mensagens['titulo'])+ 4, '#'))
        print(mensagens['boas_vindas'].rjust(len(mensagens['boas_vindas']) + 1, '#'))
        print(mensagens['escolha_opcao'].rjust(len(mensagens['escolha_opcao']) + 1, '#'))
        print(mensagens['exemplo_opcao'].rjust(len(mensagens['exemplo_opcao']) + 1, '#'))
        print("")

    def print_menu(self):
        for item in opcoes_iniciais:            
            codigo = item["codigo"]
            operacao = item["operacao"]
            print(f"[{codigo}] {operacao}")
      
    def depositar(self):
        print(mensagens['depositar_inicial'])        
        valor = input(mensagens['input'])
        print("")

        valor_formatado = filtrar_numeros(valor)
        if valor_formatado == 0:
            print(mensagens['erro_entrada_invalida'])
            return
        
        self.saldo += valor_formatado
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato_deposito = f'{agora} DEPÓSITO: R$ {valor_formatado:.2f}' 
        self.extrato.append(extrato_deposito)

        print(f'R$ {valor_formatado:.2f} depositado com sucesso.')
        print(f'O saldo atual é R$ {self.saldo:.2f}')
        print("")
        print(mensagens['depositar_outro'])
        print(mensagens['deposito_opcoes'])
        valor = input(mensagens['input'])
        if valor.lower() == 's':
            self.depositar()

    def sacar(self): 
        print(mensagens['saque_inicial'])     
        valor = input(mensagens['input'])
        print("")

        valor_formatado = filtrar_numeros(valor)
        if valor_formatado == 0:
            print(mensagens['erro_entrada_invalida'])
            return
        
        if self.numero_saques >= LIMITE_SAQUES:
            print(mensagens['erro_limite_n_saques'])
            return
        
        if valor_formatado > self.saldo:
            print(mensagens['erro_saldo_insuficiente'])
            print(f'Valor inserido: R$ {valor_formatado:.2f}  Saldo disponível: R$ {self.saldo:.2f}')
            print("")
            return
        
        if valor_formatado > self.limite:
            print(mensagens['erro_limite_saques'])
            print(f'Valor inserido: R$ {valor_formatado:.2f}  Limite disponível: R$ {self.limite:.2f}')
            print("")
            return
        
        self.saldo -= valor_formatado;
    
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato_deposito = f'{agora} SAQUE:    R$ {valor_formatado:.2f}' 
        self.extrato.append(extrato_deposito)

        print(f'R$ {valor_formatado} sacado com sucesso.')
        print(f'O saldo atual é R$ {self.saldo:.2f}')
        print("")
    
    def exibir_extrato(self):
        for item in self.extrato:   
            print(item)

    
    def iniciar(self):
        self.print_mensagem_inicial()
        while(True):
            self.print_menu()
            opcao = input(mensagens['input'])

            if opcao.lower() == "d":
                self.depositar()
            elif opcao.lower() == "s":
                self.sacar()
            elif opcao.lower() == "e":
                self.exibir_extrato()
            elif opcao.lower() == "q":
                break;
        

if __name__ == "__main__":
    operacao = Operacoes()
    operacao.iniciar()