import os

from flask import (Blueprint, Flask, flash, redirect, render_template, request,
                   session)
from flask_mysqldb import MySQL

usuario=Blueprint('usuario',__name__)
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,  'templates')

app = Flask(__name__, template_folder=template_dir)
mysql = MySQL(app)


        
@usuario.route('/usuario.consultar', methods=['GET', 'POST'])
def consultar():
    try:
        cursor = mysql.connection.cursor()
        usuarios = []

        if request.method == "POST" and 'txtBuscar' in request.form:
            search_query = '%' + request.form['txtBuscar'] + '%'
            print("Valor de búsqueda:", search_query)
            cursor.execute("SELECT idusu, nombres, apellidos, tipo_documento, num_documento, correo, telefono, telefono_respaldo, estado, contrasena, nombreusu, fk_id_rol FROM usuario WHERE nombres LIKE %s", (search_query,))
        else:
            cursor.execute("SELECT idusu, nombres, apellidos, tipo_documento, num_documento, correo, telefono, telefono_respaldo, estado, contrasena, nombreusu, fk_id_rol FROM usuario")

        usuarios = cursor.fetchall()
        cursor.close()

        # Depurar datos recuperados
        print("Usuarios:", usuarios)

        return render_template("usuario/consultar.html", usuarios=usuarios)

    except Exception as e:
        print("Error en la consulta SQL:", str(e))
        return "Error en la consulta SQL. Por favor, verifica la base de datos y la consulta."
    
    
@usuario.route('/usuario.consultarresep', methods=['GET', 'POST'])
def consultarresep():
    try:
        cursor = mysql.connection.cursor()
        usuarios = []

        if request.method == "POST" and 'txtBuscar' in request.form:
            search_query = '%' + request.form['txtBuscar'] + '%'
            print("Valor de búsqueda:", search_query)
            cursor.execute("SELECT idusu, nombres, apellidos, tipo_documento, num_documento, correo, telefono, telefono_respaldo, estado, contrasena, nombreusu, fk_id_rol FROM usuario WHERE nombres LIKE %s", (search_query,))
        else:
            cursor.execute("SELECT idusu, nombres, apellidos, tipo_documento, num_documento, correo, telefono, telefono_respaldo, estado, contrasena, nombreusu, fk_id_rol FROM usuario")

        usuarios = cursor.fetchall()
        cursor.close()

        # Depurar datos recuperados
        print("Usuarios:", usuarios)

        return render_template("usuario/consultarresep.html", usuarios=usuarios)

    except Exception as e:
        print("Error en la consulta SQL:", str(e))
        return "Error en la consulta SQL. Por favor, verifica la base de datos y la consulta."
    
@usuario.route("/usuario.correo", methods=['GET', 'POST'])
def correo():
    if request.method == 'POST':
        correo = request.form.get('correo')
        
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE correo = %s", (correo,))
        user = cursor.fetchone()
        cursor.close()
        
        if user:
            session['logeado'] = True
            session['correo'] = user['correo']
            return render_template('usuario/contraseña.html', correo=user['correo'])
        else:
            flash("Correo no encontrado")
        
    return render_template('usuario/correo.html')

@usuario.route('/actualizar_contraseña', methods=['POST'])
def actualizar_contraseña():
    if 'logeado' in session and session['logeado']:
        contrasena_nueva = request.form.get('contrasena_nueva')
        confirmar_contrasena = request.form.get('confirmar_contrasena')

        # Validar que la "Contraseña Nueva" y la "Confirmar Contraseña" coincidan
        if contrasena_nueva != confirmar_contrasena:
            flash("Error al actualizar la contraseña. Las contraseñas no coinciden.", 'error')
            return redirect('/correo')  # Redirige de vuelta a la página de inicio de sesión o recuperación de contraseña

        correo = session.get('correo')
        cursor = mysql.connection.cursor()
        sql = ("UPDATE usuario SET contrasena = %s WHERE correo = %s")
        data = (contrasena_nueva, correo)
        cursor.execute(sql, data)
        mysql.connection.commit()
        cursor.close()
        session.clear()
        flash("Contraseña actualizada con éxito", 'success')
    
    return redirect('usuario.correo')
    

@usuario.route('/usuario.registrar', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        tipo_documento = request.form["tipo_documento"]
        num_documento = request.form["num_documento"]  
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        telefono_respaldo = request.form["telefono_respaldo"]
        estado = request.form["estado"]
        contrasena = request.form["contrasena"]
        nombreusu = request.form["usuario"]
        rol = request.form["rol"]
        
        if nombres and apellidos and tipo_documento and num_documento and correo and telefono and telefono_respaldo and estado and contrasena and nombreusu and rol:
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO usuario (nombres, apellidos, tipo_documento, num_documento, correo, telefono, telefono_respaldo , estado, contrasena, nombreusu, fk_id_rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            data = (nombres, apellidos, tipo_documento, num_documento, correo, telefono, telefono_respaldo, estado, contrasena, nombreusu, rol)
            cursor.execute(sql, data)
            mysql.connection.commit()
            cursor.close() 
            return redirect('/usuario.consultar')
        if not all([nombres, apellidos, tipo_documento, num_documento, correo, telefono, estado, contrasena, nombreusu]):
            return "Por favor, complete todos los campos obligatorios."
        
        return render_template('usuario/registrar.html')

    return render_template('usuario/registrar.html')



@usuario.route('/usuario.editar/<int:idusu>', methods=['GET', 'POST'])
def editar(idusu):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE idusu = %s", (idusu,))
        data = cursor.fetchone()
        cursor.close()

        if data:
            return render_template('usuario/editar.html', data=data)
        else:
            return "No encontrado"
    elif request.method == 'POST':
        nombres = request.form.get('nombres')
        apellidos = request.form.get('apellidos')
        tipo_documento = request.form.get('tipo_documento')
        num_documento = request.form.get('num_documento')
        correo = request.form.get('correo')
        telefono = request.form.get('telefono')
        telefono_respaldo = request.form.get('telefono_respaldo')
        estado = request.form.get('estado')
        contrasena = request.form.get('contrasena')
        nombreusu = request.form.get('nombreusu')
        rol = request.form.get('rol')
        
        cursor = mysql.connection.cursor()
        sql = ("UPDATE usuario SET nombres = %s, apellidos = %s, tipo_documento = %s, num_documento = %s, correo = %s, telefono = %s, telefono_respaldo= %s, estado = %s, contrasena = %s, nombreusu = %s WHERE idusu = %s")
        data = (nombres, apellidos, tipo_documento, num_documento, correo, telefono, telefono_respaldo , estado, contrasena, nombreusu, rol)
        cursor.execute(sql, data)
        mysql.connection.commit()
        cursor.close()
        return redirect('/usuario.consultar')

    return render_template('usuario/editar.html', idusu=idusu)

@usuario.route('/usuario.eliminar/<int:idusu>', methods=['GET', 'POST'])
def eliminar(idusu):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuario WHERE idusu = %s", (idusu,))
        data = cursor.fetchone()
        cursor.close()

        if data:
            return render_template('usuario/eliminar.html', data=data)
        else:
            return "No encontrado"

    elif request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM usuario WHERE idusu = %s", (idusu,))
        mysql.connection.commit()
        cursor.close()
        return redirect('/usuario.consultar')
    





    
app.register_blueprint(usuario)
if __name__ == '__main__':
    app.run(debug=True)