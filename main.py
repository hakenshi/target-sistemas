# Exercício 1:
def is_fibonnaci(n):
    a, b = 0, 1

    if n < 0:
        return False

    while a < n:
        a, b = b, a + b

    return a == n


def fibonnaci(n):

    sequence = []
    a, b = 0, 1

    while a <= n:
        sequence.append(a)
        a, b = b, a+b

    return sequence


def main():
    try:
        n = int(input("Insira um número: \n"))
        if is_fibonnaci(n) == False:
            print(f'{n} não faz parte da sequência de fibonnaci')
        else:
            print(f'Sequência de fibonnaci de {n} até: {fibonnaci(n)}')
    except ValueError:
        print("Por favor insira um valor válido")

if __name__ == '__main__':
    main()


# Exercício 2:

# def letter_counter(frase: str):
#     counter = 0
#     frase_lower = frase.lower()

#     for _ in frase_lower:
#         if "a" in frase_lower:
#             counter+=1
#         else:
#             return f'A frase não possuí caracteres A.'

#     return f'A frase {frase} tem {counter} letras "A"'


# print(letterCounter("banana"))

# Exercício 3:

# indice: int = 12
# soma: int = 0
# k: int = 1

# while (k < indice):
#     k = k + 1
#     soma = soma + k

# print(soma)

# Resultado: 77

# Exercício 4:

# a) 9
# b) 128
# c) 49
# d) 72
# e) 13
# f) 22

# Exercício 5:
"""
Uma boa solução para esse problema é acionar o interruptor da lâmpada A e esperar em torno de 5 a 10 minutos.
após ter se passado esse tempo, acionar  o interruptor da lâmpada B e apagar a lâmpada A.
e em seguida ir até as salas onde estão as lâmpadas e verificar qual lâmpada foi acesa.
A lâmpada que estiver quente é lâmpada A, a lâmpada que estiver acesa é a lâmpada B e que estiver apagada é a lâmpada C. 
"""
