import re, requests

with open("word-list-raw.txt", "r") as f:
  for line in f:
    word = re.sub(r'\W+', '', line)
    r = requests.get(f'https://rdap.donuts.co/rdap/domain/{word}.email')
    if int(r.status_code) == 404:
        f = open("output.txt", "a")
        f.write(f"{word}.email\n")
        f.close()
    else:
        print(r.status_code)
    

