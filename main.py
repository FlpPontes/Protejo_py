'''
import subprocess
import sys

# Função para instalar pacotes automaticamente
def instalar_pacote(pacote):
    try:
        __import__(pacote)
    except ImportError:
        print(f"Instalando o pacote {pacote}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])

# Instalar pandas e openpyxl, se necessário
instalar_pacote("pandas")
instalar_pacote("openpyxl")
'''

import utilidades
import saves

# -- Começo Central --
print('\n\n-----  Central de Testes  -----')
print('')
son = str(input('Possui Login? [S/N] ').upper().strip())
# -- Fim Central --


# -- Começo de Criação de Conta --

if son != 'S':
    print('\n\n-----  Criação de Conta  -----')
    print('Nos informe suas informações pessoais:')
    name = str(input('\nInforme seu Nome Completo: \n').strip())
    name = name.split(' ', maxsplit=2)    
    
# -- Começo Idade --

    age = (input('\nInforme sua Idade: \n').strip())
    while not age.isdigit():
        print('\n-----  Ocorreu um erro ao digitar  -----')
        age = (input('Informe sua Idade: \n').strip())
    age = int(age)
    if age<=13:
        print('Você não tem idade para acessar o serviço.')
        exit()

# -- Final Idade --

# -- Começo Users --

    print('\nCrie um nome de usuário')
    user = str(input('').strip())
    cao = saves.cao(user)
    if cao == True:
        while cao == True:
            print('\n-----  Usuário já existente  -----')
            user = str(input('Crie um nome de usuário').strip())
            cao = saves.cao(user)

#  -- Final Users --

# -- Começo Senha --

    print('\nPorfavor escreva uma senha forte com pelo menos:')
    print('8 caracteres - 2 número - 1 caractere especial.')
    senha = str(input('').strip())
    
    coaf = utilidades.conf(senha)
    if coaf == 'falt' or coaf == 'number' or coaf == 'crac' or coaf == 'specil':
        while coaf == 'falt' or coaf == 'number' or coaf == 'crac' or coaf == 'specil':
            print('\n\n-----  Senha inválida  -----')
            print('Porfavor escreva uma senha forte com pelo menos:')
            print('8 caracteres - 2 número - 1 caractere especial.')
            senha = str(input('').strip())
            coaf = utilidades.conf(senha)

# -- Final Senha --
# -- Fim de Criação de Conta --

# ------------------------------------------------------------------------------

#  -- Começo Login --

if son != 'S':
    print('\n\n----- Conta Criada Com Sucesso -----')
    print('Segue a Página de Login para acessar nossos serviços.\n')

print('\n-----  Login  -----')
print('\nNos informe seu nome de Usuário:')
user = str(input('').strip())
caca = saves.caca(user)

print('\nNos informe sua senha:')
senha = str(input('').strip())
passa = saves.passa(senha,user)

if caca == False or passa == False:
    while caca == False or passa == False:
        print('\n* Usuário e/ou Senha incorretos *')
        print('-----  Login  -----')

        print('\nNos informe seu nome de Usuário:')
        user = str(input('').strip())

        print('\nNos informe sua senha:')
        senha = str(input('').strip())

        caca = saves.caca(user)
        passa = saves.passa(senha,user)

# -- Fim Login --

# ------------------------------------------------------------------------------

# -- Começo Serviços --
print('----- Seja Bem Vindo {}! ----- '.format(user))
print('Qual serviço deseja Acessar:')



# -- Fim Serviços --
