def checkMembership(ismember, age, isresident):
    if (age <= 12 or age >= 65 or ismember == True or isresident == True):
        print ("Discount granted!")
    else:
        print ("No discount for you brokie")
    


checkMembership(False, 35, False)




