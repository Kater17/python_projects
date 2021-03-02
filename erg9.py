#Άσκηση 9
import math
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
        file=file.replace("~","")
        file=file.replace(" ","")
        for i in file:
          p=ord(i) #μετατροπή σε αριθμό ascii
          if p%2==0: #αν είναι ζυγός αριθμός
            file=file.replace(i,"") #αφαιρώ τους ζυγούς αριθμούς
        mikos=len(file) #αριθμός χαρακτήρων
        for i in file:
          foresA=file.count(i) #πόσες φορές υπάρχει το i
          foresB=foresA/mikos*100 #ποσοστό 
          foresC=math.ceil(foresB) #στρογγυλοποιημένο προς τα πάνω
          if foresA>1:
            file=file.replace(i,"")
            print(i,":",foresC*"*")
          elif foresA==1:
            print(i,":",foresC*"*")
        fileOpen.close()