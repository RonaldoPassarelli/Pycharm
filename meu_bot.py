import requests
import time
import json
import os


def saudacao(msg):
    if msg.lower() in ('oi!', 'alô!', 'olá!', 'hi!', 'ei!', 'oi', 'alô', 'ola', 'olá', 'oí', 'oie',
                       'oie!', 'oiê', 'oiê!'):
        return "Olá!, Tudo bem com você?"


class TelegramBot:
    def __init__(self):
        token = '1860285136:AAEevDoDbezhhCF04ZYnpvhwHhQ8v9ulG5E'
        self.url_base = f'https://api.telegram.org/bot{token}/'
        #  iniciar o TelegramBot

    def iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_mensagens(update_id)
            mensagens = atualizacao['result']
            if mensagens:
                for mensagem in mensagens:
                    update_id = mensagem['update_id']
                    chat_id = mensagem['message']['from']['id']
                    eh_primeira_mensagem = mensagem['message']['message_id'] == 1
                    resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    def obter_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        saudei = 0
        mensagem = mensagem['message']['text']
        if eh_primeira_mensagem == True or mensagem.lower() == 'menu':
            return f'Olá!, sou a DaniRoBot. Tudo bem com você?'
        if len(mensagem) <= 4 and saudei == 0:
            saudei = 1
            return saudacao(mensagem)

            #  return f'''Queijo MAX = R$ 20,00{os.linesep}Confima pedido (s/n)'''
        elif mensagem == '2':
            return f'''Duplo burguer Bacon = R$ 34,00{os.linesep}Confima pedido (s/n)'''
        if mensagem == '3':
            return f'''Triplo XXX = R$ 35,00{os.linesep}Confima pedido (s/n)'''
        if mensagem.lower() in ('s', 'sim'):
            return 'Pedido confirmado'
        else:
            return 'Gostaria de acessar o menu? Digite "menu"'

    def responder(self, resposta, chat_id):
        #  enviar
        link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_de_envio)


bot = TelegramBot()
bot.iniciar()

