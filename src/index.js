import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import {getAuthToken} from './utils/auth';
import Store from './store';
import axios from 'axios';

axios.interceptors.request.use(config => {
  const token = getAuthToken();
  if (token != null) config.headers.Authorization = token;
  return config;
});

ReactDOM.render(
  <Store.Container>
    <App />
  </Store.Container>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
