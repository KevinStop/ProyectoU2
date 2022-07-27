#Permite acceder a las funcionalidades del sistema operativo
import os
#Import flask library
from flask import Flask, render_template, request, flash, redirect, url_for
#Importacion libreria para la coneccion con MongoDb
import pymongo

#Conexion con MongoDb


#Iniciar variable de aplicacion 
app = Flask(__name__)
app.debug = False
#Instanciamiento de la carpeta Static para acceder 
app._static_folder = os.path.abspath("templates/static/")

# Secret key for session
app.secret_key = 'mysecretkey'

#ruta principal 
@app.route("/")
#Función principal que llamará a la página HTML
def principal():
    return render_template("layouts/index.html")

#Metodo

#Ruta Login Docente
@app.route('/Login_Docente')
#Funcion de ingreso a la pagina Login de Docente
def Login_Docente():
    return render_template('layouts/Login_Docente.html')

#Ruta de tabla de alumnos
@app.route('/Tabla_Alumnos')
#Funcion de ingreso a la pagina tabla de alumnos
def Tabla_Alumnos():
    return render_template('layouts/Tabla_Alumnos.html')

#Ruta Juego de pares
@app.route('/JuegoPares')
#Funcion de ingreso a la pagina del juego
def JuegoPares():
    return render_template('layouts/Juego_Memoria.html')


# main del programa 
if __name__ == "__main__":
    #debug = true, para reiniciar automaticamente el servidor, tiempo de desarrollo
    app.run(debug=True) # Para ejecutar la aplicacion