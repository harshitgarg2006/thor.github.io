from django.shortcuts import render
from django.http import HttpResponse

def python(request):
    return render(request , "python/pythontutorial.html")

def datatypes(request):
    return render(request , "python/datatypeshome.html")

def list(request):
    return render(request , "python/listmethods.html")

def listsorted(request):
    params = {"action" : "Enter The List You Want To Sort" , "action1" : "sorted", "action2" : "list","action5":'''
a = input("Enter Elements Seperated By Comma : ")
b = a.split(",")
n = list(b)
n.sort()
print(n)
'''}
    return render(request , "python/inputforlist.html", params)

def listsortedresult(request):
    list = request.GET.get('text','default')
    items = list.split(",")
    nums = []
    strs = []
    for i in items:
        i = i.strip()
        if i.isdigit():
            nums.append(int(i))
        else:
            strs.append(i)
    nums.sort()
    strs.sort()
    result = nums + strs
    param = { "result" : result}
    return render(request , "python/output.html", param)


def listextend(request):
    params = {"action" : "Enter The List You Want To Insert In a = [10,20,30]" , "action1" : "extend", "action2" : "list","action5":'''
a = input("Enter Elements Seperated By Comma : ")
n = [10,20,30]
b = a.split(",")
c = list(b)
n.extend(c)
print(n)
'''}
    return render(request , "python/inputforlist.html", params)

def listextendresult(request):  
    a = [10,20,30]
    text = request.GET.get('text', 'default')
    items = text.split(",")
    a.extend(items)
    param = { "result" : a}
    print(a)
    return render(request , "python/output.html", param)

def listappend(request):
    params = {"action" : "Enter The Element You Want To Append Into The List a = [10,20,30]" , "action1" : "append", "action2" : "list","action5":'''
a = input("Enter A Single Element : ")
n = [10,20,30]
n.append(a)
print(n)
'''}
    return render(request , "python/inputforlist.html", params)

def listappendresult(request):  
    a = [10,20,30]
    text = int(request.GET.get('text', 'default'))
    a.append(text)
    param = { "result" : a}
    print(a)
    return render(request , "python/output.html", param)

def listinsert(request):
    params = {"action" : "Enter The Element You Want To Insert With Index Separated By A Comma Into The List a = [10,20,30]" , "action1" : "insert", "action2" : "list","action5":'''
a = input("Enter A Single Element : ")
b = int(input("Enter Index Where You Want To Insert This Element : "))
n = [10,20,30]
n.insert(b,a)
print(n)
'''}
    return render(request , "python/inputforlist.html", params)

def listinsertresult(request):  
    a = [10,20,30]
    text = request.GET.get('text', 'default')
    items = text.split(",")
    num1 = int(items[0])
    num2 = int(items[1])
    a.insert(num1 , num2)
    print(a)
    param = { "result" : a}
    return render(request , "python/output.html", param)

def listpop(request):
    params = {"action" : "Enter A List From Which You Want To Pop An Element" , "action1" : "pop", "action2" : "list","action5":'''
a = input("Enter Elements Seperated By Commas : ")
b = a.split(",")
b = list(b)
n = b.pop()
print(n)
'''}
    return render(request , "python/inputforlist.html", params)

def listpopresult(request):  
    text = request.GET.get('text', 'default')
    items = text.split(",")
    a = items.pop()
    param = { "result" : a}
    print(a)
    return render(request , "python/output.html", param)

def strings(request):
    return render(request , "python/stringmethods.html")

def stringupper(request):
    params = {"action" : "Enter The String" , "action1" : "upper", "action2" :  "string","action5":'''
a = input("Enter A String : ")
print(a.upper())
'''}
    return render(request , "python/inputforlist.html", params)

def stringupperresult(request):  
    text = request.GET.get('text', 'default')
    items = text.split(",")
    a = str(items)
    a = a.upper()
    print(type(items))
    param = { "result" : a}
    return render(request , "python/output.html", param)

def stringlower(request):
    params = {"action" : "Enter The String" , "action1" : "lower", "action2" :  "string","ACTION5":'''
a = input("Enter A String : ")
print(a.upper())
'''}
    return render(request , "python/inputforlist.html", params)

def stringlowerresult(request):  
    text = request.GET.get('text', 'default')
    items = text.split(",")
    a = str(items)
    a = a.lower()
    print(type(items))
    param = { "result" : a}
    return render(request , "python/output.html", param)

def stringcapitalize(request):
    params = {"action" : "Enter The String" , "action1" : "capitalize", "action2" :  "string","action5":'''
a = input("Enter A String : ")
print(a.capitalize())
'''}
    return render(request , "python/inputforlist.html", params)

def stringcapitalizeresult(request):  
    text = request.GET.get('text', 'default')
    items = text.split(",")
    a = str(items)
    a = a.capitalize()
    print(type(items))
    param = { "result" : a}
    return render(request , "python/output.html", param)

def stringtitle(request):
    params = {"action" : "Enter The String" , "action1" : "title", "action2" :  "string","action5":'''
a = input("Enter A String : ")
print(a.title())
'''}
    return render(request , "python/inputforlist.html", params)

def stringtitleresult(request):  
    text = request.GET.get('text', 'default')
    items = text.split(",")
    a = str(items)
    a = a.title()
    print(type(items))
    param = { "result" : a}
    return render(request , "python/output.html", param)

def stringstrip(request):
    params = {"action" : "Enter The String" , "action1" : "strip", "action2" :  "string","action5":'''
a = input("Enter A String : ")
print(a.strip())
'''}
    return render(request , "python/inputforlist.html", params)

