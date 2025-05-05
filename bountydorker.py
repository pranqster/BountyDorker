import webbrowser
import urllib.parse

def logo():
	print ('\033[94m' + """

#############################################################
#                                                           #
#    _____             _       ____          _              #
#   | __  |___ _ _ ___| |_ _ _|    \ ___ ___| |_ ___ ___    #
#   | __ -| . | | |   |  _| | |  |  | . |  _| '_| -_|  _|   #
#   |_____|___|___|_|_|_| |_  |____/|___|_| |_,_|___|_|     #
#                         |___|                             #
#                                                           #
#############################################################
   
 By: pranqster - @pranqster@infosec.exchange  
 Github: https://github.com/pranqster/
                                                     
""" + '\033[00m')
logo()

def google_dorking(domain):
    dorks = [
        {"title": "Directory Listing", "query": "site:" + domain + " intitle:index.of"},
        {"title": "Configuration Files", "query": "site:" + domain + " ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini"},
        {"title": "Database Files", "query": "site:" + domain + " ext:sql | ext:dbf | ext:mdb"},
        {"title": "WordPress", "query": "site:" + domain + " inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download"},
        {"title": "Log Files", "query": "site:" + domain + " ext:log"},
        {"title": "Backup Files", "query": "site:" + domain + " ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"},
        {"title": "Login Pages", "query": "site:" + domain + " inurl:login | inurl:signin | intitle:Login | intitle: signin | inurl:auth"},
        {"title": "Public Documents", "query": "site:" + domain + " ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"},
        {"title": "phpinfo()", "query": "site:" + domain + " ext:php intitle:phpinfo \"published by the PHP Group\""},
        {"title": "Backdoors", "query": "site:" + domain + " inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor"},
        {"title": "Install/Setup Files", "query": "site:" + domain + " inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config"},
        {"title": "SQL Errors", "query": "site:" + domain + " intext:\"sql syntax near\" | intext:\"syntax error has occurred\" | intext:\"incorrect syntax near\" | intext:\"unexpected end of SQL command\" | intext:\"Warning: mysql_connect()\" | intext:\"Warning: mysql_query()\" | intext:\"Warning: pg_connect()\""},
        {"title": "Open Redirects", "query": "site:" + domain + " inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http"},
        {"title": "Apache Struts", "query": "site:" + domain + " ext:action | ext:struts | ext:do"},
        {"title": "Pastebin Entries", "query": "site:pastebin.com" + domain},
        {"title": "Robots.txt", "query": "site:" + domain + "/robots.txt"},
        {"title": "Sensitive Files", "query": "site:" + domain + " inurl:\"/phpinfo.php\" | inurl:\".htaccess\""}

    ]

    print("Select the dorks you want to use:")
    for i, dork in enumerate(dorks):
        print(f"{i+1}. {dork['title']}")

    selected_dorks = []
    while True:
        choice = input("Enter the number of the dork you want to use, or 'a' to use all, or 'd' to done: ")
        if choice.lower() == 'a':
            selected_dorks = dorks
            break
        elif choice.lower() == 'd':
            if not selected_dorks:
                print("Please select at least one dork.")
            else:
                break
        else:
            try:
                choice = int(choice)
                if choice < 1 or choice > len(dorks):
                    print("Invalid choice")
                else:
                    selected_dorks.append(dorks[choice - 1])
            except ValueError:
                print("Invalid choice")

    for dork in selected_dorks:
        url = "https://www.google.com/search?q=" + urllib.parse.quote(dork['query'])
        webbrowser.open(url)

domain = input("Enter the domain you want to scan: ")
google_dorking(domain)
