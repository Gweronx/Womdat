def parse(file):
    f=open(file)
    keys={}
    ln=1
    for line in f:
        line=line.replace("\n","")
        if line.startswith("="):pass
        elif line.startswith("[") and line.endswith("]"):
            tokens=line.replace("[","").replace("]","").split()
            keys.update({tokens[0]:tokens[1].replace(";"," ")})
        elif line.startswith("<") and line.endswith(">"):
            tokens=line.replace("<","").replace(">","").split()
            keys.update({tokens[0]:int(tokens[1])})
        elif line=="":pass
        else:
            print(f"Error on line {str(ln)}\n  {line}\nWhat is that?")
            quit()
        ln+=1
    return keys
