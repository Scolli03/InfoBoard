from selenium.webdriver import Firefox
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

profile = FirefoxProfile(
    r"C:\Users\Scoll\AppData\Roaming\Mozilla\Firefox\Profiles\kjyf521x.default-release")
opts = Options()
#opts.headless = False

browser = Firefox(firefox_profile=profile, options=opts,
                       executable_path=r"C:\Users\Scoll\Desktop\InfoBoard\Executables\geckodriver.exe")



browser.get('https://www.torrentday.com/TopTorrents.php')

tables  = browser.find_elements_by_class_name("t1")

tables_dict = {}

for i in range(1,len(tables)+1):
    
    table_elem = browser.find_element_by_xpath(
        f'/html/body/div/main/table[{i}]')

    tbody = table_elem.find_element_by_tag_name('tbody')    

    table_rows = tbody.find_elements_by_tag_name("tr")
    
    for row in table_rows:
        print(row)
