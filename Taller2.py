import random
import os

inventario={'Producto':['tornillos', 'placas', 'cables'], 'Cantidad':[500, 1000, 2000], 'Umbral':[200, 400, 1000]}

#Función para pedir cantidades y umbrales (numeros enteros positivos)
def numeroentero(mensaje):
    while True:
        try:
            numero=int(input(mensaje))
            if numero<0:
                print('\033[91mError!\033[0m Recuerde que debe ingresar un numero entero positivo')
            else:          
                break
        except ValueError:
            print('\033[91mError!\033[0m Recuerde que debe ingresar un numero entero positivo')
    return numero

#Función para agregar productos nuevos
def agregar(inventario):
    
    while True:
        nombre=input('Ingrese el nombre del producto: ')
        nombre=nombre.lower()
        if nombre not in inventario['Producto']:
            break
        else:
            print('\033[91mError!\033[0m Este producto ya existe en el inventario')

    cantidad=numeroentero('Ingrese la cantidad inicial del nuevo producto: ')
    umbral=numeroentero('Ingrese el umbral o cantidad minima en inventario: ')
    print(f'Producto {nombre} fue agregado exitosamente. Con una cantidad inicial de {cantidad} unidades y un umbral minimo de {umbral} unidades')

    return nombre, cantidad, umbral

#Función para simular consumo 
def consumofun(inventario):
    
    consumo=[]

    for elemento in inventario['Cantidad']:
        consumo.append(random.randint(0, elemento))
    
    for i in range(len(consumo)):        
        print(f"Consumo simulado de {consumo[i]} unidades de {inventario['Producto'][i]}")

    return consumo

#Función para reabastecer producto existente
def reabastecer(inventario):
    
    while True:
        nombre=input('Ingrese el nombre del producto que desea reabastecer: ')
        nombre=nombre.strip()
        nombre=nombre.lower()   
        
        if nombre in inventario['Producto']:            
            cantidad_re=numeroentero('Ingrese la cantidad que desea reabastecer: ')
            posicion=inventario['Producto'].index(nombre)
            inventario['Cantidad'][posicion]+=cantidad_re
            print(f'Producto {nombre} reabastecido exitosamente')
            break
        else:
            print('\033[91mError!\033[0m Este producto no existe en el inventario. Intentelo nuevamente.')

    return inventario

#main        
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print('\n ¿Qué deseas hacer? \n')
    print('1. Agregar producto')
    print('2. Simular consumo')
    print('3. Mostrar reporte del inventario')
    print('4. Calcular inventario total')
    print('5. Verificar alertas de reorden')
    print('6. Reabastecer producto')
    print('7. Salir')
    opcion=input('Elige una opción: ')
    

    if opcion=='1':
        print('\033[94mAgregar producto\033[0m')
        nombre, cantidad, umbral= agregar(inventario)
        inventario['Producto'].append(nombre)
        inventario['Cantidad'].append(cantidad)
        inventario['Umbral'].append(umbral)
        
        continuar=input('\nPresione enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif opcion=='2':
        print('\033[94mConsumo Simulado\033[0m')
        consumo=consumofun(inventario)
        for i in range(len(consumo)):
            inventario['Cantidad'][i]-=consumo[i]               
    
        continuar=input('\nPresione enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcion=='3':         
        print('\033[94mReporte de inventario\033[0m')
        print("\033[93m{:<10} {:<10} {:<10}\033[0m".format("Producto", "Cantidad", "Umbral"))
        for i in range(len(inventario['Cantidad'])):
            if inventario['Cantidad'][i]<=inventario['Umbral'][i]:
                print("{:<10} \033[91m{:<10}\033[0m {:<10}".format(inventario['Producto'][i], inventario['Cantidad'][i], inventario['Umbral'][i]))
            else:
                print("{:<10} \033[92m{:<10}\033[0m {:<10}".format(inventario['Producto'][i], inventario['Cantidad'][i], inventario['Umbral'][i]))                            

        continuar=input('\nPresione enter para continuar\n')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcion=='4':
        print('\033[94mInventario total\033[0m')
        inventario_total=sum(inventario['Cantidad'])
        print(f'El inventario total es: {inventario_total} unidades')
        
        continuar=input('\nPresione enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcion=='5':
        print('\033[94mAlertas de reorden\033[0m')
        no_alertas=True
        for i in range(len(inventario['Cantidad'])):
            if inventario['Cantidad'][i]<=inventario['Umbral'][i]:
                no_alertas=False
                print(f"\033[91mAlerta:\033[0m Es necesario reabastecer {inventario['Producto'][i]}. Cantidad actual: {inventario['Cantidad'][i]}. Umbral mínimo: {inventario['Umbral'][i]}")
        if no_alertas==True:
            print('No hay alertas de reorden, por el momento no es necesario reabastecer ningún producto')           

        continuar=input('\nPresione enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcion=='6':
        print('\033[94mReabastecimiento\033[0m')
        inventario=reabastecer(inventario)      

        continuar=input('\nPresione enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif opcion=='7':
        break
    else:
        print('Opción invalida. Intentelo nuevamente')
        continue