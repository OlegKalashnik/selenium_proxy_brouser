from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import random
import zipfile

user_agents_list = [
  'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/102.0.5005.87 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/102.0.5005.87 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPod; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/102.0.5005.87 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/101.0 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (iPad; CPU OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/101.0 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (iPod touch; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/101.0 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (Android 12; Mobile; rv:68.0) Gecko/68.0 Firefox/101.0',
'Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:101.0) Gecko/101.0 Firefox/101.0',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPod touch; CPU iPhone 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36 EdgA/100.0.1185.50',
'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36 EdgA/100.0.1185.50',
'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36 EdgA/100.0.1185.50',
'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36 EdgA/100.0.1185.50',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 EdgiOS/100.1185.50 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36 Edge/40.15254.603',
'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36 OPR/63.3.3216.58675',
'Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36 OPR/63.3.3216.58675',
'Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36 OPR/63.3.3216.58675',
'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 YaBrowser/22.5.6.544 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (iPad; CPU OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 YaBrowser/22.5.6.544 Mobile/15E148 Safari/605.1',
'Mozilla/5.0 (iPod touch; CPU iPhone 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 YaBrowser/22.5.6.544 Mobile/15E148 Safari/605.1',
'Mozilla/5.0 (Linux; arm_64; Android 12; SM-G965F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 YaBrowser/21.3.4.59 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Armor X8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; Note 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; 5002H_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; TECNO LC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Armor X7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.48 Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-A022M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-A415F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; M40Pro_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; DUK-L09 Build/HUAWEIDUK-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; arm_64; Android 8.0.0; AGS-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaApp_Android/22.54.1/apad YaSearchBrowser/22.54.1/apad BroPP/1.0 SA/3 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Lenovo TB-7104F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; arm_64; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.143 YaApp_Android/22.51.1 YaSearchBrowser/22.51.1 BroPP/1.0 SA/3 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; VIE-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A305FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 Replaio/2.9.6',
'Mozilla/5.0 (Linux; Android 11; CPH1917) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; BBE100-1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A202F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; Infinix-X552 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.81 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-A320FL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A105G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0.1; ET5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Trekker-X4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; ZTE Blade A5 2020 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 newsbreak/19.2.3',
'Mozilla/5.0 (Linux; Android 10; 1AZ2P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Tommy3 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.99 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A Build/HUAWEIWAS-LX1A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; LM-G710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-J415FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; VIE-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; View) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; ASUS_X00PD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; V2111 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; T766H_EEA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; M2006C3LVG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; JSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; HUAWEI GRA-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; RMX1821 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; RNE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; JMM-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; t3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; Y9Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; moto g(9) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-G960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.1; E5823 Build/32.4.A.1.54; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; ASUS_I01WD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-T819) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2219) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; moto e5 play Build/OPGS28.54-53-8-11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-A207M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; ASUS_Z012DC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; MAR-LX3A Build/HUAWEIMAR-L23A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36 UOH/v1.6_273-android',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G570F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; SM-G611MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; STF-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.1.2; LM-X410.FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; moto e(7i) power) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.59 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 6.0; BG2-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 9; U307AS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; W-V680-OPE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 11; moto e20 Build/RON31.267-38; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36'
'Mozilla/5.0 (Linux; Android 10; BLA-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; KINGKONG MINI2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Mi 9 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; LEO-DLXX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Odd/47.2.1.1 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; ASUS_X00QD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; M2101K9G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; BLA-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; Life Geo) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SM-G770F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; BLA-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; TAB104GS Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36',
'Mozilla/5.0 (Linux; Android 7.0; SM-G920I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6.0; BTV-DL09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; CPH2219) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; NOTE 7 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Lenovo YT-X705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
]

s = Service("C:\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={random.choice(user_agents_list)}")

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
