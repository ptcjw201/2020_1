import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy import stats


def Q1():
    searcher = input("검색어 입력: ")
    starting_date = input("시작 날짜(xxxx.xx.xx): ")
    ending_date = input("끝나는 날짜(xxxx.xx.xx): ")
    key_words = urllib.parse.quote(searcher)
    url = "https://search.naver.com/search.naver?where=news&query=" + key_words + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
          + starting_date + "&de=" + ending_date + "&docid=&nso=so%3Ar%2Cp%3Afrom" +starting_date.replace(".","") + "to" + \
          ending_date.replace(".","") + "%2Ca%3Aall&mynews=0&refresh_start=0&related=0"
    req = urllib.request.urlopen(url)
    data = req.read()
    soup = BeautifulSoup(data, 'html.parser')
    anchor_set = soup.findAll("a")
    news_link = []
    for urls in anchor_set:
        try:
            if urls["href"].startswith("https://news.naver.com/main/read.nhn"):
                news_link.append(urls["href"])
        except Exception as e:
            print(e)
            continue
    for i in news_link:
        print(i)


def Q2():
    searcher = input("검색어 입력: ")
    starting_date = input("시작 날짜(xxxx.xx.xx): ")
    ending_date = input("끝나는 날짜(xxxx.xx.xx): ")
    key_words = urllib.parse.quote(searcher)
    url = "https://search.naver.com/search.naver?where=news&query=" + key_words + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
          + starting_date + "&de=" + ending_date + "&docid=&nso=so%3Ar%2Cp%3Afrom" +starting_date.replace(".","") + "to" + \
          ending_date.replace(".","") + "%2Ca%3Aall&mynews=0&refresh_start=0&related=0"
    req = urllib.request.urlopen(url)
    data = req.read()
    soup = BeautifulSoup(data, 'html.parser')
    count_tag = soup.find("div", {"class", "title_desc all_my"})
    count_text = count_tag.find("span").get_text().split()
    total_num = count_text[-1][0:-1].replace(",", "")
    new_link = []
    for val in range(int(total_num) // 10 + 1):
        start_val = str(val * 10 + 1)
        urls = "https://search.naver.com/search.naver?&where=news&query=" + key_words + "&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
               + starting_date + "&de=" + ending_date + "&docid=&nso=so:r,p:from" + starting_date.replace(".", "") + "to" + \
               ending_date.replace(".","") + ",a:all&mynews=0&cluster_rank=15&start=" + start_val + "&refresh_start=0"
        req = urllib.request.urlopen(urls)
        data = req.read()
        soup = BeautifulSoup(data, 'html.parser')
        anchor_set = soup.findAll("a")
        for u in anchor_set:
            try:
                if u["href"].startswith("https://news.naver.com/main/read.nhn"):
                    new_link.append(u["href"])
            except Exception as e:
                print(e)
                continue
    #list 에서의 중복을 제거하기 위해 set형(중복을 인정하지 않음)으로 바꾼뒤 다시 list형으로 바꿈
    new_link = list(set(new_link))
    for i in new_link:
        print(i)

def Q3():
    searcher = input("검색어 입력: ")
    starting_date = input("시작 날짜(xxxx.xx.xx): ")
    ending_date = input("끝나는 날짜(xxxx.xx.xx): ")
    key_words = urllib.parse.quote(searcher)
    url = "https://search.naver.com/search.naver?where=news&query=" + key_words + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
          + starting_date + "&de=" + ending_date + "&docid=&nso=so%3Ar%2Cp%3Afrom" + starting_date.replace(".", "") + "to" \
          + ending_date.replace(".", "") + "%2Ca%3Aall&mynews=0&refresh_start=0&related=0"
    req = urllib.request.urlopen(url)
    data = req.read()
    soup = BeautifulSoup(data, 'html.parser')
    count_tag = soup.find("div", {"class", "title_desc all_my"})
    count_text = count_tag.find("span").get_text().split()
    total_num = count_text[-1][0:-1].replace(",", "")

    new_link = []
    for val in range(int(total_num) // 10 + 1):
        start_val = str(val * 10 + 1)
        urls = "https://search.naver.com/search.naver?&where=news&query=" + key_words + "&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
               + starting_date + "&de=" + ending_date + "&docid=&nso=so:r,p:from" + starting_date.replace(".", "") + "to" + ending_date.replace(".","") \
               + ",a:all&mynews=0&cluster_rank=15&start=" + start_val + "&refresh_start=0"
        req = urllib.request.urlopen(urls)
        data = req.read()
        soup = BeautifulSoup(data, 'html.parser')
        anchor_set = soup.findAll("a")
        for u in anchor_set:
            try:
                if u["href"].startswith("https://news.naver.com/main/read.nhn"):
                    new_link.append(u["href"])
            except Exception as e:
                print(e)
                continue
    new_link = list(set(new_link))

    title_list = []
    text_list = []
    for links in new_link:
        req = urllib.request.urlopen(links)
        data = req.read()
        soup = BeautifulSoup(data, 'html.parser')
        set1 = soup.find("h3", {"id": "articleTitle"})
        for titles in set1:
            title_list.append(titles)
        set2 = soup.find("div", {"id": "articleBodyContents"})
        for atcs in set2:
            text_list.append(atcs)
    #title_list 에 기사 제목이, text_list 에 기사 내용이 담겨있다
    for i in title_list:
        print(i)
    for j in text_list:
        print(j)

def Q4():
    searcher = input("검색어 입력: ")
    starting_date = input("시작 날짜(xxxx.xx.xx): ")
    ending_date = input("끝나는 날짜(xxxx.xx.xx): ")
    key_words = urllib.parse.quote(searcher)
    url = "https://search.naver.com/search.naver?where=news&query=" + key_words + "&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
          + starting_date + "&de=" + ending_date + "&docid=&nso=so%3Ar%2Cp%3Afrom" + starting_date.replace(".", "") + "to" \
          + ending_date.replace(".", "") + "%2Ca%3Aall&mynews=0&refresh_start=0&related=0"
    req = urllib.request.urlopen(url)
    data = req.read()
    soup = BeautifulSoup(data, 'html.parser')
    count_tag = soup.find("div", {"class", "title_desc all_my"})
    count_text = count_tag.find("span").get_text().split()
    total_num = count_text[-1][0:-1].replace(",", "")

    new_link = []
    for val in range(int(total_num) // 10 + 1):
        start_val = str(val * 10 + 1)
        urls = "https://search.naver.com/search.naver?&where=news&query=" + key_words + "&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=" \
               + starting_date + "&de=" + ending_date + "&docid=&nso=so:r,p:from" + starting_date.replace(".", "") + "to" \
               + ending_date.replace(".","") + ",a:all&mynews=0&cluster_rank=15&start=" + start_val + "&refresh_start=0"
        req = urllib.request.urlopen(urls)
        data = req.read()
        soup = BeautifulSoup(data, 'html.parser')
        anchor_set = soup.findAll("a")
        for u in anchor_set:
            try:
                if u["href"].startswith("https://news.naver.com/main/read.nhn"):
                    new_link.append(u["href"])
            except Exception as e:
                print(e)
                continue
    new_link = list(set(new_link))

    title_list = []
    text_list = []
    for links in new_link:
        req = urllib.request.urlopen(links)
        data = req.read()
        soup = BeautifulSoup(data, 'html.parser')
        set1 = soup.find("h3", {"id": "articleTitle"})
        for titles in set1:
            title_list.append(titles)
        set2 = soup.find("div", {"id": "articleBodyContents"})
        for atcs in set2:
            text_list.append(atcs)
    for titles in title_list:
        titles = titles.rstrip()
        if re.findall('\S?금리.*인하\S?', titles):
            print(titles)

def Q5():
    # Q5
    csv_path = "boston_csv.csv"
    list = []
    # 1
    missing_values = ["na", "NaN"]
    df = pd.read_csv(csv_path, na_values=missing_values)
    # 2
    df = df.dropna()
    print(df)


def Q6():
    csv_path = "boston_csv.csv"
    list = []
    missing_values = ["na", "NaN"]
    df = pd.read_csv(csv_path, na_values=missing_values)
    df = df.dropna()
    print(df.describe())
    print("-----------Below are correlations-----------")
    print(df.corr())
    ax = sns.heatmap(df.corr())
    plt.title("HEATMAP")
    plt.show()


def Q7():
    csv_path = "boston_csv.csv"
    list = []
    missing_values = ["na", "NaN"]
    df = pd.read_csv(csv_path, na_values=missing_values)
    df = df.dropna()
    Im = LinearRegression()
    x_data = df[["LSTAT"]]
    y_data = df["MEDV"]
    x_train , x_test , y_train , y_test = train_test_split(x_data, y_data, test_size = 0.25, random_state = 0)
    Im.fit(x_train, y_train)
    print(Im.intercept_)
    print(Im.coef_)
    print(Im.score(x_train,y_train))
    Y1hat = Im.predict(x_train)
    print(mean_squared_error(y_train, Y1hat))
    Y2hat = Im.predict(x_test)
    print(mean_squared_error(y_test, Y2hat))


def Q8():
    csv_path = "boston_csv.csv"
    list = []
    missing_values = ["na", "NaN"]
    df = pd.read_csv(csv_path, na_values=missing_values)
    df = df.dropna()
    Im = LinearRegression()
    x_data = df[["LSTAT", "TAX"]]
    y_data = df["MEDV"]
    x_train , x_test , y_train , y_test = train_test_split(x_data, y_data, test_size = 0.25, random_state = 0)
    Im.fit(x_train, y_train)
    print(Im.intercept_)
    print(Im.coef_)
    print(Im.score(x_train,y_train))
    Y1hat = Im.predict(x_train)
    print(mean_squared_error(y_train, Y1hat))
    Y2hat = Im.predict(x_test)
    print(mean_squared_error(y_test, Y2hat))

def main():
#   과제번호에 해당하는 함수의 주석을 제거하시면 됩니다.
#   Q1()
#   Q2()
#   Q3()
#   Q4()
#   Q5()
#   Q6()
#   Q7()
#   Q8()
    return 0


main()