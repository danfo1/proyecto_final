import os

from flask import (Blueprint, Flask, flash, redirect, render_template, request,
                   session)
from flask_mysqldb import MySQL

vehiculo1=Blueprint('vehiculo',__name__)
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,  'templates')

app = Flask(__name__, template_folder=template_dir)
mysql = MySQL(app)



@vehiculo1.route("/vehiculo.registro_vehiculo", methods=['GET', 'POST'])
def vehiculo():
    if request.method == 'POST':
        modelo = request.form["modelo"]
        marca = request.form["marca"]
        color = request.form["color"]
        placa = request.form["placa"]
        cilindraje = request.form["cilindraje"]
        kilometraje = request.form["kilometraje"]
        referencia = request.form["referencia"]
        tipo_combustible = request.form["tipo_combustible"]

        if modelo and marca and color and placa and cilindraje and kilometraje and referencia and tipo_combustible:
            cursor = mysql.connection.cursor()
            sql = ("INSERT INTO vehiculo (modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_conbustible) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            data = (modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_combustible)
            cursor.execute(sql, data)
            mysql.connection.commit()
            cursor.close()
            return redirect('/vehiculo.consultar_vehiculo')
    return render_template('vehiculo/rvehiculo.html')



@vehiculo1.route('/vehiculo.consultar_vehiculo', methods=['GET', 'POST'])
def consultar_vehiculo():
    try:
        cursor = mysql.connection.cursor()
        vehiculo = []

        if request.method == "POST" and 'txtBuscar' in request.form:
            search_query = '%' + request.form['txtBuscar'] + '%'
            print("Valor de búsqueda:", search_query)
            cursor.execute("SELECT id_vehiculo, modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_conbustible FROM vehiculo WHERE placa LIKE %s", (search_query,))
        else:
            cursor.execute("SELECT id_vehiculo, modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_conbustible FROM vehiculo")

        vehiculo = cursor.fetchall()
        cursor.close()

        # Depurar datos recuperados
        print("Usuarios:", vehiculo)

        return render_template("vehiculo/consultar_vehiculo.html", vehiculo=vehiculo)

    except Exception as e:
        print("Error en la consulta SQL:", str(e))
        return "Error en la consulta SQL. Por favor, verifica la base de datos y la consulta."
    
@vehiculo1.route('/vehiculo.consultartecni', methods=['GET', 'POST'])
def consultar_vehiculo3():
    try:
        cursor = mysql.connection.cursor()
        vehiculo = []

        if request.method == "POST" and 'txtBuscar' in request.form:
            search_query = '%' + request.form['txtBuscar'] + '%'
            print("Valor de búsqueda:", search_query)
            cursor.execute("SELECT id_vehiculo, modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_conbustible FROM vehiculo WHERE placa LIKE %s", (search_query,))
        else:
            cursor.execute("SELECT id_vehiculo, modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_conbustible FROM vehiculo")

        vehiculo = cursor.fetchall()
        cursor.close()

        # Depurar datos recuperados
        print("Usuarios:", vehiculo)

        return render_template("vehiculo/consultar_vehiculotecni.html", vehiculo=vehiculo)

    except Exception as e:
        print("Error en la consulta SQL:", str(e))
        return "Error en la consulta SQL. Por favor, verifica la base de datos y la consulta."
    
    
@vehiculo1.route('/vehiculo.consultarclien', methods=['GET', 'POST'])
def consultar_vehiculo4():
    try:
        cursor = mysql.connection.cursor()
        vehiculo = []

        if request.method == "POST" and 'txtBuscar' in request.form:
            search_query = '%' + request.form['txtBuscar'] + '%'
            print("Valor de búsqueda:", search_query)
            cursor.execute("SELECT id_vehiculo, modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_conbustible FROM vehiculo WHERE placa LIKE %s", (search_query,))
        else:
            cursor.execute("SELECT id_vehiculo, modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_conbustible FROM vehiculo")

        vehiculo = cursor.fetchall()
        cursor.close()

        # Depurar datos recuperados
        print("Usuarios:", vehiculo)

        return render_template("vehiculo/vehiculo_cliente.html", vehiculo=vehiculo)

    except Exception as e:
        print("Error en la consulta SQL:", str(e))
        return "Error en la consulta SQL. Por favor, verifica la base de datos y la consulta."
    
@vehiculo1.route('/vehiculo.consultar', methods=['GET', 'POST'])
def consultar_vehiculo1():
    try:
        cursor = mysql.connection.cursor()
        vehiculo = []

        if request.method == "POST" and 'txtBuscar' in request.form:
            search_query = '%' + request.form['txtBuscar'] + '%'
            print("Valor de búsqueda:", search_query)
            cursor.execute("SELECT id_vehiculo, modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_conbustible FROM vehiculo WHERE placa LIKE %s", (search_query,))
        else:
            cursor.execute("SELECT id_vehiculo, modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_conbustible FROM vehiculo")

        vehiculo = cursor.fetchall()
        cursor.close()

        # Depurar datos recuperados
        print("Usuarios:", vehiculo)

        return render_template("vehiculo/consultarresep.html", vehiculo=vehiculo)

    except Exception as e:
        print("Error en la consulta SQL:", str(e))
        return "Error en la consulta SQL. Por favor, verifica la base de datos y la consulta."


@vehiculo1.route("/vehiculo.editar_vehiculo/<int:id_vehiculo>", methods=['GET', 'POST'])
def editar_vehiculo(id_vehiculo):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM vehiculo WHERE id_vehiculo=%s", (id_vehiculo ,))
        data = cursor.fetchone()
        cursor.close()
        
        if data:
            return render_template('vehiculo/editarvehiculo.html', data=data)
        else:
            return "No se encontró el vehículo"
    elif request.method == 'POST':
        modelo = request.form["modelo"]
        marca = request.form["marca"]
        color = request.form["color"]
        placa = request.form["placa"]
        cilindraje = request.form["cilindraje"]
        kilometraje = request.form["kilometraje"]
        referencia = request.form["referencia"]
        tipo_combustible = request.form["tipo_combustible"]

        cursor = mysql.connection.cursor()
        sql = ("UPDATE vehiculo SET modelo=%s, marca=%s, color=%s, placa=%s, cilindraje=%s, kilometraje=%s, referencia=%s, tipo_conbustible=%s "
               "WHERE id_vehiculo =%s")
        data = (modelo, marca, color, placa, cilindraje, kilometraje, referencia, tipo_combustible, id_vehiculo)
        cursor.execute(sql, data)
        mysql.connection.commit()
        cursor.close()
        return "Datos actualizados"
    return render_template('vehiculo/editarvehiculo.html')

@vehiculo1.route('/vehiculo.eliminar/<int:id_vehiculo>', methods=['GET', 'POST'])
def eliminar_vehiculo(id_vehiculo):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM vehiculo WHERE id_vehiculo = %s", (id_vehiculo,))
        data = cursor.fetchone()
        cursor.close()

        if data:
            return render_template('vehiculo/eliminar_vehiculo.html', data=data)
        else:
            return "No encontrado"

    elif request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM vehiculo WHERE id_vehiculo = %s", (id_vehiculo,))
        mysql.connection.commit()
        cursor.close()
        return "Datos eliminados"
    
app.register_blueprint(vehiculo1)
if __name__ == '__main__':
    app.run(debug=True)
    