def dividir (numerador, denominador):
  if denominador == 0:
    return (None, "Deu erro")
  return(numerador / denominador, None)

resultado, erro = (10, 5)
if not erro:
  print(resultado)
else:
  print(erro)