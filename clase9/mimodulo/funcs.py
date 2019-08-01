

def hello():
    print("Hello!")

def bye():
    print("Bye bye!")

def hello_by_name(name):
    print ("Hello {0}!".format(name))


def mifunc (val0=0, val1=0, val2=1):
    rs = (val0 + val1) * val2
    return rs

def mifunc5(val0=0, val1=0, val2=1):
    return mifunc(val0, val1, val2) * 5

def get_score(filename):
    return []

def score_top_print(list):
    print (list)

def get_secrect(top):
    return 22

def save_score(filename, list):
    pass