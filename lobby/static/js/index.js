import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import 'bootstrap/dist/css/bootstrap.min.css';
import * as serviceWorker from './serviceWorker';

class Test extends Component{
	render(){
		var list = window.props;
		return <div>{list.map(item => <App data={this.props.numData} />)}</div>;
	}
}

ReactDOM.render(
	<Test />,
	document.getElementById('react')
);
