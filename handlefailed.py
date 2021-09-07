import csv
import json 
f = open("C:/Users/x1des\Desktop/NUIG/google/failedcall_removed.csv",encoding="utf-8")
resultfile = open("failedcall.jsonl","w",encoding="utf-8")
reader = csv.reader(f)
for row in reader:
    id = row[0]
    sentenses=[]
    output_sentenses = row[2].split("|")
    input_sentenses = row[1].split("|")
    print(id)
    print(output_sentenses)
    print(input_sentenses)
    for output_sentense in output_sentenses:
        sentenses.append(output_sentense)
        if(len(input_sentenses)>0):
            sentenses.append(input_sentenses.pop(0))
    lineContent = {"id":id,"sentences":sentenses}
    resultfile.write(json.dumps(lineContent, ensure_ascii=False)+'\n')