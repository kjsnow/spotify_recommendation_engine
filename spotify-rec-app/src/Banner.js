import React from "react";

import initials from './images/ks_initials.svg'
import spotify_black_background from "./images/spotify-black-background.png";
//import kyle from "./images/kyle-bowtie.jpg";
import headshot from "./images/kyle_square_headshot_black&white.jpg"
import { NavLink } from "react-router-dom";

import resolveConfig from "tailwindcss/resolveConfig"
import config from "./tailwind.config"
const tailwindConfig = resolveConfig(config)
const theme_colors = tailwindConfig.theme.colors

// class Banner extends React.Component {
//
//   // renderBannerBody() {
//   //   return <BannerBody/>
//   // }
//
//   // renderBannerContainer() {
//   //   return <BannerContainer/>
//   // };
//
//   openPage(evt, pageName) {
//     var i, x, tablinks;
//     x = document.getElementsByClassName("page-body");
//     for (i = 0; i < x.length; i++) {
//       x[i].style.display = "none";
//     }
//     tablinks = document.getElementsByClassName("nav-tab");
//     for (i = 0; i < x.length; i++) {
//       tablinks[i].className = tablinks[i].className.replace(" current", "");
//     }
//     document.getElementById(pageName).style.display = "block";
//     evt.currentTarget.className += " active";
//   }
//
//   render() {
//    return (
//      <header className=" top-0 left-0 bg-gray-800 fixed z-10 w-full" id="banner">
//        <div className="pl-8 pr-8 ml-auto mr-auto" id="banner-container">
//          <div className="flex h-20" id="banner-body">
//            <a className="flex mr-6 h-full" id="banner-title">
//              <img src={spotify_black_background} className="spotify-logo" />
//              <span className="ml-6 font-bold leading-normal" id="title">
//                Welcome!
//              </span>
//            </a>
//            <nav className="flex overflow-x-auto overflow-y-hidden h-full" id="banner-nav">
//              <NavLink exact activeClassName="current"
//                       to='/home'
//                       classname="flex flex-row items-center transition duration-200 ease-out pl-10 pr-10 font-bold"
//                       id="nav-tab"
//                       onclick="openPage(event, 'home')">
//                Home
//                <span className="spanUnderline"/>
//              </NavLink>
//              <NavLink exact activeClassName="current" to='/analyze' className="nav-tab">
//                Analyze
//                <span className="spanUnderline"/>
//              </NavLink>
//              <NavLink exact activeClassName="current" to='/compare' className="nav-tab">
//                Compare
//                <span className="spanUnderline"/>
//              </NavLink>
//              <NavLink exact activeClassName="current" to='/todo' className="nav-tab">
//                To Do
//                <span className="spanUnderline"/>
//              </NavLink>
//              <NavLink exact activeClassName="current" to='/hold' className="nav-tab">
//                Hold
//                <span className="spanUnderline"/>
//              </NavLink>
//            </nav>
//          </div>
//        </div>
//      </header>
//    );
//   };
//
// };

function NavBar() {
  return (
    <div className="w-full block flex-grow lg:flex lg:w-auto mr-4" style={{color: theme_colors.text_secondary}}>
      <div className="text-sm lg:flex-grow">
        <a href="/home"
           className="block mt-4 lg:inline-block lg:mt-0 hover:text-white mr-4">
          Home
        </a>
        <a href="/analyze"
           className="block mt-4 lg:inline-block lg:mt-0 hover:text-white mr-4">
          Analyze
        </a>
        <a href="/compare"
           className="block mt-4 lg:inline-block lg:mt-0 hover:text-white mr-4">
          Compare
        </a>
        <a href="/todo"
           className="block mt-4 lg:inline-block lg:mt-0 hover:text-white mr-4">
          To Do
        </a>
        <a href="/hold"
           className="block mt-4 lg:inline-block lg:mt-0 hover:text-white mr-4">
          Hold
        </a>
      </div>
      <div>
        <a href="#"
           className="inline-block text-sm px-4 py-2 leading-none border rounded border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0">
          Download
        </a>
      </div>
    </div>
  )
}

function Banner() {
  return (
    <nav className="flex w-full flex-wrap p-4 items-center" style={{backgroundColor: theme_colors.primary}}>
      <div className="flex flex-shrink-0 pl-4 items-center">
        {/*<svg className="fill-current h-8 w-8 mr-2" width="54" height="54" viewBox="0 0 54 54"*/}
        {/*     xmlns="http://www.w3.org/2000/svg">*/}
        {/*  <path*/}
        {/*    d="M13.5 22.1c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05zM0 38.3c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05z"/>*/}
        {/*</svg>*/}
        <img src={headshot} className="rounded-full mr-2" width="60" height="60" />
        <span className="font-semibold text-xl tracking-tight" style={{color: theme_colors.text_secondary}}>Kyle Snow</span>
      </div>
      <div className="block lg:hidden">
        <button
          className="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white">
          <svg className="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <title>Menu</title>
            <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
          </svg>
        </button>
      </div>
      <NavBar/>
    </nav>
  )
}

export default Banner
