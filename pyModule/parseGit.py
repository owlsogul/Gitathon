import subprocess
import os
import sys

def parseGit(hackName, teamName, lastCommit, resource):
	#path = "/home/pi/remote/" + hackName + "/" + teamName
	path = "C:\Users\owlsogul\Documents\GitHub\AI_Project1"
	os.chdir(path)

	try:
		result = subprocess.check_output('git log --abbrev-commit --name-status --all', shell=True)
		newCommit = findNewCommit(result, lastCommit, resource)
		findCommandAndCode(newCommit)
		if len(newCommit) == 0:
			print("Parse Fail!")
			return 0

		else:
			print ("Parse Successful!")
			return newCommit

	except subprocess.CalledProcessError, e:
		print ("Error", e.output)
		return 0




def findNewCommit(output, lastCommit, extens):
	newCommit = []
	oneDic = {}
	isNotFirst = False
	totalRes = 0

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

		for line in lines.split("\n"):
			words = line.split()

			if len(words) != 0:

				if words[0] == "+++" or words[0] == "---":
					extension = words[1][words[1].rfind(".") + 1:]

				elif words[0][0] == "+" or words[0][0] == "-":

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
