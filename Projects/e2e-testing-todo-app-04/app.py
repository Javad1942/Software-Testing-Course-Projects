# app.py
# A simple Flask To-Do List web application (single file, for testing projects)
# In-memory data storage, REST API, and a basic HTML+JavaScript frontend.

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# In-memory list to store tasks. Each task is a dict: {"id": ..., "task": ...}
tasks = []
next_id = 1  # Incremental ID for each new task

# HTML page template with embedded (and improved) CSS and JavaScript
PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple To-Do List</title>
    <style>
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
            background-color: #f4f7f6;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2em;
            min-height: 90vh;
        }
        #app-container {
            width: 100%;
            max-width: 600px; 
            margin: 2em auto; 
            background: #ffffff;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            border-radius: 8px;
            padding: 2em;
        }
        h1 { 
            color: #2c3e50; 
            text-align: center;
            margin-top: 0;
        }
        ul { 
            list-style-type: none; 
            padding: 0; 
        }
        li { 
            margin-bottom: 0.5em; 
            padding: 0.8em; 
            border-bottom: 1px solid #eee; 
            display: flex; 
            justify-content: space-between; 
            align-items: center;
            font-size: 1.1em;
        }
        li:last-child {
            border-bottom: none;
        }
        
        /* Delete Button Style */
        li button { 
            background-color: #e74c3c; 
            color: white; 
            border: none; 
            padding: 8px 12px; 
            cursor: pointer; 
            border-radius: 5px;
            font-size: 0.9em;
            transition: background-color 0.2s;
        }
        li button:hover { 
            background-color: #c0392b; 
        }
        
        /* Form Styling */
        form { 
            margin-bottom: 1.5em; 
            display: flex;
        }
        #task-input {
            flex-grow: 1;
            padding: 0.8em;
            border: 2px solid #ddd;
            border-radius: 5px 0 0 5px;
            font-size: 1em;
            outline: none;
            transition: border-color 0.2s;
        }
        #task-input:focus {
            border-color: #3498db;
        }
        
        /* Add Task Button Style */
        form button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 0.8em 1.2em;
            border-radius: 0 5px 5px 0;
            cursor: pointer;
            font-size: 1em;
            transition: background-color 0.2s;
        }
        form button:hover {
            background-color: #2980b9;
        }
        
        #error { 
            color: #c0392b; 
            font-weight: bold;
            margin-bottom: 1em;
            text-align: center;
        }
    </style>
</head>
<body>
    <div id="app-container">
        <h1>📝 Simple To-Do List</h1>
        <form id="add-task-form">
            <input type="text" id="task-input" placeholder="Enter a new task..." required>
            <button type="submit">Add Task</button>
        </form>
        <div id="error"></div>
        <ul id="tasks-list"></ul>
    </div>
    
    <script>
        // Fetch and display tasks
        function loadTasks() {
            fetch('/tasks')
                .then(response => response.json())
                .then(data => {
                    const list = document.getElementById('tasks-list');
                    list.innerHTML = ''; // Clear
                    data.forEach(task => {
                        const li = document.createElement('li');
                        li.textContent = task.task;
                        const delBtn = document.createElement('button');
                        delBtn.textContent = 'Delete';
                        delBtn.onclick = () => deleteTask(task.id);
                        li.appendChild(delBtn);
                        list.appendChild(li);
                    });
                });
        }

        // Add new task
        document.getElementById('add-task-form').onsubmit = function(e) {
            e.preventDefault();
            const input = document.getElementById('task-input');
            const errorDiv = document.getElementById('error');
            const taskText = input.value.trim();
            
            // Basic check for empty task
            if (!taskText) {
                errorDiv.textContent = 'Task cannot be empty.';
                return;
            }

            fetch('/tasks', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({task: taskText})
            })
            .then(response => {
                if(!response.ok) {
                    // Handle server-side error (like empty task)
                    return response.json().then(err => { throw new Error(err.error || 'Failed to add task'); });
                }
                return response.json();
            })
            .then(result => {
                input.value = '';
                errorDiv.textContent = '';
                loadTasks();
            })
            .catch(err => {
                errorDiv.textContent = 'Error: ' + err.message;
            });
        };

        // Delete a task by its ID
        function deleteTask(id) {
            fetch('/tasks/' + id, {
                method: 'DELETE'
            })
            .then(response => {
                if(!response.ok) throw new Error('Failed to delete task');
                loadTasks();
            })
            .catch(err => {
                document.getElementById('error').textContent = 'Error: Could not delete task.';
            });
        }

        // Initial load
        loadTasks();
    </script>
</body>
</html>
"""

# Flask route: Display the main page with tasks UI
@app.route('/')
def index():
    # Render the HTML page from the PAGE string
    return render_template_string(PAGE)

# REST API: Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Return a JSON list of all tasks.
    Each task is a dict with 'id' and 'task' keys.
    """
    return jsonify(tasks)

# REST API: Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Add a new task.
    Expects a JSON payload: {"task": "content"}
    Responds with the created task object.
    """
    global next_id
    data = request.get_json()
    
    # Improved validation: Check for empty string
    if not data or 'task' not in data or not isinstance(data['task'], str) or not data['task'].strip():
        return jsonify({'error': 'Invalid payload or empty task'}), 400
        
    task_obj = {'id': next_id, 'task': data['task'].strip()}
    tasks.append(task_obj)
    next_id += 1
    return jsonify(task_obj), 201

# REST API: Delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """
    Remove the task with the given ID.
    Responds with 204 No Content if deleted, 404 if not found.
    """
    global tasks
    before = len(tasks)
    # Use a list comprehension for efficient removal
    tasks = [t for t in tasks if t['id'] != task_id]
    
    # Check if a task was actually removed
    if len(tasks) == before:
        return jsonify({'error': 'Task not found'}), 404
        
    return '', 204 # Standard "No Content" response for a successful DELETE

if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)