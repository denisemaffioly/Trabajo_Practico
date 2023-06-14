def contador(palabra, vector):
  cantidad = 0
  
  if len(vector) == 0:
    return None
  else:
    for palabra_buscada in vector:
      if palabra == palabra_buscada:
        cantidad += 1
  return cantidad

vector= ["python", "pan", "gato", "python", "escuela"]
palabra = "python"
resultado = contador(palabra, vector)
print(f"{palabra} aparece {resultado} veces en el vector.")