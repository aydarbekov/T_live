import csv
import time
# from bs4 import BeautifulSoup
from _hashlib import new

import openpyxl
import requests
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import csv
new_profiles = [
    "https://www.facebook.com/profile.php?id=100024119619142&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI4NDgxNzQxNTkxNTk%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100035646014370&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxMTI0NjQwMzI3MzA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100039007816358/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100052855458201/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100031599213743/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053280099498/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050445919885&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTE5NjgwNzc1ODA1MDI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100038020716357/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100038020716357/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100040007753187/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100027992526655&comment_id=Y29tbWVudDozNzY2MzE4MjY2NzE5NzkwXzM3NjY0MDUzNjAwNDQ0MTQ%3D&__cft__[0]=AZXPMoGBMnK-uzOJ_E6q4Q0TsrAm5lubqa0yn_xphY46N7y7g6M3Tm0zoXq035e_z8g-idBNy4I-jC22bbnMdYj0l5ZTiiwASXHzBZYKqLU6Nab-tBDrLrIRthDaVhDz6zAH_em9zxQkn7PsRHrFlSD1-gEarMP0Wswrkp-bQ1gfmQ&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100047338291476&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDc2NzcwMjUzMDg2MzU%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100032053387417/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100048930315565/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100024187623773&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQwNzA1NTIwMDMyNTE%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100057079411437/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100057079411437/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100022844982207/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100017147493256&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI1NjQ4NDc1MjA4MjU%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055450684281&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxMzQ2MjQwMzA1MTQ%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055450684281&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxMzYwODQwMzAzNjg%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055450684281&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTMxMDQ5NDc0NjY4MTU%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055450684281&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTMxMTAwMDc0NjYzMDk%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055450684281&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQzNDgzMjA2NzU4MTE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055450684281&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTMwODMxNDc0Njg5OTU%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055450684281&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTMwOTUyNzA4MDExMTY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049252788729/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049252788729/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056242412080&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3ODAyODU1MjA0NTQ%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056242412080&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3ODE3OTg4NTM2MzY%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056242412080&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3ODExOTU1MjAzNjM%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056242412080&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3NzkxNTg4NTM5MDA%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100045927980037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI1NDIyMjQxODk3NTQ%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055033467212/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/wolfdmitri?comment_id=Y29tbWVudDozNzY2MzE4MjY2NzE5NzkwXzM3NjY4OTc2NDMzMjg1MTk%3D&__cft__[0]=AZXPMoGBMnK-uzOJ_E6q4Q0TsrAm5lubqa0yn_xphY46N7y7g6M3Tm0zoXq035e_z8g-idBNy4I-jC22bbnMdYj0l5ZTiiwASXHzBZYKqLU6Nab-tBDrLrIRthDaVhDz6zAH_em9zxQkn7PsRHrFlSD1-gEarMP0Wswrkp-bQ1gfmQ&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100048726185090&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI4MDc2NjQxNjMyMTA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100048726185090&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI4MTY4MzA4Mjg5NjA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/%D0%94%D1%83%D1%85-%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D0%B0-2246755825604058/?comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI5NTgzNjA4MTQ4MDc%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/%D0%94%D1%83%D1%85-%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D0%B0-2246755825604058/?comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI4MDgwMTc0OTY1MDg%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/%D0%94%D1%83%D1%85-%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D0%B0-2246755825604058/?comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI1NDkyMDc1MjIzODk%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/%D0%94%D1%83%D1%85-%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D0%B0-2246755825604058/?comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIzODkyMzc1MzgzODY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/%D0%94%D1%83%D1%85-%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D0%B0-2246755825604058/?comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIzNjUwMTQyMDc0NzU%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/%D0%94%D1%83%D1%85-%D0%9A%D1%8B%D1%80%D0%B3%D1%8B%D0%B7%D0%B0-2246755825604058/?comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIxODA4NDQyMjU4OTI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045071173896/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100024307566248/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100042991065719/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100011466554682&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDc5NzQ4NzUyNzg4NTA%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056611970058&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI4ODc0Mjc0ODg1Njc%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100037848123464/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100037848123464/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100029426450508/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055996001597/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100048292399983/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100044316316069/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100052039212273/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053026155460/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053026155460/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100048709927922&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI0NzczNjA4NjI5MDc%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100048709927922&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI0NjcxNDA4NjM5Mjk%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100048709927922&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI0NzQ0MzA4NjMyMDA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/john.asangulov?comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTMwNDg1Mjg4MjY5NjM%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100044433015648/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100009251262485/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100047836039447/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100030625372408&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQzMTQ5NTQwMTI0ODE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100030625372408&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQzMTA1NjQwMTI5MjA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051120860979/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054954892473/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054954892473/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100048215745889/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100049691323681&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQzNzEzMTA2NzM1MTI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100049691323681&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTY4MTg1MjA0Mjg3OTE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100049691323681&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQzNzEyNTQwMDY4NTE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100021423007458&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIxNTA5Mzc1NjIyMTY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056246737791/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056246737791/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100040463434000/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100027482616348&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3ODAwODg4NTM4MDc%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055142845820/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046813330589/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046813330589/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056520451422/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100022063850844/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100041677804803/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100035497931809/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100040584642049/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100044986877291/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100034889615042/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051074181547/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046067181513/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055470366477/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100028368672741/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100057085989476/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100057085989476/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055268296421/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100048498724165/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100011323969669/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100008502152279/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100052012810242/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100038156122576/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100030786553934/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100016708142908&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTUwODI4NTUyMzUzNTQ%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055739300891/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100033217640842/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100054847721958&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQ0OTM1OTczMjc5NTA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100054847721958&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQ0OTUxMTczMjc3OTg%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100028397033764&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQwNjUxOTIwMDM3ODc%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053596011031/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050070822367&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxNzcwOTQwMjYyNjc%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050070822367&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxODkxMzQwMjUwNjM%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050070822367&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxOTc4MDQwMjQxOTY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050070822367&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQ1MTY2NDM5OTIzMTI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050070822367&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxNTIzNjczNjIwNzM%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050070822367&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxNjc2MTA2OTM4ODI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050070822367&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxNjExOTQwMjc4NTc%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050070822367&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxNDg4MjczNjI0Mjc%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100050070822367/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100054696455146&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQxNzc3ODg2NTkxOTQ%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100038461320949/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100031228128366/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100047624311597/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100025038948748&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQyMDEyMDg2NTY4NTI%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100024006607392/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100011676345056&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI4NDMwMTg4NDc1MTQ%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100014814762696/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100013124597229&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3OTkyNTg4NTE4OTA%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100013125361795&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIxODg0NzA4OTE3OTY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014632729336&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM3NTg1MzQwNjgxMjM%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014632729336&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM3NTQwMzA3MzUyNDA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014632729336&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM3Njg1MDc0MDA0NTk%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014632729336&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM3NjU3MTQwNjc0MDU%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014632729336&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM3NjQ0Nzc0MDA4NjI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014632729336&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM3NjI0NTQwNjc3MzE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014632729336&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM3NTYxNDA3MzUwMjk%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046492935939/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056147951047&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI5ODc3OTc0Nzg1MzA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100044130132061/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100052827982258/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055675020388/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100038184673172/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045978802785/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100050923353670/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100025616327370/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100052632800049&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTMwNzQzNTQxMzY1NDE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045930036450/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100041591103104/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100030318253418&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIxMDk5OTc1NjYzMTA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049632064296/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100037677490416/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056572470796&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI4NDI1NzIxODA4OTI%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049309246037/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100018758726010/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100028234276867/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100057082380192/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100022295179550/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100046934709485/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/kyrgyz2?comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDc2MzgzODE5NzkxNjY%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/kyrgyz2?comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQxMTgwNDg2NjUxNjg%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100049418498952&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTUzMzI4NzE5MzE4NjI%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054997775250/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100052123551079/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055016797823/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100047136135920/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100052326484695/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100040390902831&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDc4MjQ5Nzg2MjcxNzM%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100035540034387&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTMwOTQyMzA4MDEyMjA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100011324298197/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100011324298197/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100006413388229/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100006413388229/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100039683263198&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDg3NDMyOTUyMDIwMDg%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100006946789288&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQyOTUwNjczNDc4MDM%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100029771285664/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100029771285664/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100041320089179/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100050494935971/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056082690093/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100030967748316/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100032686341990&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQ1ODQ3MzczMTg4MzY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100047044695752/",
    "https://www.facebook.com/groups/123754788028526/user/100042705307766/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100032462449622/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100054968024014&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI4MjI3Mzg4NDk1NDI%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100019225629191/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100053933567448&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQxNTM1NTg2NjE2MTc%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100033884506020/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100003457412938/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100020413234871/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053376022745/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100024643729181/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100041559140279/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100030809686924/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055684283645/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100019377592087/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100050639243059/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100003956719464&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDc4NzA0MTUyODkyOTY%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100044148922138&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQzODU0MjQwMDU0MzQ%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045034641296/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100028715341616/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100035397722613/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055869098282&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTMyOTk1MDQxMTQwMjY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100046376314327/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100003518102206/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100003518102206/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100003518102206/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100047821907687/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051399909672/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100002938937444/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046324982460/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053103582965/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051341974303/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100022171206619/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100040280810900&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI5OTA0Mzc0NzgyNjY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100040280810900&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI5OTUyMTQxNDQ0NTU%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100040280810900&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTMwMDAxMzc0NzcyOTY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100034797668873/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055144941375/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055144941375/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055144941375/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055144941375/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100041161995470&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI5NTczMDg4MzYwODU%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100048153276387/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100025570532421&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM2Mjk2Nzc0MTQzNDI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100025570532421/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045697779653/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100024606367959/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100047566033874/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051905782623/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051905782623/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045682147382/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100024089988364&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM3OTYwNDQwNjQzNzI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100055789057082/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100039088501573/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/nazgul.akmatova.81?comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDg2OTM2NDE4NzM2NDA%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100034311872488/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100051523374071/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054951922754/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100050468430278/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100050468430278/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100047132719649/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100025198341729&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI2NTI2ODQxNzg3MDg%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100044791097277&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM2Nzg1Nzc0MDk0NTI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100044791097277&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM2NzQ5NjQwNzY0ODA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100044791097277&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM2Nzc2MDQwNzYyMTY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100041672889057/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100025589601212/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100025589601212/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/niyazbek.musuraliev?comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQxNDUzNTUzMjkxMDQ%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100041776719548/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100041001832526&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI4NjA3MDA4MjQ1NzM%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100041001832526&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI4NTk2MzA4MjQ2ODA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100055047667977/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100024401227531/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100052526677733/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055285071709/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100029141207551/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053284131464/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100043859724215&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI3OTI5NzA4MzEzNDY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046558309657/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100046749665251&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTE5NDY2NDQyNDkzMTI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100024443103945/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100043137995342&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM4ODYxNDQwNTUzNjI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100045406817037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5Mzk1MTA3MTY2OTI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100045406817037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5NTYwNzQwNDgzNjk%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100045406817037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5NDIyNjczODMwODM%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100045406817037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5NDA0NzA3MTY1OTY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100045406817037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5NDQzMTA3MTYyMTI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100045406817037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5NDkzMTQwNDkwNDU%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100045406817037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5NDY0OTQwNDkzMjc%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100045406817037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5NDMxOTQwNDk2NTc%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100040502926280/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100038955650861/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100044431873146/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100050791862727&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI5NDc0MDQxNDkyMzY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100010009303353&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTMwODI0Njc0NjkwNjM%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100010009303353&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTU0MDU3NTA1NzAwNjg%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053772283140/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053772283140/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100035757000031/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046515457168/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051436550871/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100036621936828&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3Nzc5NzIxODczNTI%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053449866839/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100021626765232/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100046482261906&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTY0NzAwMzA0NjM2NDA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100042915263635/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100022243298650&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTY1NDIyODcxMjMwODE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/hozyainova?comment_id=Y29tbWVudDozNzY2MzE4MjY2NzE5NzkwXzM3Njk3ODMzNDYzNzMyODI%3D&__cft__[0]=AZXPMoGBMnK-uzOJ_E6q4Q0TsrAm5lubqa0yn_xphY46N7y7g6M3Tm0zoXq035e_z8g-idBNy4I-jC22bbnMdYj0l5ZTiiwASXHzBZYKqLU6Nab-tBDrLrIRthDaVhDz6zAH_em9zxQkn7PsRHrFlSD1-gEarMP0Wswrkp-bQ1gfmQ&__tn__=R]-R",
    "https://www.facebook.com/hozyainova?comment_id=Y29tbWVudDozNzY2MzE4MjY2NzE5NzkwXzM3Njk3ODc5OTMwMzk0ODQ%3D&__cft__[0]=AZXPMoGBMnK-uzOJ_E6q4Q0TsrAm5lubqa0yn_xphY46N7y7g6M3Tm0zoXq035e_z8g-idBNy4I-jC22bbnMdYj0l5ZTiiwASXHzBZYKqLU6Nab-tBDrLrIRthDaVhDz6zAH_em9zxQkn7PsRHrFlSD1-gEarMP0Wswrkp-bQ1gfmQ&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100035216540937/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053583010819/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049842570123/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100041286468940&comment_id=Y29tbWVudDozNzY2MzE4MjY2NzE5NzkwXzM3NjYzNTMzNjMzODI5NDc%3D&__cft__[0]=AZXPMoGBMnK-uzOJ_E6q4Q0TsrAm5lubqa0yn_xphY46N7y7g6M3Tm0zoXq035e_z8g-idBNy4I-jC22bbnMdYj0l5ZTiiwASXHzBZYKqLU6Nab-tBDrLrIRthDaVhDz6zAH_em9zxQkn7PsRHrFlSD1-gEarMP0Wswrkp-bQ1gfmQ&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055568880341/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100054196883350/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100046066148225/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100046066148225/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100054231283844&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI4ODA1Njg4NDM3NTk%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100041068543223/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049199531638/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100053568728288/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100050795751827/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054149201888/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100034362572008/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056099473600/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045684400096/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014473817636&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIzMDczNTQyMTMyNDE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014473817636&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDc3MTY4MDg2Mzc5OTA%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014473817636&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQxOTYyMjUzMjQwMTc%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100033496140646/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056154581513/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054681356966/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054681356966/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054681356966/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100004770045713/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100038134193797/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100038134193797/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100038134193797/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100026560893398/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100041477838255/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100036278751145/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100044670669538/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056343224807&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTUwMTMyMTcyNzU5ODg%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/karategin.sn?comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI4MTU4MzU1MTY4OTk%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049423774412/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100030377926490/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100010901731843&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI5MTAyMjA4MTk2MjE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053680275455/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100023990593066/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100041535221312&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQyMzU0ODQwMjA0Mjg%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055466874933/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100049584693303&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI3ODU1MjQxNjU0MjQ%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100049584693303&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI3OTM1MTA4MzEyOTI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100049584693303&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI4MDIyNzc0OTcwODI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100049584693303&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI3OTk2Nzc0OTczNDI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055406589668/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049141356992/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049141356992/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100023046470501/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100032316753382/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045298361720/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100047874732460/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100034127765116/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100036029832328&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI3OTI1OTA4MzEzODQ%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051807007454/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100025125038629/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054096877949/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100056044661274/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100050066292488/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100007474059082&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI4MTg0MjIxODMzMDc%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100054896261529/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055903916041/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055903916041/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100031818406303/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100052915637697/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100049559821745&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQxMTA3Mjg2NjU5MDA%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056500791601/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100011112181034&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQwNjM3MTIwMDM5MzU%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100030949981700/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055660380681&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQ1NTg3MDg2MjExMDI%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053430909788/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100042556484806&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIzODcwNDQyMDUyNzI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100054738536392&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQ1MTgyMjM5OTIxNTQ%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055893532156&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQ2MzcxMDE5NDY1OTY%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055893532156&comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQ2Mzg3ODUyNzk3NjE%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100021949233521/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051202895681/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100040768864420/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100019348519773/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100028071021587/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100039293320247/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100017256819875&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3NTk3ODIxODkxNzE%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100054105181046/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100046996803082&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI0NDc5NjQxOTkxODA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100052918788073/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055355532304/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100050792100146/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100035950630695&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3OTQ3OTg4NTIzMzY%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100026313001441/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100028551377134/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056223578714/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100033404856715/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100044216820275/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100049360817786/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100049360817786/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100045490090126/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045490090126/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100052987538750/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055894616540/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100054411910956&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTUwMDU0NjM5NDM0MzA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100026270222109/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100029078604150&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTE5MzUxNDc1ODM3OTU%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055365330033/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055365330033/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055365330033/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100040044936948/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100014448796449&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI3OTIyMDU1MTkyNjI%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100021980348735/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100049534921686/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100027691146514/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100043928162786/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100045764327295/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100016266270524/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100022882185953&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI5NjQxMTQxNDc1NjU%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100022882185953&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQzMjE4MjQwMTE3OTQ%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100040846972483&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIzMTg0MTA4Nzg4MDI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100040846972483&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIyMDM3ODQyMjM1OTg%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056340722313/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056340722313/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053135641862/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046753444243/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046753444243/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100046753444243/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100048092493494/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100055961778803&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDgwNjUwMzE5MzY1MDE%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056264141766/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100051412996826/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100024327067216/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100055637554688/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100036803748608/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100009281988976&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI4OTA2NjIxNzYwODM%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100015111639810/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100055880651016/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100042165512887/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100054391201852/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100016967596385/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100053616048971/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100040965855801/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100039145578857/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100056021116501/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100025028116859/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100049278698701/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/groups/123754788028526/user/100049278698701/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100036030009250&comment_id=Y29tbWVudDozNzY2MzE4MjY2NzE5NzkwXzM3Njg3OTQxMTk4MDU1Mzg%3D&__cft__[0]=AZXPMoGBMnK-uzOJ_E6q4Q0TsrAm5lubqa0yn_xphY46N7y7g6M3Tm0zoXq035e_z8g-idBNy4I-jC22bbnMdYj0l5ZTiiwASXHzBZYKqLU6Nab-tBDrLrIRthDaVhDz6zAH_em9zxQkn7PsRHrFlSD1-gEarMP0Wswrkp-bQ1gfmQ&__tn__=R]-R",
    "https://www.facebook.com/groups/1412264215689407/user/100047520682193/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056294997306&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5MzczMDczODM1Nzk%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056294997306&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTM5Mzk3NTQwNTAwMDE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100056294997306&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTQxNjYyNzczNjA2ODI%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100011614249413&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDgwODgwNjUyNjc1MzE%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100011614249413&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NDgwODM5MzUyNjc5NDQ%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/profile.php?id=100011614249413&comment_id=Y29tbWVudDozNDQ3NTgxMjIxOTg0ODgyXzM0NTA2OTI5NDE2NzM3MTA%3D&__cft__[0]=AZW4NfQ2pZAXR9xa8wNLw1HxSgrkQwCGy13qO2-xNTQNgGjDoTXRAS-LysU4fxZ5ekRe3yEotPwxfQgC48HbZvJdCucoI22itsZZGCbCgdPEZ4dPlkjO0sLn2efc-EqucHcToMJISkHPUPtNXdZQU4eP&__tn__=R]-R",
    "https://www.facebook.com/belle.bell.391?comment_id=Y29tbWVudDozNDE0MDQ4NzE4NjcyMTAxXzM0MTQwNTIxNzUzMzg0MjI%3D&__cft__[0]=AZX5fQrQFrmEwMY5vX1g0CeKjHKEdxsh7pwNxSGOhxjW4PLDmrbN-x2klUKb_OuMZ6OzyWRz6ryqQtgAtTtNSicfdTg8JJKDQ36qtAYTomxbBbPka5IspJc6PN7_Pk90qOmwBYk5o-QhoCKJ9PkAcurx&__tn__=R]-R",
]
profiles = [
    'https://www.facebook.com/groups/123754788028526/user/100052102488083/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100050758069290/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100054551864880/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100043912823068/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100053041695742/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100053041695742/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100053041695742/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100047128329740/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100009196628675/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100054349990385/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100045693691894/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100042061699090/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100051490494146/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100018233329866/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100044455642600/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100048954215045/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055712866803/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100026490077162/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100047967623942/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100020913130426/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055552380912/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100044486738359/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100052190092309/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100047480018981/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100008234977777/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100055939230156/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/profile.php?id=100000518225249&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI0NTM4NzQxOTg1ODk%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100048232634699/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100043948157700/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/profile.php?id=100045969854303&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIzNTM5NjQyMDg1ODA%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100033262968865/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100052279621879/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100051770029722/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100047566412039/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100042412996852/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100047502642416/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100054664223564/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100044202100477/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100044518238133/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100054171070081/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100056372406998/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100045957021537/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100036381217586/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/profile.php?id=100027419792451&comment_id=Y29tbWVudDoyMTEyNzU3NDc1NTIyNzM1XzIxMTI5OTczNTg4MzIwODA%3D&__cft__[0]=AZWvMW_HYofAxJOigAhRRTeCgEkvhQaKNU6dUA1oa2bmHFzTSzDP-vkhNE5jlgBHk5SbgbDRbKx0PIY-UMXVFnvk3SW0euJUchi1I0xirul_G4wEhvUHlSXn_sEUk_1cf_I&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100045160620986/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/profile.php?id=100042733542710&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI4NzQ2Njc0ODk4NDM%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100006190037345/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100054730850449/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100055004106449/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100025699149226/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055263690022/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100044486920820/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100035754803096/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100048082759651/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100048163230103/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100056489840800/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100022453004396/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055882177869/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100054264733206/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100053953050007/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100051554710442/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100013041124475/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100049163087194/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100053781091101/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100044390021594/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100056477839450/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100030988570491/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100015854741161/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100030602916755/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100023983397582/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100047986461433/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/profile.php?id=100024850065073&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI3MTU1ODc1MDU3NTE%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100043306144304/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055659922035/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100026764085396/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100031599213743/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100038020716357/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100032053387417/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/profile.php?id=100045927980037&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTI1NDIyMjQxODk3NTQ%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100037848123464/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/profile.php?id=100021423007458&comment_id=Y29tbWVudDozMTkxODYzOTAwOTI0MjUzXzMxOTIxNTA5Mzc1NjIyMTY%3D&__cft__[0]=AZWaLXrCEso765B3SvFUkfW7Cyqg65OPTNfSJyYRFbgT3gvhnTXP4wcrdnotErJhWyTcXfPh8ivq0TX1Gh1YA6eFjQ6fInEpevsqwkMEEBRwJJyk9GEPO2XzINzc-lGFrnC8oQksSJPucEAB2EO-x_2E&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100056246737791/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055142845820/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100041677804803/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100057085989476/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100048498724165/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100038156122576/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100030786553934/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100033217640842/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100053596011031/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100050070822367/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100031228128366/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100024006607392/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055675020388/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100050923353670/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100025616327370/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100045930036450/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100037677490416/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100028234276867/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100054997775250/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100011324298197/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100050494935971/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100033884506020/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100024643729181/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100030809686924/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100019377592087/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100050639243059/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100045034641296/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100047821907687/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100046324982460/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100034797668873/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055144941375/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055144941375/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100047566033874/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100039088501573/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100051523374071/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100054951922754/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100047132719649/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100041776719548/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100024401227531/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100029141207551/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100046558309657/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100040502926280/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100053772283140/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100035757000031/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100053449866839/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100021626765232/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100042915263635/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100049842570123/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100046066148225/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100049199531638/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100034362572008/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100056099473600/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100054681356966/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100054681356966/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100004770045713/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100036278751145/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100049423774412/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055466874933/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100023046470501/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055903916041/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100031818406303/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100052915637697/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100056500791601/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100051202895681/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100040768864420/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100052918788073/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100028551377134/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100056223578714/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/123754788028526/user/100049360817786/?__cft__[0]=AZUHfWk9med3hdTHbbaOfBEC169EvfagkIIi2hMU8cNFQCrTgI64NxOF1XUBEi6tdibxAvPbyY2xYIOPPFx-ByWOQjkHXeAiokmxDtyT2WiVy3HJ-DQp2oByF17E63h-yemrmwbOpuhC2lCCAMZCcjaU&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055894616540/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100026270222109/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100055365330033/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100021980348735/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100027691146514/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100016266270524/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100046753444243/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100036803748608/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100042165512887/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100016967596385/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100053616048971/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R',
    'https://www.facebook.com/groups/1412264215689407/user/100025028116859/?__cft__[0]=AZXXEs2u6AFpA8hJ91_zdQnFiUQ54dMomjLbmyyikomUAeSmPlYkTaG80EwlO1v4ddv9goseQbqwl6E5V0PceYWrCZUmMqpWp3fdcRHZMMFx8OXOme0QqmFwf8WosewrNxioLyjCC9ibCKd6Ux6L4Oa8&__tn__=R]-R'
]
prof_links = []
for i in new_profiles:
    if i not in profiles:
        if i not in prof_links:
            prof_links.append(i)
