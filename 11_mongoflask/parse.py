file=open("anime-offline-database.json","r")
f=open("anime.json","w")
doc=file.read()
doc=doc.split("},")
for x in doc:
    x=x+"}"
    x=x.split("\n")
    s=""
    s=s.join(x)
    s=s.strip(" ")
    s=s.strip("{")
    s=s.strip("}")
    s=s.strip(" ")
    s="{"+s+"}"
    s+="\n"
    f.write(s)
f.close()
