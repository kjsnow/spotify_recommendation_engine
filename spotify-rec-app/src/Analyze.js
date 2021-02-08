import React, { useEffect, useState, handleChange, useReducer } from "react";
import logo from "./images/logo.svg";
import search_icon from "./images/search-icon.png";
import { requestStarted, requestSuccessful, requestFailed } from "./actions.js";
import { reducer } from "./reducer.js";

// THEMES
import resolveConfig from "tailwindcss/resolveConfig"
import config from "./tailwind.config"
const tailwindConfig = resolveConfig(config)
const theme_colors = tailwindConfig.theme.colors

//import useSWR from 'swr'

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
  const currentResult = props.currentResult;

  // ATTEMPTING TO REPLACE WITH STORE
  //const currentResult = store.searchResults

  if (currentResult.data?.name) {
    const genres = currentResult.data.genres.map((genre, index) => (
      <p key={index}> {genre} </p>
    ));
    
    const top_track_names = currentResult.data.top_tracks.map((track, index) => (
      <p key={index}> {track.name} </p>
    ));

    const image_url = currentResult.data.images[0].url;

    // const images = currentResult.images.map((image, index) =>
    //   <p key={index}> {image} </p>
    // )

    return (
      <div className="relative m-4 border border-gray-300 rounded-lg">
        <img className="inline-block h-56 w-56 p-2" viewBox="0 0 30 30" src={image_url} style={{backgroundColor: theme_colors.c1}} />
        <table className="table-auto" style={{backgroundColor: theme_colors.c3, color: theme_colors.c5}}>
          <tr>
            <th className="border px-4 py-2"> Artist Name: </th>
            <td className="border px-4 py-2"> {currentResult.data.name} </td>
          </tr>
          <tr>
            <th className="border px-4 py-2"> Followers: </th>
            <td className="border px-4 py-2"> {currentResult.data.followers} </td>
          </tr>
          <tr>
            <th className="border px-4 py-2 align-text-top"> Genres: </th>
            <td className="border px-4 py-2 text-left"> {genres} </td>
          </tr>
          <tr>
            <th className="border px-4 py-2 align-text-top"> Top 10 Tracks: </th>
            <td className="border px-4 py-2 text-left"> {top_track_names} </td>
          </tr>
        </table>
        {/*<p>Artist Name: {currentResult.data.name}</p>*/}
        {/*<p>Followers: {currentResult.data.followers}</p>*/}
        {/*Genres: {genres}*/}
      </div>
    );
  } else {
    return (
      <div className="relative pt-4">
        <p>No artist entered.</p>
        <img src={logo} className="App-logo" alt="logo" />
      </div>
    );
  }
}

function Analyze() {
  const [currentSearch, setSearch] = useState("");
  //const [currentResult, setResult] = useState({});
  const [currentResult, dispatch] = useReducer(reducer, {
    isLoading: true,
    data: null,
    error: null,
  });

  const handleChange = (event) => {
    const search = event.target.value;
    setSearch(search);
  };

  useEffect(() => {
    const abortController = new AbortController();

    const fetchArtist = async () => {
      dispatch(requestStarted());

      try {
        fetch("/api/search_artist?artist=" + currentSearch, {
          signal: abortController.signal,
        })
          .then((res) => res.json())
          .then((data) => {
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
    <div className="inline-block p-4" id="analyze">
      <span className=" pl-4 left-0 inline-block">
        <input
          className="bg-white focus:outline-none focus:shadow-outline border border-gray-300 rounded-lg py-2 px-4 block appearance-none leading-normal"
          style={{color:theme_colors.c5}}
          type="search"
          id="artist-search"
          placeholder="Search Artist"
          src={"search_icon"}
          value={currentSearch}
          autoComplete="off"
          spellCheck="false"
          onChange={handleChange}
        />

        {/*<input*/}
        {/*  type="search"*/}
        {/*  className="search-box"*/}
        {/*  id="artist-search"*/}
        {/*  src={"search_icon"}*/}
        {/*  placeholder="Search Artist"*/}
        {/*  value={currentSearch}*/}
        {/*  autoComplete="off"*/}
        {/*  spellCheck="false"*/}
        {/*  onChange={handleChange}*/}
        {/*/>*/}
      </span>
      <Artist currentResult={currentResult} />
    </div>
  );
}

export default Analyze;
