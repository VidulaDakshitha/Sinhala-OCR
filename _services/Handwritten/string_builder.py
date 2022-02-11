import re


# IT18045840
# S.D.S.L Diaaanayake

def string_CompuWa0(word):
    try:
        modifier = "ෙ"

        le1 = re.sub(modifier + "ක", "කෙ ", word)
        le1 = re.sub(modifier + "ඛ", "ඛෙ ", le1)
        le1 = re.sub(modifier + "ග", "ගෙ ", le1)
        le1 = re.sub(modifier + "ඝ", "ඝෙ ", le1)
        le1 = re.sub(modifier + "ඟ", "ඟෙ ", le1)
        le1 = re.sub(modifier + "ඟ", "ඟෙ ", le1)
        le1 = re.sub(modifier + "ච", "චෙ ", le1)
        le1 = re.sub(modifier + "ඡ", "ඡෙ ", le1)
        le1 = re.sub(modifier + "ජ", "ජෙ ", le1)
        le1 = re.sub(modifier + "ඣ්", "ඣෙ ", le1)
        le1 = re.sub(modifier + "ඤ", "ඤෙෙ ", le1)
        le1 = re.sub(modifier + "ඦ්", "ඦේ ", le1)
        le1 = re.sub(modifier + "ජ", "ජේ ", le1)
        le1 = re.sub(modifier + "ට", "ටෙ ", le1)
        le1 = re.sub(modifier + "ඨ", "ඨෙ ", le1)
        le1 = re.sub(modifier + "ඩ", "ඩෙ ", le1)
        le1 = re.sub(modifier + "ණ", "ණෙ ", le1)
        le1 = re.sub(modifier + "ත", "තෙ ", le1)
        le1 = re.sub(modifier + "ද", "දෙ ", le1)
        le1 = re.sub(modifier + "ධ", "ධෙ ", le1)
        le1 = re.sub(modifier + "න", "නෙ ", le1)
        le1 = re.sub(modifier + "ඳ", "ඳෙ ", le1)
        le1 = re.sub(modifier + "ප", "පෙ ", le1)
        le1 = re.sub(modifier + "ඵ", "ඵෙ ", le1)
        le1 = re.sub(modifier + "බ", "බෙ ", le1)
        le1 = re.sub(modifier + "හ", "භෙ ", le1)
        le1 = re.sub(modifier + "ම", "මෙ ", le1)
        le1 = re.sub(modifier + "ඹ", "ඹෙ ", le1)
        le1 = re.sub(modifier + "ය", "යෙ ", le1)
        le1 = re.sub(modifier + "ර", "රෙ ", le1)
        le1 = re.sub(modifier + "ල", "ලෙ ", le1)
        le1 = re.sub(modifier + "ව", "වෙ ", le1)
        le1 = re.sub(modifier + "ශ", "ශෙ ", le1)
        le1 = re.sub(modifier + "ෂ", "ෂෙ ", le1)
        le1 = re.sub(modifier + "ස", "සෙ ", le1)
        le1 = re.sub(modifier + "හ", "හෙ ", le1)
        le1 = re.sub(modifier + "ළ", "ළෙ ", le1)
        le1 = re.sub(modifier + "ෆ", "ෆෙ ", le1)
        le1 = re.sub(modifier + "ඹ", "ඹෙ ", le1)
        le1 = re.sub(" ", "", le1)

        return le1


    except:
        print('error occurred : string_CompuWa0')

        return word


