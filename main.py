def parse(file):
    f=open(file)
    keys={}
    sect=""
    for line in f:
        line=line.replace("\n","")
        if line.startswith("="):pass
        elif line.startswith("[") and line.endswith("]"):
            tokens=line.replace("[","").replace("]","").split()
            keys.update({f"{sect}{tokens[0]}":tokens[1].replace(";"," ")})
        elif line.startswith("<") and line.endswith(">"):
            sect=line.replace("<","").replace(">","")+"."
        elif line=="":pass
    return keys
