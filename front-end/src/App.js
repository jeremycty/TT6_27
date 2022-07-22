import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './css/App.css';
import Header from "./components/Header"
import Home from "./page/Home"
import Dashboard from "./page/Dashboard"
import Secondpage from "./page/Secondpage"
import Transaction from "./page/Transaction"

function App() {
  return (
    <div className="App">
      <Header/> 

      {/* Routes for varous pages componenets */}
      <Routes> 
        <Route path='/' element={<Home/>}></Route>
        <Route path='/second' element={<Secondpage/>}></Route>
        <Route path='/dashboard' element={<Dashboard/>}></Route>
        <Route path='/transaction' element={<Transaction/>}></Route>
      </Routes> 

    </div>
  );
}

export default App;
