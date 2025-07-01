import this
name = "bhupender"
print(name.title()) # method to make string as title

print(name.upper()) # method to make string to upper case
print(name.lower()) # method to make strong to lower case

first_name = 'bhupender'
last_name = 'gurbuxsinghani'

full_name =f"{first_name}, {last_name}" #use of format string
print(full_name) 

print(f"Hey {first_name.title()}, {last_name.title()}! Welcome to Customer Portal")

names ="Shakti\nBhau\nChirag\n" #use of line break, end line character
print(names)
name = "bhupi      "
clean_name = name.strip() # function to remove extra spaces.
print(clean_name)
compare_text='bhupi99' 
inp = input('enter username')
if(compare_text == inp.strip()): #use of strip function
    print('match')
else:
    print('no match!')
    
quote ="\"A person who never made a mistake never tried anything new.\""

quote_by=input('enter famous person name')
quote_by= quote_by.strip()

final_quote =f"{quote_by.title()} once said, {quote}"
print(final_quote)
print(5+3)
print(11-3)
print(2*4)
print(16/2)

fav_num= 8
print(f"my fav number is - {fav_num}")