#Make this url output the following:
# Youtube
# Google
# Facebook

starter = "https://youtube.com,https://google.com,https://facebook.com"

new = starter.split(",")
def myfunction(collection):
    for site in collection:
        one = site.lstrip("https://")
        two = one.rstrip(".com")
        three = two.capitalize()
        print(three)

myfunction(new)


