# Install: pip install requests
import requests
import sys

import re

# Write to files
file1 = open(' subdomains_output.bat', 'w')
file2 = open('directories_output.bat', 'w')
file3 = open('files_output.bat', 'w')

# Check subdomain
def subdomain_checker(sub, url):
	try:
		# Get Url
		get = requests.get("http://"+sub+"."+url)
		# Check if the request succeeds 
		if get.status_code == 200:
			file1.writelines("http://"+sub+"."+url+": is reachable \n")
		else:
			file1.writelines("http://"+sub+"."+url+": is Not reachable\n")

	# Exception
	except requests.exceptions.RequestException as e:
        # Continue
		pass

# Check domain
def domain_checker(dom, url):
	try:
		# Get Url
		get = requests.get("http://"+url+"/"+dom+"/")
		# Check if the request succeeds 
		if get.status_code == 200:
			file2.writelines("http://"+url+"/"+dom+"/: is reachable \n")
		else:
			file2.writelines("http://"+url+"/"+dom+"/: is Not reachable \n")

	# Exception
	except requests.exceptions.RequestException as e:
        # Continue
		pass

# Check files
def file_checker(file, url):
	try:
		# Get Url
		get = requests.get("http://"+url+"/"+file)
		# Check if the request succeeds 
		if get.status_code == 200:
			file3.writelines("http://"+url+"/"+file+": is reachable \n")
		else:
			file3.writelines("http://"+url+"/"+file+": is Not reachable \n")

	# Exception
	except requests.exceptions.RequestException as e:
        # Continue
		pass

# Get url
url = ""

if len(sys.argv) < 2:
    print("No url found")
else:
	url = sys.argv[1]

# Read from subdomains_dictionary.bat
with open('subdomains_dictionary.bat') as f:
    for line in f:
        pattern = r"^\S+$"
        sub = re.match(pattern, line)
        if sub:
        	subdomain_checker(sub, url)

# Read from dirs_dictionary.bat 
with open('dirs_dictionary.bat') as x:
    for line in x:
        pattern = r"^\S+$"
        dom = re.match(pattern, line)
        if dom:
        	domain_checker(dom, url)  
        
file_checker("user_passwords.txt", url)
    
# Parse html
try:
    # Get Url
	get = requests.get("http://"+url)
 
# Exception
except requests.exceptions.RequestException as e:
    # Continue
	pass

# Extract links
pattern = r"(?:<a\shref=(\w+)><//a>)"
lst = re.findall(pattern, get.text)

# Remove duplicates
links=[]
for i in lst:
    if i not in links:
        links.append(i)
print(links)