__author__ = 'amirjaffari'


import urllib2
import json
import urllib2
from selenium import webdriver
import uuid
import os
import csv



filePathName = raw_input("Drop the file here :")
print str(filePathName)
folderPathName = raw_input("Drop the destination folder here :")


def fullContactCollect(email):

    api_key = ""
    fullURL = "https://api.fullcontact.com/v2/person.json?apiKey=" + api_key +"&email=" + email
    print fullURL
    try:
        loadURL = urllib2.urlopen(fullURL)
        jsonData = json.load(loadURL)

        photos = jsonData['photos']

        count = 0

        for item in photos:                             #For each item with key Photo in Json use Selenium to screenshot that url
            browser = webdriver.Firefox()
            imageurl =  item['url']
            browser.get(imageurl)
            folderpath = str(folderPathName)
            browser.save_screenshot(folderpath + "/"  + (email)+".png")
            browser.quit();
            count = count +1
            counter = str(count)
            print "GOT" + counter + "pictures so far"
            os.system("afplay sound.wav")
            return count


        #                                                 #For each item with key SocialMedia in Json use Selenium to screenshot that profile
        # facebook = jsonData['url']
        # social =jsonData['typeName']
        #
        # for item in facebook:
        #     browser = webdriver.Firefox()
        #     profileurl =  item['url']
        #     browser.get(profileurl)
        #     #os.chdir(save_path)                         #For each item with key SocialMedia in Json use Selenium to screenshot that profile
        #     unique_filename = uuid.uuid4()
        #     print str(email)
        #     folderpath = str(folderPathName)
        #     browser.save_screenshot(folderpath + "/" + str(email) + ".png")
        #     browser.quit();

            print unique_filename
            print "done"
    except urllib2.URLError, e:
        print "Bad URL", e
    except KeyError:
        print "Doesn't have a picture"
        pass


ifile= open(str(filePathName),'rU')

x=0

for row in ifile:
    x = x + 1
    numbers = str(x)
    print "scanning email # " + numbers + "...."
    print row
    fullContactCollect(row)



