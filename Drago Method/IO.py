'''
Created on 8 Aug 2018

@author: benos
'''


def save(x,y,filename):
    file = open('data/'+filename+'.csv', 'w')
    for i in range(0,len(x)):
        file.write(str(x[i])+';'+str(y[i])+'\n')
    file.close()
    
def readFile(filename):
    file = open('data/'+filename+'.csv','r')
    lines = file.readlines()
    
    size = len(lines)
    x = [0]*size
    y = [0]*size
    
    for i in range(0,size):
        line = lines[i].split(';')
        x[i] = float(line[0])
        y[i] = line[1]
        y[i] = float(y[i][0:-1])
    
    file.close()
    return (x,y)

def saveData(data,filename):
    file = open('data/'+filename+'.txt', 'w')
    for i in range(0,len(data)):
        file.write(str(data[i])+'\n')
    file.close()
    
def readData(filename):
    file = open('data/'+filename+'.txt','r')
    lines = file.readlines()
    size = len(lines)
    y = [0]*size
    
    for i in range(0,size):
        y[i] = float(lines[i][0:-1])
    
    file.close()
    return y