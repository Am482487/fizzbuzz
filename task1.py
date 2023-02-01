from itertools import islice

def l33t_code(filepath):
    with open(filepath,"r") as writefile:
        filedata = writefile.read()
        filedata = filedata.replace('o', '0')
        filedata = filedata.replace('O', '0')
        filedata = filedata.replace('a', '4')
        filedata = filedata.replace('A', '4')
        filedata = filedata.replace('e', '3')
        filedata = filedata.replace('E', '3')
        filedata = filedata.replace('i', '1')
        filedata = filedata.replace('I', '1')
        
    with open(filepath, 'w') as file:
        file.write(filedata)
    
    with open(filepath,'r') as file: 

        for line in file:
   
        # reading each word        
            for word in line.split():
                if(word.endswith("er")):
                    print(word.replace("er","x0r"))


basepath = "/home/amarnath/fizzbuzz-amarnath/"

filepath = basepath + input("Enter filename: ")

numberofpages = input("Enter number of pages ")

numberoflines = int(numberofpages) * 5

with open("/home/amarnath/fizzbuzz-amarnath/task1book.txt", "r") as myfile:
    linesList = list(islice(myfile,numberoflines))


with open(filepath,"w") as writefile:
    for item in linesList:
        writefile.write(item)

l33t_code(filepath)

