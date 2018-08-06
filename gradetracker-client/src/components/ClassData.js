import React, { Component } from 'react';
import Cookies from 'js-cookie';

export default class ClassData extends Component {

  constructor(props) {
    super(props);
    this.state = {

    };
  }

  componentDidMount() {
    console.log(this.props.match.params.id)
    fetch(`http://127.0.0.1:8000/classes/${this.props.match.params.id}/`, {
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
      // this.setState((prevState, props) => {
      //   return {
      //     classes: response.results
      //   }
      // });
    })
    .catch((err) => {
      console.log(err);
    });
  }


  render() {
    return (
      <div>{this.props.match.params.id}</div>
    )
  }
}