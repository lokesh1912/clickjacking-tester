from urllib.request import urlopen
from sys import argv, exit
import argparse


def check(url):
 
    try:
        if "http" not in url: 
            url = "http://" + url
        data = urlopen(url)
        headers = data.info()

        if not "X-Frame-Options" in headers: 
            return True

    except: 
        return False


def poc(url):


    code = """
<html>
   <head><title>Clickjack test page</title></head>
   <body>
     <p>Website is vulnerable to Clickjacking!</p>
     <iframe src="{}" width="500" height="500"></iframe>
   </body>
</html>
    """.format(url)

    with open(url + ".html", "w") as f:
        f.write(code)
        f.close()



   

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--site")
args = parser.parse_args()

argv = vars(args)
p = argv['site']
print("\n[*] Checking " )
status = check(p)

if status:
    print("     [+] Website is vulnerable to Clickjacking!")
    poc(p.split('\n')[0])
    print("     [+] Created a poc and saved as {}.html".format(p))

else : print("      [+] Website is not vulnerable to Clickjacking!")