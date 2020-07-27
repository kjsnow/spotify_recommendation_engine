import React, {useEffect, useState} from "react";
import Banner from "./Banner";
import logo from "./images/logo.svg";

function Analyze() {
  const [currentResult, setResult] = useState('hi');
  
  useEffect(() => {
    fetch('/todo').then(res => res.json()).then(data => {
      setResult(data.result);
    });
  }, []);
  
  return (
    <div id="analyze" className="page-body">
      <img src={logo} className="App-logo" alt="logo" />
      <p>
        Edit <code>src/App.js</code> and save to reload.
      </p>
      <a
        className="App-link"
        href="https://reactjs.org"
        target="_blank"
        rel="noopener noreferrer"
      >
        Learn React
      </a>
      <p>{currentResult}.</p>
    </div>
  );
};

export default Analyze;