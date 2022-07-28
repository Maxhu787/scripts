import urllib.request
import urllib.parse
import urllib.error
import json
url = input("Enter location: ")
print("Retrieving " + url)
fhand = urllib.request.urlopen(url)
data = fhand.read()
info = json.loads(data)
print("Retrieved " + "0" + " characters")
count = 0
for item in info["comments"]:
    count += int(item["count"])
print(count)