"""
Proyecto

 Primero vamos a hacer un login de usuario sencillo, en donde meteremos nuestro código cuando el usuario ingrese la información correcta. Comenzaremos ingresando elusuario y la contraseña necesarios para acceder a la información

 """

USUARIO = 'Jaaz_G'
CONTRASENA = 'Abcd1234'
Intentos = 3 #Número de intentos que daremos

"""En el código a continuación el usuario podrá ingresar su usuario y contraseña, los cuales, al no ser los correctos, enviarán un mensaje de error y reducirán el número de intentos que el usuario tiene para acceder. 

El código en sí es bastante repetitivo, pues se reduce a que con ayuda de un if se verifica si el usuario y contraseña son los correctos, y de no serlo se manda un mesaje y se vuelve a intentar, por lo que sólo comentaremos la primera parte del mismo"""

usuario_ingresado = input('Nombre de usuario: ') #se pide al usuario ingresar su nombre de usuario
if usuario_ingresado == USUARIO: #Si es el correcto, se procede
  contraseña_ingresada = input('Contraseña: ') #Se pide la contraseña al usuario
  if contraseña_ingresada == CONTRASENA: #Si la contraseña es correcta, se da la bienvenida al usuario:
    print('Bienvenido usuario, a continuación de presenta la información del reporte') 
  else: #Si la contraseña presentada no es correcta
    Intentos = Intentos-1 #Se reducen los intentos
    print('Contraseña equivocada, te quedan '+str(Intentos)+' intentos.') #Se a visa del error
    contraseña_ingresada = input('Contraseña: ') #Se vuelve a pedir la contraseña
    if contraseña_ingresada == CONTRASENA: #Se vuelve a corroborar si es correcta
      print('Bienvenido usuario, a continuación de presenta la información del reporte')
    else:
      Intentos = Intentos-1
      print('Contraseña equivocada, te quedan '+str(Intentos)+' intentos.')
      contraseña_ingresada = input('Contraseña: ')
      if contraseña_ingresada == CONTRASENA:
        print('Bienvenido usuario, a continuación de presenta la información del reporte')
      else:
        Intentos = Intentos-1
        print('Contraseña equivocada, te quedan '+str(Intentos)+' intentos.')
        if Intentos == 0: #Cuado el número de intentos llega a cero, se saca al usuario
          print('Lo sentimos, has utilizado el número máximo de intentos, no puedes ingresar.')
          exit() #Con ayuda de exit() el código se deja de ejecutar, por lo que el usuario ya no podría acceder a la información
