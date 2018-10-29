import React, { Component } from 'react';
import MakeTeam from './MakeTeam';
import MainPage from './MainPage';
import LoginMain from './Login';


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
                <MainPage />
            </div>
        );
    }
}

export default App;
