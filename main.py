# 1- Ao final do processamento, qual será o valor da variável SOMA
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(f"a soma é igual a:" ,SOMA)

print(f".....................................................")  

# 2-  Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 
# valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
# escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False

numero_desejado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero_desejado):
    print(f"O número {numero_desejado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_desejado} NÃO pertence à sequência de Fibonacci.")

print(f".....................................................")    

# 3- Descubra a lógica e complete o próximo elemento:

def proximo_elemento_a(n):
    return n + 2

def proximo_elemento_b(n):
    return n * 2

def proximo_elemento_c(n):
    return (int(n ** 0.5) + 1) ** 2

def proximo_elemento_d(n):
    return ((int(n ** 0.5) / 2) + 1) ** 2 * 4

def proximo_elemento_e(n1, n2):
    return n1 + n2

def proximo_elemento_f(n, incremento):
    return n + incremento

# Sequência a
sequencia_a = [1, 3, 5, 7]
print("Sequência a:")
for elemento in sequencia_a:
    print(elemento, end=", ")
print(proximo_elemento_a(sequencia_a[-1]))

# Sequência b
sequencia_b = [2, 4, 8, 16, 32, 64]
print("\nSequência b:")
for elemento in sequencia_b:
    print(elemento, end=", ")
print(proximo_elemento_b(sequencia_b[-1]))

# Sequência c
sequencia_c = [0, 1, 4, 9, 16, 25, 36]
print("\nSequência c:")
for elemento in sequencia_c:
    print(elemento, end=", ")
print(proximo_elemento_c(sequencia_c[-1]))

# Sequência d
sequencia_d = [4, 16, 36, 64]
print("\nSequência d:")
for elemento in sequencia_d:
    print(elemento, end=", ")
print(proximo_elemento_d(sequencia_d[-1]))

# Sequência e
sequencia_e = [1, 1, 2, 3, 5, 8]
print("\nSequência e:")
for elemento in sequencia_e:
    print(elemento, end=", ")
print(proximo_elemento_e(sequencia_e[-1], sequencia_e[-2]))

# Sequência f
sequencia_f = [2, 10, 12, 16, 17, 18, 19]
print("\nSequência f:")
incremento = 2
for elemento in sequencia_f:
    print(elemento, end=", ")
print(proximo_elemento_f(sequencia_f[-1], incremento))

print(f".....................................................")    

# 4- Você está em uma sala com três interruptores, 
# cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da 
# sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
# Seu objetivo é descobrir qual interruptor controla qual lâmpada.

# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

def descobrir_interruptores():
    # Ligar o primeiro interruptor
    print("Ligando o primeiro interruptor...")
    # Simular o comportamento das lâmpadas
    l1, l2, l3 = False, False, False
    l1 = not l1
    print("Verificando as lâmpadas...")

    # Desligar o primeiro interruptor e ligar o segundo interruptor
    print("Desligando o primeiro interruptor e ligando o segundo interruptor...")
    l2 = not l2
    print("Verificando as lâmpadas...")

    # Desligar o segundo interruptor e ligar o terceiro interruptor
    print("Desligando o segundo interruptor e ligando o terceiro interruptor...")
    l3 = not l3
    print("Verificando as lâmpadas...")

    # Determinar qual interruptor controla cada lâmpada
    if l1:
        print("A lâmpada 1 está acesa. O interruptor 1 controla esta lâmpada.")
    else:
        print("A lâmpada 1 está apagada. O interruptor 1 controla esta lâmpada.")

    if l2:
        print("A lâmpada 2 está acesa. O interruptor 2 controla esta lâmpada.")
    else:
        print("A lâmpada 2 está apagada. O interruptor 2 controla esta lâmpada.")

    if l3:
        print("A lâmpada 3 está acesa. O interruptor 3 controla esta lâmpada.")
    else:
        print("A lâmpada 3 está apagada. O interruptor 3 controla esta lâmpada.")

print(f".....................................................")    

# 5- Escreva um programa que inverta os caracteres de um string.


# IMPORTANTE:

# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

# Exemplo de uso
entrada = input("Digite uma string: ")
string_invertida = inverter_string(entrada)
print("String invertida:", string_invertida)
