import subprocess
import os
import sys

def isNotVaildArguments():
    if len(sys.argv) < 2:
        return True
    else:
        return False

def isResource():
    if len(sys.argv) > 2:
        return True
    else:
        return False

def isNotVaildRemoteBranchs(remote_branch):
    if len(remote_branch) == 0:
        return True
    else:
        return False

def makeResourceList():
    res = []
    for index in range(len(sys.argv) - 2):
        res.append(sys.argv[index+2])
    return res

def changeDirAndGetOldPath(path):
	old_path = os.getcwd()
	os.chdir(path)
	return old_path

def getAllRemoteBranch():
	remoteBranch = []

	try:
		result = subprocess.check_output('git branch -r -a', shell=True).decode()
		result.encode()

		for line in result.split("\n"):
			words = line.replace("->", "/").replace(" ", "").split("/")

			if len(words) == 0:
				continue

			if words[0] == "remotes":
				if (words[2] != 'HEAD'):
				    remoteBranch.append(words[2])

	except subprocess.CalledProcessError as e:
		return []

	return remoteBranch

def parseGit(branch, resource):
	try:
		command = "git checkout " + branch
		os.system(command)

		result = subprocess.check_output('git log --abbrev-commit --name-status', shell=True).decode()
		newCommit = findNewCommit(result, lastCommit, resource)
		findCommandAndCode(newCommit)

		if len(newCommit) == 0:
			return 0

		else:
			return newCommit

	except subprocess.CalledProcessError as e:
		return 0




def findNewCommit(output, lastCommit, extens):
	newCommit = []
	oneDic = {}
	isNotFirst = False
	totalRes = 0
	output.encode()

	for line in output.split("\n"):
		words = line.split()

		if len(words) != 0:

			if words[0] == "commit":
				if lastCommit == words[1]:
					break

				if isNotFirst:
					oneDic['resource'] = totalRes
					newCommit.append(oneDic)
					totalRes = 0
					oneDic = {}

				oneDic["commit"] = words[1]
				isNotFirst = True

			elif words[0] == "Author:":
				name = ""
				for word in words:
					if word[0] == "<":
						break
					if word != "Author:":
						name = name + word + " "
				if name[len(name) - 1] == " ":
					name = name[:len(name)-1]
				oneDic["author"] = name

			elif words[0] == "A":
				for res in extens:
					if words[1][words[1].rfind(".") + 1:] == res:
						totalRes = totalRes + 1

	return newCommit

def findCommandAndCode(newCommit):
	for commit in newCommit:

		extension = ""
		command = 0
		code = 0
		isCommand = False
		lines = subprocess.check_output('git show ' + commit['commit'], shell=True)

		print("#####################")
		print("word start: ")
		for line in lines.split(b"\n"):

			words = line.split()

			if len(words) != 0:

				if words[0] == b"+++" or words[0] == b"---":
					extension = (words[1][words[1].rfind(b".") + 1:])
					extension = extension.decode()

				elif chr(words[0][0]) == '+' or chr(words[0][0]) == '-':

					print ("extension: ", extension)

					if extension == "c" or extension == "cpp" or extension == "ino":
						if isCCommand(words, isCommand):
							command = command + 1
						else:
							code = code + 1

					if extension == "java" or extension == "jj":
						if isJavaCommand(words, isCommand):
							command = command + 1
						else:
							code = code + 1

					elif extension == "py":
						if isPyCommand(words):
							command = command + 1
						else:
							code = code + 1

					else:
						code = code + 1


		commit["code"] = code
		commit["command"] = command
		code = 0
		command = 0
		print("word end")


def isCCommand(words, flag):
	if "//" in words:
		return True
	elif "/*" in words:
		flag = True
		return True

	elif flag:
		return True
	elif "*/" in words:
		flag = False
		return True
	else:
		return True

def isJavaCommand(words, flag):
	if "//" in words:
		return True
	elif ("/*" or "/**") in  words:
		flag = True
		return True
	elif flag:
		return True
	elif "*/" in words:
		flag = False
		return True
	else:
		return False

def isPyCommand(words):
	if words[1][0:1] == "#":
		return True

	return False


if __name__ == "__main__":

    if isNotVaildArguments():
        sys.exit(1)

    resouce = []
    path = sys.argv[1]
    old_path = changeDirAndGetOldPath(path)
    remote_branch = getAllRemoteBranch()
    result = {}
    branchData = {}

    if isNotVaildRemoteBranchs(remote_branch):
        sys.exit(1)

    result['branchList'] = remote_branch

    if isResource():
        resource = makeResourceList()

    for branch in remote_branch:
        branchData[branch] = parseGit(branch, resource)

    result['branchData'] = branchData

    print(result)
