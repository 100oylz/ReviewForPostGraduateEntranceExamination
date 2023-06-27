import os 
import re
if not (os.path.exists("previewinit.txt")):
    print("previewinit.txt Not Found!")
    exit(-1)
    
if not (os.path.exists("chapter")):
    os.mkdir("chapter")
matchpattern=r"#"
with open("previewinit.txt",encoding="utf8") as f:
    chapter=''
    section=[]
    while(True):
        line=f.readline()
        if not line:
            if not (os.path.exists(f"chapter/{chapter}")):
                os.mkdir(f"chapter/{chapter}")
            with open(f'chapter/{chapter}.tex','w',encoding="utf8") as fp:
                fp.write(f'\\chapter{{{chapter}}}\n')
                for sec in section:
                    fp.write(f'\\section{{{sec}}}\n')
                    fp.write(f"\\input{{chapter/{chapter}/{sec}.tex}}\n")
                    open(f"chapter/{chapter}/{sec}.tex","w")
            with open("chapterlist.txt", "a+", encoding="utf8") as fp:
                fp.write(f"\\input{{chapter/{chapter}.tex}}\n")
            section.clear()
            break
        if not (re.match(matchpattern,line)):
            if len(chapter)!=0:
                if not (os.path.exists(f"chapter/{chapter}")):
                    os.mkdir(f"chapter/{chapter}")
                with open(f'chapter/{chapter}.tex','w',encoding="utf8") as fp:
                    fp.write(f'\\chapter{{{chapter}}}\n')
                    for sec in section:
                        fp.write(f'\\section{{{sec}}}\n')
                        fp.write(f"\\input{{chapter/{chapter}/{sec}.tex}}\n")
                        open(f"chapter/{chapter}/{sec}.tex","w")
                with open("chapterlist.txt","a+",encoding="utf8") as fp:
                    fp.write(f"\\input{{chapter/{chapter}.tex}}\n")
                section.clear()
            chapter=line.replace("\n","")
        else:
            section.append(line.replace("#","").replace("\n",""))
