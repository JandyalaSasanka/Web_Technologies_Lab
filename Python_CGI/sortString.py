#!C:\Python37\python.exe

def sortedSentence(a): 
    words = a.split(" ")  
    words.sort()  
    newSentence = " ".join(words)  
    return newSentence 

import cgi
print ("Content-type:text/html\n")
print ("<html>")
print ("<head> <title>042_My First CGI program</title>")
print ("</head>")
print ("<body>")
form = cgi.FieldStorage()
a=form.getvalue("String")
#!print ('<h1>Hello '+name+' Thanks for using my screen!</h1><br/>')
print ('<form method="post" action="sort.py">')
print ('<p>Enter String to sort: <input type="text" name="String"/></p>')
print ('<input type="submit" value="submit"/>')
print ('<br>')
print ('<br>')
print ("</body>")
print ("</html>")
print ("\n")

print(sortedSentence(a))
