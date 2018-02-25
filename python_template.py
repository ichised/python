import MeCab
import sys
import os

tagger = MeCab.Tagger('-F\s%f[6] -U\s%m -E\\n')

word_dict = {}
word2_dict = {}

#file open(use with contents)
with open("pn.csv.m3.120408.trim", "r") as f:
    for l in f.readlines():  
        #string split
        l = l.split("\t")
        if l[1] == "p":
            value = 1
        elif l[1] == "e":
            value = 0
        elif l[1] == "n":
            value = -1
        else:
            value = 0
        word_dict.update({l[0]:value})

#open readlines
for line in open(text,"r").readlines():
    #delete \n
    line = line[:-1]

#print number    
print(text + ":{0}".format(num/count))
count = 0
num = 0

#get current dir
sample = os.getcwd()
#get listdir
sampledir = os.listdir(sample)


#use list
listsample = [1,2,3]
#add last [1,2,3,4]
listsample.append(4)

#add anathor list
listsample2 = [100,200,300]
listsample.extend(listsample2)
#listsample = [1,2,3,4,100,200,300]
listsample = listsample + listsample2

#use dictionary
#{key1:value1, key2:value2, ...}
dictsample = {"ramen":750, "kare-":400}
print(dictsample["ramen"] #750

#change value
dictsample["ramen"] = 1000
print(dictsample["ramen"] #1000
print(len(dictsample)) #2

#add new key:value
dictsample["karaage"] = 400

#convine
dictsample.update({"yakiniku":500,"hurikake",30})

#confirm key
print("yakiniku" in dictsample)
print(dictsample.has_key("kabotya"))


#use 
