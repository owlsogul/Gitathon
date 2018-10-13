import React from 'react';

function NaviMenu({gitathonLogo, userName, hackathonLogo, profileLogo}){
  return (
    <div className="NaviMenu">
      <div className = "GitathonLogo">
        <ShowLogo logoPath = {gitathonLogo} name = {"gitathonLogo"}/>
      </div>
      <div className = "UserName">
        <Welcome name = {userName}/>
      </div>
      <div className = "HackathonLogo">
        <ShowLogo logoPath = {hackathonLogo} name = {"hackathonLogo"}/>
      </div>
      <div className = "profileLogo">
        <ShowLogo logoPath = {profileLogo} name = {"profileLogo"} />
      </div>
    </div>
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