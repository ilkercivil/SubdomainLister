import requests

def make_requests(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_input= input("enter your target input")

with open ("subdomainlist.txt", "r") as subdomain_list:
    for word in subdomain_list:
        word=word.strip()
        print(word)
        url = "http://"+word + "." + target_input
        response=make_requests(url)
        if response:
            print("Found subdomin----->"+url)