def string_CompuWa1(word):
    try:
        modifier = "ෙ"

        letter = re.sub(modifier + "ක්", "කේ ", word)
        letter = re.sub(modifier + "ඛ්", "ඛේ ", letter)
        letter = re.sub(modifier + "ග්", "ගේ ", letter)
        letter = re.sub(modifier + "ඝ්", "ඝේ ", letter)
        letter = re.sub(modifier + "ඟ්", "ඟේ ", letter)
        letter = re.sub(modifier + "ච්", "චේ ", letter)
        letter = re.sub(modifier + "ඡ්", "ඡේ ", letter)
        letter = re.sub(modifier + "ජ්", "ජේ ", letter)

        letter = re.sub(modifier + "ජ්", "ජේ ", letter)
        letter = re.sub(modifier + "ට්", "ටේ ", letter)
        letter = re.sub(modifier + "ඨ්", "ඨේ ", letter)
        letter = re.sub(modifier + "ඩ්", "ඩේ ", letter)
        letter = re.sub(modifier + "ණ්", "ණේ ", letter)
        letter = re.sub(modifier + "ත්", "තේ ", letter)
        letter = re.sub(modifier + "ථ්", "ථේ ", letter)
        letter = re.sub(modifier + "ද්", "දේ ", letter)
        letter = re.sub(modifier + "ධ්", "ධේ ", letter)
        letter = re.sub(modifier + "න්", "නේ ", letter)

        letter = re.sub(modifier + "ප්", "පේ ", letter)

        letter = re.sub(modifier + "බ්", "බේ ", letter)
        letter = re.sub(modifier + "භ්", "භේ ", letter)
        letter = re.sub(modifier + "ම්", "මේ ", letter)
        letter = re.sub(modifier + "ඹ්", "ඹේ ", letter)
        letter = re.sub(modifier + "ය්", "යේ ", letter)
        letter = re.sub(modifier + "ර්", "රේ ", letter)
        letter = re.sub(modifier + "ල්", "ලෙ ", letter)
        letter = re.sub(modifier + "ව්", "වේ ", letter)
        letter = re.sub(modifier + "ශ්", "ශේ ", letter)
        letter = re.sub(modifier + "ෂ්", "ෂේ ", letter)
        letter = re.sub(modifier + "ස්", "සේ ", letter)
        letter = re.sub(modifier + "හ", "හේ ", letter)
        letter = re.sub(modifier + "ෆ්", "ෆේ ", letter)

        letter = re.sub(" ", "", letter)

        return letter
    except:
        print('error occurred : string_CompuWa1')

        return word


def string_CompuWa2(word):
    try:
        modifier = "ෙ"

        letter = re.sub(modifier + "කෝ", "කෝ ", word)
        letter = re.sub(modifier + "ඛෝ", "ඛෝ ", letter)
        letter = re.sub(modifier + "ගෝ", "ගේ ", letter)
        letter = re.sub(modifier + "ඝෝ", "ඝෝ ", letter)
        letter = re.sub(modifier + "චෝ", "චෝ ", letter)
        letter = re.sub(modifier + "ජෝ", "ජෝ ", letter)
        letter = re.sub(modifier + "ටෝ", "ටෝ ", letter)
        letter = re.sub(modifier + "ඩෝ", "ඩෝ ", letter)
        letter = re.sub(modifier + "තෝ", "තෝ ", letter)
        letter = re.sub(modifier + "දෝ", "දෝ ", letter)
        letter = re.sub(modifier + "ධෝ", "ධෝ ", letter)
        letter = re.sub(modifier + "නෝ", "නෝ ", letter)

        letter = re.sub(modifier + "පෝ", "පෝ ", letter)
        letter = re.sub(modifier + "බෝ", "බෝ ", letter)
        letter = re.sub(modifier + "මෝ", "මෝ ", letter)
        letter = re.sub(modifier + "යෝ", "යෝ ", letter)
        letter = re.sub(modifier + "රෝ", "රෝ ", letter)

        letter = re.sub(modifier + "ලෝ", "ලෝ ", letter)
        letter = re.sub(modifier + "වෝ", "වෝ ", letter)
        letter = re.sub(modifier + "ශෝ", "ශෝ ", letter)
        letter = re.sub(modifier + "ෂෝ", "ශෝ ", letter)

        letter = re.sub(modifier + "සෝ", "සෝ ", letter)
        letter = re.sub(modifier + "හෝ", "හෝ ", letter)
        letter = re.sub(modifier + "ෆෝ", "ෆෝ ", letter)

        letter = re.sub(" ", "", letter)

        return letter
    except:
        print('error occured : string_CompuWa2')
        return word


