#PART 1

#Loading data and Extracting passports
list_data = []
with open("day_4.txt", "r") as handle:
    joined = "".join(handle)
    current_passports = joined.strip().split("\n\n")

#Converting a list of strings into a list of lists
current_passports_2 = []
for lines in current_passports:
    a = lines.split()
    current_passports_2.append(a)


key_char = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'pid', 'ecl']
counter = 0 
for lines in current_passports_2:
    for field in key_char:
        if field in lines:
            counter += 1
#Making distionaries:

def to_dict(list_passswords):
    dict_passports = {}
    for lines in list_passswords:
        partation = lines.split(':')
        key = partation[0]
        val = partation[1]
        dict_passports[key] = val
    return(dict_passports)
    
passport_dict = [to_dict(items) for items in current_passports_2]

counter = 0 

#checking if the passport is valid

def passport_validation(passport):
    condition_1 = "byr" in passport
    condition_2 = "iyr" in passport
    condition_3 = "eyr" in passport
    condition_4 = "hgt" in passport
    condition_5 = "hcl" in passport
    condition_6 = "ecl" in passport
    condition_7 = "pid" in passport

    return (
        condition_1 and
        condition_2 and
        condition_3 and
        condition_4 and
        condition_5 and
        condition_6 and
        condition_7
    )

#counting valid passports
counter = 0
for passport in passport_dict:
    if passport_validation(passport):
        counter += 1


print(counter)