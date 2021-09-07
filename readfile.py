import glob
import json
import csv


header = ['id', 'input', 'output']
f = open('data.csv', 'w',newline='', encoding='utf-8')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(header)


# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob("dstc2_traindev/" + '**/log.json', recursive=True):
    with open(filename,"r") as logFile:
        print(filename)
        jsonContent = json.load(logFile)
        id = jsonContent["session-id"]
        input = ""
        output = ""
        for turn in jsonContent["turns"]:
            if turn.get("output"):
                output = output + turn["output"]["transcript"] + "|"
            if turn.get("input"):
                input = input + turn["input"]["batch"]["asr-hyps"][0]["asr-hyp"] +"|"
        writer.writerow([id,input,output])

        
f.close()