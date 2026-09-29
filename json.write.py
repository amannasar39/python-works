f=open("data.jason","a")



import json

content=[
    {'name':'amal','age':21},
    {'name':'arun','age':22}
]


import json
json.dump(content,f)
f.close()