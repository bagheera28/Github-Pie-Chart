import urllib.request
import collections
import json
import matplotlib.pyplot as plt

username = "Educorreia932"
repositories = []
languages = {}

url = "https://api.github.com/users/" + username + "/repos"

#Get repository list
request = urllib.request.Request(url, headers = {'Accept': 'application/vnd.github.v3+json'})
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

false = False
true = True
null = None

temp = eval(content)

#Get urls to each repositories languages page
for i in range(len(temp)):
    repositories.append(temp[i]["languages_url"])
    
for repo_url in repositories:
    request = urllib.request.Request(repo_url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    
    temp = eval(content)
    
    for key in temp:
        if key not in languages:
            languages[key] = temp[key]
            
        else:
            languages[key] += temp[key]
    
languages = dict(collections.OrderedDict(sorted(languages.items())))

#Retrieve languages color
colors = []

with open("colors.json") as json_file:
    data = json.load(json_file)
    
    for language in data:
        if language in languages:
            colors.append(data[language]["color"])          
    
#Plot
labels = []
sizes = []

for language in languages.keys():
    labels.append(language)
    sizes.append(1000 * (languages[language] / sum(languages.values())))

plt.pie(sizes, labels = labels, colors = colors, autopct='%1.1f%%', shadow = False, startangle = 180)

plt.axis('equal')
plt.show()