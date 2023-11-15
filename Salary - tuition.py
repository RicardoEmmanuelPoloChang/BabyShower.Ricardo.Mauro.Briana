seller = input("Is there any seller? (yes/no): ")

while seller == "yes":
  nombre= str(input("What´s their name? "))
  salario= float(input("What is their base salary? "))
  ventas = float(input("How much have they generated in sales? "))

  salariopequeño = salario+(ventas*0.07)
  salariomediano = salario+(ventas*0.10)
  salariopro = salario+(ventas*0.15)
  
  if ventas < 3500:
    print(f"The total salary of {nombre} is {salariopequeño}")
  elif ventas >= 3500 and ventas <= 7000:
     print(f"The total salary of {nombre} is {salariomediano}")
  elif ventas > 7000:
     print(f"The total salary of {nombre} is {salariopro}")
    
  seller = input("Is there any other seller?(yes/no):")