print(prof_links)
print(len(prof_links))
# with open('fb_profile.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter='|')
#     writer.writerow(["Ссылка", "Имя", "кол-во постов", "дата последнего поста", "фото профиля", "размер фото",
#                      "Работа", "ВУЗ", "Школа", "Адрес", "Контакты", "Сайты и соцсети", "Осн инфо", "Дата рождения",
#                      "Язык", "Статус", "Семья", "О пользователе", "Произношение имени", "Другие имена", "Цитаты", "кол-во фото из хрон", "Кол-во фоток", "кол-во нравится", "Отметки нравится", "Кол-во друзей", "Друзья"])



def parse_info(xpath):
    infos = []
    objects = driver.find_elements_by_xpath(xpath)
    for object in objects:
        print(object.text)
        infos.append(object.text)
    profile_info.append(infos)


def scroll_to_down(divs, time_plus):
    time_wait = 2
    retry = 0
    while True:
        p_height = driver.execute_script("return document.body.scrollHeight;")
        print(p_height)
        driver.execute_script(f"window.scrollTo(0, (document.body.scrollHeight)/2);")
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(time_wait)
        new_p_height = driver.execute_script("return document.body.scrollHeight;")
        print(new_p_height)
        print(p_height == new_p_height)
        objects = driver.find_elements_by_xpath(divs)
        print(len(objects))
        if len(objects) > 100:
            break
        #     time_wait = 5 + time_plus
        # elif len(objects) > 1000:
        #     time_wait = 7 + time_plus
        # elif len(objects) > 1500:
        #     time_wait = 10 +time_plus
        if p_height == new_p_height:
            if retry < 3:
                retry += 1
                print('retryyyyyyy')
                pass
            else:
                print('end')
                break
        else:
            retry = 0
    profile_info.append(len(objects))



