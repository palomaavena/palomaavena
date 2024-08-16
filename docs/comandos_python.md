#Comandos básicos:

Fonte: Chatgpt

### 1. **Entrada e Saída**
```python
# Entrada de dados
nome = input("Digite seu nome: ")

# Saída de dados
print("Olá, " + nome)
print(f"Olá, {nome}")  # Usando f-string para interpolação de string
```

### 2. **Operações Matemáticas**
```python
# Aritmética básica
soma = 5 + 3
subtracao = 10 - 2
multiplicacao = 4 * 2
divisao = 16 / 4  # Retorna um float
divisao_inteira = 16 // 3  # Retorna um inteiro
modulo = 10 % 3  # Resto da divisão
exponenciacao = 2 ** 3  # 2 elevado a 3
```

### 3. **Estruturas de Controle**
```python
# Condicionais
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Laços de repetição
# While loop
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# For loop
for i in range(5):
    print(i)
```

### 4. **Listas**
```python
# Criando uma lista
numeros = [1, 2, 3, 4, 5]

# Acessando elementos
print(numeros[0])  # Primeiro elemento

# Modificando elementos
numeros[0] = 10

# Adicionando elementos
numeros.append(6)

# Removendo elementos
numeros.remove(3)

# Tamanho da lista
tamanho = len(numeros)
```

### 5. **Funções**
```python
# Definindo uma função
def saudacao(nome):
    return f"Olá, {nome}!"

# Chamando uma função
print(saudacao("Paloma"))
```

### 6. **Dicionários**
```python
# Criando um dicionário
pessoa = {"nome": "Paloma", "idade": 30}

# Acessando valores
print(pessoa["nome"])

# Adicionando um novo par chave-valor
pessoa["cidade"] = "Salvador"

# Removendo um par chave-valor
del pessoa["idade"]
```

### 7. **Trabalhando com Arquivos**
```python
# Escrevendo em um arquivo
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')

# Lendo de um arquivo
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

### 8. **Módulos e Pacotes**
```python
# Importando um módulo
import math

# Usando funções do módulo
raiz = math.sqrt(25)

# Importando funções específicas de um módulo
from math import sqrt

# Usando a função importada diretamente
raiz = sqrt(25)
```

### 9. **Manipulação de Strings**
```python
# Tamanho da string
tamanho = len("Paloma")

# Maiúsculas e Minúsculas
maiuscula = "paloma".upper()
minuscula = "PALOMA".lower()

# Substituição
texto = "Olá, Paloma".replace("Paloma", "Mundo")

# Divisão de string
lista_palavras = "Python é incrível".split()

# Fatiamento de strings
primeira_letra = "Paloma"[0]
parte_texto = "Paloma"[1:4]  # 'alo'
```

### 10. **List Comprehension**
```python
# Criando uma lista com números de 0 a 9
numeros = [i for i in range(10)]

# Criando uma lista de quadrados dos números de 0 a 9
quadrados = [i**2 for i in range(10)]
```


### 11. **Conjuntos (Sets)**
```python
# Criando um conjunto
frutas = {"maçã", "banana", "laranja"}

# Adicionando elementos
frutas.add("uva")

# Removendo elementos
frutas.remove("banana")

# Verificando a existência de um elemento
print("maçã" in frutas)

# Operações de conjuntos
outro_conjunto = {"laranja", "abacaxi"}
uniao = frutas.union(outro_conjunto)  # União
interseccao = frutas.intersection(outro_conjunto)  # Interseção
diferenca = frutas.difference(outro_conjunto)  # Diferença
```

### 12. **Tratamento de Exceções**
```python
# Tentativa de dividir por zero
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
finally:
    print("Essa mensagem é exibida independentemente de erro.")

# Exceção personalizada
try:
    raise ValueError("Ocorreu um erro de valor.")
except ValueError as e:
    print(e)
```

### 13. **Manipulação de Data e Hora**
```python
from datetime import datetime, timedelta

# Data e hora atual
agora = datetime.now()

# Formatando a data e hora
data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

# Convertendo string para data
data_str = "15/08/2024"
data_obj = datetime.strptime(data_str, "%d/%m/%Y")

# Operações com datas
ontem = agora - timedelta(days=1)
amanha = agora + timedelta(days=1)
```

### 14. **Expressões Regulares**
```python
import re

# Verificando um padrão em uma string
padrao = r"\d+"  # Procura por um ou mais dígitos
texto = "A casa tem 4 quartos"
resultado = re.findall(padrao, texto)

# Substituindo parte da string com regex
novo_texto = re.sub(r"\d+", "X", texto)  # Substitui dígitos por "X"
```

### 15. **Classes e Objetos (Programação Orientada a Objetos)**
```python
# Definindo uma classe
class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def fazer_som(self):
        return f"O {self.nome} faz {self.som}"

# Criando um objeto
gato = Animal("gato", "miau")

# Acessando métodos e atributos
print(gato.fazer_som())
print(gato.nome)
```

### 16. **Funções Lambda**
```python
# Função lambda para somar dois números
soma = lambda x, y: x + y

# Usando a função lambda
resultado = soma(3, 5)
print(resultado)

# Ordenando uma lista de tuplas com lambda
pessoas = [("Alice", 25), ("Bob", 20), ("Carol", 30)]
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[1])
```

### 17. **Módulo `itertools` (Ferramentas para Iteradores)**
```python
import itertools

# Produto cartesiano
prod = itertools.product([1, 2], ['A', 'B'])
print(list(prod))  # [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

# Combinações
comb = itertools.combinations([1, 2, 3], 2)
print(list(comb))  # [(1, 2), (1, 3), (2, 3)]

# Permutações
perm = itertools.permutations([1, 2, 3])
print(list(perm))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

### 18. **Decorators**
```python
# Definindo um decorator simples
def meu_decorator(funcao):
    def wrapper():
        print("Algo antes da função")
        funcao()
        print("Algo depois da função")
    return wrapper

# Usando o decorator
@meu_decorator
def minha_funcao():
    print("Executando a função")

minha_funcao()
```

### 19. **Manipulação de Dados com `pandas`**
```python
import pandas as pd

# Criando um DataFrame
dados = {
    "Nome": ["Alice", "Bob", "Carol"],
    "Idade": [25, 30, 22],
    "Cidade": ["Salvador", "São Paulo", "Rio de Janeiro"]
}
df = pd.DataFrame(dados)

# Acessando colunas e linhas
print(df["Nome"])  # Coluna "Nome"
print(df.iloc[0])  # Primeira linha

# Filtrando dados
df_filtrado = df[df["Idade"] > 23]

# Estatísticas descritivas
estatisticas = df.describe()
```

### 20. **Mapeamento com `folium`**
```python
import folium

# Criando um mapa centrado em uma localização específica
mapa = folium.Map(location=[-12.9714, -38.5014], zoom_start=12)

# Adicionando um marcador no mapa
folium.Marker(location=[-12.9714, -38.5014], popup="Salvador").add_to(mapa)

# Exibindo o mapa
mapa.save("mapa.html")
```

 
