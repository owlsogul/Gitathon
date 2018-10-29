import React, { Component } from 'react';
import './Login.css';

class Login extends Component{
  render(){
    return(
      <div className="container">
      <table className="LogoMain">
        <tr>
          <td className="MainLogo">
            <ShowLogo logoPath = {this.props.gitathonLogo} name = {"gitaLogo"}/>
          </td>
        </tr>
        <tr>
          <td className="Intro">
            <Intro hackNum = {"4000"} teamNum = {"25093"} />
          </td>
        </tr>
        <tr>
          <td className="ID">
            <input type="text" name = "IdInput" value="ID를 입력하세요."/>
          </td>
        </tr>
          <td>
            <input type="text" name = "PwInput" value="PW를 입력하세요."/>
          </td>
        <tr>
          <td>
          <button>함께하기</button>
          </td>
        </tr>
        <tr>
          <td>
            <Register />
          </td>
        </tr>
      </table>
      </div>
    );
  }
}

function ShowLogo({logoPath, name}) {
  return(
    <a herf="localhost:3000"><img src = {logoPath} className = {name} alt ={name}/></a>
  )
}

function Intro({hackNum, teamNum}){
  return(
    <div>
      현재 <font color="red">{hackNum}</font>개의
      해커톤과 <font color="red">{teamNum}</font>개의 팀프로젝트가 진행중입니다.
    </div>
  )
}

function Register(){
  return(
    <div>
      아직 계정이 없으신가요?
      <font color="red"><a href="https://naver.com">회원가입</a></font>
    </div>
  )
}

export default Login;
