from os import system as cmd
from time import sleep as s

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from userbot import CHROME_DRIVER
from userbot import CMD_LIST
from userbot import GOOGLE_CHROME_BIN
from userbot.utils import admin_cmd


@command(pattern="^.help ?(.*)")
# @borg.on(admin_cmd(pattern=r"help ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@",
                                                             "!"):
        tgbotusername = Var.TG_BOT_USER_NAME_BF_HER
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "⚡ " + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                with io.BytesIO(str.encode(string)) as out_file:
                    out_file.name = "cmd.txt"
                    await bot.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="**COMMANDS**",
                        reply_to=reply_to_id,
                    )
                    await event.delete()
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "Commands found in {}:".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "    " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a valid plugin!")
        else:
            help_string = """Userbot Helper.. \nProvided by [ThunderUserbot](https://t.me/thunderuserbot)\n`Userbot Helper to reveal all the commands`"""
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbotusername, help_string)
            await results[0].click(event.chat_id,
                                   reply_to=event.reply_to_msg_id,
                                   hide_via=True)
            await event.delete()


# Imports
# Important-vars
download_path = "./"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
prefs = {"download.default_directory": "./"}


def http_loggo():
    logo = (" ██          ███████████████ ████████████ ███████████\n"
            " ██          ██     ██            ██      ██       ██\n"
            " ██          ██     ██            ██      ██       ██\n"
            " ██████████████     ██            ██      ███████████\n"
            " ██          ██     ██            ██      ██\n"
            " ██          ██     ██            ██      ██\n"
            " ██          ██     ██            ██      ██\n"
            "█████████████████████████████████████████████████████\n")
    print(f"{logo}")


def socks4_loggo():
    logo = (
        "███████████ ████████████ ████████████ ██      ██ ███████████  ██\n"
        "██          ██        ██ ██           ██    ██   ██           ██    ██\n"
        "██          ██        ██ ██	       ██  ██	  ██           ██    ██\n"
        "███████████ ██   ██   ██ ██ 	       ████       ███████████  █████████████\n"
        "         ██ ██        ██ ██	       ██  ██              ██        ██\n"
        "         ██ ██        ██ ██	       ██    ██            ██        ██\n"
        "███████████ ████████████ ████████████ ██      ██ ███████████        ██\n"
        "███████████████████████████████████████████████████████████████████████████\n"
    )
    print(f"{logo}")


def socks5_loggo():
    logo = (
        "███████████ ████████████ ████████████ ██      ██ ███████████    ███████████\n"
        "██          ██        ██ ██           ██    ██   ██             ██\n"
        "██          ██        ██ ██	       ██  ██	  ██             ██\n"
        "███████████ ██   ██   ██ ██ 	       ████       ███████████    ███████████\n"
        "         ██ ██        ██ ██	       ██  ██              ██               ██\n"
        "         ██ ██        ██ ██	       ██    ██            ██               ██\n"
        "███████████ ████████████ ████████████ ██      ██ ███████████    ███████████\n"
        "██████████████████████████████████████████████████████████████████████████████\n"
    )
    print(f"{logo}")


def success_loggo():
    logo = (
        "███████▒███ █▒       █ ███▒████ ████████ ████▒▒███ ██████████ ██████████\n"
        "█▒          █▒       █ █        ▒        █         ▒▒         █▒\n"
        "█▒          █▒       █ ▒        █        █         ██         ▒█\n"
        "███████████ █▒       █ █        █        ███▒███   ███▒██████ ██████████\n"
        "         ▒█ █▒       █ █        ▒        █                 ██         ▒█\n"
        "         ▒█ █▒       █ ▒        █        █                 ██         █▒\n"
        "████▒██████ ██████████ ████████ ████████ ▒████████ ██▒███████ ███▒███▒██\n"
        "████████████████████████████████████████████████████████████████████████\n"
    )
    print(f"{logo}")


def done_loggo():
    logo = ("█████████    █████████ ██      █ █▒███████"
            "█        █   █       █ ▒ █     ▒ █"
            "█         █  █       █ █  ▒    █ █"
            "█   ▒▒     █ █  ▒▒▒  █ █   █   █ ███▒▒██"
            "█         █  █       █ █    ▒  █ █"
            "█        █   █       █ ▒     █ █ █"
            "█████████    █████████ █      ▒▒ ███▒████▒"
            "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print(f"{logo}")


# Now This Is The Main Part
@borg.on(admin_cmd("http"))
async def HTTP_wale_proxy(http_credit_thundergang):
    http_loggo()
    await http_credit_thundergang.edit("**Please wait**")
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    await http_credit_thundergang.edit("**Wait\nI am Downloading**")
    driver.get(
        "https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all"
    )
    file = "./http_proxies.txt"
    s(3)
    driver.quit()
    await http_credit_thundergang.edit("**Still wait\It's uploading**")
    await http_credit_thundergang.client.send_file(http_credit_thundergang.chat_id,
                                             file,
                                             force_document=True)
    done_loggo()
    s(1)
    await http_credit_thundergang.edit("**Almost finish\nOk Done\nGoodbye!!**")
    cmd("rm ./http_proxies.txt")
    s(1)
    await http_credit_thundergang.delete()
    success_loggo()


@borg.on(admin_cmd("Socks4"))
async def Socks4_wale_proxy(socks4_credit_thundergang):
    socks4_loggo()
    await socks4_credit_thundergang.edit("**Please wait**")
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    await socks4_credit_thundergang.edit("**Wait\nI am Downloading**")
    driver.get(
        "https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all"
    )
    file = "./socks4_proxies.txt"
    s(3)
    driver.quit()
    await socks4_credit_thundergang.edit("**Still wait\It's uploading**"
                                   )
    await socks4_credit_thundergang.client.send_file(socks4_credit_thundergang.chat_id,
                                               file,
                                               force_document=True)
    done_loggo()
    s(1)
    await socks4_credit_thundergang.edit("**Almost finish\nOk Done\nGoodbye!!**"
                                   )
    cmd("rm ./socks4_proxies.txt")
    s(1)
    await socks4_credit_thundergang.delete()
    success_loggo()


@borg.on(admin_cmd("Socks5"))
async def Socks5_wale_proxy(socks5_credit_thundergang):
    socks5_loggo()
    await socks5_credit_thundergang.edit("**Please wait**")
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER,
                              options=chrome_options)
    await socks5_credit_thundergang.edit("**Wait\nI am Downloading**")
    driver.get(
        "https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all"
    )
    file = "./socks5_proxies.txt"
    s(3)
    driver.quit()
    await socks5_credit_thundergang.edit("**Still wait\It's uploading**"
                                   )
    await socks5_credit_thundergang.client.send_file(socks5_credit_thundergang.chat_id,
                                               file,
                                               force_document=True)
    done_loggo()
    s(1)
    await socks5_credit_thundergang.edit("**Almost finish\nDone\nGoodbye!!**"
                                   )
    cmd("rm ./socks5_proxies.txt")
    s(1)
    await socks5_credit_thundergang.delete()
    success_loggo()
