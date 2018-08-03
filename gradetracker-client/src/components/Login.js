import React, { Component } from 'react';
import { Button, Form } from 'semantic-ui-react';
import Cookies from 'js-cookie';

class Login extends Component {

  constructor(props) {
    super(props);
    this.onClickLogin = this.onClickLogin.bind(this);
  }

  onClickLogin(e) {
    e.preventDefault();
    const data = {
      username: e.target.username.value,
      password: e.target.password.value
    }
    console.log(data);
    fetch('http://127.0.0.1:8000/rest_auth/login/', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then((response) => {
      if (response.key) {
        console.log(response);
        Cookies.set('gt_key', response.key)
        console.log(document.cookie);
        this.props.handleLogin();
        this.props.history.push("/");
      } else {
        console.log('incorrect username or password');
      }

    })
    .catch((err) => {
      console.log(err);
    })
  }

  render() {

    console.log(this.props)
    return (
      <div>
        <Form onSubmit={this.onClickLogin}>

          <Form.Field>
            <Form.Input name='username' label='Username'/>
          </Form.Field>
          <Form.Field>
            <Form.Input name='password' label='Password' type='password' />
          </Form.Field>
          <Button type='submit'>Submit</Button>
        </Form>
      </div>
    )
  }
}

export default Login;