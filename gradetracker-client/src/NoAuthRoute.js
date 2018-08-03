import React from 'react';
import { Route, Redirect } from 'react-router-dom';

export default ({component: Component, authed, ...rest}) => {
  return (
    <Route {...rest} render={(props) => authed === false ? <Component {...props} {...rest}/> : 
      <Redirect to={{pathname: '/', state: {from: props.location}}} />}/>
  )
};