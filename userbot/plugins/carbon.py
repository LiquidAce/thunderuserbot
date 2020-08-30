# sed lyf
# Imports
from os import system as cmd
from time import sleep
from random import choice as r
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from userbot import CHROME_DRIVER
from userbot.utils import admin_cmd
from userbot import GOOGLE_CHROME_BIN
CARBONLANG = "auto"
LANG = "en"
Blue_Facts = ['🤡**Did U Know**\n\n🦖What is Nucleo bot username? [Nucleo](https://t.me/Nucleoofficial_bot)',
              '🤡**Did U Know**\n\n🦖[Nucleo support](https://t.me/Nucleosupport) Is The Support channel of NucleoBot!!',
              ]
bf = r(Blue_Facts)
def carbon_lago():
    logo = ('█▒█▒▒▒█▒▒█▒      ████      █▒▒▒▒▒▒▒▒█ ████████████ ▒█▒█▒█▒█▒ █▒      █\n'
            '█               █    █     █        █  █         █ █       ▒ ▒ ▒     █\n'
            '█              █      █    █        █  █         █ ▒       █ █  ▒    █\n'
            '█             █▒▒▒█▒▒▒▒█   ██████████  █▒▒▒██▒▒▒▒█ █       ▒ ▒   █   ▒\n'
            '█            █          █  ███         █         █ ▒       █ █    ▒  █\n'
            '█           █            █ █  ██       █         █ █       ▒ ▒     ▒ ▒\n'
            '████████████              ██    ██    ████████████ █████████ █      ██\n'
            '██████████████████████████████████████████████████████████████████████\n')
    print(f'{logo}')
@borg.on(admin_cmd("carbon")) # This Is The Command Recogniser , This Has Been Changed To Borg.on From Register
async def carbon_api(mytext):
    carbon_lago()
    if not mytext.text[0].isalpha() and mytext.text[0] not in ("/", "#", "@", "!"): # Checking For Alpha Or Not
        await mytext.edit('**Please wait**')
        CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
        global CARBONLANG
        textx = await mytext.get_reply_message()
        pcode = mytext.text
        if pcode[8:]:
            pcode = str(pcode[8:])
        elif textx:
            pcode = str(textx.message)  # Importing message to module
        code = quote_plus(pcode)  # Converting to urlencoded
        await mytext.edit('Meking Carbon...')
        url = CARBON.format(code=code, lang=CARBONLANG)
        chrome_options = Options() # No Need to See All This
        chrome_options.add_argument('--headless')
        chrome_options.binary_location = GOOGLE_CHROME_BIN
        chrome_options.add_argument('--window-size=1920x1080')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        prefs = {'download.default_directory': './'}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
        driver.get(url) # Url Is Given Abovee
        await mytext.edit('Wait dear\nAb It is taking some time')
        download_path = "./" # Download Path Is Very Important
        driver.command_executor._commands["send_command"] = (
            "POST",
            "/session/$sessionId/chromium/send_command",
        )
        params = {
            "cmd": "Page.setDownloadBehavior",
            "params": {
                "behavior": "allow",
                "downloadPath": download_path
            },
        }
        driver.execute("send_command", params)
        # Now It Will Download The File
        driver.find_element_by_xpath(
            "//button[contains(text(),'Export')]").click()
        await mytext.edit('Just completing in a few seconds')
        sleep(2.5)
        await mytext.edit("Ok done")
        driver.quit()
        file = "./carbon.png"
        await mytext.edit("Now it's uploading")
        # Uploading The File
        await mytext.client.send_file(
            mytext.chat_id,
            file,
            caption=
            "<< Here's Your Carbon Dear,\n  Carbonised By [ThunderUserbot](https://github.com/Thundergang/thunderuserbot)>>",
            force_document=True,
            reply_to=mytext.message.reply_to_msg_id,
        )
        cmd("rm ./carbon.png") # A Better Way A Deleting
        # Removing carbon.png after uploading
        await mytext.edit('Goodbye Have a nice day')
        sleep(2)
        await mytext.delete()
        # Deleting msg
        # This part is new
        await borg.send_message(mytext.chat_id, bf)
