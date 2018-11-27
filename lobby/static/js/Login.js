import React, {Component} from 'react';
import { Button } from 'reactstrap';

class LoginMain extends Component{
    state={
        mode: 'Login'
    }

    render(){
        {/*
        let hackNum = 0;
        let teamPNum = 0;
        items(this.props.numData, (key, value) => {
            if (key == "numHackathon"){
                hackNum = value
            }
            else if (key  == "numTeamproject"){
                teamNum = value
            }
        })
        */}

        return(
            console.log(this.props),
            <div className="LoginScreen">
            if this.state.mode == 'Login'{
                <Login
                    gitathonLogo = {this.props.gitathonLogo}
                    hackNum = {hackNum}
                    teamNum = {teamNum} />
            }
            else if {
                <Register />
            }
            </div>
        );
    }
}

class Login extends LoginMain{
    constructor(props){
        super(props);
    }

    render(){
        return (
            <div class = "container">
                <div class = "row">
                    <div class = "col-2">
                    </div>
                    <div class = "col-8">
                        <table className = "LoginMain">
                            <tr>
                                <td className = "LogoIcon">
                                    <ShowLogo logoPath = {this.props.gitathonLogo} name = {"gitathonLogo"}/>
                                </td>
                            </tr>
                            <tr>
                                <td className = "Intro">
                                    <Welcome hackNum = {this.props.hackNum} teamNum = {this.props.teamNum} />
                                </td>
                            </tr>
                            <tr>
                                <td className = "InputID">
      	    	                    <input />
                                </td>
                            </tr>
                            <tr>
                                <td className = "InputPW">
      		                        <input />
                                </td>
                            </tr>
                            <tr>
                                <td className = "LoginBtn">
                                    <Button color = "primary">함께하기</Button>
                                </td>
                            </tr>
                            <tr>
                                <td className = "Join">
                                    <div>
                                        아직 계정이 없으신가요?
                                        <Button color = "danger" onclick="regBtnClick();">회원가입</Button>
                                    </div>
                                </td>
                            </tr>
                        </table>
                    </div>
                <div class = "col-2">
                </div>
            </div>
        </div>
        );
    }

    regBtnClick(){
        this.setState({
            mode: "Register"
        });
    }
}

class Register extends LoginMain{
    render(){
        return(
            <div class = "container">
                <Button onclick="finBtnClick();">완료</Button>
            </div>
        );
    }

    finBtnClick(){
        this.setState({
            mode: "Login"
        });
    }
}

function ShowLogo({logoPath, name}) {
    return(
      <img src = {logoPath} className = {name} alt ={name}/>
    )
}

function Welcome({hackNum, teamNum}){
  return(
    <span className = "Welcoming">
      현재  <font color = "red">{hackNum}</font>개의
      해커톤과 <font color = "red">{teamNum}</font>개의
      팀프로젝트가 진행중입니다.
    </span>
  )
}

export default Login;
