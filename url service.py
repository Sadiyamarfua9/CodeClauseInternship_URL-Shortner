import pyshorteners
long_url=input("Enter long URL here: ")
short_url=pyshorteners.Shortener()
x=short_url.tinyurl.short(long_url)
print("The shortened url is:",x)


