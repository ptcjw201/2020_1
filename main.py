import re

import pyperclip
import requests
import time
import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains, Keys

def findRealLink(url):
    response = requests.get(url)

    # 웹 페이지 HTML Parse
    htmlSource = requests.get(url).text
    print(htmlSource)

    # BeautifulSoup HTML PARSE
    srcMatches = BeautifulSoup(htmlSource, 'html.parser')

    # src 태그 확인

    # iframe 태그 확인
    iframe = srcMatches.find('iframe', id = 'mainFrame')

    if iframe:
        # iframe의 src 찾기
        src = iframe.get('src')
        # 네이버 블로그 실 주소
        naverBlog = "https://blog.naver.com" + src
        print('네이버 블로그 실 주소 : ', naverBlog)
        # clickCommentButton(naverBlog)
        linksWithPageNo = findPageLogNo(naverBlog)
        login(naverBlog)
    else :
        raise Exception('블로그 주소를 불러올 수 없습니다.')

def findPageLogNo(url2):

    htmlSource = requests.get(url2).text

    match = re.search(r'source\s*:\s*"([^"]+)"', htmlSource)
    # 첫 번째 logNo 추출
    if match:
        first_log_no = match.group(1)
        return [first_log_no]
    else:
        raise Exception('Page No(source : ~) 찾을 수 없습니다.')
def login(naverBlog):
    # 크롬 드라이버
    options = ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    loginLink = "https://nid.naver.com/nidlogin.login"

    driver.get(loginLink)
    # 아이디 ㅣ 비번
    testId = "peterjw201"
    testPw = "Octdec1019!"

    # 자동 로그인 방지 우회를 위한 PyperClip
    idInput = driver.find_element(By.ID, "id")
    idInput.click()
    pyperclip.copy(testId)
    pyautogui.keyDown("command")
    pyautogui.press("v")
    pyautogui.keyUp("command")
    actions = ActionChains(driver)
    # Window 용
    # actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

    pwInput = driver.find_element(By.ID, "pw")
    pwInput.click()
    pyperclip.copy(testPw)
    pyautogui.keyDown("command")
    pyautogui.press("v")
    pyautogui.keyUp("command")
    actions = ActionChains(driver)
    # Window 용
    # actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

    # 로그인 버튼 클릭
    driver.find_element(By.ID, "log.login").click()
    time.sleep(1)

    # user_agent = driver.execute_script("return navigator.userAgent")
    #
    # # 로그인 세션 유지
    # s = requests.Session()
    # # 세션 헤더
    # headers = {
    #     'User-Agent' : user_agent
    # }
    # s.headers.update(headers)
    # print("Headers" , headers)
    #
    # loginCookies = driver.get_cookies()
    # cookieDict = {}
    # for loginCookie in loginCookies:
    #     cookieDict[loginCookie['name']] = loginCookie['value']
    # print(cookieDict)
    # s.cookies.update(cookieDict)

    clickCommentButton(driver, naverBlog)

def clickCommentButton(driver, naverBlog):
    # 크롬 드라이버
    driver.get(naverBlog)

    comment = "#printPost1 > tbody > tr > td.bcc > div.post-btn.post_btn2 > div.wrap_postcomment > div.area_comment.pcol2"
    commentElement = driver.find_element(By.CSS_SELECTOR, comment)
    driver.execute_script("arguments[0].scrollIntoView(true);", commentElement)
    commentElement.click()



if __name__ == '__main__':
    url = input("네이버 블로그 주소를 입력해주세요 : ")
    findRealLink(url)


