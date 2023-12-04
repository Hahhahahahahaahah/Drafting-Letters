name_list = []
with open ("./Contacts/names.txt","r") as names_file:
    for name in names_file:
        name = name.strip()
        name_list.append(name)

with open ("./Email/draft.txt","r") as draft_file:
    draft = draft_file.read()
    
for name in name_list:
    currdraft = draft 
    currdraft = currdraft.replace("[name]",name)
    print(currdraft)
    with open(f"./Send/Letter_for_{name}.txt","w") as letter:
        letter.write(currdraft)
