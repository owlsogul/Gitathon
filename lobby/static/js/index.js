import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';
import * as serviceWorker from './serviceWorker';

class Test extends React.Component{
	render(){
		var list = window.props;
		console.log(list)
		return <App numHackathon={list.numTeamproject} numTeamproject={list.numTeamproject} />;
	}
}

ReactDOM.render(
	<Test />,
	document.getElementById('react')
);
