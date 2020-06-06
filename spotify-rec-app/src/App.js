import React from 'react';
import './App.css';
import Banner from './Banner';
import Main from './Main';

const App = () => (
  <div className='App'>
    <div className="App-header">
      <Banner/>
      <div className="page-body">
        <Main />
      </div>
    </div>
  </div>
);

export default App;

