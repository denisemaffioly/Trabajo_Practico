mochila = ['campera', 'soga', 'linterna', 'sable de luz', 'botella de agua']

def usar_la_fuerza(mochila, objetos_sacados=0):
    
    if len(mochila) == 0:
        print('La mochila está vacía.')
        return None
    
    objeto = mochila.pop(0)
    
    if len(mochila) == 0:
            print('La mochila quedo vacia y el sable de luz no estaba adentro.')
    
    
    if objeto == 'sable de luz':
        print(f'El Jedi encontró el sable de luz después de sacar {objetos_sacados} objetos.')
        objetos_sacados += 1
        
    else:
        objetos_sacados = usar_la_fuerza(mochila, objetos_sacados + 1)
        
    return objetos_sacados

objetos_sacados = usar_la_fuerza(mochila)