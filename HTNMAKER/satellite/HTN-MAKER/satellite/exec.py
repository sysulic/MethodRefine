import subprocess
import os
import psutil
import time
import signal

current_domain_path = "./current_domain/"
htn_prob_path = "./htn_prob/"
raw_prob_path = "./raw_prob/"
solution_path = "./solution/"
max_mem = 1 * 1024 * 1024 * 1024

fw = open("result", "w")
for i in range(1, 51):
    print ("The " + str(i) + " iteration:\n")
    # training_str = "./htn-maker domain_strips.pddl tasks.pddl " + raw_prob_path + str(i) + ".pddl " + solution_path + str(i) + ".plan " + current_domain_path + "domain_partial_" + str(i - 1) + "_htn.pddl"
    # exec(training_str)
    res = os.popen("./htn-maker domain_strips.pddl tasks.pddl " + raw_prob_path + str(i) + ".pddl " + solution_path + str(i) + ".plan " + current_domain_path + "domain_partial_" + str(i - 1) + "_htn.pddl")
    fr = open(current_domain_path + "domain_partial_" + str(i) + "_htn.pddl", "w")
    content = res.readlines()
    for line in content:
        fr.write(line)
    fr.close()
    solved = 0
    unsolved = 0
    for j in range(51, 101):
        test_str = "./htn-solver2 " + current_domain_path + "domain_partial_" + str(i) + "_htn.pddl " + htn_prob_path + str(j) + ".htn"
        child = subprocess.Popen(test_str, shell=True)
        time.sleep(2)

        success_flag = True
        while (True):
            if (child.poll() is not None):
                break
            pids = psutil.pids()
            for pid in pids:
                pr = psutil.Process(pid)
                if (pr.name().find("htn") != -1):
                    htn_pid = pid
                    break
            p = psutil.Process(htn_pid)
            mem = p.memory_info().rss
            print (str(mem) + "\n")
            if (mem > max_mem):
                child.kill()
                os.kill(htn_pid, signal.SIGKILL)
                success_flag = False
                break
        if (success_flag):
            res = os.popen(test_str).readlines()
            if (len(res) > 1 and res[1].find("found") != -1):
                solved += 1
                print ("testing_" + str(j - 75) + " is solved\n")
            else:
                unsolved += 1
                print ("testing_" + str(j - 75) + " is unsolved\n")
        else:
            unsolved += 1
            print ("testing_" + str(j - 75) + " is unsolved\n")
        
    fw.write(str(i) + "\t" + str(solved) + "\t" + str(unsolved) + "\n")
    fw.flush()
fw.close()

