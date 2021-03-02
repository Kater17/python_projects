#Άσκηση 4
import random
try:
    myfile=input("Δώστε το όνομα του αρχείου ASCII σας:")
finally:
    while myfile[-3:]!= "txt":
        print("ΤΟ ΠΡΟΓΡΑΜΜΑ ΔΟΥΛΕΥΕΙ ΜΟΝΟ ΓΙΑ TXT ΑΡΧΕΙΑ")
        myfile=input("Δώστε το όνομα του αρχείου ASCII σας:")
    else:
        fileOpen=open("./"+myfile,"r+",encoding="utf-8") #διάβασμα και εγγραφή αρχείου
        file=fileOpen.read()
        file=str(file) #μετατρέπω σε str τα πάντα
        file=file.replace(".","") #αφαιρώ ότι άχρηστο/μη ascii χαρακτήρα 
        file=file.replace("\n","")
        file=file.replace("?","")
        file=file.replace("!","")
        file=file.replace("/","")
        file=file.replace("/","")
        file=file.replace("-","")
        file=file.replace("_","")
        file=file.replace("=","")
        file=file.replace("(","")
        file=file.replace(")","")
        file=file.replace('"',"")
        file=file.replace(">","")
        file=file.replace("<","")
        file=file.replace("#","")
        file=file.replace("+","")
        file=file.replace("*","")
        file=file.replace(";","")
        file=file.replace(",","")
        file=file.replace("^","")
        file=file.replace("&","")
        file=file.replace("{","")
        file=file.replace("}","")
        file=file.replace("[","")
        file=file.replace("]","")
        file=file.replace("%","")
        file=file.replace("$","")
        file=file.replace("@","")
        file=file.replace(":","")
        file=file.replace("'","")
        file=file.replace("’","")
        file=file.replace("”","")
        file=file.replace("`","")
        file=file.replace("“","")
        file=file.replace("~","")
        file = file.split(" ") 
        file=list(file)
        mikos=len(file)
        i=0
        listall=[]
        u=mikos
        while True:
          if u-2>=3:
            listall.append([file[i],file[i+1],file[i+2]])
            i=i+1
            u += -i
          else:
            break
        
        finaltext=""
        words=0
        triada=random.choice(listall)
        exeitriada=True
        while words<=200 and exeitriada:
          finaltext = finaltext + " " + triada[1] + " " + triada[2]
          for i in range(len(listall)):
            if triada[1]==listall[i][0] and triada[2]==listall[i][1]:
              triada=listall[i]
              words+=2
              break
            elif i == len(listall) - 1:
                exeitriada=False
              
        print(finaltext)