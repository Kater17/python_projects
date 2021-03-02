#Άσκηση 13
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
        file=file.replace("`","")
        file=file.replace("”","")
        file=file.replace("~","")
        file=file.replace("“","")
        file = file.split(" ")        
        zeugi=0
        for i in file:                                       
            for j in file:                                   
                if i!=j:  #όχι ζεύγος με τον ίδιο του εαυτό
                    if len(i)+len(j)==20:
                        zeugi+=1                    
                        print(zeugi,":",i,"&",j)                 
                        file.remove(i)                      
                        file.remove(j)                    
                        break
        fileOpen.close() 