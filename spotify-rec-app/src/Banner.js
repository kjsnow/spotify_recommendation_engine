import React from "react";
//import spotify_logo from './spotify-logo.jpg';
import spotify_black_background from "./spotify-black-background.png";
import { NavLink } from "react-router-dom";

// function BannerBody(props) {
//   return (
//     <div className="banner-body">hi</div>
//   )
// }
//
// function BannerContainer(props) {
//   return (
//     <div className="banner-container"></div>
//   );
// }

class Banner extends React.Component {
  
  // renderBannerBody() {
  //   return <BannerBody/>
  // }
  
  // renderBannerContainer() {
  //   return <BannerContainer/>
  // };
  
  openPage(evt, pageName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("page-body");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("nav-tab");
    for (i = 0; i < x.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" current", "");
    }
    document.getElementById(pageName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  
  render() {
   return (
     <header className="banner">
       <div className="banner-container">
         <div className="banner-body">
           <a className="banner-title">
             <img src={spotify_black_background} className="spotify-logo" />
             <span className="title">
               Welcome!
             </span>
           </a>
           <nav className="banner-nav">
             <NavLink exact activeClassName="current" to='/home' className="nav-tab" onclick="openPage(event, 'home')">
               Home
               <span className="spanUnderline"/>
             </NavLink>
             <NavLink exact activeClassName="current" to='/analyze' className="nav-tab">
               Analyze
               <span className="spanUnderline"/>
             </NavLink>
             <NavLink exact activeClassName="current" to='/compare' className="nav-tab">
               Compare
               <span className="spanUnderline"/>
             </NavLink>
             <NavLink exact activeClassName="current" to='todo' className="nav-tab">
               To Do
               <span className="spanUnderline"/>
             </NavLink>
           </nav>
         </div>
       </div>
     </header>
   );
  };
  
};

export default Banner
