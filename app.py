from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)

os.environ['DATABASE_URL'] = 'postgresql://darkness:03tppNTXMmrzFDFriBfPGpaQ99VDrTYr@dpg-cvmpkk6mcj7s73bqum8g-a.oregon-postgres.render.com/test_ww0l' 

DATABASE_URL = os.getenv('DATABASE_URL')  

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    conn = get_db_connection()
    cur = conn.cursor()
    dni = request.form['dni']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    cur.execute(
        'INSERT INTO personas (dni, nombre, apellido, direccion, telefono)'
        'VALUES (%s, %s, %s, %s, %s)',
        (dni, nombre, apellido, direccion, telefono)
    )
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/administrar')
def administrar():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM personas;')
    column_names = [desc[0] for desc in cur.description]
    personas = [dict(zip(column_names, row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return render_template('administrar.html', personas=personas)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM personas WHERE id = %s', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('administrar'))

if __name__ == '__main__':
    app.run(debug=True)