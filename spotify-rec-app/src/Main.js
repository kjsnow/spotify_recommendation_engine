import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from "./Home";
import Analyze from "./Analyze";
import ToDo from "./ToDo";

const Main = () => (
  <Switch>
    <Route exact path = '/home' component={Home}></Route>
    <Route exact path = '/analyze' component={Analyze}></Route>
    <Route exact path = '/todo' component={ToDo}></Route>
  </Switch>
)

export default Main