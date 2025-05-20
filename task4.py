                                                                          TASK-4
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>To-Do List</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f5f5f5;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
    }

    h1 {
      margin-bottom: 1rem;
    }

    .todo-container {
      background: white;
      padding: 2rem;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      width: 100%;
      max-width: 500px;
    }

    .task-form {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    input[type="text"],
    input[type="datetime-local"] {
      padding: 10px;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 6px;
      width: 100%;
    }

    button {
      padding: 10px;
      background: #007bff;
      color: white;
      font-size: 1rem;
      border: none;
      border-radius: 6px;
      cursor: pointer;
    }

    button:hover {
      background: #0056b3;
    }

    .task-list {
      margin-top: 1rem;
    }

    .task {
      background: #f9f9f9;
      margin: 0.5rem 0;
      padding: 10px;
      border-radius: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
    }

    .task.completed .text {
      text-decoration: line-through;
      color: gray;
    }

    .task .controls {
      display: flex;
      gap: 0.5rem;
    }

    .task small {
      font-size: 0.8rem;
      color: #555;
    }

    .edit-input {
      flex-grow: 1;
      margin-right: 0.5rem;
    }

    .task-actions button {
      padding: 4px 8px;
      font-size: 0.8rem;
      background: #6c757d;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    .task-actions button:hover {
      background: #495057;
    }

    .task-actions .delete {
      background: #dc3545;
    }

    .task-actions .delete:hover {
      background: #a71d2a;
    }
  </style>
</head>
<body>

  <h1>📝 To-Do List</h1>
  <div class="todo-container">
    <form class="task-form" onsubmit="addTask(event)">
      <input type="text" id="taskText" placeholder="Enter a task..." required />
      <input type="datetime-local" id="taskDate" />
      <button type="submit">Add Task</button>
    </form>

    <div class="task-list" id="taskList"></div>
  </div>

  <script>
    let tasks = [];

    function addTask(e) {
      e.preventDefault();
      const text = document.getElementById("taskText").value.trim();
      const date = document.getElementById("taskDate").value;

      if (text === "") return;

      tasks.push({
        id: Date.now(),
        text,
        date,
        completed: false
      });

      document.getElementById("taskText").value = '';
      document.getElementById("taskDate").value = '';

      renderTasks();
    }

    function toggleComplete(id) {
      tasks = tasks.map(task =>
        task.id === id ? { ...task, completed: !task.completed } : task
      );
      renderTasks();
    }

    function deleteTask(id) {
      tasks = tasks.filter(task => task.id !== id);
      renderTasks();
    }

    function editTask(id, newText) {
      tasks = tasks.map(task =>
        task.id === id ? { ...task, text: newText } : task
      );
      renderTasks();
    }

    function renderTasks() {
      const taskList = document.getElementById("taskList");
      taskList.innerHTML = '';

      tasks.forEach(task => {
        const taskDiv = document.createElement("div");
        taskDiv.className = "task" + (task.completed ? " completed" : "");
        
        const taskContent = document.createElement("div");
        taskContent.className = "text";
        taskContent.textContent = task.text;

        const taskDate = document.createElement("small");
        if (task.date) {
          const date = new Date(task.date);
          taskDate.textContent = `🕒 ${date.toLocaleString()}`;
        }

        const actions = document.createElement("div");
        actions.className = "task-actions";

        const completeBtn = document.createElement("button");
        completeBtn.textContent = task.completed ? "Undo" : "Done";
        completeBtn.onclick = () => toggleComplete(task.id);
        actions.appendChild(completeBtn);

        const editBtn = document.createElement("button");
        editBtn.textContent = "Edit";
        editBtn.onclick = () => {
          const newText = prompt("Edit task:", task.text);
          if (newText !== null && newText.trim() !== '') {
            editTask(task.id, newText.trim());
          }
        };
        actions.appendChild(editBtn);

        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.className = "delete";
        deleteBtn.onclick = () => deleteTask(task.id);
        actions.appendChild(deleteBtn);

        taskDiv.appendChild(taskContent);
        if (task.date) taskDiv.appendChild(taskDate);
        taskDiv.appendChild(actions);

        taskList.appendChild(taskDiv);
      });
    }

    renderTasks();
  </script>

</body>
</html>
