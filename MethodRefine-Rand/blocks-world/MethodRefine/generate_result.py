import os
a = "./"
dirs = os.listdir(a)
fw = open(a + "all_result", "w")
for dir in dirs:
    if (dir.find("benchmark") == -1):
        continue
    fw.write(dir + "\niteration\tmethods\tsolved\n")
    fr = open(a + dir + "/result", "r")
    lines = fr.readlines()
    i = 0
    while(i < len(lines)):
        if (lines[i].find("training") != -1 and i + 4 < len(lines)):
            fw.write(lines[i].split("_")[1].split(".")[0] + "\t")
            fw.write(lines[i + 3].split(" ")[0] + "\t")
            fw.write(lines[i + 4].split(" ")[0] + "\n")
            i = i + 4
        else:
            i = i + 1
    fw.write("\n")
fw.close()
    