def stringstripresult(request):  
    text = request.GET.get('text', 'default')
    items = text.split(",")
    a = str(items)
    a = a.strip()
    print(type(items))
    param = { "result" : a}
    return render(request , "python/output.html", param)

def sets(request):
    return render(request , "python/setmethods.html")

def setadd(request):
    params = {"action" : "Enter A Single Element You Want To Add In The Set a = {1,2,3}" , "action1" : "add", "action2" :  "sets" , "action5" : 
'''n = input('Enter An Element : ')
   if n.isdigit():
       n = int(n)
   a = {1,2,3}
   a.add(n)
   print(a)'''}
    return render(request , "python/inputforlist.html", params)

def setaddresult(request):  
    text = request.GET.get('text', 'default')
    if (text.isdigit()):
        text = int(text)
    a = {1,2,3}
    a.add(text)
    print(type(text))
    param = { "result" : a}
    return render(request , "python/output.html", param)

def setupdate(request):
    params = {"action" : "Enter A Set Separated By Commas You Want To Update In The Set a = {1,2,3}" , "action1" : "update", "action2" :  "sets","action5":'''
b = input("Enter Elements Seperated By Commas : ")
a = {1,2,3}
c = b.split(",")
c = set(c)
a.update(c)
print(a)
'''}
    return render(request , "python/inputforlist.html", params)

def setupdateresult(request):  
    text = request.GET.get('text', 'default')
    items = set(text.split(","))
    set1 = {1,2,3}
    for i in items:
        if i.isdigit():
            set1.add(int(i))
        else:
            set1.add(i)
    a = {1,2,3}
    a.update(set1)
    param = { "result" : a}
    return render(request , "python/output.html", param)

def setremove(request):
    params = {"action" : "Enter A Single Element You Want To Remove From The Set a = {1,2,3}" , "action1" : "remove", "action2" :  "sets","action5":'''
b = int(input("Enter An Element : "))
a = {1,2,3}
a.remove(b)
print(a)
'''}
    return render(request , "python/inputforlist.html", params)

def setremoveresult(request):  
    text = request.GET.get('text', 'default')
    if text.isdigit():
        text = int(text)
    a = {1,2,3}
    a.remove(text)
    param = { "result" : a}
    return render(request , "python/output.html", param)

def setdiscard(request):
    params = {"action" : "Enter A Single Element You Want To Remove From The Set a = {1,2,3}" , "action1" : "discard", "action2" :  "sets","action5":'''
b = int(input("Enter An Element : "))
a = {1,2,3}
a.discard(b)
print(a)
'''}
    return render(request , "python/inputforlist.html", params)

def setdiscardresult(request):  
    text = request.GET.get('text', 'default')
    if text.isdigit():
        text = int(text)
    a = {1,2,3}
    a.discard(text)
    param = { "result" : a}
    return render(request , "python/output.html", param)

def setunion(request):
    params = {"action" : "Enter A Single Element You Want To Add In The Set a = {1,2,3}" , "action1" : "union", "action2" :  "sets","action5":'''
b = input("Enter Elements Seperated By Commas : ")
a = {1,2,3}
c = b.split(",")
c = set(c)
a = a.union(c)
print(a)
'''}
    return render(request , "python/inputforlist.html", params)

def setunionresult(request):  
    text = request.GET.get('text', 'default')
    items = set(text.split(","))
    set1 = {1}
    for i in items:
        if i.isdigit():
            set1.add(int(i))
        else:
            set1.add(i)
    a = {1,2,3}
    a = a.union(set1)
    param = { "result" : a}
    return render(request , "python/output.html", param)

def tuples(request):
    return render(request , "python/tuplemethods.html")

def tuplecount(request):
    params = {"action" : "Enter A Single Element You Want To Count From The Set a = (1,2,3,4,3,2,6,6,5,8,5,4,9,10)" , "action1" : "count", "action2" :  "tuple","action5":'''
text = input("Enter A Number : ")
if text.isdigit():
    text = int(text)
a = (1,2,3,4,3,2,6,6,5,8,5,4,9,10)
c = a.count(text)
print(c)
'''}
    return render(request , "python/inputforlist.html", params)

def tuplecountresult(request):  
    text = request.GET.get('text', 'default')
    if text.isdigit():
        text = int(text)
    a = (1,2,3,4,3,2,6,6,5,8,5,4,9,10)
    c = a.count(text)
    param = { "result" : c}
    return render(request , "python/output.html", param)

def tupleindex(request):
    params = {"action" : "Enter A Single Element You Want To Find Index Of From The Set a = (1,2,3,4,3,2,6,6,5,8,5,4,9,10)" , "action1" : "index", "action2" :  "tuple","action5":'''
text = input("Enter A Number : ")
if text.isdigit():
    text = int(text)
a = (1,2,3,4,3,2,6,6,5,8,5,4,9,10)
c = a.index(text)
print(c)
'''}
    return render(request , "python/inputforlist.html", params)

def tupleindexresult(request):  
    text = request.GET.get('text', 'default')
    if text.isdigit():
        text = int(text)
    a = (1,2,3,4,3,2,6,6,5,8,5,4,9,10)
    c = a.index(text)
    param = { "result" : c}
    return render(request , "python/output.html", param)

