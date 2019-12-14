a = open('TestAOPS.txt', 'r')
PLZ = {}
for c in a:
    b=c.split()
    if b[0] in PLZ:
        print("HI")
        PLZ[b[0]] = PLZ[b[0]] + [int(b[1])]
    else:
        print("HELLO")
        PLZ[b[0]] = [int(b[1])]
name = input("Enter name: ")
while name in PLZ:
    avg = sum(PLZ[name])/len(PLZ[name])
    print("The average for "+str(name)+" is "+str(avg))
    name = input("Click Enter to Exit) Enter another name: ")
print ("Goodbye!")
exit()
        
    

        
