num = int(input("digite um numero: "))
anterior = 0
fibonacci = 1
while num > fibonacci:
    fibonacci = anterior + fibonacci
    anterior = fibonacci - anterior
  # print(fibonacci) # caso queira visualizar a sequencia até o numero escolhido
if num == fibonacci:
    print(f"o numero {num} pertence a sequencia fibonacci")
else:
    print(f"o numero {num} não pertence a sequencia fibonacci")