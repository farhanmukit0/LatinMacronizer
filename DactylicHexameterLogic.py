def syllabilize(x):
    vowels = 'aeiou'
    dipthongs = ['ae', 'ui', 'ei', 'eu', 'oe', 'au']
    symbols = ['+', '-']
    scan = []
    regscan = []
    regscannew = []
    joinedletters = []
    elisioncount = 0
    spacecount = 0
    consonant = 'bcdfghjklmnpqrstvwxyz '
    yasscheck = []

    for word in x.lower():
        for letter in word:
            scan.append(letter)
            regscan.append(letter)
            if len(scan)>3:
                if scan[-1] in vowels and scan[-2] == ' ' and scan[-3] in vowels:  # elision
                    del scan[-3]

                    regscan[-3] = regscan[-3] + '(x)'
                    elisioncount += 1
                joined = ''.join(scan[-2]+scan[-1])
                joinedletters.append(joined)
                if scan[-1] in consonant and scan[-2] in consonant and scan[-3] in vowels: #double consonant check
                    regscan[-3] = regscan[-3] + '-'
                if scan[-3] in vowels and scan[-2] in consonant and scan[-1] in vowels:
                    regscan[-3] = regscan[-3] + '+'
                if joined in dipthongs:
                    regscan.append('-')
                if len(scan) == len(x) - elisioncount - spacecount:
                    print('working')
                    yasscheck.append('working')
                    if scan[-1] in vowels and scan [-2] + scan[-1]  not in dipthongs: #check end
                        regscan[-1] += '-'
                    if scan[-2] in vowels and scan [-2] + scan[-1]  not in dipthongs and scan [-3] + scan[-2] not in dipthongs:
                        regscan[-2] += '-'
                    if scan[0] in vowels and scan[1] in consonant and scan[2] in consonant: #check start
                        regscan[0] += '-'
                    elif scan[0] in vowels:
                        regscan[0] += '+'
                    if len(scan) == len(x) - elisioncount - spacecount:
                        for letters in ''.join(regscan):
                            for lettem in letters:
                                regscannew.append(lettem)
                                if len(regscannew)>5:
                                    if regscannew[-1] in symbols and regscannew[-2] == ' ':
                                        del regscan[-1]
                                    if regscannew[-4] in symbols and ' ' in regscannew[-3] and regscannew[-2] in consonant and regscannew[-1] in vowels:
                                        regscannew[-4] = '+'

    return ''.join(regscan)