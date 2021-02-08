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

function Track(props) {
  const currentResult = props.currentResult.data;

  // ATTEMPTING TO REPLACE WITH STORE
  //const currentResult = store.searchResults

  if (currentResult?.track_name) {
    // const artists = currentResult.data.artists.map((artist, index) => (
    //   <p key={index}> {artist} </p>
    // ));
    
    const popularity = currentResult.popularity;
    const preview_url = currentResult.preview_url;
    // const features = currentResult.features.map((feature, index) => (
    //   <p key={index}> {feature} </p>
    // ))
    const features = Object.entries(currentResult.features).map(([key, value]) => (
      <p key={key}>{key}: {value}</p>
    ))
    
    return (
      <div className="relative m-4 border border-gray-300 rounded-lg">
        {/*<img className="inline-block h-56 w-56 p-2" viewBox="0 0 30 30" src={image_url} style={{backgroundColor: theme_colors.c1}} />*/}
        <table className="table-auto" style={{backgroundColor: theme_colors.c3, color: theme_colors.c5}}>
          <tr>
            <th className="border px-4 py-2"> Track Name: </th>
            <td className="border px-4 py-2">
              <a href={preview_url}>{currentResult.track_name}</a> </td>
          </tr>
          {/*<tr>*/}
          {/*  <th className="border px-4 py-2"> Artists: </th>*/}
          {/*  <td className="border px-4 py-2"> {currentResult.data.followers} </td>*/}
          {/*</tr>*/}
          {/*<tr>*/}
          {/*  <th className="border px-4 py-2 align-text-top"> Popularity: </th>*/}
          {/*  <td className="border px-4 py-2 text-left"> {popularity} </td>*/}
          {/*</tr>*/}
          <tr>
            <th className="border px-4 py-2 align-text-top"> Features: </th>
            <td className="border px-4 py-2 text-left"> {features} </td>
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
        <p>No track entered.</p>
        <img src={logo} className="App-logo" alt="logo" />
      </div>
    );
  }
}

function Compare() {
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

    const fetchTrack = async () => {
      dispatch(requestStarted());

      try {
        fetch("/api/search_track?track=" + currentSearch, {
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

    fetchTrack();

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
          id="track-search"
          placeholder="Search Track"
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
      <Track currentResult={currentResult} />
    </div>
  );
}

export default Compare;
