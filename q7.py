num = int(input('Digite um número com 3 digitos: '))
nume = num
inv = 0
inv = inv * 10 + num % 10
num //= 10
inv = inv * 10 + num % 10
num //= 10
inv = inv * 10 + num % 10
if inv == nume:
    print(f'O número {nume} é palíndromo!')
else:
    print(f'O número {nume} não é palíndromo!')