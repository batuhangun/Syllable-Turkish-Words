consonant = ["b", "c", "d", "g", "ğ", "j", "l", "m", "n", "r", "v", "y", "z", "ç", "f", "h", "k", "p", "s", "ş", "t"]
vowel = ["a", "ı", "o", "u", "e", "i", "ö", "ü"]


def parser(word):
    spell = list(word)
    vowel_count = sum([1 for i in spell if i in vowel])
    lenght = len(word)

    if lenght == 1 or lenght == 2:
        return word

    if (lenght == 4 or lenght == 3) and vowel_count == 1:
        return word

    if word[0] in consonant:
        if word[1] in consonant:
            if word[4] in consonant:
                return word[:4] + "-" + parser(word[4:])
            else:
                return word[:3] + "-" + parser(word[3:])
        else:
            if word[2] in consonant and word[3] in consonant and not word[4] in consonant:
                return word[:3] + "-" + parser(word[3:])
            elif word[2] in consonant and word[3] in consonant and word[4] in consonant:
                return word[:4] + "-" + parser(word[4:])
            else:
                return word[:2] + "-" + parser(word[2:])
    else:
        if word[1] in vowel:
            return word[0] + "-" + parser(word[1:])
        else:
            if word[2] in vowel:
                return word[:1] + "-" + parser(word[1:])
            else:
                return word[:2] + "-" + parser(word[2:])


words = ["araba", "oyun", "kral", "batuhan", "ekmek", "saat", "vermek", "al", "yeteneklerinin", "e", "emretmek", "elek",
         "terk", "iade", "galatasaray", "sivrisinek", "adet", "diyar", "oturmak", "değil", "geliyorum", "ağabey",
         "sertlik", "krallık", "çekoslavakyalılaştıramadıklarımızdan", "varolmak", "yarınki", "stobaj", "prestij",
         "düşeyazmak", "drenaj", "merhaba", "istiyorum", "gül", "güler", "lacivert", "kainat", "öğrenene"]

for word in words:
    print(f"{word} = {parser(word)}")
