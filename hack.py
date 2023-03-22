# should run: pip install requests
import requests
import sys

file1 = open(' subdomains_output.bat', 'w')
file2 = open('directories_output.bat', 'w')

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


url = sys.argv[1]

with open('subdomains_dictionary.bat') as f:
    for line in f:
        subdomain_checker(line.strip())

with open('dirs_dictionary.bat') as x:
    for line in x:
        domain_checker(line.strip(), url)  