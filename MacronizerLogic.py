def macronize(kj):
    scanned = []
    scan = []

    words = kj.split()
    for word in words:
        x = 0
        if 'que' in word:
            x += 1
            word = ''.join(word.split('que'))
        with open('macrons.txt') as macronlist:
            for line in macronlist:
                linesplit = line.split()
                #
                if word == linesplit[0] and word not in scan:
                    scan.append(linesplit[0])
                    scanned.append(linesplit[3])
            if x == 1:
                scanned[-1] += 'que'

    unformatted = ' '.join(scanned)

    formatted = []
    vowels = ['a','e','i','o','u']
    macronletters = ['ā', 'ē', 'ī', 'ō', 'ū']
    for word in unformatted:
        for letter in word:
            formatted.append(letter)
            if formatted[-1] == '^':
                del formatted[-1]
            if formatted[-1] == '_':
                if formatted[-2] in vowels:
                    if formatted[-2] == 'a':
                        del formatted[-1]
                        formatted[-1] = macronletters[0]
                    if formatted[-2] == 'e':
                        del formatted[-1]
                        formatted[-1] = macronletters[1]
                    if formatted[-2] == 'i':
                        del formatted[-1]
                        formatted[-1] =macronletters[2]
                    if formatted[-2] == 'o':
                        del formatted[-1]
                        formatted[-1] = macronletters[3]
                    if formatted[-2] == 'u':
                        del formatted[-1]
                        formatted[-1] =  macronletters[4]

    return ''.join(formatted)
