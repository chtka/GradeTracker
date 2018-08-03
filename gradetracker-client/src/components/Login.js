import React, { Component } from 'react';
import Cookies from 'js-cookie';

class Login extends Component {

  onClickLogin(e) {
    fetch('http://127.0.0.1:8000/courses/', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + 'e1fbdcb43e8e26cdf117fc3f555590671431bc76'
      }
    })
    .then(response => response.json())
    .then((response) => {
      console.log(response);
    })
    .catch((err) => {
      console.log(err);
    })
  }

  render() {
    return (
      <div>
        <button onClick={this.onClickLogin}>test</button>
        Login page here.
      </div>
    )
  }
}

export default Login;