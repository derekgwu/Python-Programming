from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store to-do items
todos = []
history = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    new_todo = request.form['todo']
    if new_todo:  # Ensure the input is not empty
        todos.append(new_todo)
    return redirect(url_for('index'))

@app.route('/delete_todo/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    item = todos[todo_id]
    history.append(item)
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    print(history)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
