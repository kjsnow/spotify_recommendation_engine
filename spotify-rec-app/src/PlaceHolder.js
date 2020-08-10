import React, { useState, useEffect } from 'react';
import logo from './images/logo.svg';
import './styles/App.css';
import Banner from './Banner';

function PlaceHolder() {
  const [currentTime, setCurrentTime] = useState(0);
  
  var client_id = '2d0cc7a4ed9d44a69c9ad358b216dd7e';
  var client_secret = 'bc85301ff7114dca9f2a195804b16ddc';
  var client_secret = 'bc85301ff7114dca9f2a195804b16ddc';
  var redirect_uri = 'http://localhost:8888/callback';
  var scopes = 'user-read-private user-read-email';

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);
  
  return (
    <div id="place-holder" className="page-body">


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
      <p>{currentTime}.</p>
  
      {/*<h1>Displaying User Data</h1>*/}
      {/*<p>Log in with your Spotify account and this demo will display information about you fetched using the Spotify Web*/}
      {/*  API</p>*/}
      {/*<button className="btn btn-primary" id="btn-login">Login</button>*/}
      {/*<div id="result"></div>*/}
      

      
      {/* <div id="login">
        <h1>Authorize Spotify Account</h1>
        <a href="/login" className="btn btn-login">Log in with Spotify</a>
      </div>
      <div id="loggedin">
        <div id="user-profile"/>
        <div id="oauth"/>
        <button className="btn btn-default" id="obtain-new-token">Obtain new token using the refresh token</button>
      </div> */}
    </div>
  );
};


export default PlaceHolder;