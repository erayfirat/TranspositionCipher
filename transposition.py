import math

def encryption(key,message):
    
    message=message.replace(' ', '-') # remove sapces
    
    keyCharList=[x for x in key] # listeye aktar
    keyLenght=len(key)
    messageLenght=len(message)
    nullCharsCount=messageLenght % keyLenght

# last row add chars
    if nullCharsCount!=0:
        message=message+((keyLenght-nullCharsCount)*"-")
    
    #print(message)
    # get row count
    rowsCount=int(math.ceil(messageLenght/keyLenght))
    rowKey=[]
    # set row key
    for i in range(0, rowsCount):
        rowKey.append(keyCharList[i%keyLenght])
 
    s=0
    m=0
    n=0
    MessageDict = {} 
    totalRowDict= {}
    newList = [] 
    
    # make matrice
    for k in rowKey:
        n += 1  
        t = 0
        rowDict = {}
        for y in message[s : s+keyLenght]:  
            rowDict[keyCharList[t]]=y
            t+=1
            
        totalRowDict[k] = rowDict.copy()  
        
        if len(totalRowDict) == keyLenght or len(rowKey) == n:
            newList.append(totalRowDict)  
            MessageDict[m] = totalRowDict.copy()
            totalRowDict.clear()
            m += 1  
            
        s += keyLenght
        
    # print("MessageDict : ")
    # print(MessageDict) 
    
    #order matrice columns
    for u in MessageDict:
        for v in MessageDict[u]:
            MessageDict[u][v]=sorted(MessageDict[u][v].items(),key= lambda kv : (kv[0],kv[1]))
     
    #get the ciphertext
    cipherText=""
    for i in range(0, keyLenght):
        for g in MessageDict:
            for h in MessageDict[g]:
                cipherText += MessageDict[g][h][i][1]
 
    return cipherText


def decryption(key,cipher):
  
    k=0  
    i=0
    
    cipherLenght = len(cipher)
    cipherCharList = [x for x in cipher] 
  
    # matrice column
    keyLenght = len(key) 
      
    # matrice row
    rowsCount = int(math.ceil(cipherLenght / keyLenght)) 
  
    # sort key
    sortedKeyCharList = sorted([x for x in key]) 
  
    # make empty matrice
    matrix = [] 
    for _ in range(rowsCount): 
        matrix += [[None]*keyLenght] 
  
    
    # fill matrice    
    for _ in range(keyLenght): 
        m = key.index(sortedKeyCharList[k]) 
  
        for j in range(rowsCount): 
            matrix[j][m] = cipherCharList[i] 
            i += 1
        k += 1
        
    # print(matrix)
    
    plainText=""
  
    for s in range(0, rowsCount):
        for t in range(0, keyLenght):         
            plainText +=matrix[s][t] 
  
    return plainText
    


key=input("write key : ")#"albert"#
message=input("write message : ")#"One cant learn anything so well as by experiencing it oneself"#

upperKey=key.upper() #make upper
upperMessage=message.upper() #make upper

cipher=encryption(upperKey, upperMessage)

print("Cipher Text : " + cipher)

plainText=decryption(upperKey, cipher)

print("Plain Text  : "+ plainText)





