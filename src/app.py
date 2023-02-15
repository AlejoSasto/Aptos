from flask import Flask, render_template, request, redirect, url_for, flash
from config import *

con_bd = EstablecerConexion()

app = Flask(__name__)
app.secret_key="elmatamarranos"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    cursor = con_bd.cursor()
    apellido = request.form['apellidos']
    correo = request.form['correos']
    usuario = request.form['usuarios']
    contraseña = request.form['passs']
    apartamento = request.form['apartamento']
    torre = request.form['torre']
    if apellido and correo and usuario and contraseña:
        sql = """INSERT INTO usuarios
                    (apellidos,correo,usuario,"contraseña",apartamento, torre)
                    VALUES (%s, %s ,%s, %s)"""
        cursor.execute(sql,( apellido, correo, usuario, contraseña, apartamento, torre))
        con_bd.commit()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    cursor = con_bd.cursor()
    usuario = request.form['email']
    password = request.form['password']
    sql = """
    SELECT*FROM usuarios
    """
    cursor.execute(sql)
    personas = cursor.fetchall()
    for persona in personas:
        print(persona[1])
        print(persona[2])
        if usuario in persona[1] and password in persona[2]:
            print("USUARIO HALLADO")
            return render_template("conjunto.html")
    return render_template("index.html")

@app.route('/conjunto')
def productos():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM usuarios"
    cursor.execute(sql)
    ProductosRegistrados = cursor.fetchall()
    return render_template('conjunto.html', productos = ProductosRegistrados)

@app.route('/agua')
def agua():
    cursor = con_bd.cursor()
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    UsuariosRegistrados = cursor.fetchall()
    return render_template('agua.html', usuarios = UsuariosRegistrados)

@app.route('/luz')
def luz():
    cursor = con_bd.cursor()
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    UsuariosRegistrados = cursor.fetchall()
    return render_template('luz.html', usuarios = UsuariosRegistrados)

@app.route('/gas')
def gas():
    cursor = con_bd.cursor()
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    UsuariosRegistrados = cursor.fetchall()
    return render_template('gas.html', usuarios = UsuariosRegistrados)

@app.route('/pagogas')
def pagogas():
    cursor = con_bd.cursor()
    pago = request.form['pago']
    if pago :
        sql = """UPDATE pagos SET pago = %s WHERE idpago = %s"""
        cursor.execute(sql,(pago))
        con_bd.commit()
        return redirect(url_for('gas'))
    else:
        return "Error"

@app.route('/usuarios')
def usuarios():
    cursor = con_bd.cursor()
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    UsuariosRegistrados = cursor.fetchall()
    return render_template('usuarios.html', usuarios = UsuariosRegistrados)

@app.route('/guardar_usuarios', methods=['POST'])
def guardar_usuarios():
    cursor = con_bd.cursor()
    apellido = request.form['apellido']
    correo = request.form['correo']
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    rol = request.form['rol']
    apartamento = request.form['apartamento']
    torre = request.form['torre']
    if apellido and correo and usuario and contraseña:
        sql = """INSERT INTO usuarios
                    (apellidos,correo,usuario,"contraseña",rol, apartamento, torre)
                    VALUES (%s, %s ,%s, %s, %s,%s,%s)"""
        cursor.execute(sql,( apellido, correo, usuario, contraseña, rol, apartamento, torre))
        con_bd.commit()
        return redirect(url_for('usuarios'))
    else:
        return redirect(url_for('usuarios'))


@app.route('/editar_usuario/<int:idusuarios>', methods=['POST'])
def editar(idusuarios):
    cursor = con_bd.cursor()
    nombrep = request.form['apellido']
    valorp = request.form['correo']
    cantp = request.form['usuario']
    rol = request.form['rol']
    apartamento = request.form['apartamento']
    torre = request.form['torre']
    if nombrep and valorp and cantp:
        sql="""UPDATE usuarios
            SET apellidos = %s, correo = %s, usuario = %s, rol = %s, apartamento = %s, torre = %s
            WHERE idusuarios = %s"""
        cursor.execute(sql,(nombrep, valorp, cantp, rol, apartamento, torre, idusuarios))
        con_bd.commit()
        return redirect(url_for('usuarios'))
    else:
        return "Error en la consulta"

@app.route('/eliminar_usuarios/<int:idusuarios>')
def eliminar(idusuarios):
    cursor = con_bd.cursor()
    sql = "DELETE FROM usuarios WHERE idusuarios = {0}".format(idusuarios)
    cursor.execute(sql)
    con_bd.commit()
    return redirect(url_for('usuarios'))


if __name__=='__main__':
    app.run(debug=True)
