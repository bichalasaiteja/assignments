#creating the files using file handling

#f=open("file1.txt","w")
#g=open("file2.txt","w")
#h=open("file3.txt","w")
#i=open("file4.txt","w")



#from zipfile import *

#f=ZipFile("files.zip","w")
#f.write("file1.txt")
#f.write("file2.txt")
#f.write("file3.txt")
#f.write("file4.txt")
#f.close()
#print("zip file created")



#from zipfile import *

#f=ZipFile("abcd.zip","w")
#f.write("file1.txt")
#f.write("file2.txt")
#f.write("file3.txt")
#f.write("file4.txt")
#f.write("emp.csv")
#f.close()
#print("zip file created")



from zipfile import *

f=ZipFile("abcd.zip","r")
names=f.namelist()
for i in names:
    print("filename is ",i)
    f1=open(i,"r")
    print(f1.read())
    print()

