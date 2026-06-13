salario = float(input("Qual é o seu salário?:"))

if salario <1800:
        print ("Você é desempregado ou trabalha em outra empresa!")
elif salario >1800 and salario <=2000:
    print ("Você é jovem aprendiz ou estágiario")
elif salario >2000 and salario <= 3000:
    print (" Você é programador junior")
elif salario >3000 and salario <= 6000:
    print ("Você é programador pleno")
elif salario >6000 and salario <= 15000:
    print ("Você é programador senior")
else:
    print ("Você é gerente de projetos")
