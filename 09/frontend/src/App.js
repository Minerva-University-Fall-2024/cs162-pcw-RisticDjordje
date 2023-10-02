import './App.css';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Taskform from "./pages/Taskform";


function App() {
  return (
    <>
      <Routes >
            <Route path="/" element={<Home />} />
            <Route path="/form" element={<Taskform />} />
        </Routes>
      
    </>
  );
}

export default App;
