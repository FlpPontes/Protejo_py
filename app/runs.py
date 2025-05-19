import pandas as pd
from pathlib import Path

caminho = Path(__file__).parent
diretorio = caminho / 'Counts.xlsx'

table = pd.read_excel(diretorio)


# -- Verificar Senha Forte --

def conf(s):
    a = len(s)
    if a<8:
        return False
    o = 0
    p = 0
    for yey in s:
        if yey in '0123456789':
            p += 1
    for yay in s:
        if yay in "!@#$%&<>.,*-_'":
            o += 1
    if a == p:
        return False
    if o <1:
        return False
    if p < 2:
        return False
    return True

# -- Fim Verificar Senha Forte --
# -- Começo Verificação User --

def cao(u): # Verificar se já tem usuário
    if u in table['Users'].values:
        return True
    else:
        return False

# -- Fim Verificação User --
# -- Enviar os dados --

def ne(u, s, n, d, e):
    n = n.split(" ", maxsplit=2)
    dados = {'Users':u.strip(), '1 Nome': n[0], '2 Nome': n[1], 'RestNome':n[2], 'data': d.strip(), 'email': e.strip(), 'Senha': s.strip()}
    table.loc[len(table)] = dados
    table.to_excel(diretorio, index=False)

# -- Fim Enviar os dados --
# -- Começo Login --
def log(u, s):
    exuser = True if u in table['Users'].values else False
    exsenha = True if s in table['Senha'].values else False

    if exuser == False or exsenha == False:
        return False
    
    ver = table.loc[table['Users']==u, 'Senha'].values
    if ver[0] != s:
        return False
    else:
        return True





# -- Fim Login --



