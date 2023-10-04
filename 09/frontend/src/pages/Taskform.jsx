import React from 'react';
import{ useEffect, useState } from "react";
import  addCard  from "../components/Board";


export default function Taskform() {
    const [tasks, setTasks] = useState([]);
    const [taskName, setTaskName] = useState("");
    const [taskDescription, setTaskDescription] = useState("");
    const [taskCategory, setTaskCategory] = useState("Backlog");

    function handleSubmit(e) {
        e.preventDefault();
    
        // Create a JSON object with the form data
        const formData = {
            task_name: taskName,
            task_description: taskDescription,
            task_category: taskCategory
        };
    
        // Send an HTTP POST request to your Flask server
        fetch('http://127.0.0.1:5000/form', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Set the content type to JSON
            },
            body: JSON.stringify(formData) // Convert the form data to JSON
        })
        .then(response => {
            if (response.ok) {
                console.log("ok")
                // Successfully submitted the form
                // You can redirect or perform any other actions here
            } else {
                // Handle errors if any
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    
    return (
        <div className="add-task">
          <form onSubmit={handleSubmit} id="task-form">
            <div className="form-div">
              <div className="field">
                <label htmlFor="task-name">Task Name:</label>
                <input
                  value={taskName}
                  onChange={(e) => setTaskName(e.target.value)}
                  type="text"
                  name="task-name"
                  required
                />
              </div>
      
              <div className="field">
                <label htmlFor="task-description">Task Description:</label>
                <input
                  value={taskDescription}
                  onChange={(e) => setTaskDescription(e.target.value)}
                  type="text"
                  id="task-description"
                  name="task-description"
                  required
                />
              </div>
      
              <div className="field">
                <label htmlFor="task-category">Task Category:</label>
                <select
                  value={taskCategory}
                  onChange={(e) => setTaskCategory(e.target.value)}
                  id="task-category"
                  name="task-category"
                  required
                >
                  <option value="Backlog">Backlog</option>
                  <option value="To do">To do</option>
                  <option value="In progress">In progress</option>
                  <option value="Review">Review</option>
                  <option value="Done">Done</option>
                </select>
              </div>
      
              <div className="field">
                <button className="submit" type="submit">
                  Add
                </button>
              </div>
            </div>
          </form>
        </div>
      );
    }
