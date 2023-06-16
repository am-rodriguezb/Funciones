def calcular_iva(valor_compra:int):
    iva_1=0.19
    valor_iva_producto=valor_compra*iva_1
    return valor_iva_producto

def descuento_producto(valor_sin_descuento:int,porcentaje_descuento:int):
    descuento=valor_sin_descuento*(porcentaje_descuento/100)
    return valor_sin_descuento-descuento

def calcular_IMC(peso,altura):
    #peso dividido en (altura al cuadrado)
    estado="no calculado"
    IMC=peso/altura**2
    if IMC<18.5:
        estado="bajo peso"
    elif IMC>=18.5 and IMC<=24.9:
        estado="adecuado"
    elif IMC>=25 and IMC<=29.9:
        estado="sobrepeso"
    elif IMC>=30 and IMC<=34.9:
        estado="obesida grado 1"
    elif IMC>=35 and IMC<=39.9:
        estado="mr bombastic"
    elif IMC>40:
        estado="che, le estas haciendo competencia a nicobacado"

    return estado + "IMC=" + str(IMC)