def tuplelen(request):
    params = {"action" : "Enter Tuple You Want To Find Length Of" , "action1" : "len", "action2" :  "tuple","action5":'''
tup = input("Enter Elements Seperated By Commas : ")
items = tuple(tup.split(","))
c = len(items)
print(c)
'''}
    return render(request , "python/inputforlist.html", params)

def tuplelenresult(request):  
    text = request.GET.get('text', 'default')
    items = tuple(text.split(","))
    set1 = []
    for i in items:
        if i.isdigit():
            set1.append(int(i))
        else:
            set1.add(i)
    tup = tuple(set1)
    c = len(tup)
    param = { "result" : c}
    return render(request , "python/output.html", param)

def tuplemax(request):
    params = {"action" : "Enter Tuple You Want To Find Max Elememt Of" , "action1" : "max", "action2" :  "tuple","action5":'''
tup = input("Enter Elements Seperated By Commas : ")
items = list(tup.split(","))
for i in range(0,len(items)):
    if items[i].isdigit:
        items[i] = int(items[i])
items = tuple(items)
c = max(items)
print(c)
'''}
    return render(request , "python/inputforlist.html", params)

def tuplemaxresult(request):  
    text = request.GET.get('text', 'default')
    items = tuple(text.split(","))
    set1 = []
    for i in items:
        if i.isdigit():
            set1.append(int(i))
        else:
            set1.append(i)
    tup = tuple(set1)
    c = max(tup)
    param = { "result" : c}
    return render(request , "python/output.html", param)

def tuplemin(request):
    params = {"action" : "Enter Tuple You Want To Find Min Elememt Of" , "action1" : "min", "action2" :  "tuple","action5":'''
tup = input("Enter Elements Seperated By Commas : ")
items = list(tup.split(","))
for i in range(0,len(items)):
    if items[i].isdigit:
        items[i] = int(items[i])
items = tuple(items)
c = min(items)
print(c)
'''}
    return render(request , "python/inputforlist.html", params)

def tupleminresult(request):  
    text = request.GET.get('text', 'default')
    items = tuple(text.split(","))
    set1 = []
    for i in items:
        if i.isdigit():
            set1.append(int(i))
        else:
            set1.append(i)
    tup = tuple(set1)
    c = min(tup)
    param = { "result" : c}
    return render(request , "python/output.html", param)

def dictionary(request):
    return render(request , "python/dictionarymethods.html")

def dictget(request):
    params = {"action" : "Enter The Key Who's Value You Want From The Dictionary with keys a,b and c", "action1" : "get", "action2" :  "dict","action5":'''
num = input("Enter A Number : ")
dict = {
    "a":1,
    "b":2,
    "c":3
}
c = dict.get(num)
print(c)
'''}
    return render(request , "python/inputforlist.html", params)

def dictgetresult(request):
    text = request.GET.get('text', 'default')
    dict = {
        "a":1,
        "b":2,
        "c":3
    }
    c = dict.get(text)
    param = { "result" : c}
    return render(request , "python/output.html", param)

def dictkeys(request):
    params = {"action" : "Enter The Keys And Values Separated By Commas To Get keys", "action1" : "keys", "action2" :  "dict","action5":'''
keys = input("Enter Keys Seperated By Commas : ")
values = input("Enter Values Seperated By Commas : ")
d = {}
key = keys.split(",")
value = values.split(",")
for i in range(0,len(key)):
    if key[i].isdigit():
        key[i] = int(key[i])
        d[(key[i])] = value[i]
    else:
        d[(key[i])] = value[i]
print(d.keys())
'''}
    return render(request , "python/inputfordictionary.html", params)

def dictkeysresult(request):
    keys = request.GET.get('keys', 'default')
    values = request.GET.get('values', 'default')
    d = {}
    key = keys.split(",")
    value = values.split(",")
    for i in range(0,len(key)):
        if key[i].isdigit():
            key[i] = int(key[i])
            d[(key[i])] = value[i]
        else:
            d[(key[i])] = value[i]
    l = tuple(d.keys())
    param = { "result" : l}
    return render(request , "python/output.html", param)

def dictvalues(request):
    params = {"action" : "Enter The Keys And Values Separated By Commas To Get values", "action1" : "values", "action2" :  "dict","action5":'''
keys = input("Enter Keys Seperated By Commas : ")
values = input("Enter Values Seperated By Commas : ")
d = {}
key = keys.split(",")
value = values.split(",")
for i in range(0,len(key)):
    if key[i].isdigit():
        key[i] = int(key[i])
        d[(key[i])] = value[i]
    else:
        d[(key[i])] = value[i]
print(d.values())
'''}
    return render(request , "python/inputfordictionary.html", params)

def dictvaluesresult(request):
    keys = request.GET.get('keys', 'default')
    values = request.GET.get('values', 'default')
    d = {}
    key = keys.split(",")
    value = values.split(",")
    for i in range(0,len(key)):
        if value[i].isdigit():
            d[key[i]] = int(value[i])
        else:
            d[(key[i])] = value[i]
    l = tuple(d.values())
    print(l)
    param = { "result" : l}
    return render(request , "python/output.html", param)

def dictitems(request):
    params = {"action" : "Enter The Keys And Values Separated By Commas To Get Items", "action1" : "items", "action2" :  "dict","action5":'''
keys = input("Enter Keys Seperated By Commas : ")
values = input("Enter Values Seperated By Commas : ")
d = {}
key = keys.split(",")
value = values.split(",")
for i in range(0,len(key)):
    if key[i].isdigit():
        key[i] = int(key[i])
        d[(key[i])] = value[i]
    else:
        d[(key[i])] = value[i]
print(d.items())
'''}
    return render(request , "python/inputfordictionary.html", params)

