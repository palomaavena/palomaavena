#Comandos básicos:

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

