from Operacoes import soma,subtracao,multiplicacao,divisao

def main():
    a = int(input())
    operador = input()
    b = int(input())

    if operador == "+":
          print(f"= {soma(a, b)}")
    elif operador == "-":
          print(f"= {subtracao(a, b)}")   
    elif operador == "*":
          print(f"= {multiplicacao(a, b)}") 
    elif operador == "/":
          print(f"= {divisao(a, b)}")  
    else:
          print("Operador inválido. Use +,-,*, ou /.")
          

if __name__ == "__main__":
    main()