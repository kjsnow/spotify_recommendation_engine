import React, {useEffect, useState, handleChange, useReducer} from "react";
import logo from "./images/logo.svg";
import search_icon from "./images/search-icon.png";
import {
  requestStarted,
  requestSuccessful,
  requestFailed,
} from './actions.js';
import { reducer } from './reducer.js';

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
  
  if (currentResult.data?.name) {
    
    const genres = currentResult.data.genres.map((genre, index) =>
      <p key={index}> {genre} </p>
    )
    
    const image_url = currentResult.data.images[0].url
    
    // const images = currentResult.images.map((image, index) =>
    //   <p key={index}> {image} </p>
    // )
    
    return (
      <div>
        <p>Artist Name: {currentResult.data.name}</p>
        <p>Followers: {currentResult.data.followers}</p>
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
  //const [currentResult, setResult] = useState({});
  const [currentResult, dispatch] = useReducer(reducer, {
    isLoading: true,
    data: null,
    error: null,
  });
  
  const handleChange = event => {
    const search = event.target.value
    setSearch(search);
  }
  
  
  useEffect(() => {
    
    const abortController = new AbortController();
    
    const fetchArtist = async () => {
      dispatch(requestStarted());
      
      try {
        fetch('/api/analyze?artist=' + currentSearch, {signal: abortController.signal})
          .then(res => res.json())
          .then(data => {
            dispatch(requestSuccessful({ data }));
            });
      } catch (e) {
        // Only throw error when the fetch was not aborted
        if (!abortController.signal.aborted) {
          //console.error(e);
          dispatch(requestFailed({ error: e.message }));
        }
      }
    };
    
    fetchArtist();
    
    return () => {
      abortController.abort();
    };
  }, [currentSearch]);
  
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