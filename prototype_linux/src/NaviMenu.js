import React from 'react';
import './NaviMenu.css'

function NaviMenu({gitathonLogo, userName, hackathonLogo, profileLogo}){
  return (
     <table className="NaviMenu">
      <tr>
        <td className = "MainLogo">
          <ShowLogo logoPath = {gitathonLogo} name = {"gitathonLogo"}/>
        </td>
        <td className = "UserName">
          <Welcome name = {userName}/>
        </td>
        <td className = "Hackathon">
          <ShowLogo logoPath = {hackathonLogo} name = {"hackathonLogo"}/>
          <b>Hackathon</b>
        </td>
        <td className = "profile">
          <ShowLogo logoPath = {profileLogo} name = {"profileLogo"} />
          <b>Profile</b>
        </td>
      </tr>
    </table>
  )
}

function Welcome({name}){
  return(
    <span className = "Welcoming">
      <font color = "purple">{name} </font> 님 환영합니다!!
    </span>
  )
}

function ShowLogo({logoPath, name}) {
    return(
      <img src = {logoPath} className = {name} alt ={name}/>
    )
}

export default NaviMenu;
