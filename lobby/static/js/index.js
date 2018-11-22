import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';
import * as serviceWorker from './serviceWorker';

const element = <App />;

ReactDOM.render(
	element,
	document.getElementById('react')
);
