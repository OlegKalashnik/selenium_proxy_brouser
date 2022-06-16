from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time
import zipfile

s = Service("C:\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36")

options.add_argument("--disable-blink-features=AutomationControlled")

options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

#---proxy_settings---
with open('proxy.txt', 'r') as f:
  proxy = f.read()

first_delimetr = proxy.find(':')
PROXY_USER = proxy[:first_delimetr]

first_delimetr += 1
second_delimetr = proxy.find('@', first_delimetr)
PROXY_PASS = proxy[first_delimetr: second_delimetr]

second_delimetr += 1
fird_delimetr = proxy.find(':', second_delimetr)
PROXY_HOST = proxy[second_delimetr: fird_delimetr]

fird_delimetr += 1
forth_delimetr = proxy.find('|', fird_delimetr)
PROXY_PORT = proxy[fird_delimetr:forth_delimetr]

forth_delimetr += 1
PROXY_REBOOT = proxy[forth_delimetr:].strip()
#---proxy_settings---

#---proxy---
# PROXY_HOST = '193.105.114.148'
# PROXY_PORT = 64051
# PROXY_USER = '79284292496'
# PROXY_PASS = '4ger5E'
# PROXY_REBOOT = 'https://mobileproxy.space/reload.html?admin&login=79284292496&pass=4ger5E&port=64051'

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

pluginfile = 'proxy_auth_plugin.zip'

with zipfile.ZipFile(pluginfile, 'w') as zp:
    zp.writestr("manifest.json", manifest_json)
    zp.writestr("background.js", background_js)
# options.add_extension(pluginfile)
#---proxy---

browser = webdriver.Chrome(service=s, options=options)

url_0 = "https://ident.me/"
# url_1 = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
# url_3 = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"

try:
  browser.get(url=PROXY_REBOOT)
  browser.close()
  options.add_extension(pluginfile)
  browser = webdriver.Chrome(service=s, options=options)
  browser.get(url=url_0)
except Exception as ex:
  pass
  # print(ex)
finally:
  pass
  # browser.close()
  # browser.quit()
