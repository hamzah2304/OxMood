from selenium import webdriver
from time import sleep
import re
import json

class scraperrr:

    def __init__(self, email, password):

        self.email = email
        self.password = password

        # options for web browser object
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(options=options)
        self._login()

    def _login(self):
        self.browser.get('https://www.facebook.com/')
        self.browser.implicitly_wait(5)

        annoyingButton = self.browser.find_element_by_xpath("//button[text()='Accept All']")
        annoyingButton.click()
        username_input = self.browser.find_element_by_css_selector("input[name='email']")
        password_input = self.browser.find_element_by_css_selector("input[name='pass']")

        username_input.send_keys(self.email)
        password_input.send_keys(self.password)

        login_button = self.browser.find_element_by_xpath("//button[text()='Log In']")
        login_button.click()

        sleep(5)

    # time limit in milliseconds
    # data will be in the format:
    # [{ 'Initials': initials,
    #    'College': college,
    #    'DateOfPost': date of post in UTC,
    #    'Hashtag': hashtag,
    #    'Content': content,
    #    'NameOfPage': name of page,
    #    'NumberOfLikes': number of likes }]
    def scrap3Page(self, scrapeCap, url, filename):

        self.browser.get(url)
        saveFile = open(f"{filename}.txt", "w")

        postsScraped = 0
        scrapedData = []
        while postsScraped < scrapeCap:
            #mainDiv = self.browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[@class="k4urcfbm"]')
            posts = self.browser.find_elements_by_xpath('//div[@role="main"]//div[@role="main"]/div/div/div[@class="du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"]')
            '''
            posts = []
            for element in mainDivs:
                posts += element.find_elements_by_xpath("./*")
            '''
            for post in posts[postsScraped:]:
                print(f"[{postsScraped}/{scrapeCap}]")
                try:
                    content = post.text.split("\n")
                    hashtag = content[3]
                    #print(post.find_element_by_xpath(".//div").get_attribute("innerHTML"))
                    #text = post.find_element_by_xpath(".//div//div[@class='o9v6fnle cxmmr5t8 oygrvhab hcukyx3x c1et5uql']").text
                    text = content[4]
                    count = 5
                    regex = "[1-9]+"
                    checker = re.compile(regex)
                    while not checker.match(content[count]):
                        text += content[count]
                        count += 1
                    initialsAndCollege = self.getInitialsAndCollege(text=text)
                    dateOfPost = content[1]
                    pagename = content[0]
                    newRecord = {
                        "Initials": initialsAndCollege[0],
                        "College": initialsAndCollege[1],
                        "DateOfPost": dateOfPost,
                        "Hashtag": hashtag,
                        "Content": text,
                        "NameOfPage": pagename,
                    }
                    if newRecord not in scrapedData:
                        scrapedData.append(newRecord)
                        saveFile.write((json.dumps(newRecord)+"\n"))
                    postsScraped += 1
                except Exception as exception:
                    print("bad formatting but we gucci")
                    print(exception)

            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return scrapedData

    def getInitialsAndCollege(self, text):
        regex = "[A-Z\-]+ ?@ ?[A-Z]+"
        checker = re.compile(regex)
        try:
            initialsAndCollege = checker.findall(text)[0]
            regex = "[A-Z\-]+"
            checker = re.compile(regex)
            initials = checker.findall(initialsAndCollege)[0]
            regex = "@ ?[A-Z]+"
            checker = re.compile(regex)
            college = checker.findall(initialsAndCollege)[0]
            college = college.replace("@","")
            college = college.replace(" ", "")
            return [initials, college]
        except:
            return ["N/A", "N/A"]



myMan = scraperrr(email="xecuteorda66@gmail.com", password="HelloThere66")
records = myMan.scrap3Page(scrapeCap=13271, url="https://www.facebook.com/oxlovethethird", filename="Oxlove3")