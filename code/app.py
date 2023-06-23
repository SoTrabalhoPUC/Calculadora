import sympy as sp
from colorama import Fore
x = sp.symbols('x')

#Autores: Gabriel Ribeiro Todt Ferreira, Marcos Eduardo Melin Araujo

#Função para calcular integrais indefinidas
def integral_indefinida(expr):
    simbolica = sp.sympify(expr)
    integral = sp.Integral(simbolica, x)
    print("Expressão:"+Fore.GREEN)
    print("\n")
    sp.pprint(integral)
    print("\n")
    print(Fore.RESET+"Antiderivada:\n"+Fore.GREEN)
    sp.pprint(integral.doit())
    print(Fore.RESET+"\n")
   

#função para calcular integrais definidas
def integral_definida(expt, inferior, superior):
    simbolica = sp.sympify(expr)
    integral = sp.Integral(simbolica, x)
    integralDmst = sp.Integral(simbolica, (x,inferior,superior)) ##Apenas para mostrar na tela 
    integral = integral.doit()
    print("Atiderivada:\n"+Fore.GREEN)
    sp.pprint(integralDmst)
    print(Fore.RESET)
    print("Substituição\n"+Fore.GREEN)
    sp.pprint(integral.subs(x,superior))
    print(Fore.GREEN+"-")
    sp.pprint(integral.subs(x,inferior))
    print()
    print(Fore.RESET+"Resultado:\n"+Fore.GREEN)
    sp.pprint(integralDmst.doit())
    print(Fore.RESET)

##Função para calcular integrais por partes
def integral_partes(exp, u, dv):
    du = sp.diff(u,x)
    v = sp.integrate(dv, x)
    print("Valor de du:\n"+Fore.GREEN)
    dx = sp.symbols('dx')
    sp.pprint(du*dx)
    print(Fore.RESET)
    print("Valor de V:\n"+Fore.GREEN)
    sp.pprint(v)
    print(Fore.RESET)
    print("Integral reescrita por por partes:\n"+Fore.GREEN)
    integral = u * v - sp.Integral(v * du, x)
    sp.pprint(integral)
    print(Fore.RESET)
    print("Expressão final:\n"+Fore.GREEN)
    integral = u * v - sp.integrate(v * du, x)
    sp.pprint(integral)
    print(Fore.RESET)

#Menu
while True:
    print((12*"==")+"MENU"+12*"==")
    print("Manual de cores: "+Fore.GREEN+"Operações(+,-,*..) "+Fore.RESET+"&"+Fore.RED+" Erros"+Fore.RESET)
    opt = (input("1 -> Integral indefinida\n2 -> Integral definida\n3 -> Integral por partes\n0 -> Sair\n"))
    try:#Contornar um possivel erro de digitação do usuário
        if int(opt) == 1:
            expr = input("Expressão desejada: ")
            print("\n")
            integral_indefinida(expr)
        elif int(opt) == 2:
            expr = input("Expressão desejada: ")
            inferior = int(input("Limite inferior: "))
            superior = int(input("Limite superior: "))
            print("\n")
            integral_definida(expr, inferior, superior)
            
        elif int(opt) == 3:
            expr = input("Expressão desejada: ")
            u = sp.sympify(input("Substituição por u: "))
            dv = sp.sympify(input("Substituição por dv: "))
            integral_partes(expr, u,dv)
        elif int(opt) == 0:
            break
        else:
            print(Fore.RED+"Opção inválida"+Fore.RESET)

    except:
        print(Fore.RED+"Opção inválida"+Fore.RESET)




