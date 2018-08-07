import React, { Component } from 'react';
import Cookies from 'js-cookie';
import { Message, Button } from 'semantic-ui-react';
import { Link } from 'react-router-dom';

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
    const class_infos = this.state.classes.map((class_) => {
      return (
        <Message key={class_['id']}>
          <Message.Header>
            <Link to={`/class/${class_['id']}`}>{class_['full_desc']}</Link>
          </Message.Header>
          <Message.List>
            <Message.Item>
              Term: {class_['quarter'] + class_['year']}
            </Message.Item>
          </Message.List>
        </Message>
      )
    })
    return (
      <div>
        {class_infos}
        <Link to="/new">
          <Button>
            <i className="plus icon"/>
            Create New Class
          </Button>
        </Link>
      </div>
    )
  }
}

export default Home;