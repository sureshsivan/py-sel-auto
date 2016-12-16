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
driver = webdriver.Chrome()

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
def process_actin_tag(action_tag):
    is_optional = False
    css_selector = action_tag.find("cssSelector").text
    type = action_tag.find("type").text
    do = action_tag.find("do").text

    if action_tag.find("optional").text == "true":
        is_optional = True;

    if type == "button" and do == "click":
        execute_click(css_selector, is_optional)
    elif type == "link" and do == "click":
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

    for page in root.findall("page")
        if 'wait' in page.attrib:
            time.sleep(float(page.attrib["wait"]))
        for action in page.findall("action"):
            process_actin_tag(action)


##############################################################################################
#
##############################################################################################
run_xml_suite("")



##############################################################################################
#
##############################################################################################



##############################################################################################
#
##############################################################################################



##############################################################################################
#
##############################################################################################
