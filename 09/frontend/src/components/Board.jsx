import { useState, useEffect } from "react";
import {myTasks} from "../data/Tasks.js";



export default function Board() {
    const [tasks, setTasks] = useState([]);

    useEffect(() => {
        // Fetch tasks from the backend when the component mounts
        fetch('http://127.0.0.1:5000/get_tasks') // Replace with your backend URL
            .then(response => response.json())
            .then(data => {
                if (data.tasks) {
                    // log to console
                    console.log(data.tasks);
                    setTasks(data.tasks);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }, []); // The empty dependency array ensures this effect runs once on component mount

    return(
        <div className = "board_container">
        <div className = "board">
            <h2 className = "board_title">Backlog</h2>
            <div>
                {myTasks.map((task) => {
                    if (task.taskCategory === 'Backlog') {
                        return (
                            <div className = "card" key={task.id}>
                                <p className="card_description">{task.taskName}</p>
                            </div>
                        );
                    }

                    return null;
                })}
            </div>
        </div>
        <div className = "board">
            <h2 className = "board_title">To do</h2>
            <div>
                {myTasks.map((task) => {
                    if (task.taskCategory === 'To Do') {
                        return (
                            <div className = "card" key={task.id}>
                                <p className="card_description">{task.taskName}</p>
                            </div>
                        );
                    }

                    return null;
                })}
            </div>
        </div>
        
        <div className = "board">
            <h2 className = "board_title">In progress</h2>
            <div>
                {myTasks.map((task) => {
                    if (task.taskCategory === 'In Progress') {
                        return (
                            <div className = "card" key={task.id}>
                                <p className="card_description">{task.taskName}</p>
                            </div>
                        );
                    }

                    return null;
                })}
            </div>
        </div> 
    
        <div className = "board">
            <h2 className = "board_title">Review</h2>
            <div>
                {myTasks.map((task) => {
                    if (task.taskCategory === 'Review') {
                        return (
                            <div className = "card" key={task.id}>
                                <p className="card_description">{task.taskName}</p>
                            </div>
                        );
                    }

                    return null;
                })}
            </div>
        </div>  
        
        <div className = "board">
            <h2 className = "board_title">Done</h2>
            <div>
                {myTasks.map((task) => {
                    if (task.taskCategory === 'Done') {
                        return (
                            <div className = "card" key={task.id}>
                                <p className="card_description">{task.taskName}</p>
                            </div>
                        );
                    }

                    return null;
                })}
            </div>
        </div>          
    </div>
    )
}