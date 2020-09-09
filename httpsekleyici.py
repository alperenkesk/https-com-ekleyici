url_file = open("urls.txt")
urls = url_file.readlines()

new_url_file = open("new_urls.txt", "w")

for url in urls:
    url = "https://" + url
    new_url_file.write(url)
