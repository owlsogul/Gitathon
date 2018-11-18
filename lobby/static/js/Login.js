import React from 'react';

function Login ({gitathonLogo, hackNum, teamNum}){
    return (
      <table className = "LoginMain">
          <tr>
              <td className = "LogoIcon">
                  <ShowLogo logoPath = {gitathonLogo} name = {"gitathonLogo"}/>
              </td>
          </tr>
          <tr>
              <td className = "Intro">
                  <Welcome hackNum = {hackNum} teamNum = {teamNum} />
              </td>
          </tr>
          <tr>
              <td className = "InputID">
                  <input type="text" name = "inputID"/>
              </td>
          </tr>
          <tr>
              <td className = "InputPW">
                  <input type="text" name = "inputPW"/>
              </td>
          </tr>
          <tr>
              <td className = "LoginBtn">
                  <button>?®Íªò?òÍ∏∞</button>
              </td>
          </tr>
          <tr>
              <td className = "Join">
                  <div>
                      ?ÑÏßÅ Í≥ÑÏ†ï???ÜÏúº?†Í???
                       <font color = "red"> ?åÏõêÍ∞Ä??</font>
                  </div>
              </td>
          </tr>
      </table>
    )
}

function ShowLogo({logoPath, name}) {
    return(
      <img src = {logoPath} className = {name} alt ={name}/>
    )
}

function Welcome({hackNum, teamNum}){
  return(
    <span className = "Welcoming">
      «ˆ¿Á <font color = "red">{hackNum}</font>∞≥¿«
      «ÿƒø≈Ê∞˙ <font color = "red">{teamNum}</font>∞≥¿«
      ∆¿«¡∑Œ¡ß∆Æ∞° ¡¯«‡¡ﬂ¿‘¥œ¥Ÿ.
    </span>
  )
}

export default Login;
