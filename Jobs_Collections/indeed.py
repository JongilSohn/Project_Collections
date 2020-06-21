
from bs4 import BeautifulSoup
import requests
import json
import re
from flask import Flask, render_template, jsonify, request


global URL
global LIMIT
LIMIT = 20


def get_last_page():
    result = requests.get(URL)

    # 뷰티풀숩을 사용해 Html을 전체 가져온다.
    soup = BeautifulSoup(result.text, 'html.parser')

    # page 수를 찾기 위해 해당 div를 가져와서 확인한다.
    pagination = soup.find("div", {"class": "pagination"})

    if pagination is not None:
        
        links = pagination.find_all('a')  # 가져온것에서 페이지의 링크 수를 찾아온다.
        pages = []  # 링크에서 span이 붙은것만 빼와서 리스트에 저장한다. 뒤에 짜잘한것을 없애주기 위해.

    # Operation spans[-1] 하면 맨 마지막것을 칭한다.  So, [:-1]은 span을 가져오되 마지막 하나를 제외한다.
        for link in links[:-1]:
        # [0:5]하면 0부터 5까지 가져온다.
        # pages.append(link.find("span"))
        # pages.append(link.find("span").string)      #<sapn>1<span/>, <span>2><span/> 에서 문자만 가져오기 위해 string 사용

        # pages.append(link.string)   #바로 위의 결과와 같게 나온다. 위에 것을 쉽게 만든것이다. 링크 안에는 많은 내용이 있지만 string은 단 1개이다.
          pages.append(int(link.string))  # 위에것을 가져오면 문자열이기때문에 정수형으로 바꿔준다.
        # print(page)
        # Operation spans[-1] 하면 맨 마지막것을 칭한다.  So, [:-1]은 span을 가져오되 마지막 하나를 제외한다.
        # [0:5]하면 0부터 5까지 가져온다.
        # print(pages) 최종적으로 가져온 페이지의 수는 2, 3, 4, 5 이렇게 정수형으로만 가져온다.
        # 이렇게 하게되면 Page의 총 갯수를 불러오게 된다.

    # 1.  가장 마지막 페이지를 가져온다.
    # print(pages[-1]) #마지막것 1개를 출력한다.
        max_page = pages[-1]  # 가장 마지막 페이지를 찾아 변수로 지정한다.
    # print(range(max_page))  # range를 사용하여 0부터 maxpage까지 출력
        return max_page
    else:
        return 0


def extract_job(html):
    company_a = str(html.find("span", {"class": "company"}))
    companys= re.sub('<.+?>', '', company_a, 0).strip()

    # if companys is not None:
    #     companys = companys
    # else :
    #     companys_b = companys_a.find("b")
    #     companys = companys_a.string
    #     print(companys)


    positions = html.find("a", {"data-tn-element": "jobTitle"})["title"]
    locations_span = html.find(
        "span", {"class": "location accessible-contrast-color-location"})
    if locations_span is not None:
        locations = locations_span.string
    else:
        locations = '위치정보는 링크를 통해서 확인'
    job_id = html["data-jk"]
    # income_span = html.find("span", {"class": "salaryText"})
    # if income_span is not None:
    #     income = income_span.string.strip()    
    # else:
    #     income = '회사 내규에 따름'
    links = f'https://kr.indeed.com/viewjob?jk={job_id}&tk=1e9t47m537los801&from=serp&vjs=3'


    # return {'company': company, 'position': position, 'location': location, 'link': link, 'income': income}
    return {'companys': companys, 'positions': positions, 'locations': locations, 'links': links }

# wep page를 넘길때마다 start=0, 20, 40 넘어가는 규칙을 사용하기 위해 x20을 해준다.
def extracts_jobs(last_page):
    id_jobs = []
    # for page in range(last_page):
    for page in range(1):
        print(f"Scrapping Indeed : Page : {page+1}")
        # URL을 추가하고 page수와 LIMIT을 정하는 문자열을 연결시켜주었다.
        #print(URL)
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        # print(soup)
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job = extract_job(result)
            id_jobs.append(job)
    return id_jobs

        
def id_get_jobs(input_keyword_recieve, input_location_recieve, input_jobtype_recieve):
    

    global URL
    global LIMIT
    LIMIT = 20
    
    if input_location_recieve == '전체(희망 지역)':
        input_location = ''
    else:
        input_location = input_location_recieve


    if input_jobtype_recieve == '전체(근무 형태)':
        input_jobtype = ''
    elif input_jobtype_recieve == '정규직':
        input_jobtype = 'fulltime'
    elif input_jobtype_recieve == '계약직':
        input_jobtype = 'contract'
    elif input_jobtype_recieve == '인턴':
        input_jobtype = 'internship'
    elif input_jobtype_recieve == '아르바이트':
        input_jobtype = 'parttime'
    elif input_jobtype_recieve == '병역특례':
        input_jobtype = 'custom_1'

    print("검색어는", input_keyword_recieve)
    print("근무형태 입력은", input_jobtype)
    print("위치 입력은", input_location)

    URL = f'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q={input_keyword_recieve}&l={input_location}&jt={input_jobtype}&limit={LIMIT}&radius=25'
    print(URL)
    last_page = get_last_page()      # 최대 페이지를 정의하는 함수를 변수에 넣는다.
    id_jobs = extracts_jobs(last_page)      #최대 페이지를 정의하는 함수를 넣은 변수를 인자로 넣고 함수를 실행한다.
    
    return id_jobs
    # return jsonify ({'result':'success','id_jobs':id_jobs})
