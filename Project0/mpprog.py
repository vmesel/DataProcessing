from system import stdin

stdin.decode("win1252")

for line in stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower().replace("!"," !")
        word = word.replace("?"," ? ").replace(","," , ")
        word = word.replace(";"," ; ").replace("..."," ... ")
        word = word.replace(":"," : ").replace("("," ( ")
        word = word.replace(")"," ) ").replace("."," . ").replace("\""," \" ")

        word = word.split()
        if len(word) > 1:
        	for x in word:
        		print (("%s\t\t%s") % (x, 1))	
        else:
        	print (("%s\t\t%s") % (word[0], 1))
