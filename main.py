import logging
import logging.handlers
import os
from lxml import etree
from lxml import html
#from requests_ntlm import HttpNtlmAuth
#import getpass  # To get your Windows username and password
import csv

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


if __name__ == "__main__":
    eSignNum = "E000234480" #input("Please input esign number: ")
    url = f'https://esign.microchip.com/Request?requestNumber={eSignNum}'
    headers = {
    "Cookie": "eService3Core=r8t0fiwzUtcUZlcysL%2BViiDTODU4HvfQKEr0A63YB5m7Z7kyAL2LBnMv7iMUFJM0%2BbnSjS5K7x%2FrRivy2Is%2BMAYEGLV1FOdFsz9S6K4kXf3TOQAZR9IJPZ6GSWdc9zmKkslbjxiCANw196rjZKAelLVL4kOz4Y3r1HDb4kDYfRcJEXf1BMvNGbtKwqJguDJDBsbYCwM6Ovchu06CFjjkMg%3D%3D; BIGipServerESIGN-PROD.MICROCHIP.COM_443_SF=!g1wkqSQZ/R7ZMQzU2jTEExnY54N6xSKbvJFvuiKXStQ8IX9uKu8G/Fgd5PwPNTje/twTRO8yDPuSLUg=; eSignAppCookieMicrochip.BPM.eSign.UI=CfDJ8G9yYwwOdAlJoDvyN5E81OkhueVPng2f6BTRFlPSS59w7I0kf7vVuxQVwUYrZsqOEowEb8Il9OfZ6xqwqIFkZOdjZQ6NkqiDOaQpt4KFP0BF9qozxmlzx53pP-K9Z_a4siQJCJ472GNQUSMCbUvD5jxKwFbllBQdApgXGHOPxAhgIgzzVWU6BPW_aKwZsffv8JXR_EgrCv7_VkKy0PO4noTYocBMZ2_IuoWE8GhmeytQg1abiOUCpMISMT6ISZfY_TnZiy_ZwceAkfrRKO_5LhapuQqiH0oDV1A4oMQIq-XmxaP466yN-FFasxKUU7C4E-qUADGgt17XC_xDAj-782qP2LBc_av2_qYIIjLFval7xPhgSw8xlzu1mLsnKlOWEQFfyU2UYmneoQ278sWWOeTQCdYjWf-cGZQUQydHiV1ITrJSRTCW55NYJTeyYBlC_ljTF4q2YSuNJG6sGW7uCdPEqvebnusXsQr3fgNbatao5IAbh9OxbvCHsxQpsdEyMFNH5n2n5kMohNKODNi0JcKEA_FYzvSDNMSmFFGnpcpbVLr9atbvDQ1HaD7glG7l9puQz0_5AL3HJbKpSbEAPhLvgs2SPIwequm5vnn1QSYW; .AspNetCore.Session=CfDJ8G9yYwwOdAlJoDvyN5E81OmerMeTZMnd8rUqQ1kcI4goGdn5wU%2B6Mv%2BusjaOoS1WEfJtONQLOjP6n7NC6bF2H1zX3wt4zTQrnLGKi0%2FuiJ4cU0GT%2BAeVCmn308q2f7%2BYer4j5dgaLkn%2BupLKpqS4KhS0kyYTjNRm1YGdedNCaoZP; _gid=GA1.2.1174356564.1750375658; .AspNetCore.Antiforgery.G4u5rIwOjHk=CfDJ8G9yYwwOdAlJoDvyN5E81OncqsZyoG4o55v5szJ4t5_MjqHcxy3_u9mSo2NS1YFqDnDyBUt3QZ_Uz4UQuZMRwAnNb5yKsgdcdPN4woJ4YuO35Rr2GdXzKdvCFt8BHI9-CCctBAm_sq0HjxAZYTKZL78; _ga_FQBEW2M802=GS2.1.s1750375657$o22$g1$t1750376730$j34$l0$h0; _ga=GA1.1.10213859.1749534076",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",  # (Optional) mimic browser user agent
    }
    #username = "A78133"
    #password = "09614215898Asd."
    r = requests.get(url, headers=headers)

    


    if r.status_code == 200:
        print("Request was successful.")
        tree = html.fromstring(r.content)
        li_elements = tree.xpath('//ul[@id="ItemInfo"]/li[contains(@class, "hideForTablet")]')
        status = li_elements[0].text_content().strip().split()[0]  
        date = li_elements[1].text_content().strip()               
        created_by = li_elements[2].text_content().strip()         
        logger.info(status)
        logger.info(date)
        logger.info(created_by)
        
       
