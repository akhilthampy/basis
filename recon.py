print(r"""   ___  _        __  _____  __  __    __  ___   ___    __ 
  / _ \/_\    /\ \ \/__   \/__\/__\  /__\/ __\ /___\/\ \ \
 / /_)//_\\  /  \/ /  / /\/_\ / \// /_\ / /   //  //  \/ /
/ ___/  _  \/ /\  /  / / //__/ _  \//__/ /___/ \_// /\  / 
\/   \_/ \_/\_\ \/   \/  \__/\/ \_/\__/\____/\___/\_\ \/  
             
             https://github.com/akhilwrist                                               """)

import os
a=(input("Enter the domain  :- "))
cmd = 'echo '+a+'|subfinder | httpx |nuclei -t nuclei-templates'
c=os.popen(cmd)
d=c.read()
print(d)