else: #Esta opción es si se falla por primera vez en ingresar correctamente el usuario
  Intentos = Intentos - 1 #Se reducen los intentos
  print('El usuario ingresado no existe, te quedan '+str(Intentos)+' intentos.') #avisa del error
  usuario_ingresado = input('Nombre de usuario: ') #se pide de nuevo el usuario
  if usuario_ingresado == USUARIO: #si es correcto se repite el ciclo anterior
    contraseña_ingresada = input('Contraseña: ')
    if contraseña_ingresada == CONTRASENA:
      print('Bienvenido usuario, a continuación de presenta la información del reporte') 
    else:
      Intentos = Intentos-1
      print('Contraseña equivocada, te quedan '+str(Intentos)+' intentos.')
      contraseña_ingresada = input('Contraseña: ')
      if contraseña_ingresada == CONTRASENA:
        print('Bienvenido usuario, a continuación de presenta la información del reporte')
      else:
        Intentos = Intentos-1
        print('Contraseña equivocada, te quedan '+str(Intentos)+' intentos.')
        if Intentos == 0:
              print('Lo sentimos, has utilizado el número máximo de intentos, no puedes ingresar.')
              exit()
        else:
          contraseña_ingresada = input('Contraseña: ')
          if contraseña_ingresada == CONTRASENA:
            print('Bienvenido usuario, a continuación de presenta la información del reporte')
          else:
            Intentos = Intentos-1
            print('Contraseña equivocada, te quedan '+str(Intentos)+' intentos.')
            if Intentos == 0:
              print('Lo sentimos, has utilizado el número máximo de intentos, no puedes ingresar.')
              exit()
  else: 
    Intentos = Intentos - 1  #Si el usuario no es correcto una segunda vez, se vuelve a repetir el proceso
    print('El usuario ingresado no existe, te quedan '+str(Intentos)+' intentos.')
    usuario_ingresado = input('Nombre de usuario: ')
    if usuario_ingresado == USUARIO:
      contraseña_ingresada = input('Contraseña: ')
      if contraseña_ingresada == CONTRASENA:
        print('Bienvenido usuario, a continuación de presenta la información del reporte')
      else:
        Intentos = Intentos-1
        print('Contraseña equivocada, te quedan '+str(Intentos)+' intentos.')
        if Intentos == 0:
              print('Lo sentimos, has utilizado el número máximo de intentos, no puedes ingresar.')
              exit()
        else:
          contraseña_ingresada = input('Contraseña: ')
          if contraseña_ingresada == CONTRASENA:
            print('Bienvenido usuario, a continuación de presenta la información del reporte')
          else:
            Intentos = Intentos-1
            print('Contraseña equivocada, te quedan '+str(Intentos)+' intentos.')
            contraseña_ingresada = input('Contraseña: ')
            if contraseña_ingresada == CONTRASENA:
              print('Bienvenido usuario, a continuación de presenta la información del reporte')
            else:
              Intentos = Intentos-1
              print('Contraseña equivocada, te quedan '+str(Intentos)+' intentos.')
              if Intentos == 0:
                print('Lo sentimos, has utilizado el número máximo de intentos, no puedes ingresar.')
                exit()
    else: 
      Intentos = Intentos - 1 
      print('El usuario ingresado no existe, te quedan '+str(Intentos)+' intentos.')
      if Intentos == 0:
        print('Lo sentimos, has utilizado el número máximo de intentos, no puedes ingresar.')
        exit() #Si al final no se encontró el usuario, el programa nos saca

  """Notemos que el número de intentos puede ser gastado entre errores de nombre de usuario y contraseña, por lo que si se fallaran, por ejemplo, dos veces uno y una vez el otro, el programa nos sacaría. Una vez que nuestro usuario puede ingresar, podremos observar toda la información solicitada en el reporte, para lo cual se desarrolló el siguiente código.
  
   Lo primero que haremos, es importar las listas que nos serán útiles en este proyecto, pues en ellas está la información relevante del mismo. 
  """

from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
En cada caso vamos a considerar como producto a su nombre. 

Productos más vendidos y productos rezagados. 

> Hacer un listado con los 5 productos más vedidos y otro con los 10 productos más buscados:

Para poder obtener esta información, utilizaremos los recursos brindados en el archivo lifestore_file.py. 

Comenzaremos obteniendo los 5 productos más vendidos, para lo cual tenemos que hacer uso de las listas lifestore_products y lifestore_sales. 

