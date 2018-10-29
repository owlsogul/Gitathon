import React from 'react';
import NaviMenu from './NaviMenu';
import './MakeTeam.css'

function MakeTeam (){
    return (
      <div className = "MakeTeam">
          <NaviMenu />

          <table className = "TeamMake">
              <tr>
                  <td>
                      팀프로젝트 명
                  </td>
                  <td>
                      <input type="text" name = "teamProjectName"/>
                  </td>
              </tr>
              <tr>
                  <td>
                      소속 해커톤
                  </td>
                  <td>
                      <input type="text" name = "hackathonName" />
                  </td>
              </tr>
              <tr>
                  <td>
                      <button>개설</button>
                  </td>
              </tr>
          </table>
      </div>
    )
}

export default MakeTeam;
