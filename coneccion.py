import mysql.connector # SE IMPORTA LA LIBRERIA PARA MANEJAR LAS CONECCIONES MYSQL
from credenciales import * # LAS CREDENCIALES
coneccion = mysql.connector.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE) # SE INICIALIZA LA CONECCION A LA  BASE DE DATOS-
consultor=coneccion.cursor() 

consulta=["insert into persona(nombre) values('eduardo')", "select * from persona"]

while True: # BUCLE QUE REPETIRA LAS INSTRUCCIONES INDEFINIDAMENTE
    print ("opciones \n1. crear\n2. listar")
    opcion=input()
    
    if opcion=="1":
        print ("creando")
        consultor.execute(consulta[0]) # SE EJECUTA LA CONSULTA PARA CREAR UNA NUEVA PERSONA
        coneccion.commit()
        print(consultor.rowcount, "registro insertado")  
    
    elif opcion=="2":
        print ("listando")
        consultor.execute(consulta[1]) # SE EJECUTA LA CONSULTA PARA MOSTRAR LAS PERSONAS CREADAS
        resultado=consultor.fetchall()
        print (resultado)
        for x in resultado:
            print (x)
    else :
        print("opcion no entcontrada")
    print ("reiniciar? \n [s],[n]") 
    select=input()
    if select!="s": # ACTUA COMO DO-WHILE
        exit();

 