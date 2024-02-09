from flask import Flask
import mysql.connector
from credenciales import *
coneccion = mysql.connector.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DATABASE)
consultor = coneccion.cursor() 

app=Flask(__name__)
@app.route("/")
def home():
    return '<a href ="/consulta"> consulta</a> <a href ="/insercion"> insercion </a>'

@app.route('/consulta')
def consulta():
    consultor.execute("select * from persona")
    resultado=consultor.fetchall()
    print('consultando') 
    return resultado
    

@app.route('/insercion')
def insercion():
    consultor.execute("insert into persona(nombre) values('eduardo')")
    coneccion.commit()
    print(consultor.rowcount, "registro insertado")
    return 'insertando'

if __name__ =='__main__':
    app.run(debug=True ,host="0.0.0.0")