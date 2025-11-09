# taking total amount of input from user
amount =int(input("please enter the amount of money:"))
#calculating the amount of notes 
Note_1 = (amount//100)
Note_2 = (amount%100)//50
Note_3 = ((amount%100)%50)//20
print ("Notes of 100 ruppess",Note_1)
print ("notes of 50 ruppess",Note_2)
print ("notes of 20 ruppes", Note_3)