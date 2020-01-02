import os

def trim_the_type(str):
    items = str.split(" - ")
    res = items[0]
    for i in range(1, len(items)):
        res = res + " " + items[i].split(" ")[1]
    return res
    
prob_path = "./htn_prob/"
solution_path = "./solution/"
htn_domain_path = "./"
head_str = "( defplan Blocks4 Prob"
problems = os.listdir(prob_path)
problems.sort()
for problem in problems:
    name = problem.split(".")[0]
    res = os.popen("./htn-solver2 " + htn_domain_path + "domain_htn.pddl " + prob_path + problem)
    lines = res.readlines()
    if (lines[1].find("found") == -1):
        print("can not solve " + problem + " !\n")
        break
    fw = open(solution_path + name + ".plan", "w")
    fw.write(head_str + name + "\n")
    for i in range(2, len(lines)):
        fw.write(trim_the_type(lines[i]))
    fw.write(")")
    fw.close()