#TERCEIRA QUESTÃO
num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero : '))
num3 = int(input('Terceiro numero: '))

    
maior = num1

if (num2 > maior):
        maior = num2
if (num3 > maior):
        maior = num3

print('Maior: ',maior)

    
menor = num1

if (num2 < menor):
        menor = num2
if (num3 < menor):
        menor = num3

print('Menor: ',menor)
