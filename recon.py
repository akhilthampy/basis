import os
a=(input("enter the domain url :- "))
cmd = 'echo ',a+ '|subfinder | httpx |nuclei -t nuclei-templates'
c=os.popen(cmd)
d=c.read()
print(d)
