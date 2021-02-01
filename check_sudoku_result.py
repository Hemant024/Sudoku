# board string
bd="123456789"
#input rows
row1="295743861"
row2="431865927"
row3="876192543"
row4="387459216"
row5="612387495"
row6="549216738"
row7="763524189"
row8="928671354"
row9="154938672"
# store input into dictionary
d={"key1":row1,"key2":row2,"key3":row3,"key4":row4,"key5":row5,"key6":row6,"key7":row7,"key8":row8,"key9":row9}
# sduk fuction check given string is cointain all 9 numbers
def sduk(bd,string):
    counter2=0
    for i in range(9):
        if bd[i] in string:
            counter2+=1
            continue
        else:
            break
    return counter2==9
#rowcheck function check every row contain 1-9 numbers 
#if all rows are correct it return true else false 
def rowcheck():       
    counter1=0
    # for loop take each row and check via sduk function
    for i in d:     
        strrow=d[i]
        if sduk(bd,strrow):
            counter1+=1
        else:
            break
    return counter1==9
#colcheck function check every column contain 1-9 numbers 
#if all column are correct it return true else false
def colcheck():
    counter3=0

    list1=[row1,row2,row3,row4,row5,row6,row7,row8,row9] 
    #for loop gives col number to nested for loop 
    for g in range(9):
        strcol=""
        #nested for loop create a string of all 'gs'(from 1st for loop) number in rows 
        for i in range(9):
            row=list1[i]
            item=row[g]
            strcol+=item
        #here if check every string via sduk function
        if sduk(bd,strcol):
            counter3+=1
        else:
            break
    return counter3==9
#sqrcheck function check every small squares contain 1-9 numbers 
#if all squares are correct it return true else false
def sqrcheck():
    r,w=0,3
    counter5=0
    # this loop for 3 large columns
    for l in range(3):
        x,y=0,3
        counter4=0
         # this loop for 3 large rows
        for k in range(3):  
            stringsqr=""
            # this loop for 3 small columns 
            for j in range(r,w):    
                list1=[row1,row2,row3,row4,row5,row6,row7,row8,row9]
                # this loop for small row's 3 digits store in stringsqr string
                for i in range (x,y):
                    s=list1[j]
                    d=s[i]
                    stringsqr+=d 
            #check every large square rows if correct contiune loop else break the loop         
            if sduk(bd,stringsqr):
                counter4+=1     
                x,y=y,x
                y=x+3                                    
                continue        
            else:   break           
          
        #if all large square is correct then continue check for nxt large row else break the loop
        if counter4==3:
            counter5+=1
            r,w=w,r
            w=r+3           
            continue
        else:
            break
    # all large square is counter return True else false     
    return counter5==3



if rowcheck() and colcheck() and sqrcheck():   print("sudoku")
else:    print("not sudoku")
    
#also try this as input

# row1='195743862'
# row2='431865927'
# row3='876192543'
# row4='387459216'
# row5='612387495'
# row6='549216738'
# row7='763524189'
# row8='928671354'
# row9='254938671'