import React, { Component } from 'react';
import LoginMain from './Login';

const metaInfo = [
    {
      gitathonLogo : "127.0.0.1:8000/img/gitathonLogo.png",
      userName : "wkdthf21",
      hackathonLogo : "127.0.0.1:8000/img/hackathonLogo.png",
      profileLogo : "127.0.0.1:8000/img/profileLogo.png"
    }
]

class App extends Component {
    render() {
        return (
            <div className="App">
                <LoginMain
                    gitathonLogo = {metaInfo[0].gitathonLogo}
                    numHackathon = {3000}
                    numTeamproject = {27450}
                />
            </div>
        );
    }
}

export default App;
