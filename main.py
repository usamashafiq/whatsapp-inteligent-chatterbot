from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import spacy
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

spacy.load('en')

chat = ChatBot('chat',
               read_only=False,
               logic_adapters=["chatterbot.logic.BestMatch"],
               storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ListTrainer(chat)

# Training chat
# training from corpus
corpus_tranier = ChatterBotCorpusTrainer(chat)
corpus_tranier.train("chatterbot.corpus.english")
current_Time = datetime.datetime.now()
# save the QR code Scan one time QR Code then save until logout
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\HafizUsama\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
options.add_argument('--profile-directory=Default')
try:
    # Register the drive
    chrome_browser = webdriver.Chrome(executable_path='C:\chromedriver', options=options)
    chrome_browser.get('https://web.whatsapp.com/')
    # Sleep to scan the QR Code
    time.sleep(15)
    # selected username
    user_name = 'Usama Mine'

    while True:
        time.sleep(2)
        try:

            # only DMs and no group messages by checking mute icon.
            unreadMsgs = chrome_browser.find_elements_by_xpath(
                "/html/body/div/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[2]/div["
                "2]/span[ "
                "1]/div/span")

            print(len(unreadMsgs))
            if int((len(unreadMsgs))) == 1:
                # Select  the title having user name

                user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
                user.click()
                # read the client massege
                msg_got = chrome_browser.find_elements_by_css_selector(
                    'span._3-8er.selectable-text.copyable-text')
                msg = [message.text for message in msg_got]
                # read last msg
                print(msg[-1])
                response = chat.get_response(msg[-1])

                time.sleep(2)

                # Typing message into message box
                message_box = chrome_browser.find_element_by_xpath(
                    '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
                time.sleep(1)
                message_box.send_keys(str(response))
                time.sleep(1)
                # Click on send button

                message_box.send_keys(Keys.RETURN)
                time.sleep(2)
                chrome_browser.refresh()
                time.sleep(2)

            else:
                # browsre refresh
                chrome_browser.refresh()
                time.sleep(3)

        except:
            time.sleep(2)
            chrome_browser.refresh()
            print("no new massege")
            time.sleep(2)

except:
    chrome_browser.close()
    print("internet not working")
# send the attachment
# attachment_box = chrome_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[
# 4]/div[1]/footer/div[1]/div[1]/div[2]/div') attachment_box.click()
# image_box = chrome_browser.find_element_by_xpath( '//input[@accept="image/*,video/mp4,video/3gpp,
# video/quicktime"]') image_box.send_keys("C:\\Users\\HafizUsama\\OneDrive\\Pictures\\Screenshots\\Screenshot (
# 5).png") time.sleep(3) send_button = chrome_browser.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[2]/div[
# 2]/span/div[1]/span/div[1]/div/div[2]/span/div') send_button.click()
