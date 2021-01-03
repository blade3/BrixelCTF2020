#/usr/bin/python3
from timeit import default_timer as timer
import urllib3
import requests

# Are you fast enough?10
#Can you program something that is fast enough to submit the solution before the time runs out?
#http://timesink.be/speedy
pageHTTP  = "http://timesink.be/speedy/"
pagePOST = "http://timesink.be/speedy/"

## after clicked on the link, We saw the code was between the following HTML tag with unique ID:
# <div id="rndstring" align="center">[theCode]</div>
preCode="<div id=\"rndstring\" align=\"center\">"
postCode="</div>"
preCode_len=len(preCode)
start = timer()
# Connecting to the page to retrieve code:
with requests.Session() as s:
    page = s.get(pageHTTP).text

    # we'll try to find the real code by srink html before and after:
    pos=page.index(preCode)

    word = page[pos+preCode_len:page.index(postCode,pos+preCode_len)].strip()
    # submit the word
    data = {"rndstring":word,"randomstring":word,"inputfield":word,"submit":"enter"}
    flagPage = s.post(pageHTTP, data = data)
    end = timer()
    
print("page:")
print(page)
print('\n\n')
print('word found:',word)

print("result page:")
print(flagPage.text)
print('\n')
print('times: ', end-start)

print('data sent on post:',data)