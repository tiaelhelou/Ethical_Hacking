# should run: pip install requests
import requests
import sys

# pip install pycurl
import pycurl
from io import BytesIO

import re

file1 = open(' subdomains_output.bat', 'w')
file2 = open('directories_output.bat', 'w')
file3 = open('files_output.bat', 'w')

def subdomain_checker(sub, url):
	try:
		#Get Url
		get = requests.get("http://"+sub+"."+url)
		# if the request succeeds 
		if get.status_code == 200:
			file1.writelines("http://"+sub+"."+url+": is reachable \n")
		else:
			file1.writelines("http://"+sub+"."+url+": is Not reachable\n")

	#Exception
	except requests.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

def domain_checker(dom, url):
	try:
		#Get Url
		get = requests.get("http://"+url+"/"+dom+"/")
		# if the request succeeds 
		if get.status_code == 200:
			file2.writelines("http://"+url+"/"+dom+"/: is reachable \n")
		else:
			file2.writelines("http://"+url+"/"+dom+"/: is Not reachable \n")

	#Exception
	except requests.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

def file_checker(file, url):
	try:
		#Get Url
		get = requests.get("http://"+url+"/"+file)
		# if the request succeeds 
		if get.status_code == 200:
			file3.writelines("http://"+url+"/"+file+": is reachable \n")
		else:
			file3.writelines("http://"+url+"/"+file+": is Not reachable \n")

	#Exception
	except requests.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(f"{url}: is Not reachable \nErr: {e}")


url = sys.argv[1]

with open('subdomains_dictionary.bat') as f:
    for line in f:
        subdomain_checker(line.strip())

with open('dirs_dictionary.bat') as x:
    for line in x:
        domain_checker(line.strip(), url)  
        
b_obj = BytesIO()
crl = pycurl.Curl()
crl.setopt(crl.URL,'https://'+url)
crl.setopt(crl.WRITEDATA, b_obj)
crl.perform()
crl.close()
get_body = b_obj.getvalue()
html_string = get_body.decode('utf8')

pattern = r"(?:<a\shref=(\w+)><//a>)"
lst = re.findall(pattern, html_string)

links=[]
for i in lst:
    if i not in links:
        links.append(i)
