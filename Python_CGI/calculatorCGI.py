#!C:\Python37\python.exe

def calculator(a,b,op):
    if(op=='Addition'):
        print ("Addition of two numbers is :",int(a)+int(b))
    if(op=='Subtraction'):
        print ("Subtraction of two numbers is :",int(a)-int(b))
    if(op=='Multiplication'):
        print ("Multiplication of two numbers is :",int(a)*int(b)) 
    if(op=='Modulus'):
        print ("Modulus of two numbers is :",int(a)%int(b))
        


import cgi
print ("Content-type:text/html\n")
print ("<html>")
print ("<head> <title>042_My Second CGI program</title>")
print ("</head>")
print ("<body>")
form = cgi.FieldStorage()
a=form.getvalue("first")
b=form.getvalue("second")
op=form.getvalue("operation")
#!print ('<h1>Hello '+name+' Thanks for using my screen!</h1><br/>')
print ('<form method="post" action="calculator.py">')
print ('<p>Enter First Number: <input type="text" name="first"/></p>')
print ('<p>Enter Second Number: <input type="text" name="second"/></p>')
print ('<p>Select operation:</p><select name="operation"><option>Addition</option><option>Subtraction</option><option>Multiplication</option><option>Modulus</option></select>')
print ('<input type="submit" value="submit"/>')
print ('<br>')
print ('<br>')
print ("</body>")
print ("</html>")
print ("\n")

calculator(a,b,op)
