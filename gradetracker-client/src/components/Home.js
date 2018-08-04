import React, { Component } from 'react';
import Cookies from 'js-cookie';
import { Message } from 'semantic-ui-react';

class Home extends Component {

  constructor(props) {
    super(props);

    this.state = {
      classes: []
    }
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/classes/', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + Cookies.get('gt_key')
      }
    })
    .then(response => response.json())
    .then((response) => {
      console.log(response);
      this.setState((prevState, props) => {
        return {
          classes: response.results
        }
      });
    })
  }

  render() {
    console.log(this.state.classes)
    const class_infos = this.state.classes.map((class_) => {
      return (
        <Message>
          <Message.Header>
            {class_['full_desc']}
          </Message.Header>
          <Message.List>
            <Message.Item>
              Term: {class_['quarter'] + class_['year']}
            </Message.Item>
            <Message.Item>
              Grade: {(class_['grade'] * 100).toString() + '%'}
            </Message.Item>
          </Message.List>
        </Message>
      )
    })
    console.log(this.state.classes)
    return (
      <div>
        <p>{class_infos}</p>
      </div>
    )
  }
}

export default Home;