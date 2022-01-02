print(r"""                     
 ._   __/__  /._  _ 
// /_\ / /_|/// //_/
                 _/  
             
             https://github.com/akhilwrist                                               """)

import os
cmd = 'go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest&&go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest&&go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest'
c=os.popen(cmd)
d=c.read()
print(d)