def string_CompuWa3(word):
    modifier = "M"

    le1 = re.sub(modifier + "ක", "කෛ ", word)
    le2 = re.sub(modifier + "ඛ", "ඛෛ ", le1)
    le3 = re.sub(modifier + "ග", "ගෛ ", le2)
    le4 = re.sub(modifier + "ඝ", "ඝෛ ", le3)
    le5 = re.sub(modifier + "ච", "චෛ ", le4)
    le6 = re.sub(modifier + "ජ", "ජෛ ", le5)
    le7 = re.sub(modifier + "ට", "ටෛ ", le6)
    le8 = re.sub(modifier + "ත", "තෛ ", le7)
    le9 = re.sub(modifier + "ද", "දෛ ", le8)
    le10 = re.sub(modifier + "න", "නෛ ", le9)
    le11 = re.sub(modifier + "ප", "පෛ ", le10)
    le12 = re.sub(modifier + "ල", "ලෛ ", le11)
    le13 = re.sub(modifier + "ය", "යෛ ", le12)
    le14 = re.sub(modifier + "ස", "සෛ ", le13)
    le15 = re.sub(modifier + "හ", "හෛ ", le14)

    le16 = re.sub(" ", "", le15)

    return le16


# supportive letters

def is_suppotiveLetter(word):
    modified_word = word

    if re.search('Y', modified_word):
        modified_word = string_supportLetterY(modified_word)

    if re.search('Hq', modified_word):
        modified_word = string_supportLetterHq(modified_word)

    if re.search('O', modified_word):
        modified_word = string_supportLetterO(modified_word)

    if re.search('ා', modified_word):
        modified_word = string_supportLettersAlapaiila(modified_word)

    return modified_word


def string_supportLettersAlapaiila(word):
    try:
        modifier = "ා"
        letter = re.sub("අ" + modifier, "ආ", word)
        letter = re.sub("ක" + modifier, "කා", letter)
        letter = re.sub("ඛ" + modifier, "ඛා", letter)
        letter = re.sub("ග" + modifier, "ගා", letter)
        letter = re.sub("ඝ" + modifier, "ඝා", letter)
        letter = re.sub("ච" + modifier, "චා", letter)
        letter = re.sub("ජ" + modifier, "ඡා", letter)
        letter = re.sub("ට" + modifier, "ටා", letter)
        letter = re.sub("ඨ" + modifier, "ඨා", letter)
        letter = re.sub("ඩ" + modifier, "ඩා", letter)
        letter = re.sub("ඪ" + modifier, "ඪා", letter)
        letter = re.sub("ත" + modifier, "තා", letter)
        letter = re.sub("ථ" + modifier, "ථා", letter)
        letter = re.sub("ද" + modifier, "දා", letter)
        letter = re.sub("ධ" + modifier, "ධා", letter)
        letter = re.sub("න" + modifier, "නා", letter)
        letter = re.sub("ණ" + modifier, "ණා", letter)
        letter = re.sub("ප" + modifier, "පා", letter)
        letter = re.sub("ඵ" + modifier, "ඵා", letter)
        letter = re.sub("බ" + modifier, "බා", letter)
        letter = re.sub("භ" + modifier, "භා", letter)
        letter = re.sub("ම" + modifier, "මා", letter)
        letter = re.sub("ය" + modifier, "යා", letter)
        letter = re.sub("ර" + modifier, "රා", letter)
        letter = re.sub("ල" + modifier, "ලා", letter)
        letter = re.sub("ස" + modifier, "සා", letter)
        letter = re.sub("ශ" + modifier, "ශා", letter)
        letter = re.sub("ෂ" + modifier, "ෂා", letter)
        letter = re.sub("හ" + modifier, "හා", letter)
        letter = re.sub("ළ" + modifier, "ළා", letter)
        letter = re.sub("ෆ" + modifier, "ෆා", letter)

        return letter
    except:
        print('error occured : postSupportLettersAlapaiila')
        return word