""" 



numero_ventas = []  #Creamos una lista vacía que guardará listas formadas por el id del producto y el número de veces que fue vendido
mas_vendidos = [] #Creamos otra lista vacía, en la que sòlo se colocarán el total de ventas de cada producto

for producto in lifestore_products: #Se revisa cada producto en la lista
  obj = producto[0] #Se toma el id del producto
  ventas_obj = 0 #Se coloca un contador que alamacenará la cantidad de veces que ese producto fue comprado
  for venta in lifestore_sales: #Teniendo el id del producto, se revisa la lista de ventas
    if venta[1] == obj: #se compara el id del producto con cada venta
      ventas_obj = ventas_obj + 1 #Si se encuentra que el producto se vendió, el contador aumenta en una unidad
  mas_vendidos.append(ventas_obj)#Una vez que se termina de contar, se agrega el total de ventas por un producto
  numero_ventas.append([obj,ventas_obj])#En la otra lista se agrega el id del producto junto al número de ventas que tuvo, pues se usará más adelante

mas_vendidos.sort(reverse=True)#Usando el método sort, se ordena de mayor a menor la lista con el número de ventas

mejores5 = mas_vendidos[0:5] #Se crea una nueva lista, donde sólo tomaremos los 5 con mejores ventas

top5_ventas = []#Creamos una lista donde se colocaran los id de productos con mejores ventas


for producto in numero_ventas: #Para cada objeto en esta lista, donde teníamos almacenado el id producto con su venta, se busca si es el mejor vendido
  for top in mejores5: #De la lista de mejores ventas
    if producto[1]==top: #Se compara el valor de la venta con el valor de la venta para cada id_del producto
      if producto[0] in top5_ventas:#Esta línea es para no repetir productos
        do="no hace nada"
      else:
        top5_ventas.append(producto[0]) #Si coincide con estar en la lista de las mejores ventas, el id del producto se agrega a la lista de mejores vendidos


i = 0 #Se inicia un contador para marcar los más vendidos
los_5_mas_vendidos = [] #Creamos una lista vacía para los 5 más vendidos
print('-----Los cinco más vendidos son:')#Se coloca una leyenda para que el usuario pueda saber qué es la información a continuación
for elemento in top5_ventas: #Se checa cada id en la lista de los mejores vendidos
  i = i + 1 #Se aumenta el contador para ponerlo junto al nombre del producto
  for producto in lifestore_products:#Para cada producto en la lista de productos, se busca su id entre los mejores 
    if elemento == producto[0]:#Si coincide...
      los_5_mas_vendidos.append(producto[1])#Se agrega el producto a la lista de los 5 más vendidos
      print(str(i)+'.-'+producto[1])# Se imprime el contador (1,2,3 ...) + el nombre del producto
    if len(los_5_mas_vendidos) == 5: #línea para sólo mostrar 5 elementos aunque coincidan sus ventas
      break #Si se llega a 10elementos en la lista, se rompe el bucle
print(los_5_mas_vendidos)

"""
Una vez que se tiene el trabajo para los 5 más vendidos,
encontrar uno con los 10 más buscados es muy parecido, en este caso se utilizarán las listas lifestore_products y lifestore_searches
"""
numero_consultas = []  #Creamos una lista vacía que guardará listas formadas por el id del producto y el número de veces que fue vendido
mas_buscados = [] #Creamos otra lista vacía, en la que sòlo se colocarán el total de ventas de cada producto

for producto in lifestore_products: #Se revisa cada producto en la lista
  obj = producto[0] #Se toma el id del producto
  busqueda_obj = 0 #Se coloca un contador que alamacenará la cantidad de veces que ese producto fue buscado
  for busqueda in lifestore_searches: #Teniendo el id del producto, se revisa la lista de búsquedas
    if busqueda[1] == obj: #se compara el id del producto con cada busqueda
      busqueda_obj = busqueda_obj + 1 #Si se encuentra que el producto se buscó, el contador aumenta en una unidad
  mas_buscados.append(busqueda_obj)#Una vez que se termina de contar, se agrega el total de ventas por un producto
  numero_consultas.append([obj,busqueda_obj])#En la otra lista se agrega el id del producto junto al número de ventas que tuvo, pues se usará más adelante

mas_buscados.sort(reverse=True)#Usando el método sort, se ordena de mayor a menor la lista con el número de busquedas


masbuscados10 = mas_buscados[0:10] #Se crea una nueva lista, donde sólo tomaremos los 10 con más búsquedas


top10_busquedas = []#Creamos una lista donde se colocarán los id de productos con más búsquedas

for producto in numero_consultas: #Para cada objeto en esta lista, donde teníamos almacenado el id producto con su número de busquedas, se busca si está entre los más buscados
  for top in masbuscados10: #De la lista de mayores búsquedas
    if producto[1]==top: #Se compara el valor de búsquedas con el valor para cada id del producto
      if producto[0] in masbuscados10: #esta línea la colocamos para no repetir productos
        do="no hace nada"
      else:
        top10_busquedas.append(producto[0]) #Si coincide con estar en la lista de más buscados, el id del producto se agrega a la lista de más buscados

i = 0 #Se inicia un contador para marcar los más buscados
los_10_mas_buscados = [] #Creamos una lista vacía para los 10 más buscados

print('-----Los diez más buscados son:')#Se coloca una leyenda para que el usuario pueda saber qué es la información a continuación
for elemento in top10_busquedas: #Se checa cada id en la lista de los mejores vendidos
  i = i + 1 #Se aumenta el contador para ponerlo junto al nombre del producto
  for producto in lifestore_products:#Para cada producto en la lista de productos, se busca su id
    if elemento == producto[0]:#Si coincide...
      los_10_mas_buscados.append(producto[1])#Se agrega el producto a la lista de los más buscados
      print(str(i)+'.-'+producto[1])# Se imprime el contador (1,2,3 ...) + el nombre del producto
    if len(los_10_mas_buscados) == 10: #línea para sólo mostrar 10 elementos aunque coincidan sus búsquedas
      break #Si se llega a 10elementos en la lista, se rompe el bucle
print(los_10_mas_buscados)

"""
En cada caso se rompe el bucle cuando se llega al número de elementos que se busca tener en cada lista, pero puede haber elementos que coincidan con ese número de ventas o búsquedas. Para visualizar más fácilmente, dejaremos este filtro, pero se puede eliminar simplemente borrando la condición if que cuenta los elementos de la lista. 

 Para poder observar más claramente los productos rezagados, vamos a considerar también el inventario que se tiene de los productos, por lo que buscaremos los 10 objetos con más inventario, y los compararemos con aquellos de menor búsqueda (también vamos a ver aquellos menos buscados).

