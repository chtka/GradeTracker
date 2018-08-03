import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import { List } from 'semantic-ui-react';
import logo from './logo.svg';
import './App.css';
import Home from './components/Home';
import Login from './components/Login';
import Register from './components/Register';
import Cookies from 'js-cookie';
import PrivateRoute from './PrivateRoute'
import NoAuthRoute from './NoAuthRoute';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isAuthenticated: false
    }

    this.handleLogin = this.handleLogin.bind(this);
    this.handleLogout = this.handleLogout.bind(this);
  }

  componentDidMount() {
    console.log(document.cookie)
    if (Cookies.get('gt_key')) {
      this.setState((prevState, props) => {
        return {
          ...prevState,
          isAuthenticated: true
        }
      });
    }
  }

  handleLogin() {
    this.setState((prevState, props) => {
      return {
      ...prevState,
        isAuthenticated: true
      }
    });
  }

  handleLogout() {
    fetch('http://localhost:8000/rest_auth/logout/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json', 
        'Authorization': 'Token ' + Cookies.get('gt_key')
      }
    })
    .then((response) => {
      console.log(response);
      Cookies.remove('gt_key')
      console.log(document.cookie);
      this.setState((prevState, props) => {
        return {
          ...prevState,
          isAuthenticated: false
        }
      });
    });

  }

  render() {
    const childProps = {
      handleLogin: this.handleLogin
    };
    console.log(this.state.isAuthenticated);
    return (
      <div className="App">
        <Router>
          <div>
            <List>
              <List.Item>
                <Link to="/">Home</Link>
              </List.Item>
              {this.state.isAuthenticated ? 
                <List.Item onClick={this.handleLogout}>
                  <Link to="/login">Logout</Link>
                </List.Item> :
                <List.Item>
                  <Link to="/login">Login</Link>
                </List.Item>
              }

            </List>
            <PrivateRoute exact path="/" authed={this.state.isAuthenticated} component={Home} />
            <NoAuthRoute path="/login" authed={this.state.isAuthenticated} component={Login}  handleLogin={this.handleLogin}/>
            <NoAuthRoute path="/register" authed={this.state.isAuthenticated} component={Register} handleLogin={this.handleLogin}/>
          </div>
        </Router>
      </div>
    );
  }
}

export default App;
