import os
files = os.listdir("./")
for i in range(1, 51):
	fr = open("domain_partial_" + str(i) + "_htn.pddl", "r")
	lines = fr.readlines()
	count = 0
	for line in lines:
		if (line.find("method") != -1):
			count += 1
	print (str(i) + "\t" + str(count))