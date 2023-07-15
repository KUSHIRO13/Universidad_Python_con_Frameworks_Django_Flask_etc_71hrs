# Ejercicio 4: Calculadora de impuesto
def calcularImpuestos(a=0.0, b=0.0):
    return a + a * (b / 100)


precion_neto = float(input("Proporcione  el precio neto del producto: "))
IVA = float(input("Proporcione  impuesto a pagar del producto: "))

resultado = calcularImpuestos(precion_neto, IVA)

print(f"El pago total es: {resultado}")
