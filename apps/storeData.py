import cgi, cgitb
import mysql.connector
cgitb.enable()

data = cgi.FieldStorage()

mydb = mysql.connector.connect(host="localhost", user="katekhova", 
  password="@8=PF3s1U^I-H4l#", database="mydatabase")
mycursor = mydb.cursor()

sql = "INSERT INTO wp2data (email) VALUES (%s)"
email=""
if len(data)==1:
  email = data["email"].value
val = (email, )
mycursor.execute(sql, val)
mydb.commit()

url = "../files/send.zip"

print('Content-Type:text/html')
print('\n')
print('<html><body>\
<a id="do" href="%s" download="application.zip">do</a>\
<script>document.getElementById("do").click();</script>\
</body></html>' %url)
