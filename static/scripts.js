document.addEventListener("DOMContentLoaded", function() {
    fetch("/tasks")
        .then(response => response.json())
        .then(tasks => {
            const taskList = document.getElementById("task-list");
            tasks.forEach(task => {
                task.completed = undefined;
                const li = document.createElement("li");
                li.className = "task";
                li.textContent = task.title;
                if (task.completed) {
                    li.classList.add("completed");
                }
                taskList.appendChild(li);
            });
        })
        .catch(error => console.error("Error fetching tasks:", error));
});