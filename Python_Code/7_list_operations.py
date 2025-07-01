# chapter 3  -  Lists

#create new list
invitees= ['shakti','bhau','chirag']

for i in invitees:
    print(f"inviting {i} on dinner!")

not_coming='shakti'
newly_coming='anup'

invitees.remove(not_coming) #remove element from the list using element name.
invitees.append(newly_coming) #add an element into the list at the end 

for i in invitees:
    print(f"inviting {i} on dinner!")

print('i found bigger space')

invitees.insert(0,'manu') # adding manu at start
invitees.insert(2,'chetan')# adding chetan at middle
invitees.append('sagar') #adding element at end

for i in invitees:
    print(f"inviting {i} on dinner!")

print('there is change in plan, space available only for 2 people')

while len(invitees)>2: #using len to find out length of the list.
    print(f"Sorry {invitees.pop()}, i had to cancel dinner plan")

for i in invitees:
    print(f"Hey {i}! hoping you will make it to dinner..")

print(invitees)
del(invitees[0]) #fetching element at location in list.
del(invitees[0])
print("the final list is",invitees)