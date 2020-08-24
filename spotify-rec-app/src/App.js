import React from 'react';
import './styles.css';
import Banner from './Banner';
import Main from './Main';

import resolveConfig from "tailwindcss/resolveConfig"
import config from "./tailwind.config"
const tailwindConfig = resolveConfig(config)
const theme_colors = tailwindConfig.theme.colors

const App = () => (
  <div className='App'>
    <div className="App-header w-full">
      <Banner/>
      <div className="flex-auto w-full pt-4 items-center justify-center" style={{backgroundColor: theme_colors.c5, color: theme_colors.c1}}>
        <Main />
      </div>
    </div>
  </div>
);

export default App;

