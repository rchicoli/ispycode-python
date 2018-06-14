
def string_test(s):
    d=&#123;"UPPER":0, "LOWER":0&#125;
    for c in s:
        if c.isupper():
           d["UPPER"]+=1
        elif c.islower():
           d["LOWER"]+=1
        else:
           pass

    print("String: %s " % (s) )
    print("Upper case characters: %s" % (d["UPPER"]))
    print("Lower case characters: %s" % (d["LOWER"]))

string_test('The Cat In The Hat')


