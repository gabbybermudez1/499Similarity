# Represents the ACTTGGACTT pattern
pattern = "ACTTGGACTTTTTCAACTGACTGATCGATGCTACGATGCTAGCTACACTATCGATCGATCGATCGCGCCCTAGCTAGGCTAGCTATATTCGTATCGGCTACGATGCTGACTGCTAGCTACGATCTAGCTGACTAGCGATCGATGCATGCTGAGCTATGCTACGTATGCATGACGTCTCAGTACGTCATCGTGACTGCTGCATGCTAGCTGCTACGACTTGGACTTTTTCAACTGACTGATCGATGCTACGATGCTAGCTACACTATCGATCGATCGATCGCGCCCTAGCTAGGCTAGCTATATTCGTATCGGCTACGATGCTGACTGCTAGCTACGATCTAGCTGACTAGCGATCGATGCATGCTGAGCTATGCTACGTATGCATGACGTCTCAGTACGTCATCGTGACTGCTGCATGCTAGCTGCTACGACTTGGACTTTTTCAACTGACTGATCGATGCTACGATGCTAGCTACACTATCGATCGATCGATCGCGCCCTAGCTAGGCTAGCTATATTCGTATCGGCTACGATGCTGACTGCTAGCTACGATCTAGCTGACTAGCGATCGATGCATGCTGAGCTATGCTACGTATGCATGACGTCTCAGTACGTCATCGTGACTGCTGCATGCTAGCTGCTACGACTTGGACTTTTTCAACTGACTGATCGATGCTACGATGCTAGCTACACTATCGATCGATCGATCGCGCCCTAGCTAGGCTAGCTATATTCGTATCGGCTACGATGCTGACTGCTAGCTACGATCTAGCTGACTAGCGATCGATGCATGCTGAGCTATGCTACGTATGCATGACGTCTCAGTACGTCATCGTGACTGCTGCATGCTAGCTGCTACGACTTGGACTTTTTCAACTGACTGATCGATGCTACGATGCTAGCTACACTATCGATCGATCGATCGCGCCCTAGCTAGGCTAGCTATATTCGTATCGGCTACGATGCTGACTGCTAGCTACGATCTAGCTGACTAGCGATCGATGCATGCTGAGCTATGCTACGTATGCATGACGTCTCAGTACGTCATCGTGACTGCTGCATGCTAGCTGCTACGACTTGGACTTTTTCAACTGACTGATCGATGCTACGATGCTAGCTACACTATCGATCGATCGATCGCGCCCTAGCTAGGCTAGCTATATTCGTATCGGCTACGATGCTGACTGCTAGCTACGATCTAGCTGACTAGCGATCGATGCATGCTGAGCTATGCTACGTATGCATGACGTCTCAGTACGTCATCGTGACTGCTGCATGCTAGCTGCTACG"
first_4 = pattern[0:4]
small_pattern = "ACTTGGACTT"



def convert(char):
    if char == 'A':
        return 1
    elif char == 'C':
        return 2
    elif char == 'G':
        return 3
    elif char == 'T':
        return 4

# convert some string into a hash function
def convert2(char):
    return(ord(char))

# This works!
# a quick way to compute polynomial coefficient
def horners_rule(some_str):
    length = len(some_str)
    result = convert(some_str[0])
    for i in range(1, length):
        result = (result * 10) + (convert(some_str[i]))
    return result

def rolling_hash(search_string, desired_length):
    E = 10 **(desired_length - 1)
    next_str = search_string[0:desired_length]
    next_hash = horners_rule(next_str)
    print(next_str)
    print(next_hash)
    
    for i in range(0, len(search_string) - desired_length):
        print("-------------------------------")
        current_str = next_str
        print("current_str: ", current_str)
        current_hash = next_hash
        print("current_hash: ", current_hash)

        # get the new stuff
        next_str = search_string[i + 1: desired_length + i + 1]
        print("next_str: ", next_str)
        next_hash = ((current_hash - (convert(current_str[0]) * E)) * 10) + convert(next_str[desired_length - 1])
        print("next_hash: ", next_hash)
        print("------------------------------")

def rolling_hash_mod(search_string, desired_length):
    for i in range(len(search_string) - desired_length + 1):
        current_str = search_string[i:(desired_length + i)]
        print(current_str)
        print(horners_rule(current_str))
        print("")
    


def main():
    rolling_hash(small_pattern, 4)
    rolling_hash_mod(small_pattern, 4)

main()