nome = input('digite seu nome:')
idade = input('digite sua idade:')
print("seu nome é:", nome)
print("sua idade é:", idade)

if idade >='18' and idade <='27':
    print(f"{nome} tem {idade} anos de idade, por conta disso paga 10")
elif idade >='28':
    print(f"{nome} ja tem mais q 27 e paga 5")
else:
    print(f"{nome} tem {idade} anos de idade, por conta disso paga 15")