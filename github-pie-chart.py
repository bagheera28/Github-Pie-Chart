from collections import OrderedDict
import json
import matplotlib.pyplot as plt
import github3

token_file = "token.txt"
repositories = []
languages = {}

with open(token_file) as f:
        my_token = f.read()

#Get repository list
gh = github3.login(token = my_token)

for repo in gh.repositories(type='owner'):
    for l in repo.languages():
        if l[0] not in languages:
            languages[l[0]] = l[1]
            
        else:
            languages[l[0]] += l[1]

languages = dict(OrderedDict(sorted(languages.items())))

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
