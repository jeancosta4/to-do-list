from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuração do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'tasks'
mysql = MySQL(app)

# Rota para exibir a lista de tarefas
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    cur.close()
    return render_template('index.html', tasks=tasks)

# Rota para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        description = request.form['description']
        due_date = request.form['due_date']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tasks (description, due_date) VALUES (%s, %s)", (description, due_date))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)