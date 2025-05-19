import subprocess
import sys

def instalar_pacote(pacote):
    try:
        __import__(pacote)
    except ImportError:
        print(f'Instalando o pacote {pacote}...')
        subprocess.check.call([sys.executable, '-m', 'pip', 'install', pacote])
instalar_pacote('pandas')
instalar_pacote('pathlib')
instalar_pacote('customtkinter')
instalar_pacote('numpy')


import customtkinter as ck
import runs

ck.set_appearance_mode("system")
ck.set_default_color_theme("dark-blue")

app = ck.CTk()
app.title("Projects Central")
app.geometry('1050x650+20+20')

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)



# DEFs

def ente(u, s):
    kaa = runs.log(u, s)
    if kaa == False:
        ck.CTkLabel(login,
                    text='*Usuário e/ou Senha incorretos*',
                    font=("Ubuntu", 14, 'italic'),
                    text_color="red"
                    ).grid(row=4, column=0, columnspan=2, pady=(10,0), sticky="s")
        return
    else:
        ck.CTkLabel(login,
                    text='*Seja bem Vindo*',
                    font=("Ubuntu", 14, 'italic'),
                    text_color="green"
                    ).grid(row=4, column=0, columnspan=2, pady=(10,0), sticky="s")
        return

# ^^ Def de login


def castr(u, ss, sa, n, d, e):
    mens = ck.CTkLabel(create,
                        text='*texto*',
                        font=("Ubuntu", 13, 'italic'),
                        text_color="red",
                        width=350)

    Uu = runs.cao(u)
    Oo = runs.conf(sa)

    if u == '' or n == '' or d == '' or e == '' or ss == '' or sa == '':
        mens.configure(text='*Campos Faltantes*')
        mens.grid(row=4, column=0, columnspan=2, pady=(0,20), sticky="s")
        return

    if Uu == True:
        mens.configure(text='*Usuário já existente*')
        mens.grid(row=4, column=0, columnspan=2, pady=(0,20), sticky="s")
        return

    if ss != sa:
        mens.configure(text='*Senhas não conferem*')
        mens.grid(row=4, column=0, columnspan=2, pady=(0,20), sticky="s")
        return

    if ss == sa and Oo == False:
        mens.configure(text='*Senha fraca*')
        mens.grid(row=4, column=0, columnspan=2, pady=(0,20), sticky="s")
        return
    
    # Se tudo estiver válido 
    runs.ne(u, sa, n, d, e)
    caff()
    ck.CTkLabel(login, 
                text='CADASTRO REALIZADO COM SUCESSO', 
                font=('Ubuntu', 17, 'bold'),
                text_color='green',
                ).grid(row=0, column=0, columnspan=2, pady=(20,0), sticky="ew")
# ^^ Def de cadastro

# Def de paginação abaixo
def coff():
    info.grid_remove()
    login.grid_remove()
    create.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=40, pady=30)

def caff():
    create.grid_remove()
    info.grid(row=0, column=0, sticky="nsew", padx=(30,40), pady=30)
    login.grid(row=0, column=1, sticky="nsew", padx=(40,30), pady=30)

# DEFs

# Frame Principal
FFr = ck.CTkFrame(app)
FFr.grid(row=0, column=0, sticky="nsew", padx=75, pady=30)
FFr.grid_rowconfigure(0, weight=1)
FFr.grid_columnconfigure((0,1), weight=1)
# Fim Frame Principal

# Frame de telas
info = ck.CTkFrame(FFr)
info.grid(row=0, column=0, sticky="nsew", padx=(30,40), pady=30)
# info.grid_rowconfigure((0,1), weight=1)
# info.grid_columnconfigure((0,1), weight=1)


login = ck.CTkFrame(FFr)
login.grid(row=0, column=1, sticky="nsew", padx=(40,30), pady=30)
login.grid_rowconfigure((0,1,2,3,4,5,), weight=1)
login.grid_columnconfigure((0,1), weight=1)


create = ck.CTkFrame(FFr)
create.grid_rowconfigure((0,1,2,3,4), weight=1)
create.grid_columnconfigure((0,1), weight=1)
# Fim do Frame de telas


# Slot de Login

ck.CTkLabel(login, 
            text="- Tela de Login -",
            font=("Ubuntu", 25, "bold")
            ).grid(row=0, column=0, columnspan=2, pady=15, sticky="new")


ck.CTkLabel(login,
            text="Informe seu user:",
            font=("Ubuntu", 20)
            ).grid(row=2, column=0, padx=(0,25), pady=(0,10), sticky="se")

user = ck.CTkEntry(login,
                    placeholder_text="usuário", 
                    font=("Ubuntu", 18)
                    )
user.grid(row=2, column=1, padx=(25,0), pady=(0,10), sticky="sw")


ck.CTkLabel(login,
            text="Informe sua senha:",
            font=("Ubuntu", 20)
            ).grid(row=3, column=0, padx=(0,25), pady=(10,0), sticky="ne")

senha = ck.CTkEntry(login,
                    placeholder_text="senha",
                    font=("Ubuntu", 18),
                    show="*"
                    )
senha.grid(row=3, column=1, padx=(25,0), pady=(10,0), sticky="nw")
def mostr():
    if senha.cget('show') == "*":
        senha.configure(show="")
        v0.configure(fg_color='#697060')
    else:
        senha.configure(show="*")
        v0.configure(fg_color='transparent')