def string_supportLetterHq(word):
    try:
        modifier = "Hq"

        letter = re.sub("ක" + modifier, "ක්‍යු", word)
        letter = re.sub("ග" + modifier, "ග්‍යු", letter)
        letter = re.sub("ච" + modifier, "ච්‍යු", letter)
        letter = re.sub("ජ" + modifier, "ජ්‍යු", letter)
        letter = re.sub("ට" + modifier, "ට්‍යු", letter)
        letter = re.sub("ඩ" + modifier, "ඩ්‍යු", letter)
        letter = re.sub("ත" + modifier, "ත්‍යු", letter)
        letter = re.sub("ද" + modifier, "ද්‍යු", letter)
        letter = re.sub("න" + modifier, "න්‍යු", letter)
        letter = re.sub("ප" + modifier, "ප්‍යු", letter)
        letter = re.sub("බ" + modifier, "බ්‍යු", letter)
        letter = re.sub("ම" + modifier, "ම්‍යු", letter)
        letter = re.sub("ය" + modifier, "ය්‍යු", letter)
        letter = re.sub("ස" + modifier, "ස්‍යු", letter)
        letter = re.sub("හ" + modifier, "හ්‍යු", letter)
        letter = re.sub("ෆ" + modifier, "ෆ්‍යු", letter)

        return letter
    except:
        print('error occured : string_supportLetterHq')
        return word


def string_supportLetterY(word):
    try:
        modifier = "Y"

        letter = re.sub("ක" + modifier, "ක්‍ය", word)
        letter = re.sub("ග" + modifier, "ග්‍ය", letter)
        letter = re.sub("ච" + modifier, "ච්‍ය", letter)
        letter = re.sub("ජ" + modifier, "ජ්‍ය", letter)
        letter = re.sub("ට" + modifier, "ට්‍ය", letter)
        letter = re.sub("ඩ" + modifier, "ඩ්‍ය", letter)
        letter = re.sub("ත" + modifier, "ත්‍ය", letter)
        letter = re.sub("ද" + modifier, "ද්‍ය", letter)
        letter = re.sub("න" + modifier, "න්‍ය", letter)
        letter = re.sub("ප" + modifier, "ප්‍ය", letter)
        letter = re.sub("බ" + modifier, "බ්‍ය", letter)
        letter = re.sub("ම" + modifier, "ම්‍ය", letter)
        letter = re.sub("ය" + modifier, "ය්‍ය", letter)
        letter = re.sub("ස" + modifier, "ස්‍ය", letter)
        letter = re.sub("හ" + modifier, "හ්‍ය", letter)
        letter = re.sub("ෆ" + modifier, "ෆ්‍ය", letter)

        return letter
    except:
        print('error occured : string_supportLetterH')
        return word


def string_supportLetterO(word):
    try:
        modifier = "ං"

        letter = re.sub("ක" + modifier, "කං", word)
        letter = re.sub("ග" + modifier, "ගං", letter)
        letter = re.sub("ච" + modifier, "චං", letter)
        letter = re.sub("ජ" + modifier, "ජං", letter)
        letter = re.sub("ට" + modifier, "ටං", letter)
        letter = re.sub("ඩ" + modifier, "ඩං", letter)
        letter = re.sub("ත" + modifier, "තං", letter)
        letter = re.sub("ද" + modifier, "දං", letter)
        letter = re.sub("න" + modifier, "නං", letter)
        letter = re.sub("ප" + modifier, "පං", letter)
        letter = re.sub("බ" + modifier, "බං", letter)
        letter = re.sub("ම" + modifier, "මං", letter)
        letter = re.sub("ය" + modifier, "යං", letter)
        letter = re.sub("ස" + modifier, "සං", letter)
        letter = re.sub("හ" + modifier, "හං", letter)
        letter = re.sub("ෆ" + modifier, "ෆං", letter)

        return letter
    except:
        print('error occured : string_supportLetterO')
        return word