Aquí, usando la lista de los objetos buscados, simplemente invertimos el orden y llamamos menos_buscados a la lista con los 10 objetos menos buscados"""

mas_buscados_al_reves = sorted(mas_buscados, reverse=True)

menos_buscados = mas_buscados_al_reves[0:10]


top10_menosbusquedas = []#Creamos una lista donde se colocarán los id de productos con menos búsquedas

for producto in numero_consultas: #Para cada objeto en esta lista, donde teníamos almacenado el id producto con su número de busquedas, se busca si está entre los menos buscados
  for top in menos_buscados: #De la lista de menores búsquedas
    if producto[1]==top: #Se compara el valor de búsquedas con el valor para cada id del producto
      if producto[0] in top10_menosbusquedas:
        do="no hace nada"
      else:
        top10_menosbusquedas.append(producto[0])  #Si coincide con estar en la lista de más buscados, el id del producto se agrega a la lista de más buscados


i = 0 #Se inicia un contador para marcar los menos buscados
los_10_menos_buscados = [] #Creamos una lista vacía para los 10 menos buscados

print('-----Los diez menos buscados son:')#Se coloca una leyenda para que el usuario pueda saber qué es la información a continuación

for elemento in top10_menosbusquedas: #Se checa cada id en la lista de los mejores vendidos
  i = i+1
  for producto in lifestore_products:#Para cada producto en la lista de productos, se busca su id
    if elemento == producto[0]:#Si coincide...
      los_10_menos_buscados.append(producto[1])#Se agrega el producto a la lista de los menos buscados
      print(str(i)+'.-'+producto[1])# Se imprime el contador (1,2,3 ...) + el nombre del producto
    if len(los_10_menos_buscados) == 10: #línea para sólo mostrar 10 elementos aunque coincidan sus búsquedas
      break
print(los_10_menos_buscados)

"""Finalmente agregaremos a los objetos con más inventario"""

cantidad_inventario = []  #Creamos una lista vacía que guardará listas formadas por el id del producto y el stock que tiene
inventario_lista = [] #Creamos otra lista vacía, en la que sólo se colocará el stock de cada objeto

for producto in lifestore_products: #Se revisa cada producto en la lista
  obj = producto[0] #Se toma el id del producto
  inventario = producto[4] #Se toma su stock
  cantidad_inventario.append([obj,inventario])
  inventario_lista.append(inventario)

inventario_lista.sort(reverse=True)#Usando el método sort, se ordena de mayor a menor la lista con el número productos

masstock10 = inventario_lista[0:10] #Se crea una nueva lista, donde sólo tomaremos los 10 con más productos


top10_stock = []#Creamos una lista donde se colocarán los id de productos con más búsquedas

for producto in cantidad_inventario: #Para cada objeto en esta lista, donde teníamos almacenado el id producto con su número de productos, se busca si está entre los de más stock
  for top in masstock10: #De la lista de mayor reserva
    if producto[1]==top: #Se compara el valor de búsquedas con el valor para cada id del producto
      top10_stock.append(producto[0]) #Si coincide con estar en la lista de más buscados, el id del producto se agrega a la lista de más buscados

i = 0 #Se inicia un contador para marcar los más buscados
los_10_mas_reservas = [] #Creamos una lista vacía para los 10 más buscados

print('-----Los diez con más reservas son:')#Se coloca una leyenda para que el usuario pueda saber qué es la información a continuación
for elemento in top10_stock: #Se checa cada id en la lista de los mejores vendidos
  i = i + 1 #Se aumenta el contador para ponerlo junto al nombre del producto
  for producto in lifestore_products:#Para cada producto en la lista de productos, se busca su id
    if elemento == producto[0]:#Si coincide...
      if producto[0] in los_10_mas_reservas:
        do="no hace nada"
      else:
        los_10_mas_reservas.append(producto[1])#Se agrega el producto a la lista de los más buscados
      print(str(i)+'.-'+producto[1])# Se imprime el contador (1,2,3 ...) + el nombre del producto
    if len(los_10_mas_reservas) == 10: #línea para sólo mostrar 10 elementos aunque coincidan sus búsquedas
      break #Si se llega a 10elementos en la lista, se rompe el bucle
print(los_10_mas_reservas)





"""Lo siguiente por hacer es generar un listado de más y menos vendidos, pero considerando las categorías, por lo que se repetirá parte del trabajo anterior:
"""
categorias = [] #Creamos una lista vacía donde colocaremos todos las categorías en la lista
cat = None #Creamos una variable vacía que se utilizará para encontrar todas las categorías

for elemento in lifestore_products: #Para cada producto de la lista
  if elemento[3] != cat: #Se compara la categoría del producto con la variable cat, para encontrar los que son distintos
    categorias.append(elemento[3])#Si cumple ser distinto, se coloca al elemento en la lista de categorias
    cat = elemento[3]#Se renombra a la variable para que no se repitan categorías en la lista

"""Ya que se tiene la lista de categorías, podemos encontrar los elemenos menos vendidos y los menos buscados por categoría utilizando lo mismo que antes para cada una """
  
for cat in categorias: #Para cada categoría en la lista se va a realizar todo lo que viene a continuación:
  lifestore_products_category = []#Se crea una lista vacía para guardar cada producto que corresponda a la categoría que se esté revisando
  for prod in lifestore_products: #Se revisa cada producto en la lista
    if cat == prod[3]: #Se revisa su categoría
      lifestore_products_category.append(prod)#Se coloca al producto en la lista correspondiente

  numero_ventas_cat = []  #Creamos una lista vacía que guardará listas formadas por el id del producto y el número de veces que fue vendido
  ventas = [] #Creamos otra lista vacía, en la que sólo se colocarán el total de ventas de cada producto

  for producto in lifestore_products_category: #Se revisa cada producto en la lista
    obj = producto[0] #Se toma el id del producto
    ventas_obj = 0 #Se coloca un contador que alamacenará la cantidad de veces que ese producto fue vendido
    for venta in lifestore_sales: #Teniendo el id del producto, se revisa la lista de ventas
      if venta[1] == obj: #se compara el id del producto con cada venta
        ventas_obj = ventas_obj + 1 #Si se encuentra que el producto se vendió, el contador aumenta en una unidad
    ventas.append(ventas_obj)#Una vez que se termina de contar, se agrega el total de ventas por un producto
    numero_ventas_cat.append([obj,ventas_obj])#En la otra lista se agrega el id del producto junto al número de ventas que tuvo, pues se usará más adelante

  ventas.sort()#Usando el método sort, se ordena de menor a mayor la lista con el número de ventas

  peores5 = ventas[0:5] #Se crea una nueva lista, donde sólo tomaremos los 5 con peores ventas

  top5peores_ventas = []#Creamos una lista donde se colocaran los id de productos con más bajas ventas

  for producto in numero_ventas_cat: #Para cada objeto en esta lista, donde teníamos almacenado el id producto con su venta, se busca si es de bajas ventas
    for top in peores5: #De la lista de peores ventas
      if producto[1]==top: #Se compara el valor de la venta con el valor de la venta para cada id del producto
        if producto[0] in top5peores_ventas:
          do="no hace nada"
        else:
          top5peores_ventas.append(producto[0]) #Si coincide con estar en la lista de las ventas más bajas, el id del producto se agrega a la lista.

  i = 0 #Se inicia un contador para marcar los menos vendidos
  los_5_menos_vendidos_cat = [] #Creamos una lista vacía para los 5 menos vendidos por categoria
  print('-----Los cinco menos vendidos en la categoria' +' '+ cat+ ' ' + 'son:')#Se coloca una leyenda para que el usuario pueda saber qué es la información a continuación
  
  for elemento in top5peores_ventas: #Se checa cada id en la lista de los mejores vendidos
    i = i + 1 #Se aumenta el contador para ponerlo junto al nombre del producto
    for producto in lifestore_products_category:#Para cada producto en la lista de productos, se busca su id entre los peor vendidos
      if elemento == producto[0]:#Si coincide...
        los_5_menos_vendidos_cat.append(producto[1])#Se agrega el producto a la lista de los 5 menos vendidos por categoría
        print(str(i)+'.-'+producto[1])# Se imprime el contador (1,2,3 ...) + el nombre del producto"""
      if len(los_5_menos_vendidos_cat) == 5: #línea para sólo mostrar 5 elementos aunque coincidan sus búsquedas
        break #Si se llega a 5 elementos en la lista, se rompe el bucle
  print(los_5_menos_vendidos_cat)

  numero_consultas_cat = []  #Creamos una lista vacía que guardará listas formadas por el id del producto y el número de veces que fue vendido
  busquedas = [] #Creamos otra lista vacía, en la que sólo se colocarán el total de ventas de cada producto

  for producto in lifestore_products_category: #Se revisa cada producto en la lista
    obj = producto[0] #Se toma el id del producto
    busqueda_obj = 0 #Se coloca un contador que alamacenará la cantidad de veces que ese producto fue buscado
    for busqueda in lifestore_searches: #Teniendo el id del producto, se revisa la lista de búsquedas
      if busqueda[1] == obj: #se compara el id del producto con cada busqueda
        busqueda_obj = busqueda_obj + 1 #Si se encuentra que el producto se buscó, el contador aumenta en una unidad
    busquedas.append(busqueda_obj)#Una vez que se termina de contar, se agrega el total de ventas por un producto
    numero_consultas_cat.append([obj,busqueda_obj])#En la otra lista se agrega el id del producto junto al número de ventas que tuvo, pues se usará más adelante

  busquedas.sort()#Usando el método sort, se ordena de menor a mayor la lista con el número de busquedas


  menosbuscados10 = busquedas[0:10] #Se crea una nueva lista, donde sólo tomaremos los 10 con menos


  top10_busquedas = []#Creamos una lista donde se colocarán los id de productos con menos búsquedas

  for producto in numero_consultas_cat: #Para cada objeto en esta lista, donde teníamos almacenado el id producto con su número de busquedas, se busca si está entre los menos buscados
    for top in menosbuscados10: #De la lista de menores búsquedas
      if producto[1]==top: #Se compara el valor de búsquedas con el valor para cada id del producto
        if producto[0] in top10_busquedas:
          do="no hace nada"
        else:
          top10_busquedas.append(producto[0]) #Si coincide con estar en la lista de menos buscados, el id del producto se agrega a la lista de menos buscados

  i = 0 #Se inicia un contador para marcar los menos buscados
  los_10_menos_buscados_cat = [] #Creamos una lista vacía para los 10 menos buscados por categoría
  print('-----Los diez menos buscados en la categoria' +' '+ cat+ ' ' + 'son:') #Se coloca una leyenda para que el usuario pueda saber qué es la información a continuación
  for elemento in top10_busquedas: #Se checa cada id en la lista de los menos buscados
    i = i + 1 #Se aumenta el contador para ponerlo junto al nombre del producto
    for producto in lifestore_products:#Para cada producto en la lista de productos, se busca su id
      if elemento == producto[0]:#Si coincide...
        los_10_menos_buscados_cat.append(producto[1])#Se agrega el producto a la lista de los menos buscados
        print(str(i)+'.-'+producto[1])# Se imprime el contador (1,2,3 ...) + el nombre del producto
      if len(los_10_menos_buscados_cat) == 10: #línea para sólo mostrar 10 elementos aunque coincidan sus búsquedas
        break #Si se llega a 10elementos en la lista, se rompe el bucle
  print(los_10_menos_buscados_cat)