def dictitemsresult(request):
    keys = request.GET.get('keys', 'default')
    values = request.GET.get('values', 'default')
    d = {}
    key = keys.split(",")
    value = values.split(",")
    for i in range(0,len(key)):
        if value[i].isdigit():
            d[key[i]] = int(value[i])
        else:
            d[(key[i])] = value[i]
    l = tuple(d.items())
    print(l)
    param = { "result" : l}
    return render(request , "python/output.html", param)

def dictupdate(request):
    params = {"action" : "Enter The Key And Value You Want To Update In The Dictionary with keys a,b and c With Values 1,2 And 3 Respectively", "action1" : "update", "action2" :  "dict","action5":'''
d1 = {
    "name" : "HARSHIT",
    "department":"Textile Techgnology"
}
keys = input("Enter Keys Seperated By Commas : ")
values = input("Enter Values Seperated By Commas : ")
d = {}
key = keys.split(",")
value = values.split(",")
for i in range(0,len(key)):
    if key[i].isdigit():
        key[i] = int(key[i])
        d[(key[i])] = value[i]
    else:
        d[(key[i])] = value[i]
d1.update(d)
print(d1)
'''}
    return render(request , "python/inputfordictionary.html", params)

def dictupdateresult(request):
    d1 = {
        "a":1,
        "b":2,
        "c":3
    }
    keys = request.GET.get('keys', 'default')
    values = request.GET.get('values', 'default')
    d = {}
    key = keys.split(",")
    value = values.split(",")
    for i in range(0,len(key)):
        d[key[i]] = int(value[i])
    d1.update(d)
    param = { "result" : d1}
    return render(request , "python/output.html", param)

def operators(request):
    return render(request , "python/operatorshome.html")

