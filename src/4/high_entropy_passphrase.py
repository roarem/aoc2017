import itertools

def part_1(filename):
    with open(filename,'r') as passphrases:
        valids = 0
        for line in passphrases.readlines():
            passphrase = line.strip().split()
            valid = 1
            for i,word1 in enumerate(passphrase):
                for word2 in passphrase[i+1:]:
                    if word1==word2:
                        valid=0
            valids+=valid
        print(valids)

def part_2(filename):
    with open(filename,'r') as passphrases:
        valids = 0
        invalid = 0
        for j,line in enumerate(passphrases.readlines()):
            passphrase = line.strip().split()
            valid = 1
            for i,word1 in enumerate(passphrase):
                word1_anagrams = ["".join(perm) for perm in itertools.permutations(word1)]
                for word2 in passphrase[i+1:]:
                    for word in word1_anagrams:
                        if word==word2:
                            valid=0
                    
                    #hit = 0
                    #if len(word1)==len(word2):
                    #    for letter_1 in word1:
                    #        for letter_2 in word2:
                    #            if letter_1==letter_2:
                    #                hit += 1

                    #    if hit==len(word1): 
                    #        print('Line: ',j)
                    #        print(word1,word2)
                    #        valid = 0
                    #        break
                    
            if valid:
                valids+=1
        print(valids,j)
#part_1('in_test_1.data')
#part_1('in_1.data')
#part_2('in_test_2.data')
part_2('in_2.data')
