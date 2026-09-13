# Entrada
temperatura=float(input("Digite a temperatura do laboratório, em C°:" ))

# Processamento e Saída
if temperatura <0:
    print("Temperatura abaixo de zero! Cuidado com o congelamento.")
elif temperatura <15:
    print("Frio intenso no laboratório.")
elif temperatura <25:
    print("Tetmperatura agradável.")
else:
    print("Temperatura alta! Ligar sistema de refrigeração.")
