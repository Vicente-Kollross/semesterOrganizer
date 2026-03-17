# 1. DEFINIR PRIORIDADES (Regra de Ouro da Lógica)
prioridade = {
    'not': 4,
    'and': 3,
    'or': 2,
    '->': 1,
    '<->': 0,
    '(': -1
}


# 2. Essa parte esta designando os conectivos e os operadores logicos para que o python consiga interpretar de uma forma mais simples
def calcular(op, b, a=None):
    if op == 'not': return not b
    if op == 'and': return a and b
    if op == 'or':  return a or b
    if op == '->':  return (not a) or b
    if op == 'XOR': return a != b
    if op == '<->': return a == b
    return False


# 3. TRANSFORMAR A FRASE EM "Arvore" (Ordem de Prioridade)
def organizar_prioridade(expressao):
    # Limpa a frase e separa por espaços para facilitar
    tokens = expressao.replace('(', ' ( ').replace(')', ' ) ').split()
    pilha_operadores = []
    saida = []

    for t in tokens:
        if t.isupper():  # Se for letra (A, B, C...)
            saida.append(t)
        elif t == '(':
            pilha_operadores.append(t)
        elif t == ')':
            while pilha_operadores and pilha_operadores[-1] != '(':
                saida.append(pilha_operadores.pop())
            pilha_operadores.pop()  # Remove o '('
        else:  # Se for conectivo (and, or, ->)
            while (pilha_operadores and
                   prioridade.get(pilha_operadores[-1], -1) >= prioridade.get(t, -1)):
                saida.append(pilha_operadores.pop())
            pilha_operadores.append(t)

    while pilha_operadores:
        saida.append(pilha_operadores.pop())
    return saida


# 4. RESOLVER A CONTA FINAL
def avaliar(posfixa, valores):
    pilha = []
    for t in posfixa:
        if t.isupper():
            pilha.append(valores[t])
        elif t == 'not':
            v = pilha.pop()
            pilha.append(calcular('not', v))
        else:
            v_dir = pilha.pop()
            v_esq = pilha.pop()
            pilha.append(calcular(t, v_dir, v_esq))
    return pilha[0]


# 5. GERAR A TABELA (O coração do programa)
def gerar_tabela():
    formula = input("Digite a fórmula (not) (and) (or) (->) (XOR) (<->) (use espaços: ( A and B ) -> C ): ")

    # Descobre as letras usadas
    letras = sorted(list(set([c for c in formula if c.isupper()])))
    posfixa = organizar_prioridade(formula)

    # Cabeçalho
    print("\n" + " | ".join(letras) + " | RESULTADO")
    print("-" * (len(letras) * 4 + 12))

    # Gera combinações de V e F manualmente
    n = len(letras)
    for i in range(2 ** n):
        valores = {}
        for j in range(n):
            # Lógica para alternar V e F como na mão
            valor = (i // (2 ** (n - 1 - j))) % 2 == 0
            valores[letras[j]] = valor

        res = avaliar(posfixa, valores)

        linha = " | ".join(["V" if valores[l] else "F" for l in letras])
        print(f"{linha} | {'V' if res else 'F'}")


# Execução
while True:
    gerar_tabela()
    if input("\nOutra? (s/n): ") == 'n': break

