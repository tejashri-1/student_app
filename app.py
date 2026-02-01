from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Home page (form)
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

    return redirect('/students')

# Display students
@app.route('/students')
def students():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()

    return render_template('students.html', students=data)

if __name__ == '__main__':
    app.run(debug=True)