"""
A continuación se crearán dos listados de 5 productos cada uno, uno con los que tienen peores reseñas, y otros con las mejores. Para poder obtener esto, se hará uso de las listas lifestore_products y lifestore_sales. Recordemos que para cada venta hay una calificación que va de 1 a 5, que es lo que consideraremos para considerar la reseña. 

"""
todas_mejores_resenas = [] #Creamos una lista vacía para encontrar todos los productos con reseña 5
todas_peores_resenas = [] #Creamos una lista vacía para encontrar todos los productos con reseña 1
id_mejores=0
id_peores=0
for producto in lifestore_sales: # Buscamos en la reseña de cada producto de la lista de ventas
  if producto[2] == 5 and producto[1]!=id_mejores: #Si la reseña es 5, se agrega el producto a las mejores reseñas
    id_mejores = producto[1]
    todas_mejores_resenas.append(producto)
  elif producto[2] == 1 and producto[1]!= id_peores: #Si la reseña es 1 se agrega al producto a las peores reseñas
    id_peores = producto[1]
    todas_peores_resenas.append(producto)

#Dado que sólo queremos 5 productos en cada lista, arbitrariamente elegimos los primeros 5 de cada lista: 

top_mejores_resenados = todas_mejores_resenas[0:5]
top_peores_resenados = todas_peores_resenas[0:5]

