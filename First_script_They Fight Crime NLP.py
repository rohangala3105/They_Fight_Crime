from selenium import webdriver
import glob#The credentials file has two functions getusername() and getpassword() returning username and password repectively
import credentials

#url to the Canvas->Financial Technology->Discussions->TFC Character Submissions
url = 'https://sit.instructure.com/courses/30002/discussion_topics/126409'

#Setting up chromedriver for the dowload file locations
driver = webdriver.Chrome('chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
prefs = { 'download.default_directory': 'E:/Stevens/FE-595/FE-595-They-Fight-Crime-NLP-master/Final' }
chrome_options.add_experimental_option('prefs', prefs)
driver.close()

driver = webdriver.Chrome(chrome_options=chrome_options)

#getting the url
driver.get(url)

#getting credentials from the credentials python file
username = driver.find_element_by_id("username").send_keys(credentials.getusername())
password = driver.find_element_by_id("password").send_keys(credentials.getpassword())
driver.find_element_by_css_selector('button').click()

#downloading the files
for i in driver.find_elements_by_class_name('comment_attachments'):
    i.find_element_by_css_selector("a").click()


driver.close()
#Merging all of the various files from people posted on the discussion board into a single file

read_files = glob.glob("*.txt")
read_files.extend(glob.glob('*.csv'))
print(read_files)
with open("merged.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
