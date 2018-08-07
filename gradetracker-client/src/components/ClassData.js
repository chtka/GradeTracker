import React, { Component } from 'react';
import Cookies from 'js-cookie';
import { Header, List } from 'semantic-ui-react';

export default class ClassData extends Component {

  constructor(props) {
    super(props);
    this.state = {
      class_data: {
        categories: [],
        course: undefined,
        full_desc: undefined,
        grade: undefined,
        id: undefined,
        professor: undefined,
        quarter: undefined,
        year: undefined
      }
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
      this.setState((prevState, props) => {
        return {
          class_data: response
        }
      });
    })
    .catch((err) => {
      console.log(err);
    });
  }


  render() {
    console.log('state', this.state)
    const class_categories = this.state.class_data.categories.map((category) => {
      return (
        <div key={category.id}>
          <Header as='h2'>{category.name}</Header>
          <List>
            {category.assignments.map((assignment) => {
              console.log(assignment.id)
              return (
                <List.Item key={assignment.id}>
                  {assignment.name}
                </List.Item>
              );
            })}
          </List>
        </div>
      )
    });
    return (
      <div>
        {class_categories}
      </div>
    )
  }
}