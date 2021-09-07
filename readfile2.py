import glob
import json


header = ['id', 'input', 'output']
f = open('dataforslot.jsonl', 'w',newline='', encoding='utf-8')




# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob("dstc2_traindev/" + '**/log.json', recursive=True):
    with open(filename,"r") as logFile:
        print(filename)
        jsonContent = json.load(logFile)
        id = jsonContent["session-id"]
        input = ""
        output = ""
        sentenses = []
        for turn in jsonContent["turns"]:
            if turn.get("output"):
                sentenses.append(turn["output"]["transcript"])
            if turn.get("input"):
                sentenses.append(turn["input"]["batch"]["asr-hyps"][0]["asr-hyp"])
        lineContent = {"id":id,"sentences":sentenses}
        f.write(json.dumps(lineContent, ensure_ascii=False)+'\n')

        
f.close()