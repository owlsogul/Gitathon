import subprocess
import os
import sys

old_path = ""

def parseGit(hackName, teamName, lastCommit, resource):
	old_path = os.getcwd()
	path = "/home/pi/remote/" + hackName + "/" + teamName
	#path  = "C:\\Users\\owlsogul\\Documents\\GitHub\\AI_Project1"
	os.chdir(path)

	try:
		result = subprocess.check_output('git log --abbrev-commit --name-status --all', shell=True).decode()
		newCommit = findNewCommit(result, lastCommit, resource)
		findCommandAndCode(newCommit)
		if len(newCommit) == 0:
			print("Parse Fail!")
			os.chdir(old_path)
			return 0

		else:
			print ("Parse Successful!")
			os.chdir(old_path)
			return newCommit

	except subprocess.CalledProcessError as e:
		print ("Error", e.output)
		os.chdir(old_path)
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

		for line in lines.split(b"\n"):

			words = line.split()

			if len(words) != 0:

				if words[0] == b"+++" or words[0] == b"---":
					extension = (words[1][words[1].rfind(b".") + 1:])
					extension = extension.decode()

				elif chr(words[0][0]) == '+' or chr(words[0][0]) == '-':


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


def showAllRemoteBranch(path):
        os.chdir(path)
	remoteBranch = []

	try:
		result = subprocess.check_output('git branch -r -a', shell=True).decode()
		result.encode()

		for line in result.split("\n"):
			words = line.replace("->", "/").replace(" ", "").split("/")

			if len(words) == 0:
				continue

			if words[0] == "remotes":
				remoteBranch.append(words[2])

	except subprocess.CalledProcessError as e:
		print ("Error //  ", e.output)
		os.chdir(old_path)

	print (remoteBranch)

def countMergedBranch(hackName, teamName):
	changeDir(hackName, teamName)
	mergedBranch = 0
	old_branch = ""

	try:
		old_branch = getCurrentBranch()
		branchs = []
		os.system('git checkout dev')
		result = subprocess.check_output('git log --merges --oneline', shell=True).decode()
		result.encode()

		for line in result.split('\n'):
			words = line.replace('->', '/').split()

			if len(words) == 0:
				continue

			if words[1] == "Merge":
				if words[2] == "branch":
					if words[3] in branchs:
						continue
					else:
						branchs.append(words[3])
						mergedBranch = mergedBranch + 1
				elif words[2] == 'remote-tracking':
					if words[4] in branchs:
						continue
					else:
						branchs.append(words[4])
						mergedBranch = mergedBranch + 1


	except subprocess.CalledProcessError as e:
		print("Error //  ", e.output)
		os.chdir(old_path)

	command = 'git checkout ' + old_branch
	os.system(command)
	return mergedBranch


def changeDir(hackName, teamName):
	old_path = os.getcwd()
	path = "/home/pi/remote/" + hackName + "/" + teamName
	os.chdir(path)


def getCurrentBranch():
	try:
		result = subprocess.check_output('git branch', shell=True).decode()
		result.encode()

		for line in result.split('\n'):
			words = line.split()

			if len(words) == 0:
				continue
			if words[0] == '*':
				return words[1]

	except subprocess.CalledProcessError as e:
		print ("Error //   ", e.output)
	return ""


def countAllRemoteBranch(hackName, teamName):
	rm = showAllRemoteBranch(hackName, teamName)
	return len(rm)

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
		return Falsde

def isPyCommand(words):
	if words[1][0:1] == "#":
		return True

	return False
