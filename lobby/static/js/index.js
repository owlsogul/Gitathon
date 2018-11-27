import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';
import * as serviceWorker from './serviceWorker';

class Test extends React.Component{
	render(){
		var list = window.props;
		console.log(list)
		return <div>
			{list.map(item =>
				<App
				numHackathon={list.numHackathon}
				numTeamproject={list.numTeamproject} />)}</div>;
	}
}

ReactDOM.render(
	<Test />,
	document.getElementById('react')
);
