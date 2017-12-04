def validity_1(passphrase):
    for i,word1 in enumerate(passphrase):
        for word2 in passphrase[i+1:]:
            if word1==word2:
                return 0
    return 1

def validity_2(passphrase):
    for i,word1 in enumerate(passphrase):
        for word2 in passphrase[i+1:]:
            if ''.join(sorted(word1))==''.join(sorted(word2)):
                return 0
    return 1

def entropy_passphrase(filename,validity):
    with open(filename,'r') as passphrases:
        valids = 0
        for passphrase in passphrases.readlines():
            passphrase = passphrase.strip().split()
            valids += validity(passphrase)
        print(valids)

entropy_passphrase('in_test_1.data',validity_1)
entropy_passphrase('in_1.data',validity_1)
entropy_passphrase('in_test_2.data',validity_2)
entropy_passphrase('in_2.data',validity_2)
