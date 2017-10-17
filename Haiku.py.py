## Felicia Villalobos
## CSC 250 HW 6
## Random Haiku generator
import random 
from random import randint


def listPicker(Lists):
    
    random_list = random.choice(Lists)
    return random_list
    

def randomPicker(random_list):
    
    wordIndex = randint(0,len(random_list)-1)    
    return random_list[wordIndex]

def firstLine(haiku,counter,random_list,Lists):
   
    if counter == 1:
        #print('firstline 1')
        z = Lists[2]
        word = random.choice(z)
        #haiku = haiku + ' '+str(word)

        a = Lists[0]
        word2 = random.choice(a)
        haiku = haiku + ' ' +str(word) + ' ' +str(word2)
        print(haiku)
        
        
    if counter ==  2:
        #print('firstline 2')
        z = Lists[2]
        word = random.choice(z)
        haiku = haiku +' '+ str(word)
        print(haiku)
        
        
    if counter == 3:
        #print('first line 3')
        z = Lists[1]
        word = random.choice(z)
        haiku = haiku +' '+ str(word)
        print(haiku)
        
        
    if counter == 4:
        #print('first line 4')
        z = Lists[0]
        word = random.choice(z)
        haiku = haiku +' '+ str(word)
        print(haiku)
       
        
    if counter == 5:
        ##done, next one
        print('done')
        

##def secondLine(haiku,counter,random_list,Lists):
##    print('inside second line')
##    #looking for 3 syllables
##
##    if counter == 1:
##        print('made it to checking cnd')
##        f = Lists[1]
##        word2 = random.choice(f)
##        haiku2 =  str(word2)
##        print('line2=',haiku2)
##        finalH = haiku + '\n' + haiku2
##        print(finalH)
##
##    if counter == 2:
##        f = Lists[0]
##        word2 = random.choice(f)
##        haiku2 = str(word2)
##        print('line2=',haiku2)
##        finalH = haiku + '\n' + haiku2
##        print(finalH)
##    
##        
##        
##    if counter == 3:
##        print('calling first line')
##        finalH = haiku + '\n' + haiku2
##        print(finalH)
    
def haikuCounter(random_list,counter,Lists):
    
    if random_list == Lists[0]:
        
        counter = counter + 1
        
    elif random_list == Lists[1]:
        counter = counter + 2
        

    elif random_list == Lists[2]:
        counter = counter + 3
        
        
    return counter
    
        
   
def haikuCheck(random_list, haiku,counter,Lists):
    if counter == 1:
        cnt = haikuCounter(random_list,counter,Lists)
        firstLine(haiku,counter,random_list,Lists)
            
    elif counter == 2:
        cnt = haikuCounter(random_list,counter,Lists)
        firstLine(haiku,counter,random_list,Lists)
        
    elif counter == 3:
        cnt = haikuCounter(random_list,counter,Lists)
        firstLine(haiku,counter,random_list,Lists)
        
    elif counter == 4:
        cnt = haikuCounter(random_list,counter,Lists)
        firstLine(haiku,counter,random_list,Lists)
        
    else:
        print('counter was 5')
        print('done/next')
        
        
        
def main():
    #take in filename
    filename = input('Filename:')

    #read file
    file = open(filename,'r')
    
    counter = 0
    #read each line and store it in x (list var)
    x = eval(file.readline()) # 1 syllable
    y = eval(file.readline()) # 2 syllable 
    z = eval(file.readline()) # 3 syllable

    print('W1(1 syll,x)=',x)
    print('W2(2 syll,y)=',y)
    print('W3(3 syll,z)=',z)
    Lists = [x,y,z]
    h = listPicker(Lists)
    haiku = randomPicker(h)
    
    
    ##count what is in the haiku
    c  = haikuCounter(h,counter,Lists)
    
    ## check what to do next 
    haikuCheck(h,haiku,c,Lists)

    second = Lists[2]
    haiku2 = random.choice(second)
    finalHaik = haiku2
    print(finalHaik)

    last = Lists[2]
    haiku3 = random.choice(last)

    last2 = Lists[1]
    haiku4 = random.choice(last2)

    print(haiku3, haiku4)

    
    
main()

    
    





