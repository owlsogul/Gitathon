import subprocess
import os
import sys

old_path = ""

def showDiffCommit(hackName, teamName, commitId):

	changeDir(hackName, teamName)

	try:
		result = subprocess.check_output('git show' + commitId, shell=True).decode()
		result.encode()


	except subprocess.CalledProcessError as e:
		print ("Error //  ", e.output)
		os.chdir(old_path)

	return result
