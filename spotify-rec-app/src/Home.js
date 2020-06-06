import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import Banner from './Banner';

function Home() {
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
  
  // const script = url => {
  //   useEffect(() => {
  //     const script = document.createElement('script');
  //   }, []);
  // };
  
  // var resultTemplate = React.createClass({
  //   render: function() {
  //     return (
  //       <script id="result-template" type="text/x-handlebars-template">
  //         &lt;dl&gt;
  //         &lt;img src="{'{'}{'{'}images.0.url{'}'}{'}'}"&gt;
  //         &lt;dt&gt;User Name&lt;/dt&gt;
  //         &lt;dd&gt;{'{'}{'{'}id{'}'}{'}'}&lt;/dd&gt;
  //         &lt;dt&gt;Display Name&lt;/dt&gt;
  //         &lt;dd&gt;{'{'}{'{'}display_name{'}'}{'}'}&lt;/dd&gt;
  //         &lt;dt&gt;Country&lt;/dt&gt;
  //         &lt;dd&gt;{'{'}{'{'}country{'}'}{'}'}&lt;/dd&gt;
  //         &lt;dt&gt;Followers&lt;/dt&gt;
  //         &lt;dd&gt;{'{'}{'{'}followers.total{'}'}{'}'}&lt;/dd&gt;
  //         &lt;dt&gt;Profile&lt;/dt&gt;
  //         &lt;dd&gt;&lt;a href="{'{'}{'{'}external_urls.spotify{'}'}{'}'}" target="_blank"&gt;{'{'}{'{'}external_urls.spotify{'}'}{'}'}&lt;/a&gt;&lt;/dd&gt;
  //         &lt;dt&gt;Email&lt;/dt&gt;
  //         &lt;dd&gt;{'{'}{'{'}email{'}'}{'}'}&lt;/dd&gt;
  //         &lt;dt&gt;Product&lt;/dt&gt;
  //         &lt;dd&gt;{'{'}{'{'}product{'}'}{'}'}&lt;/dd&gt;
  //         &lt;/dl&gt;
  //       </script>
  //     );
  //   }
  // });
  //
  // (function() {
  //
  //     function login(callback) {
  //         var CLIENT_ID = '6b284830006843e7ae7b170725715aed';
  //         var REDIRECT_URI = 'http://jmperezperez.com/spotify-oauth-jsfiddle-proxy/';
  //         function getLoginURL(scopes) {
  //             return 'https://accounts.spotify.com/authorize?client_id=' + CLIENT_ID +
  //               '&redirect_uri=' + encodeURIComponent(REDIRECT_URI) +
  //               '&scope=' + encodeURIComponent(scopes.join(' ')) +
  //               '&response_type=token';
  //         }
  //
  //         var url = getLoginURL([
  //             'user-read-email'
  //         ]);
  //
  //         var width = 450,
  //             height = 730,
  //             left = (1000) - (width / 2),
  //             top = (1000) - (height / 2);
  //
  //         window.addEventListener("message", function(event) {
  //             var hash = JSON.parse(event.data);
  //             if (hash.type == 'access_token') {
  //                 callback(hash.access_token);
  //             }
  //         }, false);
  //
  //         var w = window.open(url,
  //                             'Spotify',
  //                             'menubar=no,location=no,resizable=no,scrollbars=no,status=no, width=' + width + ', height=' + height + ', top=' + top + ', left=' + left
  //                            );
  //
  //     }
  //
  //     function getUserData(accessToken) {
  //         return $.ajax({
  //             url: 'https://api.spotify.com/v1/me',
  //             headers: {
  //                'Authorization': 'Bearer ' + accessToken
  //             }
  //         });
  //     }
  //
  //     var templateSource = document.getElementById('result-template').innerHTML,
  //         template = Handlebars.compile(templateSource),
  //         resultsPlaceholder = document.getElementById('result'),
  //         loginButton = document.getElementById('btn-login');
  //
  //     loginButton.addEventListener('click', function() {
  //         login(function(accessToken) {
  //             getUserData(accessToken)
  //                 .then(function(response) {
  //                     loginButton.style.display = 'none';
  //                     resultsPlaceholder.innerHTML = template(response);
  //                 });
  //             });
  //     });
  //
  // })();

  return (
    <div id="home" className="page-body">
  
      {/*<h1>Displaying User Data</h1>*/}
      {/*<p>Log in with your Spotify account and this demo will display information about you fetched using the Spotify Web*/}
      {/*  API</p>*/}
      {/*<button className="btn btn-primary" id="btn-login">Login</button>*/}
      {/*<div id="result"></div>*/}
      

      
      <div id="login">
        <h1>Authorize Spotify Account</h1>
        <a href="/login" className="btn btn-login">Log in with Spotify</a>
      </div>
      <div id="loggedin">
        <div id="user-profile"/>
        <div id="oauth"/>
        <button className="btn btn-default" id="obtain-new-token">Obtain new token using the refresh token</button>
      </div>
      
{/*      <script id="user-profile-template" type="text/x-handlebars-template">
        <h1>Logged in as {{display_name}}</h1>
        <div className={"media"}>
          <div className={"pull-left"}>
            <img className={"media-object"} width={"150"} src="{{images.0.url}}" />
          </div>
          <div className={"media-body"}>
            <dl className={"dl-horizontal"}>
              <dt>Display name</dt><dd className={"clearfix"}>{display_name}</dd>
              <dt>Id</dt><dd>{{id}}</dd>
              <dt>Email</dt><dd>{{email}}</dd>
              <dt>Spotify URI</dt><dd><a href="{{external_urls.spotify}}">{{external_urlsspotify}}</a></dd>
              <dt>Link</dt><dd><a href={"{{href}}"}>{{href}}</a></dd>
              <dt>Profile Image</dt><dd className={"clearfix"}><a href="{"{{images.0.url}}"}"}>{{images.0.url}}</a></dd>
              <dt>Country</dt><dd>{{country}}</dd>
            </dl>
          </div>
        </div>
      </script>*/}
      
      {/*<script id={"oauth-template"} type={"text/x-handlebars-template"}>*/}
      {/*  <h2>oAuth info</h2>*/}
      {/*  <dl className={"dl-horizontal"}>*/}
      {/*    <dt>Access token</dt><dd className={"text-overflow"}>{{access_token}}</dd>*/}
      {/*    <dt>Refresh token</dt><dd className={"text-overflow"}>{{refresh_token}}</dd>*/}
      {/*  </dl>*/}
      {/*</script>*/}
      
      {/*<script src={"//cdnjs.cloudflare.com/ajax/libs/handlebars.js/2.0.0-alpha.1/handlebars.min.js"}></script>*/}
      {/*<script src={"http://code.jquery.com/jquery-1.10.1.min.js"}></script>*/}
      {/*<script>*/}
      {/*  (function() {*/}
      {/*  */}
      {/*  /***/}
      {/*   * Obtains parameters from the hash of the URL*/}
      {/*   * @return Object*/}
      {/*   */}
      {/*  function getHashParams() {*/}
      {/*    var hashParams = {};*/}
      {/*    var e, r = /([^&;=]+)=?([^&;]*)/g,*/}
      {/*      q = window.location.hash.substring(1);*/}
      {/*    while(e = r.exec(q)) {*/}
      {/*      hashParams[e[1]] = decodeURIComponent(e[2]);*/}
      {/*    }*/}
      {/*    return hashParams;*/}
      {/*  }*/}
      {/*  */}
      {/*  var userProfileSource = document.getElementById('user-profile-template').innerHTML,*/}
      {/*      userProfileTemplate = Handlebars.compile(userProfileSource),*/}
      {/*      userProfilePlaceholder = document.getElementById('user-profile');*/}
      {/*  */}
      {/*  var oauthSource = document.getElementById('oauth-template').innerHTML,*/}
      {/*      oauthTemplate = Handlebars.compile(oauthSource),*/}
      {/*      oauthPlaceholder = document.getElementById('oauth');*/}
      {/*  */}
      {/*  var params = getHashParams();*/}
      {/*  */}
      {/*  var access_token = params.access_token,*/}
      {/*      refresh_token = params.refresh_token,*/}
      {/*      error = params.error;*/}
      {/*  */}
      {/*  if (error) {*/}
      {/*    alert('There was an error during the authentication');*/}
      {/*  } else {*/}
      {/*    if (access_token) {*/}
      {/*      // render oauth info*/}
      {/*      oauthPlaceholder.innerHTML = oauthTemplate({*/}
      {/*        access_token: access_token,*/}
      {/*        refresh_token: refresh_token*/}
      {/*      });*/}
      {/*      */}
      {/*      $.ajax({*/}
      {/*        url: 'https://api.spotify.com/v1/me',*/}
      {/*        headers: {*/}
      {/*          'Authorization': 'Bearer ' + access_token*/}
      {/*        },*/}
      {/*        success: function(response) {*/}
      {/*          userProfilePlaceholder.innerHTML = userProfileTemplate(response);*/}
      {/*          $('#login').hide();*/}
      {/*          $('#loggedin').show();*/}
      {/*        }*/}
      {/*      });*/}
      {/*    } else {*/}
      {/*      // render initial screen*/}
      {/*      $('#login').show();*/}
      {/*      $('#loggedin').hide();*/}
      {/*    }*/}
      {/*  */}
      {/*    document.getElementById('obtain-new-token').addEventListener('click', function() {*/}
      {/*      $.ajax({*/}
      {/*        url: '/refresh_token',*/}
      {/*        data: {*/}
      {/*          'refresh_token': refresh_token*/}
      {/*        }*/}
      {/*      }).done(function(data) {*/}
      {/*        access_token = data.access_token;*/}
      {/*        oauthPlaceholder.innerHTML = oauthTemplate({*/}
      {/*          access_token: access_token,*/}
      {/*          refresh_token: refresh_token*/}
      {/*        });*/}
      {/*      });*/}
      {/*      }, false);*/}
      {/*  }*/}
      {/*})();*/}
      {/*</script>*/}
      
      {/*<img src={logo} className="App-logo" alt="logo" />*/}
      {/*<p>*/}
      {/*  Edit <code>src/App.js</code> and save to reload.*/}
      {/*</p>*/}
      {/*<a*/}
      {/*  className="App-link"*/}
      {/*  href="https://reactjs.org"*/}
      {/*  target="_blank"*/}
      {/*  rel="noopener noreferrer"*/}
      {/*>*/}
      {/*  Learn React*/}
      {/*</a>*/}
      {/*<p>The current time is {currentTime}.</p>*/}
    
      {/*resultTemplate();*/}
    </div>
    
    
  );
};

export default Home;