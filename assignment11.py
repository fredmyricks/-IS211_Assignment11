from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)
todo_list = []

# View List of To Do Items
@app.route('/')
def view_list():
    return render_template('list.html', todo_list=todo_list)

# New To Do Item Form
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        task = request.form['task']
        email = request.form['email']
        priority = request.form['priority']

        # Data Validation
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(email_regex, email):
            return redirect(url_for('view_list'))

        priorities = ['Low', 'Medium', 'High']
        if priority not in priorities:
            return redirect(url_for('view_list'))

        # Append new item to the list
        todo_list.append({'task': task, 'email': email, 'priority': priority})

        return redirect(url_for('view_list'))

    return render_template('add.html')

# Clear the List
@app.route('/clear')
def clear_list():
    global todo_list
    todo_list = []
    return redirect(url_for('view_list'))

if __name__ == '__main__':
    app.run()
