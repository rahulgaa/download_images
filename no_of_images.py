import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
chrome_options = Options()
chrome_options.add_argument("--incognito")

# ("select 1 for asian male")
# ("select 2 for asian female")
# ("select 3 for Black male")
# ("select 4 for Black female")
# ("select 5 for white male")
# ("select 6 for white female")
# ("select 7 for indian male")
# ("select 8 for indian female")
# ("select 9 for middle_eastern male")
# ("select 10 for middle_eastern female")
# ("select 11 for latino_hispanic male")
# ("select 12 for latino_hispanic female")
spec = 1
# (select n no of images you want to download)
n = 2

gender1 = "male"
gender2 = "female"
ethnicity1 = "asian"
ethnicity2 = "black"
ethnicity3 = "white"
ethnicity4 = "indian"
ethnicity5 = "middle_eastern"
ethnicity6 = "latino_hispanic"


#ethnicity2 = ""
path = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\shyam\\Downloads\\chromedriver_win32(1)\\chromedriver.exe")
path.get("https://this-person-does-not-exist.com/en")
path.maximize_window()

def close_tabs():
    # Get the handle of the current window
    current_handle = path.current_window_handle

    # Get a list of all open window handles
    handles = path.window_handles

    # Loop through the window handles
    for handle in handles:
        # Switch to the window
        path.switch_to.window(handle)

        # If the window is not the current one, close it
        if handle != current_handle:
            path.close()

    # Switch back to the current window
    path.switch_to.window(current_handle)


def image_download( gender, ethnicity):
    # path.find_element(By.ID,'oldButtonDownload').click()
    # path.switch_to.window(path.window_handles[1])
    # time.sleep(2)
    # path.find_element(By.CLASS_NAME,'download-page-avatar').click()
    # time.sleep(35)

#    path.close()
#   path.switch_to.window(path.window_handles[0])
#     path.get("https://this-person-does-not-exist.com/en")

    # path = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\shyam\\Downloads\\chromedriver_win32(1)\\chromedriver.exe")
    # path.get("https://this-person-does-not-exist.com/en")
    # path.maximize_window()
    element = path.find_element(By.NAME, "gender")
    drp = Select(element)
    drp.select_by_value(gender)
    time.sleep(1)

    element = path.find_element(By.NAME, "age")
    drp = Select(element)
    drp.select_by_value("26-35")
    time.sleep(1)

    element = path.find_element(By.NAME, "etnic")
    drp = Select(element)
    drp.select_by_value(ethnicity)
    time.sleep(1)

    element = path.find_element(By.ID, "reload-button").click()
    time.sleep(7)
    path.find_element(By.ID, 'oldButtonDownload').click()
    time.sleep(5)
    path.switch_to.window(path.window_handles[1])
    time.sleep(2)
    path.find_element(By.CLASS_NAME,'download-page-avatar').click()
    time.sleep(35)
    path.switch_to.window(path.window_handles[0])
#    time.sleep(5)
    close_tabs()

#download = image_download(gender1, ethnicity1)



if isinstance(spec, int):
    if spec == 1:
        for i in range(n):
            image_download(gender1, ethnicity1)
    elif spec == 2:
        for i in range(n):
            image_download(gender2, ethnicity1)
    elif spec == 3:
        for i in range(n):
            image_download(gender1, ethnicity2)
    elif spec == 4:
        for i in range(n):
            image_download(gender2, ethnicity2)
    elif spec == 5:
        for i in range(n):
            image_download(gender1, ethnicity3)
    elif spec == 6:
        for i in range(n):
            image_download(gender2, ethnicity3)
    elif spec == 7:
        for i in range(n):
            image_download(gender1, ethnicity4)
    elif spec == 8:
        for i in range(n):
            image_download(gender2, ethnicity4)
    elif spec == 9:
        for i in range(n):
            image_download(gender1, ethnicity5)
    elif spec == 10:
        for i in range(n):
            image_download(gender2, ethnicity5)
    elif spec == 11:
        for i in range(n):
            image_download(gender1, ethnicity6)
    else:
        for i in range(n):
            image_download(gender2, ethnicity6)

else:
    print(spec)
    print("Enter Correct value")


print("Done")