#Creamos dos listas vacías para colocar los nombres de los productos correspondientes a los 5 mejor y 5 peor reseñados:

mejores_resenados = [] 
peores_resenados = []

for elemento in top_mejores_resenados: #En la lista de mejores reseñados
  for producto in lifestore_products: #Comparamos el id del producto en la lista de reseñados y en la lista general de productos
    if elemento[1] == producto[0]:
      mejores_resenados.append(producto[1]) #Si coincide el id, se agrega el nombre del roducto a la lista
for elemento in top_peores_resenados: #En la lista de peores reseñados 
  for producto in lifestore_products: #Comparamos el id del producto en la lista de reseñados y en la lista general de productos
    if elemento[1] == producto[0]:
      peores_resenados.append(producto[1]) #Si coincide el id, se agrega el nombre del roducto a la lista

i = 0 #Creamos un contador para listar los mejor reseñados
j = 0 #Creamos un contador para listar los peor reseñados
print('----- Los productos mejor reseñados (5), son:') #Anunciamos al usuario
for best in mejores_resenados: #Buscamos para los mejores de la lista
  i = i+1 #agregamos al contador 
  print(str(i)+'.-'+best) #Imprimimos el valor del bien reseñado
print(mejores_resenados) #imprimimos la lista
print('----- Los productos peor reseñados (1), son:') #Anunciamos al usuario 
for worst in peores_resenados: #Buscamos para los mejores de la lista
  j = j+1 #agregamos al contador
  print(str(j)+'.-'+worst) #Imprimimos el valor del mal reseñado
