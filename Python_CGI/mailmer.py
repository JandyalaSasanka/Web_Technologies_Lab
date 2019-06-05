import imaplib
import csv
import email
import time

srv = imaplib.IMAP4_SSL("imap.gmail.com")
srv.login('jandyala.sasanka@gmail.com', 'Sbablu619')
srv.select('[Gmail]/Drafts')

def send_m(first_name, address):
  message = email.message_from_string("""To: %s
Subject: Regarding WTLab Record
Dear %s,

you are not maintaining record properly try to paste the colour prints otherwise will cut down marks
""" % (address, first_name))
  srv.append("[Gmail]/Drafts",
              '',
              imaplib.Time2Internaldate(time.time()),
              str(message))

csvreader = csv.reader(open("contacts1.csv"))
for row in csvreader:
  first = row[0]
  print ("first="+first)
  full = row[0] + " " + row[1] 
  print ("full="+full)
  addresses =  [row[2]]
  print (addresses)
  

  a = " ".join(map( lambda x: "%s <%s>" % (full, x), addresses))
  print (first, a)
  send_m(first, a)
  time.sleep(1)
