num = int(input("Digite um número inteiro para saber se é divisível por 3 ou 5: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
else:
    print(num)