import subprocess
import os
import sys

old_path = ""

def showAllRemoteBranch(hackName, teamName):
	changeDir(hackName, teamName)
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
	
	return remoteBranch

def showMergedBranch(hackName, teamName):
	changeDir(hackName, teamName)
	mergedBranch = []
	old_branch = ""

	try:
		old_branch = getCurrentBranch()
		os.system('git checkout master')
		result = subprocess.check_output('git branch -r --merged', shell=True).decode()
		result.encode()

		for line in result.split('\n'):
			words = line.replace('->', '/').replace(' ','').split('/')

			if len(words) < 2:
				continue

#			if words[1] != "HEAD":
			mergedBranch.append(words[1])

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
