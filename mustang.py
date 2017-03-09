import xml.etree.ElementTree as ET

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import csv
import time

# driver = webdriver.Firefox()

# config for chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--lang=en_US')


driver = webdriver.Chrome(executable_path="C:\mydev\programs\selenium\chromedriver\chromedriver", chrome_options=chrome_options)

wait5 = WebDriverWait(driver, 5)



##############################################################################################
#
##############################################################################################
def execute_click(selector, is_optional):
    if is_optional:
        el = driver.find_element_by_css_selector(selector)
        if el.is_displayed():
            el.click()
    else:
        el = wait5.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        el.click()

##############################################################################################
#
##############################################################################################
def execute_link_click_by_text(link_text, is_optional):
    if is_optional:
        el = driver.find_elements_by_link_text(link_text)[0]
        if el.is_displayed():
            el.click()
    else:
        el = wait5.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
        el.click()

##############################################################################################
#
##############################################################################################
def execute_hidden_element_click(selector):
    el = driver.find_element_by_css_selector(selector)
    el.click()

##############################################################################################
#
##############################################################################################
def execute_keystroke(selector, value, is_optional):
    if is_optional:
        el = driver.find_element_by_css_selector(selector)
        if el.is_displayed():
            el.send_keys(value)
    else:
        el = wait5.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        el.send_keys(value)

##############################################################################################
#
##############################################################################################
def process_action_tag(action_tag):
    is_optional = False
    # css_selector = action_tag.find("selector").text
    # type = action_tag.find("type").text
    # do = action_tag.find("do").text

    css_selector = action_tag.attrib["selector"]
    type = action_tag.attrib["type"]
    do = action_tag.attrib["do"]

    # if action_tag.find("optional").text == "true":
    #     is_optional = True;

    if type == "button" and do == "click":
        execute_click(css_selector, is_optional)
    elif type == "link" and do == "clickbytext":
        execute_link_click_by_text(action_tag.find("linktext"), is_optional)
    elif type == "link" and do == "clickbyselector":
        execute_click(css_selector, is_optional)
    elif type == "text" and do == "keystroke":
        execute_keystroke(css_selector, action_tag.find("value").text, is_optional)

##############################################################################################
#
##############################################################################################

def run_xml_suite(file):
    root = ET.parse(file).getroot()
    try:
        driver.get(root.attrib["url"])
    except:
        pass

    for page in root.findall("page"):
        if 'wait' in page.attrib:
            time.sleep(float(page.attrib["wait"]))
        for action in page.findall("action"):
            process_action_tag(action)


##############################################################################################
#
##############################################################################################
run_xml_suite("test-robots/mv-test-1.xml")



##############################################################################################
#
##############################################################################################



##############################################################################################
#
##############################################################################################



##############################################################################################
#
##############################################################################################
