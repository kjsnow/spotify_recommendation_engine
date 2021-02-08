import React from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from "./Home";
import Analyze from "./Analyze";
import Compare from "./Compare"
import ToDo from "./ToDo";
import PlaceHolder from "./PlaceHolder"

const Main = () => (
  <Switch>
    <Route exact path = '/home' component={Home}></Route>
    <Route exact path = '/analyze' component={Analyze}></Route>
    <Route exact path = '/compare' component={Compare}></Route>
    <Route exact path = '/todo' component={ToDo}></Route>
    <Route exact path = '/hold' component={PlaceHolder}></Route>
  </Switch>
)

export default Main