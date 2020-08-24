import React, { useState, useEffect } from "react";
import logo from "./images/logo.svg";
import kyle from "./images/kyle-bowtie.jpg";
import Banner from "./Banner";
import './styles.css'

function HeadShot() {
  return (
    <div className="flex" id="head-shot-container">
      <img className="p-4 rounded-full" src={kyle} alt="head-shot" />
      <p className="">
        Welcome! Take a look at my bio and resume
        to learn a little about me and my background
        or jump in and explore my app!
      </p>
    </div>
  )
}

function Home() {
  return (
    <HeadShot/>
  );
}

export default Home;
