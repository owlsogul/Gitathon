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
                  <button>?�께?�기</button>
              </td>
          </tr>
          <tr>
              <td className = "Join">
                  <div>
                      ?�직 계정???�으?��???
                       <font color = "red"> ?�원가??</font>
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
      ���� <font color = "red">{hackNum}</font>����
      ��Ŀ��� <font color = "red">{teamNum}</font>����
      ��������Ʈ�� �������Դϴ�.
    </span>
  )
}

export default Login;
