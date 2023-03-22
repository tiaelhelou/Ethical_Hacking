# Ethical Hacking Project:

### Description:

This project is about creating a Python script that can be run on a website to discover subdomains, directories and files. This script will reveal hidden links that may lead to pages with vulnerabilities. Inaddition to that, it also use regular expressions to extract links from the HTML file.

### Steps Taken To Complete The Project:

- Install requests to use it for url
- Import requests, sys (to read arg), re (regex)
- Defined 3 functions to check reachable subdomains, directories and files
- Read subdomains and directories from subdomains_dictionary.bat and dirs_dictionary.bat, then started checking each combination if it exists or reacchable and then write results to subdomains_output.bat anf directories_output.bat ( same for files )
- Parsed html of the url and used Regex to extract all links

### How To Run:
-
      git clone https://github.com/tiaelhelou/Ethical_Hacking.git
      
- 
      cd Ethical_Hacking
      
- 
      pip install requests
      
- 
      pip install pycurl
      
- 
      python hack.py url
      

    
    
    
