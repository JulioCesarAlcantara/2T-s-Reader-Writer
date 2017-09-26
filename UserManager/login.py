# from DisplayInterface.Reader import tk
from tkinter import *
from DisplayInterface.messages import *
from DisplayInterface.welcome import *

import requests

from Model.UserModel import UserModel


class Login():
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame (master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack ()

        self.segundoContainer = Frame (master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack ()

        self.terceiroContainer = Frame (master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack ()

        self.quartoContainer = Frame (master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack ()

        self.titulo = Label (self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack ()

        self.nomeLabel = Label (self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack (side=LEFT)

        self.nome = Entry (self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack (side=LEFT)

        self.senhaLabel = Label (self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack (side=LEFT)

        self.senha = Entry (self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack (side=LEFT)

        self.autenticar = Button (self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack ()

        self.mensagem = Label (self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack ()

    # Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get ()
        senha = self.senha.get ()

        autentica = self.autenticaUser(usuario, senha)



    def autenticaUser(self, email, senha):
        try:
            url="https://dg-2ts-server.herokuapp.com/"
            response = requests.get(url + "user_autenticate/email=" + email + "&password=" + senha)
            print(url + "user_autenticate/email=" + email + "&password=" + senha)
            data = response.json()
            print(data)

            if response.ok:
                try:
                    if data["response"] == None:
                        messageError ('Nenhum Usuário Encontrado !!')
                    else :
                        messageError ('Nenhum Usuário Encontrado !!')
                        #print(data["response"])
                except Exception as e:
                    user = UserModel (**data)
                    root.destroy ()
                    window = Window(user.token, user.name)
                    window.mainloop ()
        except Exception as e:
            messageError ('Erro no servidor, contate o analista reponsável !')


root = Tk()
Login(root)
root.mainloop()