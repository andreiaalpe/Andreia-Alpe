# cria uma função
def biscoito():
    x = "está com fome!"
    print("Joca", x)


#name = "Joca da Silva"
#age=43


name = input("Qual o seu nome?")
age = input("Quantos anos você tem?")

age = int(age)

print(type (name))
print(type(age))
older = age + 10 
print(f"{name} terá {older} daqui a 10")

print("Olá", name, "!")
print()
print("Você tem", age, "anos")

print()

biscoito()


