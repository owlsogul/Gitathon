import subprocess
import os
import sys

old_path = ""

def showDiffCommit(hackName, teamName, commitId):

    #path = "C:\\Users\\장예솔\\Desktop\\Yedori\\중앙대\\3학년\\2학기\\캡스톤\\Source\\Gitathon"
    #os.chdir(path)
	changeDir(hackName, teamName)
    print('실행')
    try:
        output = subprocess.check_output('git show ' + commitId, shell=True).decode()
        output.encode()

        print(output)


    except subprocess.CalledProcessError as e:
        print("Error //" , e.output)

    return output
