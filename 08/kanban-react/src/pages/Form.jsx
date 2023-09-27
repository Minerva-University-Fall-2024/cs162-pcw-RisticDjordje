import React from "react";

export default function Form(){
    return(
        <>
        <div class="add-task">
          <h2>Add New Task</h2>
          <form id="task-form">
            <label for="task-description">Task Description:</label>
            <input type="text" id="task-description" name="task-description" required />
              <button type="submit">Add Task</button>
          </form>
        </div>
        
        </>
    )
}