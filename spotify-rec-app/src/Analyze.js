import React, { useEffect, useState, handleChange } from "react";
import logo from "./logo.svg";
import search_icon from "./search-icon.png";

// STORE
// import { store } from 'react-recollect';
//
// const storedData = JSON.parse(localStorage.getItem('store'));
// store.searchResults = storedData
//   ? storedData.searchResults
//   : {
//     name: null,
//     followers: null,
//     genres: null,
//   };

function Artist(props) {
  const currentResult = props.currentResult
  
  // ATTEMPTING TO REPLACE WITH STORE
  //const currentResult = store.searchResults
  
  if (currentResult?.name) {
    
    console.log(currentResult.name)
    console.log(currentResult.genres)
    // var jsonGenres = JSON.parse(currentResult.genres);
    // for (var i = 0; i < jsonGenres.genres.length; i++) {
    //     var genre = jsonGenres.genres[i];
    //     console.log(genre);
    // }
    
    const genres = currentResult.genres.map((genre, index) =>
      <p key={index}> {genre} </p>
    )
    
    // const images = currentResult.images.map((image, index) =>
    //   <p key={index}> {image} </p>
    // )
    
    return (
      <div>
        <p>Artist Name: {currentResult.name}</p>
        <p>Followers: {currentResult.followers}</p>
        {genres}
        <img src={currentResult.images[0].url} />
      </div>

      )
  } else {
    return(
      <p>No artist entered.</p>
    )
  }
}


function Analyze() {
  const [currentSearch, setSearch] = useState('');
  const [currentResult, setResult] = useState(null);

  
  // WORKS!!!
  const fetchArtist = () => {
    fetch('/api/analyze?artist='+currentSearch)
      .then(res => res.json())
      .then(data => {
      setResult({
        name: data.name,
        followers: data.followers,
        genres: data.genres,
        images: data.images,
      });
      })
  }
  
  // ATTEMPTING TO REPLACE WITH STORE...
  // const fetchArtist = () => {
  //   fetch('/api/analyze?artist='+currentSearch)
  //     .then(res => res.json())
  //     .then(data => {
  //     store.searchResults = data;
  //     })
  // }

  // IS NOT CURRENTLY USED -> HANDLE CHANGE IS, CAN I CHANGE THAT?
  useEffect(() => {
    fetchArtist()
  }, []);
  
  
  function handleChange(e) {
    const search = e.target.value
    setSearch(search)

    if (search !== '') {
      fetchArtist()
    }
  }

  return (
    <div id="analyze" className="page-body">
      <span className="search-span">
        <input type="search"
               className="search-box"
               id="artist-search"
               src={"search_icon"}
               placeholder="Search Artist"
               autoComplete="off"
               spellCheck="false"
               onChange={handleChange}
        />
      </span>
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
      <Artist currentResult={currentResult} />
    </div>
  );
};


export default Analyze;