import React from 'react';
import {Route, Routes} from "react-router-dom";
import Taskform from "../pages/Taskform";
import { Link } from 'react-router-dom';

export default function Navbar() {
    return(

        <>
         <div className = "navbar">
            <div className = "nav_container">
                <div className = "title">
                    <h1 className="t_header"> Kanban Board </h1>     
                </div>
                <div className = "add-div">
                    <Link to="/form" className="logout-link">Add task</Link>
                </div>
                <div className = "logout">
                    <a href="logout" class="logout-link">Logout</a>
                </div>       
            </div>
        </div>

        <Routes >
            <Route path="/form" element={<Taskform />} />
        </Routes>
        
        </>
    );  
}
