import React, { Component } from 'react';
import NaviMenu from './NaviMenu';
import MakeTeam from './MakeTeam';
import LoginMain from './Login';

const metaInfo = [
    {
      gitathonLogo : "/img/gitathonLogo.png",
      userName : "장예솔",
      hackathonLogo : "/img/hackathonLogo.png",
      profileLogo : "/img/profileLogo.png"
    }
]

class App extends Component {
    render() {
        return (
            <div className="App">
                {
                /*
                 * Team Make Site

                <MakeTeam />
                */
                }
                {
                /*
                 * Login Site

                <LoginMain
                    gitathonLogo = {metaInfo[0].gitathonLogo}
                    hackNum = {3000}
                    teamNum = {27450}
                />
                */
                }
            </div>
        );
    }
}

export default App;
