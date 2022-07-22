import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './css/App.css';
import Header from "./components/Header"
import Home from "./page/Home"
import Secondpage from "./page/Secondpage"

function App() {
  return (
    <div className="App">
      <Header/> 

      {/* Routes for varous pages componenets */}
      <Routes> 
        <Route path='/' element={<Home/>}></Route>
        <Route path='/second' element={<Secondpage/>}></Route>
      </Routes> 

    </div>
  );
}

export default App;
