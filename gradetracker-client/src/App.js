import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import { List } from 'semantic-ui-react';
import logo from './logo.svg';
import './App.css';
import Home from './components/Home';
import Login from './components/Login';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Router>
          <div>
            <List>
              <List.Item>
                <Link to="/">Home</Link>
              </List.Item>
              <List.Item>
                <Link to="/login">Login</Link>
              </List.Item>
            </List>
            <Route exact path="/" component={Home}/> 
            <Route path="/login" component={Login}/>
          </div>
        </Router>
      </div>
    );
  }
}

export default App;
