from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

def getFrameSourceAnywhere(username, password):
    with Display():
        return getFrameSource(username, password)

def getFrameSource(username, password):
    loginURL="https://www.my.bham.ac.uk/cp/home/displaylogin"
    timetableLoginURL="""https://onlinetimetables.bham.ac.uk/Timetable/current_academic_year_2/default.aspx"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--window-size=1920,1080")
    chrome_options.add_argument("--hide-scrollbars")
    driver = webdriver.Chrome(options=chrome_options)
    driver=webdriver.Chrome(options=chrome_options)
    driver.get(loginURL)

    #navigates through login page
    driver.find_element_by_name("user").send_keys(username)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_css_selector("""img[alt=\"Login\"]""").click()

    driver.find_element_by_link_text("my.timetables").click()
    driver.get(timetableLoginURL)
    driver.find_element_by_name("tUserName").send_keys(username)
    driver.find_element_by_name("tPassword").send_keys(password)
    driver.find_element_by_name("bLogin").click()

    javascript = "javascript:__doPostBack('LinkBtn_mystudentset','')"
#    driver.execute_script(javascript)
#    print("clicked element... worked")
#    driver.save_screenshot("screenshot.png")

    driver.execute_script(javascript)
#    el = driver.find_element_by_id("dlType")
#    el.click()
#    select = Select(el)
#    select.select_by_visible_text("List Timetable (with calendar dates)")
    
    driver.find_element_by_id("bGetTimetable").click()
    driver.maximize_window()
    javascript = "javascript:__doPostBack('bNextWeek',  '');"
    for i in range(4):
        driver.save_screenshot(f'timetable{i}.png')
        driver.execute_script(javascript)
    driver.quit()
