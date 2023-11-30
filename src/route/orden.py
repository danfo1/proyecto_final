import os

from flask import (Blueprint, Flask, flash, redirect, render_template, request,
                   session)
from flask_mysqldb import MySQL

ORDEN=Blueprint('ORDEN',__name__)
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,  'templates')

app = Flask(__name__, template_folder=template_dir)
mysql = MySQL(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@ORDEN.route('/ORDEN.consultar', methods=['GET', 'POST'])
def consultar_orden_trabajo():
    try:
        cursor = mysql.connection.cursor()
        orden = []
        search_query = ''  # Inicializa search_query antes del bloque condicional

        if request.method == "POST" and 'txtBuscar' in request.form:
            search_query = request.form['txtBuscar']
            print("Valor de búsqueda:", search_query)
            cursor.execute("SELECT placa, descripcion, radio, antena, encendedor, tapetes, soat, grua, estado_llantas, llave_pernos, llanta_repuesto, tapa_gasolina, url, golpe, rayado, manchado, sucio, herramientas, kit_carretera, copas, tarjeta_de_propiedad, estado_proceso, periodo_de_tiempo_ini, periodo_de_tiempo_fin FROM orden_trabajo WHERE placa LIKE %s", ('%' + search_query + '%',))
        else:
            cursor.execute("SELECT placa, descripcion, radio, antena, encendedor, tapetes, soat, grua, estado_llantas, llave_pernos, llanta_repuesto, tapa_gasolina, url, golpe, rayado, manchado, sucio, herramientas, kit_carretera, copas, tarjeta_de_propiedad, estado_proceso, periodo_de_tiempo_ini, periodo_de_tiempo_fin FROM orden_trabajo")

        orden = cursor.fetchall()
        cursor.close()

        print("Orden:", orden)
        print("Valor de búsqueda después de la ejecución de la consulta:", search_query)

        return render_template("orden/consultar_1.html", orden=orden)

    except Exception as e:
        app.logger.error("Error en la consulta SQL: %s", str(e))
        app.logger.error("Consulta SQL: SELECT ... FROM orden_trabajo WHERE placa LIKE %s", ('%' + search_query + '%',))
        return "Error en la consulta SQL. Por favor, verifica la base de datos y la consulta."

@ORDEN.route('/ORDEN.consultarresep', methods=['GET', 'POST'])
def consultar_orden_trabajo2():
    try:
        cursor = mysql.connection.cursor()
        orden = []
        search_query = ''  # Inicializa search_query antes del bloque condicional

        if request.method == "POST" and 'txtBuscar' in request.form:
            search_query = request.form['txtBuscar']
            print("Valor de búsqueda:", search_query)
            cursor.execute("SELECT placa, descripcion, radio, antena, encendedor, tapetes, soat, grua, estado_llantas, llave_pernos, llanta_repuesto, tapa_gasolina, url, golpe, rayado, manchado, sucio, herramientas, kit_carretera, copas, tarjeta_de_propiedad, estado_proceso, periodo_de_tiempo_ini, periodo_de_tiempo_fin FROM orden_trabajo WHERE placa LIKE %s", ('%' + search_query + '%',))
        else:
            cursor.execute("SELECT placa, descripcion, radio, antena, encendedor, tapetes, soat, grua, estado_llantas, llave_pernos, llanta_repuesto, tapa_gasolina, url, golpe, rayado, manchado, sucio, herramientas, kit_carretera, copas, tarjeta_de_propiedad, estado_proceso, periodo_de_tiempo_ini, periodo_de_tiempo_fin FROM orden_trabajo")

        orden = cursor.fetchall()
        cursor.close()

        print("Orden:", orden)
        print("Valor de búsqueda después de la ejecución de la consulta:", search_query)

        return render_template("orden/consultarresep.html", orden=orden)
    except Exception as e:
        app.logger.error("Error en la consulta SQL: %s", str(e))
        app.logger.error("Consulta SQL: SELECT ... FROM orden_trabajo WHERE placa LIKE %s", ('%' + search_query + '%',))
        return "Error en la consulta SQL. Por favor, verifica la base de datos y la consulta."

@ORDEN.route('/ORDEN.consultartecni', methods=['GET', 'POST'])
def consultar_orden_trabajo3():
    try:
        cursor = mysql.connection.cursor()
        orden = []
        search_query = ''  # Inicializa search_query antes del bloque condicional

        if request.method == "POST" and 'txtBuscar' in request.form:
            search_query = request.form['txtBuscar']
            print("Valor de búsqueda:", search_query)
            cursor.execute("SELECT placa, descripcion, radio, antena, encendedor, tapetes, soat, grua, estado_llantas, llave_pernos, llanta_repuesto, tapa_gasolina, url, golpe, rayado, manchado, sucio, herramientas, kit_carretera, copas, tarjeta_de_propiedad, estado_proceso, periodo_de_tiempo_ini, periodo_de_tiempo_fin FROM orden_trabajo WHERE placa LIKE %s", ('%' + search_query + '%',))
        else:
            cursor.execute("SELECT placa, descripcion, radio, antena, encendedor, tapetes, soat, grua, estado_llantas, llave_pernos, llanta_repuesto, tapa_gasolina, url, golpe, rayado, manchado, sucio, herramientas, kit_carretera, copas, tarjeta_de_propiedad, estado_proceso, periodo_de_tiempo_ini, periodo_de_tiempo_fin FROM orden_trabajo")

        orden = cursor.fetchall()
        cursor.close()

        print("Orden:", orden)
        print("Valor de búsqueda después de la ejecución de la consulta:", search_query)

        return render_template("orden/consultartecni.html", orden=orden)
    except Exception as e:
        app.logger.error("Error en la consulta SQL: %s", str(e))
        app.logger.error("Consulta SQL: SELECT ... FROM orden_trabajo WHERE placa LIKE %s", ('%' + search_query + '%',))
        return "Error en la consulta SQL. Por favor, verifica la base de datos y la consulta."


@ORDEN.route('/ORDEN.registrar', methods=['GET', 'POST'])
def registrar():
        
    if request.method == 'POST':
        placa = request.form["placa"]
        descripcion = request.form["descripcion"]
        radio = request.form["radio"]
        antena = request.form["antena"]
        encendedor = request.form["encendedor"]
        tapetes = request.form["tapetes"]
        soat = request.form["soat"]
        grua = request.form["grua"]
        estado_llantas = request.form["estado_llantas"]
        llave_pernos = request.form["llave_pernos"]
        llanta_repuesto = request.form["llanta_repuesto"]
        tapa_gasolina = request.form["tapa_gasolina"]
        kit_carretera = request.form["kit_carretera"]
        copas = request.form["copas"]
        tarjeta_de_propiedad = request.form["tarjeta_de_propiedad"]
        sucio = request.form['sucio']
        manchado = request.form['manchado']
        golpe = request.form['golpe']
        rayado = request.form['rayado']
        url = request.form['fotos']  # Cambiado a getlist
        estado_proceso = request.form["estado_proceso"]
        periodo_de_tiempo_ini = request.form["periodo_de_tiempo_ini"]
        periodo_de_tiempo_fin = request.form["periodo_de_tiempo_fin"]
        herramientas = request.form["herramientas"]
        
        if placa and descripcion and radio and antena and encendedor and tapetes and soat and grua and estado_llantas and llave_pernos and llanta_repuesto and tapa_gasolina and kit_carretera and  sucio and manchado and golpe and rayado and copas and tarjeta_de_propiedad and estado_proceso and periodo_de_tiempo_ini and periodo_de_tiempo_fin and herramientas and url:
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO orden_trabajo (placa, descripcion, radio, antena, encendedor, tapetes, soat, grua, estado_llantas, llave_pernos, llanta_repuesto, tapa_gasolina, kit_carretera, copas, sucio, manchado, golpe, rayado, tarjeta_de_propiedad, estado_proceso,url, periodo_de_tiempo_ini, periodo_de_tiempo_fin, herramientas) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
            data = (placa, descripcion, radio, antena, encendedor, tapetes, soat, grua, estado_llantas, llave_pernos, llanta_repuesto, tapa_gasolina, kit_carretera, copas, sucio, manchado, golpe, rayado, tarjeta_de_propiedad, estado_proceso,url, periodo_de_tiempo_ini, periodo_de_tiempo_fin, herramientas)

            cursor.execute(sql, data) 
            mysql.connection.commit()
            cursor.close() 
            return redirect('/ORDEN.consultar')
        if not all([placa , descripcion , radio , antena , encendedor, tapetes ,soat ,grua , estado_llantas ,url, llave_pernos , llanta_repuesto , tapa_gasolina , kit_carretera , copas , tarjeta_de_propiedad , estado_proceso , periodo_de_tiempo_ini , periodo_de_tiempo_fin ,herramientas]):
            return "Por favor, complete todos los campos obligatorios."
        
        return render_template('orden/registrarorden.html')

    return render_template('orden/registrarorden.html')






@ORDEN.route('/ORDEN.editar_orden/<int:id_orden>', methods=['GET', 'POST'])
def editar_orden(id_orden):
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM orden_trabajo WHERE id_orden=%s", (id_orden,))
        data = cursor.fetchone()
        cursor.close()
        
        if data:
            return render_template('orden/editarorden.html', data=data)
        else:
            return "No se encontró la orden de trabajo"
    elif request.method == 'POST':
        placa = request.form["placa"]
        descripcion = request.form["descripcion"]
        radio = request.form["radio"]
        antena = request.form["antena"]
        encendedor = request.form["encendedor"]
        tapetes = request.form["tapetes"]
        soat = request.form["soat"]
        grua = request.form["grua"]
        estado_llantas = request.form["estado_llantas"]
        llave_pernos = request.form["llave_pernos"]
        llanta_repuesto = request.form["llanta_repuesto"]
        tapa_gasolina = request.form["tapa_gasolina"]
        sucio = request.form['sucio']
        manchado = request.form['manchado']
        golpe = request.form['golpe']
        rayado = request.form['rayado']
        url = request.form['url']
        kit_carretera = request.form["kit_carretera"]
        copas = request.form["copas"]
        tarjeta_de_propiedad = request.form["tarjeta_de_propiedad"]
        estado_proceso = request.form["estado_proceso"]
        periodo_de_tiempo_ini = request.form["periodo_de_tiempo_ini"]
        periodo_de_tiempo_fin = request.form["periodo_de_tiempo_fin"]
        herramientas = request.form["herramientas"]
     
        cursor = mysql.connection.cursor()
        sql = ("UPDATE orden_trabajo SET placa=%s, descripcion=%s, radio=%s, antena=%s, encendedor=%s, tapetes=%s, soat=%s, grua=%s, estado_llantas=%s, llave_pernos=%s, llanta_repuesto=%s, tapa_gasolina=%s, kit_carretera=%s, copas=%s, tarjeta_de_propiedad=%s, estado_proceso=%s, periodo_de_tiempo_ini=%s, periodo_de_tiempo_fin=%s,url=%s,golpe=%s,rayado=%s,sucio=%s,manchado=%s, herramientas=%s WHERE id_orden=%s")
        data = (placa, descripcion, radio, antena, encendedor, tapetes, soat, grua, estado_llantas, llave_pernos, llanta_repuesto, tapa_gasolina, kit_carretera, copas, tarjeta_de_propiedad, estado_proceso, periodo_de_tiempo_ini, periodo_de_tiempo_fin,url,golpe,rayado,sucio,manchado, herramientas, id_orden)
        cursor.execute(sql, data)
        mysql.connection.commit()
        cursor.close()
        
        return redirect('')
    return render_template('orden/editarorden.html')

@ORDEN.route('/ORDEN.solicitud', methods=['GET','POST'])
def solicitud():
    if request.method == 'POST':
        cliente = request.form.get('cliente')
        tecnico = request.form.get('tecnico')

        if cliente and tecnico:
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO solicitud_servicio (cliente, tecnico) VALUES (%s, %s)"
            data = (cliente, tecnico)
            cursor.execute(sql, data)
            mysql.connection.commit()
            cursor.close()
            
            
            return redirect('ORDEN.registrar')

    return render_template('orden/solicitud.html')
app.register_blueprint(ORDEN)
if __name__ == '__main__':
    app.run(debug=True)