print(peores_resenados)  #imprimimos la lista


"""En cada uno de los ejercicios hechos hasta ahora, además de la lista con los nombres de los productos que se solicita, se realizó una lista de cada uno de los productos con la finalidad de facilitar la  visualización del trabajo.


El último inciso del proyecto solicita realizar el cálculo del total de ingresos y ventas promedio mensuales, además del total anual y los meses con más ventas en el año. Para poder calcular todo lo anterior, haremos uso de las listas lifestore_products y lifestore_sales, además de los recursos obtenidos en incisos anteriores .

Primero debemos hacer cáculos mensuales, por lo que crearemos una lista con los meses del año, además del año para hacer el cáculo de las ventas, los cuales obtendremos de la lista de ventas, donde ya tenemos el formato de la fecha:

"""

meses = [] #Creamos una lista vacía donde colocaremos los meses registrados
años = [] #Creamos una lista vacía que se utilizará para registrar los años
mes = None # Creamos una variable vacía que se utilizará para encontrar todos los valores
año = None # Creamos una variable vacía que se utilizará para encontrar todos los valores

for elemento in lifestore_sales: #Para cada venta de la lista
  comparador = elemento[3] #elegimos como elemento a comparar la fecha
  mes = comparador[3:5]#tomamos del lugar 3 al 5, que según el formato corresponde al mes
  if mes in meses: #checamos si ya registramos el mes en la lista de meses posibles
    a = 'no hacemos nada' #si ya está ahí el año, no hacemos nada
  else:  
    meses.append(mes) #si noe stá registrado, lo colocamos
  
meses.sort() #acomodamos la lista de meses de menor a mayor


for elemento in lifestore_sales: #Para cada venta de la lista
  comparador_a = elemento[3] # elegimos la fecha para comparar
  año = comparador_a[6:] #tomamos del lugar 6 al final, que corresponde al año
  if año in años: #Si el año ya está registrado en la lista de años posibles, no hacemos nada
    b = 'no hacemos nada'
  else: 
    años.append(año) # Si no está registrado, lo agregamos

años.sort() #organizamos la lista de años de menor a mayor

"""Ya que tenemos los meses y años posibles para las ventas, vamos a hacer el cálculo de ingresos y ventas promedio por mes, para lo cual consideraremos al ingreso mensual el total que se vendió en el mes y venta promedio el total de la venta del mes entre el número de ventas. Para poder calcular lo anterior, necesitamos dos datos importantes: el número de venta por producto y el costo del producto. 

Vamos a comenzar haciendo una lista que contenga el id del producto y su precio """

precios = [] #Creamos la lista vacía

for producto in lifestore_products: #para cada producto:
  precios.append([producto[0],producto[2]])#Se toma sólo el id y el precio

"""Ahora vamos a haces un bucle que haga nuestros cáculos, y además vamos a guardarlo todo en una lista. 

Nota: Debido a que los meses disponibles comienzan desde el '01', se obtiene desde ese mes para todos los años posibles"""

ventas_mensuales=[] #Creamos la lista con las ventas mensuales

