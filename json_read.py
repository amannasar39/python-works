import json
f=open("data.jason","r")
content=json.load(f)
# content=f.read()
print(content)
f.close()