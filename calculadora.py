#Trabalho de Programação Web de Gabriel Albuquerque da Silva / 2° ano de TADS

def calculadora():
    pilha = []
    simbolo = ["+", "-", "*", "/"]
    
    while True:
        num = input("Insira os valores (break para sair):")
        if num == "break":
            break
        if num in simbolo:
            if len(pilha) < 2:
                return "Erro: números insuficientes"
            if num == "+":
                num1, num2 = pilha.pop(), pilha.pop()
                pilha.append(num1 + num2)
                
            if num == "-":
                num1, num2 = pilha.pop(), pilha.pop()
                pilha.append(num1 - num2)
                
            if num == "*":
                num1, num2 = pilha.pop(), pilha.pop()
                pilha.append(num1 * num2)
                
            if num == "/":
                num1, num2 = pilha.pop(), pilha.pop()
                try:
                    pilha.append(num1 / num2)
                except:
                    return "Erro: divisão por zero"
        else:
            pilha.append(int(num))    
    return pilha.pop()
print(calculadora())