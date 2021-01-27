
#PART 1

#loading data

data = open('day_2.txt', 'r')

all_passwords = []
for lines in data:
    data_1 = lines.strip().split()
    all_passwords.append(data_1)



#assign min, max, char and passwords to a variable
valid_passwords = 0
valid_passwords_2 = 0
for lines in all_passwords:
    values = lines[0]
    split_val = values.split("-")
    min_val = int(split_val[0])
    max_val = int(split_val[1])
    char = lines[1][0]
    current_password = lines[2]

#counting occurance
    if char in current_password:
        counter = current_password.count(char)

#counting valid passwords
        if min_val <= counter <= max_val:
            valid_passwords += 1


#PART 2
    if (current_password[min_val-1]==char) and not (current_password[max_val-1]==char):
        valid_passwords_2 += 1 
    if (current_password[max_val-1]==char) and not (current_password[min_val-1]==char):
        valid_passwords_2 +=1
print(f'Number of Valid Psswords PART 1= {valid_passwords}')
print(f'Number of Valid Passwords PART 2= {valid_passwords_2}')



