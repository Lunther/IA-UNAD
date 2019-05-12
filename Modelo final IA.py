#Sistema para identificar entre Gripe y Resfriado
#Universidad Nacional Abierta y a Distancia
#2019
#Alumnos: Luis Botero y Sergio Zapata
#Úlitmo ajuste 05/05/2019


from sklearn import tree
#Construcción del array de atributos
features = [[36.5, 0, 1], [37.3, 1, 0], [35, 0, 1], [38.9, 1, 0], [36, 0, 1], [36.9, 1, 0], [36.6, 0, 1], [38, 1, 0], [36.4, 0, 1], [37.6, 0, 0], [41, 1, 0], [39.2, 1, 0], [39, 1, 0], [36, 0, 1], [37, 0, 1], [37.5, 0, 1], [36, 0, 1], [38.6, 1, 0], [35, 0, 1], [38, 1, 0]]

#Construcción del array de respuestas
labels = [0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1]

#Construcción del clasificador se construye en esta fase y permite realizar la clasificación
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#Prueba para conocer como funciona el algoritmo, con base en las selecciones del usuario.

#Menú que recibe datos por teclado por parte del usuario final.
print ("Ingrese la temperatura en grados celcius -separe con puntos-")
fiebre = input()
print ("Ingrese si la persona tiene dolo -En caso afirmativo escriba 1, sino 0- ")
dolor = input()
print ("Ingrese si la persona tiene congestión nasal fuerte -En caso afirmativo escriba 1, sino 0- ")
congestion = input()

#Evaluación de la máquina con base en la base de conocimiento descrita entre las lineas 10-17
resultado = (clf.predict([[fiebre, dolor, congestion]]))

#Traducción al usuario final y salida en pantalla.
if resultado == 0:
  print ("El resultado de la persona es: Resfriado")  
else: 
  print ("El resultado de la persona es: Gripa")  

