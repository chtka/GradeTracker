import React, { Component } from 'react';
import { Button, Form } from 'semantic-ui-react';
import Cookies from 'js-cookie';


export default class Register extends Component {

  constructor(props) {
    super(props);

    this.handleRegister = this.handleRegister.bind(this);
  }

  handleRegister(e) {
    e.preventDefault();
    const data = {
      username: e.target.username.value,
      email: e.target.email.value,
      password1: e.target.password1.value,
      password2: e.target.password2.value,
    }
    fetch('http://localhost:8000/rest-auth/registration/', {
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
        console.log('error registering')
      }
    })
    .catch((err) => {
      console.log(err)
    })
  }

  render() {
    return (
      <div>
        <Form onSubmit={this.handleRegister}>
          <Form.Field>
            <Form.Input name='username' label='Username' placeholder='username'/>
          </Form.Field>
          <Form.Field>
            <Form.Input name='email' type='email' label='E-mail Address' placeholder='username@example.com'/>
          </Form.Field>          
          <Form.Field>
            <Form.Input name='password1' type='password' label='Password'/>
          </Form.Field>
          <Form.Field>
            <Form.Input name='password2' type='password' label='Re-type Password'/>
          </Form.Field>
          <Button type='submit'>Register</Button>
        </Form>
      </div>
    )
  }  
}