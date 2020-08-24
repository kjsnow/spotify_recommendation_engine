import React from "react";
import { NavLink } from "react-router-dom";

// IMAGES

import { GitCircleLogo, LinkedInCircleLogo, EmailLogo } from "./images/banner-logos"
import spotify_black_background from "./images/spotify-black-background.png";
//import kyle from "./images/kyle-bowtie.jpg";
import headshot from "./images/kyle_square_headshot_black&white.jpg"

// THEMES
import resolveConfig from "tailwindcss/resolveConfig"
import config from "./tailwind.config"
const tailwindConfig = resolveConfig(config)
const theme_colors = tailwindConfig.theme.colors




function NavBar() {
  return (
    <div className="w-full block flex-grow items-center lg:flex lg:w-auto m-4">
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
      <div className="flex">
        <a className="p-1" href="https://github.com/kjsnow" target="_blank">
          <GitCircleLogo/>
        </a>
        <a className="p-1" href="https://www.linkedin.com/in/snowkyle/" target="_blank">
          <LinkedInCircleLogo/>
        </a>
        <a className="p-1" href="mailto: kjsnow11@gmail.com" target="_blank">
          <EmailLogo/>
        </a>
        {/*<a href="#"*/}
        {/*   className="inline-block text-sm px-4 py-2 leading-none border rounded border-white hover:border-transparent hover:text-teal-500 hover:bg-white mt-4 lg:mt-0">*/}
        {/*  Download*/}
        {/*</a>*/}
      </div>
    </div>
  )
}

function Banner() {
  return (
    <nav className="flex w-full flex-wrap items-center" style={{backgroundColor: theme_colors.c4, color: theme_colors.c1}}>
      <div className="flex flex-shrink-0 items-center">
        <img src={headshot} className="rounded-full p-4 h-12 w-12" viewBox="0 0 12 12"  />
        <span className="font-semibold text-xl p-2 tracking-tight">Kyle Snow</span>
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

export default Banner