v0 = ck.CTkButton(login,
            text='👁',
            font=("Ubuntu", 15),
            width=0,
            fg_color='transparent',
            command=lambda: mostr()
            )
v0.grid(row=3, column=1, pady=(10,0), padx=(0,15), sticky="ne")


entri = ck.CTkButton(login,
            text="Entrar",
            font=("Ubuntu", 18),
            command=lambda: ente(user.get(), senha.get())
            )
entri.grid(row=4, column=0, columnspan=2, pady=(10,0), sticky="n")


ck.CTkLabel(login,
            text="Não tem conta?",
            font=("Ubuntu", 16)
            ).grid(row=5, column=0, pady=(0,30), padx=(0,20), sticky="se")

ck.CTkButton(login,
            text="Clique aqui",
            font=("Ubuntu", 16),
            command=lambda:coff()
            ).grid(row=5, column=1, pady=(0,30), padx=(0,20), sticky="sw")

# Final Slot de Login

# Slot de Cadastro

ck.CTkLabel(create,
            text="- Tela de Cadastro -",
            font=("Ubuntu", 25, "bold")
            ).grid(row=0, column=0, columnspan=2, pady=15, sticky="n")

ck.CTkButton(create,
            text="<",
            font=("Ubuntu", 20),
            width=0,
            command=lambda:caff()
            ).grid(row=0, column=0, padx=(15,0), pady=15, sticky="nw")


ck.CTkLabel(create,
            text="Nome Completo:",
            font=("Ubuntu", 20)
            ).grid(row=1, column=0, padx=(50, 0), pady=0, sticky="nw")
nome = ck.CTkEntry(create,
                    font=("Ubuntu", 18)
                    )
nome.grid(row=1, column=0, padx=(50, 0), pady=0, sticky="ew")


ck.CTkLabel(create,
            text="Data de nascimento:",
            font=("Ubuntu", 20)
            ).grid(row=2, column=0, padx=(50,65), pady=0, sticky="nw")
data = ck.CTkEntry(create,
                    placeholder_text="dd/mm/aaaa",
                    font=("Ubuntu", 18),
                    width=115
                    )
data.grid(row=2, column=0, padx=(50,65), pady=0, sticky="w")


ck.CTkLabel(create,
            text="E-mail:",
            font=("Ubuntu", 20)
            ).grid(row=3, column=0, padx=(50,65), pady=0, sticky="nw")
email = ck.CTkEntry(create,
                    placeholder_text="emailadress@dominio.com",
                    font=("Ubuntu", 18),
                    width=350
                    )
email.grid(row=3, column=0, padx=(50,0), pady=0, sticky="ew")


ck.CTkLabel(create,
            text="Nome de Usuário:",
            font=("Ubuntu", 20)
            ).grid(row=1, column=1, padx=(75, 60), pady=0, sticky="nw")
usar = ck.CTkEntry(create,
                    font=("Ubuntu", 18)
                    )
usar.grid(row=1, column=1, padx=(75, 60), pady=0, sticky="we")



ck.CTkLabel(create,
            text="Senha:",
            font=("Ubuntu", 20)
            ).grid(row=2, column=1,rowspan=2, padx=(75,60), pady=0, sticky="nw")

ck.CTkLabel(create,
            text="Faça com que a senha tenha pelo menos:\n• 8 caracteres\n• 2 números\n• 1 caractere especial",
            font=("Ubuntu", 16),
            justify="left"
            ).grid(row=2, column=1,rowspan=2, padx=(75,60), pady=(30,0), sticky="nw")


def d1():
    if s1.cget('show') == "*":
        s1.configure(show="")
        v1.configure(fg_color='#697060')
    else:
        s1.configure(show="*")
        v1.configure(fg_color='transparent')

def d2():
    if s2.cget('show') == "*":
        s2.configure(show="")
        v2.configure(fg_color='#697060')
    else:
        s2.configure(show="*")
        v2.configure(fg_color='transparent')

s1 = ck.CTkEntry(create,
                font=("Ubuntu", 18),
                placeholder_text="senha",
                show="*",
                width=200
                )
s1.grid(row=3, column=1, padx=(75,0), pady=(30,0), sticky="nw")
v1 = ck.CTkButton(create,
            text='👁',
            font=("Ubuntu", 15),
            width=0,
            fg_color='transparent',
            command=lambda: d1()
            )
v1.grid(row=3, column=1, pady=(30,0), padx=(280,5), sticky="nw")

s2 = ck.CTkEntry(create,
                font=("Ubuntu", 18),
                placeholder_text="confirmar senha",
                show="*",
                width=200
                )
s2.grid(row=3, column=1, padx=(75,0), pady=(0,30), sticky="sw")
v2 = ck.CTkButton(create,
            text='👁',
            font=("Ubuntu", 15),
            width=0,
            fg_color='transparent',
            command=lambda: d2()
            )
v2.grid(row=3, column=1, pady=(0,30), padx=(280,5), sticky="sw")



castri = ck.CTkButton(create,
            text='Confirmar Cadastro',
            font=('Ubuntu', 18),
            command=lambda: castr(usar.get(), s1.get(), s2.get(), nome.get(), data.get(), email.get()))
castri.grid(row=4, column=0, columnspan=2, pady=(10,0), padx=(0,0), sticky="n")

# Final Slot de Cadastro

app.mainloop()