def operatorexponent(request):
    param = {"action2": "operator" , "action1" :"exponent","action" : "Find Exponent Of A Number", "action3" : "Enter The Number ", "action4" : "Enter The Power","action5":'''
a = int(input("Enter The Number : "))
b = int(input("Enter The Power : "))
print(a**b)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorexponentresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)**int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorunaryplus(request):
    param = {"action2": "operator" , "action1" :"unaryplus","action" : "Find Unary Plus Of A Number", "action3" : "Enter The Number ","action5":'''
a = int(input("Enter The Number : "))
a = +a
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatorunaryplusresult(request):
    num1 = request.GET.get('num1','default')
    a = +int(num1)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorunaryminus(request):
    param = {"action2": "operator" , "action1" :"unaryminus","action" : "Find Unary Minus Of A Number", "action3" : "Enter The Number ","action5":'''
a = int(input("Enter The Number : "))
a = -a
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatorunaryminusresult(request):
    num1 = request.GET.get('num1','default')
    a = -int(num1)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorbitwisenot(request):
    param = {"action2": "operator" , "action1" :"bitwisenot","action" : "Find Bitwise Not Of A Number", "action3" : "Enter The Number ","action5":'''
n = int(input("Enter A Number : "))
b = bin(n)[2:]
f = ""
for i in b:
    if i == "0":
           f += "1"
    else:
         f += "0"
a = int(f, 2)
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatorbitwisenotresult(request):
    num1 = request.GET.get('num1','default')
    n = int(num1)
    b = bin(n)[2:]

    f = ""
    for i in b:
        if i == "0":
            f += "1"
        else:
            f += "0"
    a = int(f, 2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatormultiplication(request):
    param = {"action2": "operator" , "action1" :"multiplication","action" : "Find Product Of Two Numbers", "action3" : "Enter First Number ", "action4" : "Enter Second Number ","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1*n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatormultiplicationresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)*int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatordivision(request):
    param = {"action2": "operator" , "action1" :"division","action" : "Find Division Of One Number By Another", "action3" : "Enter First Number ", "action4" : "Enter Second Number ","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1/n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatordivisionresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)/int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorfloordivision(request):
    param = {"action2": "operator" , "action1" :"floordivision","action" : "Find Floor Division Of One Number By Another", "action3" : "Enter First Number ", "action4" : "Enter Second Number ","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1//n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorfloordivisionresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)//int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatormodulus(request):
    param = {"action2": "operator" , "action1" :"modulus","action" : "Find Modulus Of One Number By Another", "action3" : "Enter First Number ", "action4" : "Enter Second Number ","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1%n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatormodulusresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)%int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatoraddition(request):
    param = {"action2": "operator" , "action1" :"addition","action" : "Find The Addition Of Two Numbers", "action3" : "Enter First Number ", "action4" : "Enter Second Number ","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1+n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatoradditionresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)+int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorsubtraction(request):
    param = {"action2": "operator" , "action1" :"subtraction","action" : "Find Subtraction Of One Number By Another", "action3" : "Enter First Number ", "action4" : "Enter Second Number ","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1-n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorsubtractionresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)-int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorbsl(request):
    param = {"action2": "operator" , "action1" :"bsl","action" : "Find Bitwise Shift Left Of A Number", "action3" : "Enter The Number ", "action4" : "Enter How Many Bits To Shift","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1<<n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorbslresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)<<int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorbsr(request):
    param = {"action2": "operator" , "action1" :"bsr","action" : "Find Bitwise Shift Right Of A Number", "action3" : "Enter The Number ", "action4" : "Enter How Many Bits To Shift","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1>>n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorbsrresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)>>int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorbitwiseand(request):
    param = {"action2": "operator" , "action1" :"bitwiseand","action" : "Find Bitwise And Of Two Numbers", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1&n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorbitwiseandresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)&int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorbitwisexor(request):
    param = {"action2": "operator" , "action1" :"bitwisexor","action" : "Find Bitwise Xor Of Two Numbers", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n^<n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorbitwisexorresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)^int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorbitwiseor(request):
    param = {"action2": "operator" , "action1" :"bitwiseor","action" : "Find Bitwise Or Of Two Numbers", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1|n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorbitwiseorresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1)|int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorisequal(request):
    param = {"action2": "operator" , "action1" :"isequal","action" : "Check If Two Numbers Are Equal", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1==n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorisequalresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) == int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorisnotequal(request):
    param = {"action2": "operator" , "action1" :"isnotequal","action" : "Check If Two Numbers Are Not Equal", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1!=n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorisnotequalresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) != int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorgreater(request):
    param = {"action2": "operator" , "action1" :"greater","action" : "Check If First Number Is Greater Than The Second Number", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1>n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorgreaterresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) > int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorsmaller(request):
    param = {"action2": "operator" , "action1" :"smaller","action" : "Check If First Number Is Smaller Than The Second Number", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1<n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorsmallerresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) < int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorgreaterequal(request):
    param = {"action2": "operator" , "action1" :"greaterequal","action" : "Check If First Number Is Greater Than Or Equal To The Second Number", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1>=n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorgreaterequalresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) >= int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorsmallerequal(request):
    param = {"action2": "operator" , "action1" :"smallerequal","action" : "Check If First Number Is Smaller Than Or Equal To The Second Number", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1<=n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorsmallerequalresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) <= int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatoris(request):
    param = {"action2": "operator" , "action1" :"is","action" : "Check If Both Numbers Are Same Or Not", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1 is n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorisresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) is int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorisnot(request):
    param = {"action2": "operator" , "action1" :"isnot","action" : "Check If Both Numbers Are Not Same Or Are They", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1 is not n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorisnotresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) is not int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorin(request):
    param = {"action2": "operator" , "action1" :"in","action" : "Check If A number Is In The List = [1,3,7,6,4,3,9,10]", "action3" : "Enter The Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1 in n2)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatorinresult(request):
    num1 = request.GET.get('num1','default')
    l = [1,3,7,6,4,3,9,10]
    a = int(num1) in l
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatornotin(request):
    param = {"action2": "operator" , "action1" :"notin","action" : "Check If A number Is Not In The List = [1,3,7,6,4,3,9,10]", "action3" : "Enter The Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1 not in n2)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatornotinresult(request):
    num1 = request.GET.get('num1','default')
    l = [1,3,7,6,4,3,9,10]
    a = int(num1) not in l
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorlnot(request):
    param = {"action2": "operator" , "action1" :"lnot","action" : "Find Logical Not Of A Number", "action3" : "Enter The Number ","action5":'''
n1 = int(input("Enter First Number : "))
print(not n1)
'''}
    return render(request, "python/inputforoperators1.html", param)


def operatorlnotresult(request):
    num1 = request.GET.get('num1','default')
    a = not int(num1) 
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorland(request):
    param = {"action2": "operator" , "action1" :"land","action" : "Find Logical And Of Two Numbers", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1 and n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorlandresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) and int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)


def operatorlor(request):
    param = {"action2": "operator" , "action1" :"lor","action" : "Find Logical Or Of Two Numbers", "action3" : "Enter First Number ", "action4" : "Enter Second Number","action5":'''
n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number : "))
print(n1 or n2)
'''}
    return render(request, "python/inputforoperators.html", param)

def operatorlorresult(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    a = int(num1) or int(num2)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorassopereq(request):
    param = {"action2": "operator" , "action1" :"assopereq","action" : "Assign A Number To a", "action3" : "Enter The Number ","action5":'''
x = 5
print(x)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatorassopereqresult(request):
    num1 = request.GET.get('num1','default')
    a = int(num1)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorassopereqpl(request):
    param = {"action2": "operator" , "action1" :"assopereqpl","action" : "Enter A Number To Addition Assign It To a = 3", "action3" : "Enter The Number ","action5":'''
x = int(input("Enter A Number : "))
a = 3
a += x
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatorassopereqplresult(request):
    num1 = request.GET.get('num1','default')
    a = 3
    a += int(num1)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorassopereqsu(request):
    param = {"action2": "operator" , "action1" :"assopereqsu","action" : "Enter A Number To Subtraction Assign It To a = 3", "action3" : "Enter The Number ","action5":'''
x = int(input("Enter A Number : "))
a = 3
a -= x
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatorassopereqsuresult(request):
    num1 = request.GET.get('num1','default')
    a = 3
    a -= int(num1)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorassopereqmu(request):
    param = {"action2": "operator" , "action1" :"assopereqmu","action" : "Enter A Number To Multiplication Assign It To a = 3", "action3" : "Enter The Number ","action5":'''
x = int(input("Enter A Number : "))
a = 3
a *= x
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatorassopereqmuresult(request):
    num1 = request.GET.get('num1','default')
    a = 3
    a *= int(num1)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def operatorassopereqdi(request):
    param = {"action2": "operator" , "action1" :"assopereqdi","action" : "Enter A Number To Division Assign It To a = 3", "action3" : "Enter The Number ","action5":'''
x = int(input("Enter A Number : "))
a = 3
a /= x
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def operatorassopereqdiresult(request):
    num1 = request.GET.get('num1','default')
    a = 3
    a /= int(num1)
    param = {"result" : a}
    return render(request, "python/output.html", param)
    
def con(request):
    return render(request, "python/ifelsehome.html")

def conex1(request):
    param = {"action2": "con" , "action1" :"ex1","action" : "Check If You Are Eligible For Driving License", "action3" : "Enter Your Age", "action5" : '''
n = int(input("Enter A Number"))
if (n>=18):
    a = 'You Are Eligible For A Driving License.'
else:
    a = 'You Are Not Eligible For A Driving License.'
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def conex1result(request):
    num1 = request.GET.get('num1','default')
    if(int(num1)>=18):
        a = 'You Are Eligible For A Driving License.'
    else:
        a = 'You Are Not Eligible For A Driving License.'
    param = {"result" : a}
    return render(request, "python/output.html", param)

def conex2(request):
    param = {"action2": "con" , "action1" :"ex2","action" : "Check If You Are Accountable To Pay Tax Or Not(Min. Salary Per Year Is 12,00,000)", "action3" : "Enter Your Monthly Income", "action5" :'''
n = int(input("Enter A Number : " ))
if(12*int(n)>=1200000):
    a = 'You Have To Pay Income Tax'
else:
    a = 'You Do Not Have To Pay Income Tax.'
print(a)             '''}
    return render(request, "python/inputforoperators1.html", param) 

def conex2result(request):
    num1 = request.GET.get('num1','default')
    if(12*int(num1)>=1200000):
        a = 'You Have To Pay Income Tax'
    else:
        a = 'You Do Not Have To Pay Income Tax.'
    param = {"result" : a}
    return render(request, "python/output.html", param)

def conex3(request):
    param = {"action2": "con" , "action1" :"ex3","action" : "Check If You Are Eligible For A Discount Or Not(Min Shopping Cart Must Be 2000.)", "action3" : "Enter Total Price Of Shopping Cart", "action5" : '''
n = int(input("Enter A Number : " ))
if(n>=2000):
    a = 'You Are Eligible For A Discount'
else:
    a = 'You Are Not Eligible For A Discount.'
print(a)
             '''}
    return render(request, "python/inputforoperators1.html", param)

def conex3result(request):
    num1 = request.GET.get('num1','default')
    if(int(num1)>=2000):
        a = 'You Are Eligible For A Discount'
    else:
        a = 'You Are Not Eligible For A Discount.'
    param = {"result" : a}
    return render(request, "python/output.html", param)

def conex4(request):
    param = {"action2": "con" , "action1" :"ex4","action" : "Check Your Height Category", "action3" : "Enter Your Height In Centimeters", "action5" : '''
n = int(input("Enter A Number : " ))
if(n>2000):
    a = 'You Are A Titan'
elif(n>200):
    a = 'You Are Too Tall'
elif(n>180):
    a = 'You Are Tall'
elif(n>150):
    a = 'You Have An Average Height'
else:
    a = 'You Must Be Hard To Find From Above'
print(a)
             '''}
    return render(request, "python/inputforoperators1.html", param)

def conex4result(request):
    num1 = request.GET.get('num1','default')
    if(int(num1)>2000):
        a = 'You Are A Titan'
    elif(int(num1)>200):
        a = 'You Are Too Tall'
    elif(int(num1)>180):
        a = 'You Are Tall'
    elif(int(num1)>150):
        a = 'You Have An Average Height'
    else:
        a = 'You Must Be Hard To Find From Above'
    param = {"result" : a}
    return render(request, "python/output.html", param)

def conex5(request):
    param = {"action2": "con" , "action1" :"ex5","action" : "Check If You Are Eligible To Take Admission In The College", "action3" : "Enter Marks Out Of 300", "action5" : '''
n = int(input("Enter Marks : " ))
if(n>300):
    a = 'You Are Hallucinating'
elif(n>280):
    a = 'You Should Not Be Bothered About Not Getting Admission'
elif(n>250):
    a = 'You Will Get Admission In Top Branch Easily'
elif(n>200):
    a = 'Maybe Be A Competition For Top Branch But You Will Still Get Admission'
elif(n>150):
    a = 'You Will Atleast Get The Lowest Branch'
elif(n>120):
    a = 'You Still Have Chances To Get Addmision But Too Much Competitive In This Range'
else:
    a = 'Better Luck Next Time Probably'
print(a)
             '''}
    return render(request, "python/inputforoperators1.html", param)

def conex5result(request):
    num1 = request.GET.get('num1','default')
    if(int(num1)>300):
        a = 'You Are Hallucinating'
    elif(int(num1)>280):
        a = 'You Should Not Be Bothered About Not Getting Admission'
    elif(int(num1)>250):
        a = 'You Will Get Admission In Top Branch Easily'
    elif(int(num1)>200):
        a = 'Maybe Be A Competition For Top Branch But You Will Still Get Admission'
    elif(int(num1)>150):
        a = 'You Will Atleast Get The Lowest Branch'
    elif(int(num1)>120):
        a = 'You Still Have Chances To Get Addmision But Too Much Competitive In This Range'
    else:
        a = 'Better Luck Next Time Probably'
    param = {"result" : a}
    return render(request, "python/output.html", param)

def loop(request):
    return render(request , "python/loophome.html")

def loopex1(request):
    param = {"action2": "loop" , "action1" :"ex1","action" : "Print Table Of A Number", "action3" : "Enter The Number", "action5" : '''
n = int(input("Enter Marks : " ))
for i in range(1, 11):
    print(n*i)
'''}
    return render(request, "python/inputforoperators1.html", param)

def loopex1result(request):
    num = request.GET.get('num1','default')
    num1 = int(num)
    a = ""
    for i in range(1, 11):
        a = a + f"{num1} x {i} = {num1*i}"
        a = a + "\n"
    param = {"result" : a}
    return render(request, "python/outputforloops.html", param)

def loopex2(request):
    param = {"action2": "loop" , "action1" :"ex2","action" : "Enter Rows And Columns Of Star Pattern", "action3" : "Enter The Number Of Rows" , "action4" : "Enter The Number Of Columns","action5":'''
i = int(input("Enter Number Of Rows : " ))
j = int(input("Enter Number Of Columns : " ))
c = ""
for a in range(0, i):
    for b in range(0,j):
        c = c +"* "
    c = c + "\n"
print(c)
'''}
    return render(request, "python/inputforoperators.html", param)

def loopex2result(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    i = int(num1)
    j = int(num2)
    c = ""
    for a in range(0, i):
        for b in range(0,j):
            c = c+"* "
        c = c+"\n"
    param = {"result" : c}
    return render(request, "python/outputforloops.html", param)

def loopex3(request):
    param = {"action2": "loop" , "action1" :"ex3","action" : "Find Sum Of First n Numbers", "action3" : "Enter The Value Of n","action3":'''
n = int(input("Enter A Number : " ))
a = 0
for i in range(1,n+1 ):
    a = a +i
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def loopex3result(request):
    num = request.GET.get('num1','default')
    n = int(num)
    a = 0
    for i in range(1,n+1 ):
        a = a +i
    param = {"result" : a}
    return render(request, "python/outputforloops.html", param)

def loopex4(request):
    param = {"action2": "loop" , "action1" :"ex4","action" : "Make Pattern Of A Number", "action3" : "Enter The Number", "action5":'''
n = int(input("Enter A Number : " ))
i = 1
a = ""
while i <= n:
    j = 1
    while j <= i:
        a = a + f"{j}"
        a = a + " "
        j += 1
    a = a +"\n"
    i += 1
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def loopex4result(request):
    num = request.GET.get('num1','default')
    n = int(num)
    i = 1
    a = ""
    while i <= n:
        j = 1
        while j <= i:
            a = a + f"{j}"
            a = a + " "
            j += 1
        a = a +"\n"
        i += 1
    param = {"result" : a}
    return render(request, "python/outputforloops.html", param)

def loopex5(request):
    param = {"action2": "loop" , "action1" :"ex5","action" : "Check Number Of  Digits In A Number", "action3" : "Enter The Number", "action5":'''
n = int(input("Enter A Number : " ))
for n in range(1, n + 1):
    h = n
    c = 0
    while h > 0:
        h //= 10
        c = c +  1
print(c)
'''}
    return render(request, "python/inputforoperators1.html", param)

def loopex5result(request):
    num = request.GET.get('num1','default')
    n = int(num)
    a = ""
    for n in range(1, n + 1):
        h = n
        c = 0
        while h > 0:
            h //= 10
            c = c +  1

    a = f"{n} has {c} digits"
    param = {"result" : a}
    return render(request, "python/outputforloops.html", param)

def func(request):
    return render(request , "python/funchome.html")

def funcex1(request):
    param = {"action2": "func" , "action1" :"ex1","action" : "Get Area Of A Rectangle", "action3" : "Enter The Length Of The Rectangle", "action4" : "Enter The Width Of The Rectangle","action5":'''
l = int(input("Enter Length : " ))
b = int(input("Enter Breadth : " ))
def area(a,b):
    global c
    c = a*b
area(l,b)
print(c)
'''}
    return render(request, "python/inputforoperators.html", param)

def funcex1result(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    l = int(num1)
    b = int(num2)
    def area(a,b):
        global c
        c = a*b
    area(l,b)
    param = {"result" : c}
    return render(request, "python/outputforloops.html", param)

def funcex2(request):
    param = {"action2": "func" , "action1" :"ex2","action" : "Enter The Details", "action3" : "Enter Your Name", "action4" : "Enter Your Age","action5":'''
name = input("Enter Your Name : ")
age = int(input("Enetr Your Age : "))
c= ""
def details(age):
    global d
    if age>=18:
         d = "You Can Get A Driving License"
    else:
        d = "You Can Not Get A Driving License"
details(age)
c = f"Hi {name}, You Are {age} Years Old So, {d}"
print(c)
'''}
    return render(request, "python/inputforoperators.html", param)

def funcex2result(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    b = int(num2)
    def details(name,age):
        global c
        if age>=18:
            d = "You Can Get A Driving License"
        else:
            d = "You Can Not Get A Driving License"
        c = f"Hi {name}, You Are {age} Years Old So, {d}"
    details(name = num1,age = b)
    param = {"result" : c}
    return render(request, "python/outputforloops.html", param)

def funcex3(request):
    param = {"action2": "func" , "action1" :"ex3","action" : "Enter Some Numbers Separated By Commas", "action3" : "Enter Your Name", "action5" : '''
num1 = input("Enter Numbers Separated by Commas : ")
s = num1.split(",")
def summation(*s):
    summ = 0
    for num in s:
        summ = int(num) + summ
    return summ
a = summation(*s)
print(a)

'''}
    return render(request, "python/inputforoperators1.html", param)

def funcex3result(request):
    num1 = request.GET.get('num1','default')
    s = num1.split(",")
    def summation(*s):
        summ = 0
        for num in s:
            summ = int(num) + summ
        return summ
    a = summation(*s)
    param = {"result" : a}
    return render(request, "python/outputforloops.html", param)

def funcex4(request):
    param = {"action2": "func" , "action1" :"ex4","action" : "Enter Some Numbers Separated By Commas", "action3" : "Enter Your Name", "action5" :'''
num1 = input("Enter Three Numbers Separated by Commas : ")
s = num1.split(",")
def Max(a,b,c):
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    return max(a,b,c)
a = Max(*s)
print(a)

'''}
    return render(request, "python/inputforoperators1.html", param)

def funcex4result(request):
    num1 = request.GET.get('num1','default')
    s = num1.split(",")
    def Max(a,b,c):
        a = int(s[0])
        b = int(s[1])
        c = int(s[2])
        return max(a,b,c)
    a = Max(*s)
    param = {"result" : a}
    return render(request, "python/outputforloops.html", param)

def funcex5(request):
    param = {"action2": "func" , "action1" :"ex5","action" : "Calculate Simple Interest For 5 Years", "action3" : "Enter Principal Amount", "action4" : "Enter Rate","action5":'''
p = int(input("Enter Principal Amount : "))
r = int(input("Enter Rate : "))
def interest(a,b):
    print(a,b)
    return (a*b*5)/100
a = interest(p , b = r)
print(a)
'''}
    return render(request, "python/inputforoperators.html", param)

def funcex5result(request):
    num1 = request.GET.get('num1','default')
    num2 = request.GET.get('num2','default')
    p = int(num1)
    r = int(num2)
    def interest(a,b):
        print(a,b)
        return (a*b*5)/100
    a = interest(p , b = r)
    param = {"result" : a}
    return render(request, "python/outputforloops.html", param)

def rec(request):
    return render(request , "python/rec.html")

def recex1(request):
    param = {"action2": "rec" , "action1" :"ex1","action" : "Enter A Number Whose Factorial You Want", "action3" : "Enter A Number","action5":'''
f = int(input("Enter The Number : "))
def factorial(f):
        if f  == 0:
            return 1
        return f * factorial(f-1)
a = factorial(f)
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def recex1result(request):
    num1 = request.GET.get('num1','default')
    f = int(num1)
    def factorial(f):
            if f  == 0:
                  return 1
            return f * factorial(f-1)
    a = factorial(f)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def recex2(request):
    param = {"action2": "rec" , "action1" :"ex2","action" : "Check If A Number Is Even Or Not", "action3" : "Enter A Number","action5":'''
n = int(input("Enter A Number : "))
def is_even(n):
    if n == 0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n == 0:
        return False
    return is_even(n-1)
a= is_even(n)
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def recex2result(request):
    num1 = request.GET.get('num1','default')
    n = int(num1)
    def is_even(n):
        if n == 0:
            return True
        return is_odd(n-1)

    def is_odd(n):
        if n == 0:
            return False
        return is_even(n-1)
    a= is_even(n)
    param = {"result" : a}
    return render(request, "python/output.html", param)

def recex3(request):
    param = {"action2": "rec" , "action1" :"ex3","action" : "Print Numbers From n To 1", "action3" : "Enter A Number","action5":'''
n = int(input("Enter A Number : "))
a = ""
def print_numbers(n):
    global a
    if n == 0:
        return
    a =  a + str(n) + "\n"
    print_numbers(n-1)
print_numbers(n) 
print(a)
'''}
    return render(request, "python/inputforoperators1.html", param)

def recex3result(request):
    num1 = request.GET.get('num1','default')
    n = int(num1)
    a = ""
    def print_numbers(n):
        nonlocal a
        if n == 0:
            return
        a =  a + str(n) + "\n"
        print_numbers(n-1)
    print_numbers(n) 
    param = {"result" : a}
    return render(request, "python/outputforloops.html", param)
        
def recex4(request):
    param = {"action2": "rec" , "action1" :"ex4","action" : "Print Numbers From 1 To n", "action3" : "Enter A Number","acton5":'''
             n = int(input("Enter A Number : "))
num = 1
a = ""
def print_numbers():
    global n
    global a
    global num
    if num>n:
        return
    a =  a + str(num) + "\n"
    num += 1
    print_numbers()
print_numbers()
print(a)'''}
    return render(request, "python/inputforoperators1.html", param)

def recex4result(request):
    num1 = request.GET.get('num1','default')
    n = int(num1)
    num = 1
    a = ""
    def print_numbers():
        nonlocal n
        nonlocal a
        nonlocal num
        if num>n:
            return
        a =  a + str(num) + "\n"
        num += 1
        print_numbers()
    print_numbers()
    param = {"result" : a}
    return render(request, "python/outputforloops.html", param)

def recex5(request):
    param = {
        "action2": "rec","action1": "ex5","action": "Print Fibonacci Series Till n Numbers Given By The User","action3": "Enter Number Of Terms","action5":'''
n = int(input("Enter A Number : "))
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
a = []
for i in range(n):
    a.append(str(fib(i)))
print("\n".join(a))
'''
    }
    return render(request, "python/inputforoperators1.html", param)


def recex5result(request):
    num1 = request.GET.get('num1', 'default')
    n = int(num1)
    def fib(n):
        if n <= 1:
            return n
        return fib(n-1) + fib(n-2)   
    a = ""
    for i in range(n):
        a = a + str(fib(i)) + "\n"
    param = {"result": a}
    return render(request, "python/outputforloops.html", param)

def cred(request):
    return render(request, "python/credits.html")