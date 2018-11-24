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
