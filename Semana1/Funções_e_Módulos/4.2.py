calcular_potencia = lambda base, expoente: base ** expoente

calcular_perimetro_retangulo = lambda comprimento, largura: 2 * (comprimento + largura)

verificar_maior = lambda a, b: a if a > b else b

print(f"2 elevado a 8 = {calcular_potencia(2, 8)}")
print(f"Perímetro do retângulo (5x3) = {calcular_perimetro_retangulo(5, 3)}")
print(f"O maior entre 10 e 7 é: {verificar_maior(10, 7)}")
