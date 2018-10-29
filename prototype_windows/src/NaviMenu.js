import React from 'react';
import './NaviMenu.css'

const metaInfo = [
    {
      gitathonLogo : "/img/gitathonLogo.png",
      userName : "장예솔",
      hackathonLogo : "/img/hackathonLogo.png",
      profileLogo : "/img/profileLogo.png"
    }
]

function NaviMenu(){
  return (
    <div className = "NaviMenuJS">
        <table className="NaviMenu">
            <tr>
                <td className = "MainLogo">
                    <ShowLogo logoPath = {metaInfo[0].gitathonLogo} name = {"gitathonLogo"}/>
                </td>
                <td className = "UserName">
                    <Welcome name = {metaInfo[0].userName}/>
                </td>
                <td className = "Hackathon">
                    <ShowLogo logoPath = {metaInfo[0].hackathonLogo} name = {"hackathonLogo"}/>
                    <b>Hackathon</b>
                </td>
                <td className = "profile">
                    <ShowLogo logoPath = {metaInfo[0].profileLogo} name = {"profileLogo"} />
                    <b>Profile</b>
                </td>
            </tr>
        </table>
    </div>
  )
}

function Welcome({name}){
  return(
    <span className = "Welcoming">
      <font color = "purple">{name} </font> 님 환영합니다!!
      <div className = "Logout">  logout</div>
    </span>
  )
}

function ShowLogo({logoPath, name}) {
    return(
      <img src = {logoPath} className = {name} alt ={name}/>
    )
}

export default NaviMenu;
