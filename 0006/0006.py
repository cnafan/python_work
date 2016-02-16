#encoding=utf-8

import sys,re

def fin():
    file=open('C:\\Users\\small\\Documents\\GitHub\\python_work\\0005\\text.txt','r+')
    lines=file.readlines()
    file.close()
    return lines
def all(lines):
    dict_1={}
    for line in lines:
        if line!=' \n':
            reg=r'[\s,\.;\']'
            line=line.rstrip('.\n')   
            list_line=re.split(reg,line)
            for i in list_line:
                if i not in dict_1.keys():
                    dict_1[i]=1
                else:
                    dict_1[i]+=1
    print(sorted(dict_1.items(),key=lambda asd:asd[1],reverse=True))
    print("--------------------------")
    

if __name__=='__main__':
    data=fin()
    all(data)
