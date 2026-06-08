# -----------------------------------------------------------------
## Python - Part 1
# What will the output be?


myList = [1,2,3]
max = len(myList)

i = 1
while i <= max:
    print(myList[i])
    i += 1



# -----------------------------------------------------------------
## Python - Part 2
# What does this function do


def mysteryFunction(items: list):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)



# -----------------------------------------------------------------
## Python - Part 3
# What issue does the following code have:


import myPackage

# The default number of times the function should retry failed events before giving up
retryLimit = 1

def sendFile(file, delay=0, retryCount=0):
    time.sleep(delay)

    if retryCount >= retryLimit:
		raise myPackage.ExhaustedRetryLimit

    try:
        myPackage.send_file_to_server(file)
    except:
        sendFile(file, delay+10, retryCount+1)

sendFile('/home/user/testFile.yaml')
