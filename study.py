# studyset.txt
    # file in this folder
    # PROMPT \t ANSWER \n\n (including after last) - eg export quizlet, + \n\n at the end
# python3 study.py
    # for all the prompt/answer combos:
        # prompt will be shown, you should type the answer, and if your answer did not match you can override and say you were correct
        # after all - restart with the prompt/answer combos you got wrong (not overridden)
# studyresults.txt
    # output file created in this folder
    # NUMBER OF ROUNDS IT TOOK TO GET RIGHT --- PROMPT \t ANSWER \n\n (including after last)


studysetfile = open("studyset.txt")
studyset = {}
studyresults = {}
promptanswerpair = ""
for line in studysetfile:
    if (line == "\n"):
        prompt, answer = promptanswerpair.strip().split("\t")
        studyset[prompt] = answer
        studyresults[prompt] = -1
        promptanswerpair = ""
    else:
        promptanswerpair += line
studysetfile.close()

import random
roundprompts = list(studyset.keys())
random.shuffle(roundprompts)
while (len(roundprompts) > 0):
    roundn = len(roundprompts)
    roundi = 1
    nextroundprompts = []
    print("-------------------------------------------------------")
    print("NEW ROUND ---------------------------------------------")
    print("-------------------------------------------------------")
    for prompt in roundprompts: #doesn't handle break line answers
        print(roundi,"/",roundn," ---------------------------------------------")
        useranswer = input(prompt + "\nYour answer -------> ")
        if (useranswer != studyset[prompt]):
            print("INCORRECT, expected:", studyset[prompt])
            if (input("override? [y for I was right] --> ") != "y"):
                nextroundprompts.append(prompt)
                studyresults[prompt] = roundi
        else:
            studyresults[prompt] = roundi
        roundi+=1
    roundprompts = nextroundprompts
    random.shuffle(roundprompts)




studyresultsfile = open("studyresults.txt", "w")
for prompt in studyresults.keys():
    studyresultsfile.write(studyresults[prompt] + "---" + prompt + "\t" + studyset[prompt] + "\n\n")
studyresultsfile.close()
