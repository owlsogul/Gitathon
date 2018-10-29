import React, { Component } from 'react';
import NaviMenu from './NaviMenu';
import './MainPage.css';

class MainPage extends Component {
    render() {
        return (
            <div className="MainPage">
                <NaviMenu />
                <table borader = "1" bordercolor="red">
                    <tr>
                        <td className = "MyTeams">
                            FIRST
                        </td>
                        <td className = "Recents" rowspan =  "2">
                            SECOND
                        </td>
                    </tr>
                    <tr>
                        <td className = "MyHacks">
                            THIRD
                        </td>
                    </tr>
                </table>
            </div>
        );
    }
}

function TeamTable(){
    return(
        <div className = "TeamTable">
            <table boarder = "1" bordercolor = "blue">
            </table>
        </div>
    )
}

export default MainPage;
