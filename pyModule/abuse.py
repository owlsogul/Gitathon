import subprocess
import os
import sys

old_path = ""

def showDiffCommit(hackName, teamName, commitId):

    #path = "C:\\Users\\장예솔\\Desktop\\Yedori\\중앙대\\3학년\\2학기\\캡스톤\\Source\\Source\\capstone\\Gitathon"
    #os.chdir(path)
	changeDir(hackName, teamName)os
    try:
        output = subprocess.check_output('git show ' + commitId, shell=True).decode()
        output.encode()

        print(output)


    except subprocess.CalledProcessError as e:
        print("Error //" , e.output)

    return output


def makeFileList(hackName, teamName, commitId):

	#path = "C:\\Users\\장예솔\\Desktop\\Yedori\\중앙대\\3학년\\2학기\\캡스톤\\Source\\Source\\capstone\\Gitathon"
	#os.chdir(path)
	changeDir(hackName, teamName)
	print('파일리스트 만들기 실행')

	fileList = []

	try:
		output = subprocess.check_output('git show ' + commitId + ' --name-status', shell=True).decode()
		output.encode()

		fileList.append(commitId)

		for line in output.split("\n"):

			words = line.split()

			if len(words) != 0 :
				# 파일추가
				if words[0] == "A" or words[0] == "D" or words[0] == "M":

					fileName = words[1]
					fileList.append(fileName)

	except subprocess.CalledProcessError as e:
		print("Error //" , e.output)


	return fileList
