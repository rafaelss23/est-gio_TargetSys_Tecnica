#!/usr/bin/env python
# coding: utf-8

# #### 1) Observe o trecho de código abaixo: <br>
# <code>
# int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?</code>

# In[1]:


INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)


# #### 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será <br> a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa <br> na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci <br> e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# In[2]:


def fibonacci(n):
    if n < 0:
        return False
    
    a, b = 0, 1
    
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
        
    return False

numero = 21
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


# #### 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:<br>
# - O menor valor de faturamento ocorrido em um dia do mês;
# - O maior valor de faturamento ocorrido em um dia do mês;
# - Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.<br>
# 
# <i>IMPORTANTE:<br>
# <b>a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;</b><br>
# <b>b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;</b>

# In[3]:


import json


with open('dados.json', 'r') as file:
    dados = json.load(file)

valores = [dia["valor"] for dia in dados if dia["valor"] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")


# #### 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# - SP – R$67.836,43
# 
# - RJ – R$36.678,66
# 
# - MG – R$29.229,88
# 
# - ES – R$27.165,48
# 
# - Outros – R$19.849,53
# 
# <b>Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.</b>

# In[4]:


faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())

for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")


# #### 5) Escreva um programa que inverta os caracteres de um string. <br>
# 
# 
# 
# <i>IMPORTANTE:</i>
# 
# <b>a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;</b><br>
# <b>b) Evite usar funções prontas, como, por exemplo, reverse;</b>

# In[5]:


def inverte_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

string_sistema = "Sistema"
print(inverte_string(string_sistema))

