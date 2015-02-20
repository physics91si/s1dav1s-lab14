#!/usr/bin/python2.7

# Init script from Lab #5

import sys
import os
import subprocess as sp
import re

def shell(cmd):
	return sp.check_output(cmd, shell=True)

user = shell('whoami').strip()
SUBMISSIONS = "/afs/ir.stanford.edu/class/physics91si/submissions/"
lab14dir = os.path.join(SUBMISSIONS, user, 'lab14')
lab15dir = shell('pwd').strip()
os.chdir(lab14dir)
shell("hg update tip")
targets = shell("ls").split('\n')[:-1]

for target in targets:
	# Find language.py and check commit status
	try:
		os.chdir(lab14dir)

	# hg update to show files, if necessary
		if not target in os.listdir('.'):
			ans = raw_input("%s not found in %s. Try hg update? \nWarning: this will overwrite current directory contents. [y/n] " % (target, lab14dir))
			if 'y' in ans:
				shell("hg update tip")
		if not target in os.listdir('.'):
	       		raise IOError
	except:
		print "Error: unable to find %s" % os.path.join(lab4dir, target)
		continue

	os.chdir(lab15dir)

# Copy over and commit
	try:
		files = os.listdir('.')
		if target in files:
			ans = raw_input("%s exists. Overwrite? [y/n] " % target)
			if 'n' in ans: continue
		shell("cp %s ." % os.path.join(lab14dir, target))
		shell("hg add %s" % target)
		print "%s copied from %s and added to repo" % (target, lab14dir)
	except:
		print "Error: unable to copy %s" % target
		continue

	try:
		ans = raw_input("Commit to current repo? [y/n] ")
		if 'y' in ans:
			shell("hg commit -m \"auto-commit of %s\" %s" % (target, target))
	except:
		print "Error: unable to commit %s" % target
		continue
