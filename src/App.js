import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import RegisterPage from './pages/RegisterPage';

function App() {
  

  return (
    <BrowserRouter>
        <Switch>
          <Route exact path="/" component={LandingPage} />
          <Route path="/register" component={RegisterPage} />
        </Switch>
    </BrowserRouter>
  );
}

export default App;
