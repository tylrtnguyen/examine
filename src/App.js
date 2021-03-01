import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import NotFoundPage from './pages/NotFoundPage';
import AdminDashboard from './pages/AdminDashboard';

function App() {
  
  return (
    <BrowserRouter>
        <Switch>
          <Route exact path="/" component={LandingPage} />
          <Route path="/register" component={RegisterPage} />
          <Route path="/login" component={LoginPage} />
          <Route exact path="/dashboard" component={AdminDashboard} />
          <Route path="*" component={NotFoundPage} />
        </Switch>
    </BrowserRouter>
  );
}

export default App;
