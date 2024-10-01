import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict()
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here

        # Reading the entire file and converting all letters to uppercase
        fileContent = f.read().upper()
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Initializing count of each letter in the alphabet to 0
        for letter in alphabet:
            X[letter] = 0

        # Incrementing the count for each letter found in the file
        for letter in fileContent:
            if letter in X:
                X[letter] += 1

    # Returning the dictionary with the counts of each letter
    return X



# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!

# Get the filename and the prior probabilities
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 hw2.py [letter file] [english prior] [spanish prior]")
        sys.exit(1)
    # Storing the filename and the prior probabilities for English and Spanish
    filename = sys.argv[1]
    english_prior = float(sys.argv[2])
    spanish_prior = float(sys.argv[3])

#Q1: Display the counts of each letter in the shredded document
print("Q1")
file = shred(filename)
for letter in file:
    print(letter, file[letter])

#Q2: Compute X1 log e1 and X1 log s1 (where X1 is the count of 'A')
print("Q2")
freq = file['A']
english = freq * math.log(get_parameter_vectors()[0][0])
spanish = freq * math.log(get_parameter_vectors()[1][0])
print("%.4f" %english)
print("%.4f" %spanish)

#Q3: Compute F(English) and F(Spanish), the log probabilities
print("Q3")
sigma_english = 0.0
sigma_spanish = 0.0

# Summing over all letters A-Z (26 letters in total)
for i in range(0, 26):
    value = list(file.values())[i]
    sigma_english += value * math.log(get_parameter_vectors()[0][i])
    sigma_spanish += value * math.log(get_parameter_vectors()[1][i])

# Calculating the log probabilities for English and Spanish
freq_english = math.log(english_prior) + sigma_english
freq_spanish = math.log(spanish_prior) + sigma_spanish

# Printing the results of Q3
print("%.4f" %freq_english)
print("%.4f" %freq_spanish)

#Q4: Compute the posterior probability P(Y=English|X) using Bayes' rule
print("Q4")
bayes_english = 0.0

# Handling underflow/overflow by checking large differences between F(Spanish) and F(English)
if (freq_spanish - freq_english) >= 100:
    bayes_english = 0
elif (freq_spanish - freq_english) <= -100:
    bayes_english = 1
else:
    # Calculating the posterior probability using the logistic function
    bayes_english = 1/(1 + math.exp(freq_spanish - freq_english))

print("%.4f" %bayes_english)
