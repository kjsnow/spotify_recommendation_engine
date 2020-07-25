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
    
    const genres = currentResult.genres.map((genre, index) =>
      <p key={index}> {genre} </p>
    )
    
    const image_url = currentResult.images[0].url
    
    // const images = currentResult.images.map((image, index) =>
    //   <p key={index}> {image} </p>
    // )
    
    return (
      <div>
        <p>Artist Name: {currentResult.name}</p>
        <p>Followers: {currentResult.followers}</p>
        {genres}
        <img src={image_url} />
      </div>

      )
  } else {
    return(
      <div>
        <p>No artist entered.</p>
        <img src={logo} className="App-logo" alt="logo" />
      </div>
    )
  }
}


function Analyze() {
  
  const [currentSearch, setSearch] = useState('');
  const [currentResult, setResult] = useState({});
  
  const handleChange = event => {
    const search = event.target.value
    setSearch(search);
  }
  
  useEffect(() => {
    fetchArtist()
  }, [currentSearch]);
  
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

  return (
    <div id="analyze" className="page-body">
      <span className="search-span">
        <input type="search"
               className="search-box"
               id="artist-search"
               src={"search_icon"}
               placeholder="Search Artist"
               value={currentSearch}
               autoComplete="off"
               spellCheck="false"
               onChange={handleChange}
        />
      </span>
      <Artist currentResult={currentResult} />
    </div>
  );
};


export default Analyze;