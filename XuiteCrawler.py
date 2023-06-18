from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
#載入相關模組

options = Options()
options.chrome_executable_path = "E:\sideproject\chromedriver.exe"
#設定Chrome Driver的執行檔路徑

driver = webdriver.Chrome(options=options)
driver.maximize_window() #視窗最大化
#建立 driver 物件實體，用程式操作瀏覽器運作

# ---------------------------------------------------------------------------
#此次爬蟲因為隨意窩的文章連結有些問題
#所以必須分成三次爬蟲，確保每一篇文章的內容都完整

all_article = []
#設定全部文章標題+內容的變數用來存放標題+文章
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
#第一次執行爬蟲
driver.get("https://blog.xuite.net/ttii5566/twblog/589328741")
#連線到隨意窩的目標網站(的第一篇文章)
time.sleep(1)
#等待連線1秒

link = driver.find_element(By.CLASS_NAME,"selectbar")
next_link = link.text.split("|")
next_link = next_link[0]
#取得"上一則"的標籤

while next_link != "沒有上一則":
    title = driver.find_element(By.CLASS_NAME,"titlename")
    content = driver.find_element(By.ID,"content_all")
    columns = content.text.split("\n")
    #因為有時候content.text會包含除了內文以外的廣告內容文字
    #所以必須多寫一個columns分割文字檔案
    all_article.append(title.text)
    # all_article.append(columns[0])
    #將取得的標題+內容加入"所有文章"變數中

    target = driver.find_element(By.CLASS_NAME,"posted")
    #取得"posted"的標籤
    driver.execute_script("arguments[0].scrollIntoView();", target)
    #此處是因為隨意窩本身有許多彈出視窗
    #用此方式定位出"上一則"標籤的位置方便點擊

    nextpage = driver.find_element(By.LINK_TEXT, next_link)
    nextpage.click()
    #連結到下一頁
    time.sleep(1)
    #等1秒
    link = driver.find_element(By.CLASS_NAME,"selectbar")
    next_link = link.text.split("|")
    next_link = next_link[0]
    #重新取得下一篇文章的"上一則"標籤
#藉由迴圈重複執行取得上一篇的資料

title = driver.find_element(By.CLASS_NAME,"titlename")
content = driver.find_element(By.ID,"content_all")
columns = content.text.split("\n")
all_article.append(title.text)
# all_article.append(columns[0])
#由於進入最後一頁會先判定文字是否為"沒有上一則"因此不進入迴圈取得資料
#但最後一頁的資料必須再取得一次，所以直接採取再取得一次資料的動作
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
#第二次執行爬蟲
driver.get("https://blog.xuite.net/ttii5566/twblog/573676470")
#連線到隨意窩的目標網站(的第一篇文章)
time.sleep(1)
#等待連線1秒

link = driver.find_element(By.CLASS_NAME,"selectbar")
next_link = link.text.split("|")
next_link = next_link[0]
#取得"上一則"的標籤

while next_link != "沒有上一則":
    title = driver.find_element(By.CLASS_NAME,"titlename")
    content = driver.find_element(By.ID,"content_all")
    columns = content.text.split("\n")
    #因為有時候content.text會包含除了內文以外的廣告內容文字
    #所以必須多寫一個columns分割文字檔案
    all_article.append(title.text)
    # all_article.append(columns[0])
    #將取得的標題+內容加入"所有文章"變數中

    target = driver.find_element(By.CLASS_NAME,"posted")
    #取得"posted"的標籤
    driver.execute_script("arguments[0].scrollIntoView();", target)
    #此處是因為隨意窩本身有許多彈出視窗
    #用此方式定位出"上一則"標籤的位置方便點擊

    nextpage = driver.find_element(By.LINK_TEXT, next_link)
    nextpage.click()
    #連結到下一頁
    time.sleep(1)
    #等1秒
    link = driver.find_element(By.CLASS_NAME,"selectbar")
    next_link = link.text.split("|")
    next_link = next_link[0]
    #重新取得下一篇文章的"上一則"標籤
#藉由迴圈重複執行取得上一篇的資料

title = driver.find_element(By.CLASS_NAME,"titlename")
content = driver.find_element(By.ID,"content_all")
columns = content.text.split("\n")
all_article.append(title.text)
# all_article.append(columns[0])
#由於進入最後一頁會先判定文字是否為"沒有上一則"因此不進入迴圈取得資料
#但最後一頁的資料必須再取得一次，所以直接採取再取得一次資料的動作
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
#第三次執行爬蟲
driver.get("https://blog.xuite.net/ttii5566/twblog/434515654")
#連線到隨意窩的目標網站(的第一篇文章)
time.sleep(1)
#等待連線1秒

link = driver.find_element(By.CLASS_NAME,"selectbar")
next_link = link.text.split("|")
next_link = next_link[0]
#取得"上一則"的標籤

while next_link != "沒有上一則":
    title = driver.find_element(By.CLASS_NAME,"titlename")
    content = driver.find_element(By.ID,"content_all")
    columns = content.text.split("\n")
    #因為有時候content.text會包含除了內文以外的廣告內容文字
    #所以必須多寫一個columns分割文字檔案
    all_article.append(title.text)
    # all_article.append(columns[0])
    #將取得的標題+內容加入"所有文章"變數中

    target = driver.find_element(By.CLASS_NAME,"posted")
    #取得"posted"的標籤
    driver.execute_script("arguments[0].scrollIntoView();", target)
    #此處是因為隨意窩本身有許多彈出視窗
    #用此方式定位出"上一則"標籤的位置方便點擊

    nextpage = driver.find_element(By.LINK_TEXT, next_link)
    nextpage.click()
    #連結到下一頁
    time.sleep(1)
    #等1秒
    link = driver.find_element(By.CLASS_NAME,"selectbar")
    next_link = link.text.split("|")
    next_link = next_link[0]
    #重新取得下一篇文章的"上一則"標籤
#藉由迴圈重複執行取得上一篇的資料

title = driver.find_element(By.CLASS_NAME,"titlename")
content = driver.find_element(By.ID,"content_all")
columns = content.text.split("\n")
all_article.append(title.text)
# all_article.append(columns[0])
#由於進入最後一頁會先判定文字是否為"沒有上一則"因此不進入迴圈取得資料
#但最後一頁的資料必須再取得一次，所以直接採取再取得一次資料的動作
driver.close()
# ---------------------------------------------------------------------------
print(all_article)
