import sys,re

def tongji():
    file=open('C:\\Users\\small\\Documents\\GitHub\\python_work\\0004\\text.txt','r+')
    lines=file.readlines()
    file.close()
    lens=0
    
    for line in lines:
        if line!=' \n':
            reg=r'[\s,\.;\']'
            line=line.rstrip('.\n')    
            print(line)
            list_str=re.split(reg,line)
            lens+=len(list_str)
            print(len(list_str))

    return lens
  

if __name__=='__main__':
    x=tongji()
    print('all='+str(x))
    
