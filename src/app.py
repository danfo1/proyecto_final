import os

from dotenv import load_dotenv
from flask import (Flask, flash, jsonify, redirect, render_template, request,
                   session, url_for)
from flask_cors import CORS
from flask_mail import Mail, Message
from flask_mysqldb import MySQL
from route.orden import ORDEN
from route.usuario import usuario
from route.vehiculo import vehiculo1

app = Flask(__name__)
CORS(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mg'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST' and 'usuario' in request.form and 'contrasena' in request.form:
        nombreusu = request.form['usuario']
        contrasena = request.form['contrasena']
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE nombreusu=%s and contrasena=%s", (nombreusu, contrasena))
        account = cursor.fetchone()  # Utiliza fetchone para obtener una sola fila
        cursor.close()  # Cierra el cursor después de usarlo
        
        if account:
            session['logeado'] = True
            session['id'] = account['idusu']
            session['rol'] = account['fk_id_rol']
            return redirect('/inicio')  
        else:   
            flash('Nombre de usuario o contraseña incorrectos')
        
    return render_template('login.html')

# Configuración del servidor SMTP de Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'vtovarcapera19@gmail.com'
app.config['MAIL_PASSWORD'] = os.getenv("PASSWORD")

# Configuración de Flask-Mail
mail = Mail(app)

# Carga las variables de entorno desde el archivo .env
load_dotenv()

@app.route('/enviar-correos-usuarios', methods=['POST'])
def enviar_correos_usuarios():
    try:
        # Verifica si el usuario actual está logueado
        if 'logeado' in session and session['logeado']:
            # Obtiene la lista de usuarios registrados en la base de datos
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT u.correo FROM usuario u JOIN rol r ON u.fk_id_rol = r.id_rol WHERE r.nombre_rol IN ('Recepcionista', 'Cliente Jurídico', 'Cliente Natural')")
            usuarios = cursor.fetchall()
            cursor.close()

            # Si hay usuarios y el usuario actual es administrador, envía correos
            if usuarios and session.get('rol') == 1:
                for usuario in usuarios:
                    enviar_correo(usuario['correo'], "Mantenimiento preventivo", "Su vehículo aplica para un mantenimiento preventivo.")

                return jsonify({'success': True, 'message': 'Correos electrónicos enviados exitosamente'})
            else:
                return jsonify({'success': False, 'message': 'El usuario no es administrador'})
        else:
            return jsonify({'success': False, 'message': 'Usuario no autenticado'})
    except Exception as e:
        print('Error al enviar correos:', str(e))
        return jsonify({'success': False, 'message': f'Error al enviar correos electrónicos: {str(e)}'})

def enviar_correo(destinatario, asunto, mensaje):
    try:
        msg = Message(asunto, sender='vtovarcapera19@gmail.com', recipients=[destinatario])
        msg.body = mensaje
        mail.send(msg)
        print(f'Correo enviado a {destinatario}')
        return True
    except Exception as e:
        print(f'Error al enviar correo a {destinatario}: {str(e)}')
        return False
    
    
@app.route("/inicio")
def inicio():
    if 'logeado' in session and 'rol' in session:
        if session['rol'] == 1:
            mostrar_alerta_correos = True  # Define la variable según la lógica de tu aplicación
            return render_template('inicio.html', mostrar_alerta_correos=mostrar_alerta_correos)    
        elif session['rol'] == 4:
            return render_template('cliente.html')
        elif session['rol'] == 3:
            return render_template('recepcionista.html')
        elif session['rol'] == 2:
            return render_template('tecnico.html')
    
    # Si no se cumple ninguna condición, devolver algo (puede ser un redirect, un render_template, etc.
    return redirect('/login')

@app.route('/seguimiento')
def seguimiento():
    return render_template('seguimiento.html')

@app.route('/logout')
def logout():
    session.pop('idusu', None)  
    return render_template('/login.html') 

@app.route("/ini")
def ini():
    return render_template('admin.html')
@app.route("/ini2")
def ini2():
    return render_template('recepcionista.html')
@app.route("/ini3")
def ini3():
    return render_template('tecnico.html')
@app.route("/ini4")
def ini4():
    return render_template('cliente.html')
@app.route("/segui")
def ini5():
    return render_template('seguimiento.html')

app.register_blueprint(ORDEN)
app.register_blueprint(vehiculo1)
app.register_blueprint(usuario)
if __name__ == '__main__':
    app.secret_key="daniel_forero"
    app.run(debug=True , host='0.0.0.0', port=5000 , threaded=True) 






    

    

        
 

       

    