option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# option.add_argument("--headless")
option.add_argument("--window-size=1325x744")
# option.add_argument("--remote-debugging-port=9221")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option)
# driver.maximize_window(driver.window_handles)
# driver.window_handles
print('Захожу на фб')
driver.get("https://www.facebook.com")
driver.implicitly_wait(10)
# time.sleep(2)

print('Жму на закрытие окоша модалки')
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-cookiebanner="accept_button"]'))).click()

driver.implicitly_wait(10)
time.sleep(1)

print("Логинюсь")
driver.find_element_by_name('email').send_keys('akyl.aydarbekov@gmail.com')
driver.find_element_by_name('pass').send_keys('sprite05')
print("Отправляю форму")
time.sleep(2)
driver.find_element_by_css_selector('button[type="submit"]').click()

driver.implicitly_wait(10)
time.sleep(2)

for profile in prof_links:
    profile_info = []

    print("Захожу на профиль")

    profile_link = profile
    profile_info.append(profile_link)
    driver.get(profile_link)
    driver.implicitly_wait(10)
    time.sleep(7)
    try:
        driver.implicitly_wait(0)
        deleted = driver.find_element_by_xpath(".//*[contains(text(), 'Этот контент сейчас недоступен')]")
        driver.implicitly_wait(0)
        profile_info.append('НЕ ДОСТУПЕН')
        with open('fb_profile.csv', 'a+', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow(profile_info)
        continue
    except:
        pass
    try:
        full_profile = driver.find_element_by_css_selector('a[aria-label="Посмотреть основной профиль"]').click()
        time.sleep(7)
    except:
        pass


    # id_prof = profile_link.split('id=')
    # print(id_prof[1])

    name_h1 = driver.find_element_by_tag_name('h1')
    print(name_h1.text)
    profile_info.append(name_h1.text)


    # парсинг постов
    print("Парсю посты")
    post_divs = "//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div"
    scroll_to_down(post_divs, 2)
    try:
        last_post = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div[last()]")
        time_post = last_post.find_element_by_css_selector('a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]')
        hover = ActionChains(driver).move_to_element(time_post)
        hover.perform()
        time.sleep(1)
    except:
        try:
            last_post = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div[last()-3]")
            time_post = last_post.find_element_by_css_selector('a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]')
            hover = ActionChains(driver).move_to_element(time_post)
            hover.perform()
            time.sleep(1)
        except:
            print('Нет публикаций')

    # hover = ActionChains(driver).move_to_element(time_post)
    # hover.perform()
    # time.sleep(1)
    try:
        time_full = driver.find_element_by_css_selector('span[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 tia6h79c fe6kdd0r mau55g9w c8b282yb iv3no6db e9vueds3 j5wam9gi knj5qynh oo9gr5id hzawbc8m"]')
        print(time_full.text)
        profile_info.append(time_full.text)

    except:
        try:
            time_icon = last_post.find_element_by_css_selector('span[class="tojvnm2t a6sixzi8 abs2jz4q a8s20v7p t1p8iaqh k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y iyyx5f41"]')
            prelast_post = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb d2edcug0 hpfvmrgz gile2uim buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div[last()-1]")
            time_post = prelast_post.find_element_by_css_selector(
            'a[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"]')
            hover = ActionChains(driver).move_to_element(time_post)
            hover.perform()
            time.sleep(1)
            time_full = driver.find_element_by_css_selector(
                'span[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 tia6h79c fe6kdd0r mau55g9w c8b282yb iv3no6db e9vueds3 j5wam9gi knj5qynh oo9gr5id hzawbc8m"]')
            print(time_full.text)
            profile_info.append(time_full.text)

        except:
            print('some error')
            profile_info.append('')
        # hover = ActionChains(driver).move_to_element(time_icon)
        # hover.perform()
        # time.sleep(1)
        # time_full = driver.find_element_by_css_selector('span[class="d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 tia6h79c fe6kdd0r mau55g9w c8b282yb iv3no6db e9vueds3 j5wam9gi knj5qynh oo9gr5id hzawbc8m"]')

    # time.sleep(2)

    # Парсинг фото профиля
    try:
        print('Ищу фото профиля и кликаю')
        profile_photo = driver.find_element_by_css_selector('div[class="b3onmgus e5nlhep0 ph5uu5jm ecm0bbzt spb7xbtv bkmhp75w emlxlaya s45kfl79 cwj9ozl2"]').click()
        try:
            print('Смотрю нет ли истории')
            time.sleep(3)
            story_or_photo = driver.find_element_by_xpath(".//*[contains(text(), 'Посмотреть фото профиля')]").click()
            time.sleep(3)
            img = driver.find_element_by_css_selector('img[class="ji94ytn4 r9f5tntg d2edcug0"]')
            width = driver.execute_script(
                "return document.getElementsByClassName('ji94ytn4 r9f5tntg d2edcug0')[0].naturalWidth")
            height = driver.execute_script(
                "return document.getElementsByClassName('ji94ytn4 r9f5tntg d2edcug0')[0].naturalHeight")
        except:
            time.sleep(3)
            img = driver.find_element_by_css_selector('img[class="ji94ytn4 r9f5tntg d2edcug0"]')
            width = driver.execute_script(
                "return document.getElementsByClassName('ji94ytn4 r9f5tntg d2edcug0')[0].naturalWidth")
            height = driver.execute_script(
                "return document.getElementsByClassName('ji94ytn4 r9f5tntg d2edcug0')[0].naturalHeight")
        time.sleep(2)
        print(img.get_attribute('src'))
        profile_info.append(img.get_attribute('src'))
        print(width)
        print(height)
        profile_info.append(str(width) + ' x ' + str(height))
        driver.back()
        time.sleep(2)
    except:
        print('нет фото')
        profile_info.append('Нет фото')
        profile_info.append('0х0')

    # try:
    #     profile_photo = driver.find_element_by_css_selector('a[class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l oo9gr5id"]')
    #     profile_photo_full =  profile_photo.get_attribute('href')
    #     driver.get(profile_photo_full)
    #     driver.implicitly_wait(10)
    #     time.sleep(2)
    #     img = driver.find_element_by_css_selector('img[class="gitj76qy r9f5tntg d2edcug0"]')
    #     width = driver.execute_script("return document.getElementsByClassName('gitj76qy r9f5tntg d2edcug0')[0].naturalWidth")
    #     height = driver.execute_script("return document.getElementsByClassName('gitj76qy r9f5tntg d2edcug0')[0].naturalHeight")
    #     time.sleep(2)
    #     print(img.get_attribute('src'))
    #     profile_info.append(img.get_attribute('src'))
    #     print(width)
    #     print(height)
    #     profile_info.append(str(width) + ' x ' + str(height))
    #     driver.back()
    #     time.sleep(2)
    # except:
    #     profile_info.append('Нет фото')
    #     profile_info.append('0х0')

    # Парсинг инфо
    driver.execute_script(f"window.scrollTo(0, 0);")
    time.sleep(2)
    infoblock = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr']/div[@class='tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p']/div[@class='cb02d2ww ni8dbmo4 stjgntxs l9j0dhe7 k4urcfbm du4w35lb lzcic4wl']/div[@class='soycq5t1 l9j0dhe7']/div[@class='i09qtzwb rq0escxv n7fi1qx3 pmk7jnqg j9ispegn kr520xx4']/a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 tkr6xdv7 bzsjyuwj cb02d2ww j1lvzwm4'][2]/div[@class='bp9cbjyn rq0escxv j83agx80 pfnyh3mw frgo5egb l9j0dhe7 cb02d2ww hv4rvrfc dati1w0a']")
    infoblock.click()
    time.sleep(3)
    informations = driver.find_element_by_css_selector("div[class='ls2amcm3 pcp91wgn ihqw7lf3 p8fzw8mz discj3wi pfnyh3mw rq0escxv maa8sdkg'")
    infos = informations.find_elements_by_css_selector('div[class="bi6gxh9e"]')
    infos[1].click()
    time.sleep(1)

    # jobs
    parse_info("//div[@class='tu1s4ah4'][1]/div[position()>1]")
    # ihes
    parse_info("//div[@class='tu1s4ah4'][2]/div[position()>1]")
    # schools
    parse_info("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']/div[3]/div[position()>1]")

    infos[2].click()
    time.sleep(1)

    # addresses
    parse_info("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']/div/div[position()>1]")

    infos[3].click()
    time.sleep(1)

    # contacts
    parse_info("//div[@class='tu1s4ah4'][1]/div[@class='oygrvhab']")
    # websites
    parse_info("//div[@class='tu1s4ah4'][2]/div[@class='oygrvhab']")
    # main_info
    parse_info("//div[@class='c9zspvje'][1]")
    # birthday_dates
    parse_info("//div[@class='c9zspvje'][2]")
    # languages
    parse_info("//div[3]/div[@class='oygrvhab']")

    infos[4].click()
    time.sleep(2)

    # statuses
    parse_info("//div[1]/div[@class='oygrvhab']")
    # families
    parse_info("//div[2]/div[@class='oygrvhab']")

    infos[5].click()
    time.sleep(1)

    # about_list
    parse_info("//div[1]/div[@class='oygrvhab']")
    # names
    parse_info("//div[2]/div[@class='oygrvhab']")
    # other_names
    parse_info("//div[3]/div[@class='oygrvhab']")
    # quotes
    parse_info("//div[4]/div[@class='oygrvhab']")


    # time.sleep(1)

    # Парсинг кол-во фото
    try:
        print('Ищу Фото')
        fotoblock = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr']/div[@class='tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p']/div[@class='cb02d2ww ni8dbmo4 stjgntxs l9j0dhe7 k4urcfbm du4w35lb lzcic4wl']/div[@class='soycq5t1 l9j0dhe7']/div[@class='i09qtzwb rq0escxv n7fi1qx3 pmk7jnqg j9ispegn kr520xx4']/a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 tkr6xdv7 bzsjyuwj cb02d2ww j1lvzwm4'][4]/div[@class='bp9cbjyn rq0escxv j83agx80 pfnyh3mw frgo5egb l9j0dhe7 cb02d2ww hv4rvrfc dati1w0a']")
        fotoblock.click()
    except:
        print('Не нашел, Ищу в Ещё')
        driver.find_element_by_xpath(".//*[contains(text(), 'Ещё')]").click()
        time.sleep(1)
        fotoblock2 = driver.find_element_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 oi9244e8 oygrvhab h676nmdw pybr56ya dflh9lhu f10w8fjw scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb'][1]")
        print('Нашел. Жму')
        fotoblock2.click()

    time.sleep(2)
    print('Ищу Альбомы')
    try:
        alboms = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb gderk4og hpfvmrgz dxtxif39 buofh1pr g5gj957u aov4n071 oi9244e8 bi6gxh9e h676nmdw aghb5jc5']/div[1]//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 tkr6xdv7 bzsjyuwj cb02d2ww j1lvzwm4'][last()]")
        alboms.click()
        time.sleep(1)
        counts = driver.find_elements_by_xpath("//div[@class='rq0escxv rj1gh0hx buofh1pr ni8dbmo4 stjgntxs l9j0dhe7']/div[@class='l9j0dhe7']//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t buofh1pr tgvbjcpo sv5sfqaa obtkqiv7']//div[@class='qzhwtbm6 knvmm38d'][2]")
        a = 0
        hron = []
        for count in counts:
            alb_name = count.find_element_by_xpath('.//..')
            if not 'Фото из хроники' in alb_name.text:
                ads = (count.text).split(' ')
                a += int(ads[0])
                print(ads[0])
                print(a)
                profile_info.append(hron)
                profile_info.append(a)
            else:
                ads = (count.text).split(' ')
                print(ads[0])
                hron.append(ads[0])
                print(a)
                profile_info.append(hron)
                profile_info.append(a)

    except:
        print('НЕт фото')
        profile_info.append('[]')
        profile_info.append('0')

    # time.sleep(2)


    # отметки нравится
    likes_list = []
    try:
        driver.find_element_by_xpath(".//*[contains(text(), 'Ещё')]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[contains(text(), 'Отметки \"Нравится\"')]").click()
        time.sleep(1)
        likes = "//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 sjgh65i0 hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8']"
        scroll_to_down(likes, 0)
        likes_sel = driver.find_elements_by_xpath(likes)
        for like in likes_sel:
            print(like.get_attribute('href'))
            like_name = like.find_element_by_xpath(".//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql gk29lw5a a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb hrzyx87i jq4qci2q a3bd9o3v lrazzd5p oo9gr5id hzawbc8m']")
            print(like_name.text)
            likes_list.append(like_name.text + "----" + like.get_attribute('href'))
    except:
        profile_info.append('0')
    profile_info.append(likes_list)


    # Парсинг друзей
    # time.sleep(3)
    profiles_friends = []
    driver.execute_script(f"window.scrollTo(0, 0);")
    hover = ActionChains(driver).move_to_element(infoblock)
    hover.perform()
    print('Ищу кнопку друзей')
    friends_btn = driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t g5gj957u d2edcug0 hpfvmrgz rj1gh0hx buofh1pr']/div[@class='tojvnm2t a6sixzi8 k5wvi7nf q3lfd5jv pk4s997a bipmatt0 cebpdrjk qowsmv63 owwhemhu dp1hu0rb dhp61c6y l9j0dhe7 iyyx5f41 a8s20v7p']/div[@class='cb02d2ww ni8dbmo4 stjgntxs l9j0dhe7 k4urcfbm du4w35lb lzcic4wl']/div[@class='soycq5t1 l9j0dhe7']/div[@class='i09qtzwb rq0escxv n7fi1qx3 pmk7jnqg j9ispegn kr520xx4']/a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 pq6dq46d p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l dwo3fsh8 ow4ym5g4 auili1gw mf7ej076 gmql0nx0 tkr6xdv7 bzsjyuwj cb02d2ww j1lvzwm4'][3]")
    print('Нашел кликаю друзей')
    time.sleep(1)
    friends_btn.click()

    try:
        driver.find_element_by_xpath(".//*[contains(text(), 'Все друзья')]")
        friends = "//div[@class='sjgh65i0'][1]/div/div/div/div[@class='j83agx80 btwxx1t3 lhclo0ds i1fnvgqd']/div[@class='bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr']/div[@class='buofh1pr hv4rvrfc']/div[1]/a"
        scroll_to_down(friends, 0)
        friends = driver.find_elements_by_xpath("//div[@class='sjgh65i0'][1]/div/div/div/div[@class='j83agx80 btwxx1t3 lhclo0ds i1fnvgqd']/div[@class='bp9cbjyn ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi n1f8r23x rq0escxv j83agx80 bi6gxh9e discj3wi hv4rvrfc ihqw7lf3 dati1w0a gfomwglr']/div[@class='buofh1pr hv4rvrfc']/div[1]/a")
        for friend in friends:
            print(friend.get_attribute('href'))
            print(friend.text)
            profiles_friends.append(friend.text + "-----" + friend.get_attribute('href'))
    except:
        print('скрытый профиль походу')

    profile_info.append(profiles_friends)
    print(profile_info)

    with open('fb_profile.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(profile_info)
