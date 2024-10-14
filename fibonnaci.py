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
