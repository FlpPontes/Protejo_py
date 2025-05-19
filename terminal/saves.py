import pandas as pd
from pathlib import Path

caminho = Path(__file__).parent
diretorio = caminho / 'Acessos.xlsx'

table = pd.read_excel(diretorio)
# -- Começo Verificação User --

def cao(u): # Verificar se já tem usuário
    if u in table['Users'].values:
        return True
    else:
        return False

# -- Fim Verificação User --



# -- Começo Confirmação Conta --

def caca(u): # Vai localizar usuário na Planilha
    if u in table['Users'].values:
        return True
    else:
        return False

def passa(s,u): # Confirmar Senha
    user = True if u in table['Users'].values else False
    senha = True if s in table['Senha'].values else False

    if user == False or senha == False:
        return False
    
    veri = table.loc[table['Users']==u, 'Senha'].values

    if veri == s:
        return True
    else:
        return False

# -- Fim Confirmação Conta --

# -- Enviar os dados --

def ne(u,x,y,z,a,s):
    dados = { 'Users': u,'1 Nome': x,'2 Nome': y,'RestNome': z, 'Idade': a, 'Senha': s}
    table.loc[len(table)] = dados
    table.to_excel(diretorio, index=False)

    return True

#  -- Enviar os dados --

