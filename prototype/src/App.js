import React, { Component } from 'react';
import NaviMenu from './NaviMenu';
import MakeTeam from './MakeTeam';

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
                <NaviMenu
                    gitathonLogo={metaInfo[0].gitathonLogo}
                    userName={metaInfo[0].userName}
                    hackathonLogo = {metaInfo[0].hackathonLogo}
                    profileLogo={metaInfo[0].profileLogo}
                />
                <br/><br/><br/>
                <MakeTeam />
            </div>
        );
    }
}

export default App;
