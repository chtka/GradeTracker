import React, { Component } from 'react';
import { Form, Dropdown, Button, Message } from 'semantic-ui-react';
import Cookies from 'js-cookie';

export default class NewClassForm extends Component {

  constructor(props) {
    super(props);
    this.currentYear = new Date().getFullYear();
    this.state = {
      year: undefined,
      quarter: undefined,
      creatingClass: false,
      errorMsgs: []
    }
  }
  
  onCreateClass = (e) => {
    e.preventDefault();
    this.setState((prevState, props) => {
      return {
        ...prevState,
        creatingClass: true,
        errorMsgs: []
      }
    });
    const inputs = {
      coursenumber: e.target.coursenumber.value,
      coursedepartment: e.target.coursedepartment.value,
      firstname: e.target.firstname.value,
      lastname: e.target.lastname.value,
    }
    
    const data = {
      course: undefined,
      professor: undefined,
      quarter: this.state.quarter,
      year: this.state.year
    }

    console.log(inputs);

    fetch(`http://localhost:8000/courses/?department=${inputs.coursedepartment}&number=${inputs.coursenumber}`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Authorization': 'Token ' + Cookies.get('gt_key')
      }
    })
    .then((response) => response.json())
    .then((response) => {
      if (response.count > 1) {
        throw new Error('More than one course matches the specified course information.');
      } else {
        data.course = response.results[0].id
        return fetch(`http://localhost:8000/professors/?first_name=${inputs.firstname}&last_name=${inputs.lastname}`, {
          method: 'GET',
          headers : {
            'Accept': 'application/json',
            'Authorization': 'Token ' + Cookies.get('gt_key')
          }
        })
      }
    })
    .then((response) => response.json())
    .then((response) => {
      if (response.count > 1) {
        throw new Error('More than one professor matches the specified first and last names.');
      } else {
        data.professor = response.results[0].id
        console.log(JSON.stringify(data));
        return fetch('http://localhost:8000/classes/', {
          method: 'POST',
          headers : {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + Cookies.get('gt_key')
          },
          body: JSON.stringify(data)
        });
      }
    })
    .then((response) => {
      console.assert(response.status === 201);
      return response.json();
    })
    .then((response) => {
      console.log(response);
      this.props.history.push("/");
    })
    .catch((err) => {
      console.log(err.message);
      this.setState((prevState, props) => {
        return {
          ...prevState,
          creatingClass: false,
          errorMsgs: prevState.errorMsgs.concat([err.message])
        }
      });
    })
  }

  handleChangeQuarter = (e, { value }) => {
    console.log(value);
    this.setState((prevState, props) => {
      return {
        ...prevState,
        quarter: value
      }
    });
  }

  handleChangeYear = (e, { value }) => {
    this.setState((prevState, props) => {
      return {
        ...prevState,
        year: value
      }
    });
  }

  render() {
    const yearOptions = Array.from({length: 9}, (x, i) => i + this.currentYear - 4).map((year) => {
      return {
        text: year.toString(),
        value: year
      }
    })
    const termOptions = [
      {
        text: 'Fall',
        value: 'FA'
      },
      {
        text: 'Winter',
        value: 'WI'
      },
      {
        text: 'Spring',
        value: 'SP'
      },
      {
        text: 'Summer Session 1',
        value: 'SS1'
      },
      {
        text: 'Summer Session 2',
        value: 'SS2'
      }
    ];
    return (
      <div>
        {this.state.errorMsgs.length !== 0 && 
          <Message negative>
            <Message.Header>There was a problem creating the class:</Message.Header>
            <Message.List>
              {this.state.errorMsgs.map((errorMsg) => {
                return (
                  <Message.Item key={errorMsg}>{errorMsg}</Message.Item>
                )
              })}
            </Message.List>
          </Message>
        }
        <Form onSubmit={this.onCreateClass}>
          <label>Course Department Code</label>
          <input name='coursedepartment' placeholder='CSE'/>
          <label>Course Number</label>
          <input name='coursenumber' placeholder='110'/>
          <label>Professor's First Name</label>
          <input name='firstname' placeholder='Gary'/>
          <label>Professor's Last Name</label>
          <input name='lastname' placeholder='Gillespie'/>
          <label>Academic Term</label>
          <Dropdown name='quarter' placeholder='Select Academic Term' fluid onChange={this.handleChangeQuarter} selection options={termOptions}/>
          <label>Year</label>
          <Dropdown name='year' placeholder={this.currentYear.toString()} onChange={this.handleChangeYear} fluid selection options={yearOptions}/>
          <Button className={this.state.creatingClass ? "loading": ""}>
            <i className="plus icon"/>
            Create Class
          </Button>
        </Form>
      </div>
    );
  }
}