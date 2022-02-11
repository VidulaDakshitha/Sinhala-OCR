#malidi wageesha
#IT18194272
import re
import numpy as np
import time
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

def editDistance(str1, str2, weight=1):
    len1 = len(str1)
    len2 = len(str2)
    matrix = [[0] * (len2 + 1) for j in range(len1 + 1)]
    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if min(i, j) == 0:
                matrix[i][j] = max(i, j)
            else:
                addValue = 0 if str1[i-1] == str2[j-1] else weight
                matrix[i][j] = min(matrix[i-1][j-1] + addValue,
                                matrix[i-1][j] + 1,
                                matrix[i][j-1] + 1)
    return matrix[len1][len2]


def findMinimumValue(array,check2):
    checkArray=[]
    value = np.asarray(array)[:, 1]
    results = [int(i) for i in value]
    results2 = np.array(results)
    output = np.where(results2 == results2.min())

    spell_arr = []
    for x in output[0]:
        # print(array[x][0])
        #         if array[x][1]==0:

        #             if "true" not in spell_arr:
        #                 spell_arr.append("true")
        #         elif array[x][1]>0:

        #             if array[x][0] not in spell_arr:
        #                 spell_arr.append(array[x][0])
        if array[x][0] not in spell_arr:
            spell_arr.append(array[x][0])
    if check2 not in spell_arr:
        spell_arr.insert(0,check2)

    checkArray.append(spell_arr)
    spell_arr = []

    idx = np.argmin(results)
    return checkArray
    #return (array[idx][0])

def nGramAlgorithm(StringCheck,filename):
    n = 1 #value of n to form ngrams
    threshold = 75 #threshold for similarity percentage
    queryFile = open (filename, encoding="utf8")
    querylist = StringCheck.split()
    arrayVal=[]

    numNgramsPattern = len(list(zip(*[''.join(querylist)[i:] for i in range(n)]))) #list of ngrams in the pattern query
    lineCount = 0

    for queryvalue in queryFile:
        words = queryvalue.split()

        strings = zip(*[words[i:] for i in range(len(querylist))]) #list of strings with the same number of tokens as the query
        for token in strings:

            string = ''.join(token)
            ngrams = list(zip(*[string[i:] for i in range(n)])) #list of ngrams in the string
            numNgrams = len(ngrams)
            count = 0
            for ngram in ngrams:
                ng = ''.join(ngram)
                if re.search(ng, ''.join(querylist)): #searching for the presence of ngram in the pattern
                    count = count + 1
            if (numNgrams != 0 and (count * 100/numNgramsPattern) > threshold):
                    #print(token[0])
                    distance=editDistance(StringCheck,token[0])
                    arrayVal.append([token[0],distance])
    return arrayVal


def grammarAndWordChecker(list_value):
    blank_list = []
    processedlist = []

    for i in list_value:
        value_2 = nGramAlgorithm(i, env('PROJECT_SRC')+"_models/spelling/sin.wordlist")
        min_2 = findMinimumValue(value_2,i)

        processedlist.append(min_2)
    for j in list_value:
        for k in processedlist:
            processedlist

    return processedlist

def spellchecker_main(list_array):
    array_result = grammarAndWordChecker(list_array)
    return array_result