for year in años: #Para cada año posible
  for month in meses: #Para cada mes posible
    venta_del_mes=[] #Creamos una lista vacía para las vemntas del mes
    total = 0 #Creamos un contador para el total de ventas
    promedio = 0 #Creamos un contador para calcular venta promedio
    ventas = 0 #Creamos un contador para el número de venntas
    for venta in lifestore_sales: #Para cada venta en la lista de ventas
      if venta[3][3:5] == month and venta[3][6:]== year: #Comparamos que el mes Y el año coincidan con los que estamos analizando
        venta_del_mes.append(venta) #Agregamos la venta a la lista de ventas del mes
        ventas = ventas + 1 #contamos la venta
    for producto in venta_del_mes: #para cada venta realizada
      for precio in precios: #y usando la lista de precios
        if producto[1] == precio[0]: #Comparamos el id del producto en ambas listas, y si coinciden:
          total = total + (ventas * precio[1]) #Sumamos la ganancia al total
          promedio = total/ventas #Y calculamos el promedio de ventas dividiendo el total entre el número de ventas
    ventas_mensuales.append([month,year,total,promedio,ventas]) #ya que revisé cada venta, agrego los datos importantes en forma de lista a mi lista de ventas mensuales
    print('Para el mes'+' '+month+' '+ 'del año' + ' '+ year+' '+'la venta total fue de' + ' '+ str(total)+ ', la venta promedio fue de '+' '+str(promedio)+' ' + 'y el número de ventas fue' + ' '+str(ventas)) #Imprimo este texto para que se entienda más claramente la información del mes

print(ventas_mensuales) #Esta es la lista con las ventas mensuales. 

"""Ahora tenemos que encontrar el total de ventas anual y los meses con más ventas, lo cual será más sencillo de calcular gracias a nuestra lista de ventas mensuales."""

total_anual = 0 #Creamos una variable vacía para calcular el total del año
ventas_anuales=[] #creamos una lista para llenar con el año y su venta total

for year in años: #para cada año posible
  for venta in ventas_mensuales: #para cada venta mensual
    if venta[1]==year: #si coincide el año de la venta con el año que analizamos
      total_anual= total_anual + venta[2] #sumamosla venta de ese mes a la venta del año
  print('Para el año'+' '+year+' '+'la venta fue de'+' '+str(total_anual)) #Una vez que sumamos sobre el año, mostramos el total del año 
  ventas_anuales.append([year,total_anual]) #Además agregamos el año y su venta correspondiente a nuestra lista
print(ventas_anuales) #Observamos nuestra lista

"""Para obtener los meses con mayores ventas, sólo tomaremos el valor de las ventas de la lista ventas_mensuales y la ordenaremos de menor a mayor, tomando, supongamos, los 5 meses con más ventas"""

valor_ventas_mensuales=[] #Creamos una lista vacía para registar el valor de las ventas mensuales

for registro in ventas_mensuales: #Para cada registo de las ventas mensuales
  valor_ventas_mensuales.append(registro[2]) #Se toma sólo el valor de las ganancias

valor_ventas_mensuales.sort(reverse=True) #Acomodamos la lista con los valores de ventas de mayor a menor
mejores_5_meses = valor_ventas_mensuales[0:5] #Suponiendo que buscamos los 5 meses con mayores ventas, elegimos esos valores de nuestra lista ordenada

lista_top5_meses =[] #Creamos una lista vacía para registrar los meses con su respectivo año (los mejores)

print('Los 5 meses con mejores ventas fueron:') #Le aviso al usuario la información que verá a continuación
for ganancia in mejores_5_meses: #Para cada una de las mejores 5 ganancias
  for ms in ventas_mensuales: #para cada mes en las ventas mensuales
    if ganancia == ms[2]: #comparo el valor de las ganancias registradas en cada lista
      lista_top5_meses.append([ms[0],ms[1]]) #si coinciden las ganacias, registro el respectivo mes y año en una lista
      print('mes'+' '+ms[0]+' '+'año'+' '+ms[1]) #Imprimo el valor del mes y el año con las mejores ventas

print(lista_top5_meses) #Observo la lista de los meses con lasmejores ventas. 

"""Un punto a destacar es que en cada caso se tiene primero el elemento que se acerca más a lo solicitado. Por ejemplo, si nos preguntamos por el producto con menos búsquedas, el primero que noes va a mostrar el algoritmo es el que menos búsquedas de todos tendría. En el caso de los meses con mejores ventas, el primero de la lista será el que mejores ventas de todos tuvo."""
    


      





      






  





      
   




  

  
  

  

