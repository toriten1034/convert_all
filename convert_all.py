#!/usr/bin/env python3
import os 
import subprocess

f_io = None
dict = {"null":"hoge"}

try:
    f_io =  open("files.log", 'r+')
    lines = f_io.readlines();
    #print(lines)
    for line in lines:
        key, data = line.split(",")
        dict[key] = data.replace('\n','')
    f_io.close()
except:
    print("creat New file")


f_io = open("files.log","w")

files = os.listdir("figs_raw/")


for file in files:
    name, ext = os.path.splitext(file)
    cmd = "md5sum figs_raw/"+file
    tmp =  subprocess.check_output( cmd , shell=True)
    hash_v,dummy = str(tmp).split("  ")

    if(file in dict):
        #print(dict[file],"!=", hash_v)
        if(dict[file] != hash_v):
            print("reconvert:"+file)
            cmd = "convert figs_raw/"+file+" -resize 480x320 "+"figs/"+name+".pdf"
            print(cmd)
            subprocess.call( cmd, shell=True  )
            dict[file] = hash_v
    else:
        print("add:"+file)
        dict[file] = hash_v
        cmd = "convert figs_raw/"+file+" -resize 480x320 "+"figs/"+name+".pdf"
        print(cmd)
        subprocess.call( cmd , shell=True  )   


for k, v in dict.items():   # for/if文では文末のコロン「:」を忘れないように    
    f_io.write(str(k)+","+str(v)+"\n");
f_io.close()
