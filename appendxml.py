import xml.etree.ElementTree as ET
import cgi, cgitb
import os

from datetime import date



form = cgi.FieldStorage()
id=0

Name = form.getvalue('sign_user')
num = form.getvalue('sign_Num')
email = form.getvalue('sign_Email')
pw = form.getvalue('sign_pw')

captcha_IN = form.getvalue('captcha_IN')
captcha_TEXT = form.getvalue('test')

if captcha_IN != captcha_TEXT:
    os.remove(captcha_TEXT + 'Captcha.png')
    print("Content-Type: text/html\n")
    print("<meta http-equiv='refresh' content=\"0;url=cap.py\" />")
    exit()



tree = ET.parse('customerOrders.xml')
root = tree.getroot()
for type_tag in tree.findall('customers'):
    id=id+1

b = ET.SubElement(root, 'customers')
custid = ET.SubElement(b, 'cid')
custid.text = str(id + 1)
custadd = ET.SubElement(b, 'address')
custadd.text = 'NULL'
custemail = ET.SubElement(b, 'email')
custemail.text = email
custnum = ET.SubElement(b, 'number')
custnum.text = num
dateregistered = ET.SubElement(b, 'date')
dateregistered.text = str(date.today())

b_xml=ET.tostring(root)

with open("customerOrders.xml", "wb") as f:
    f.write(b_xml)


os.remove(captcha_TEXT + 'Captcha.png')
print("Content-Type: text/html\n")
print("<meta http-equiv='refresh' content=\"0;url=loginPage.html\" />")