from bs4 import BeautifulSoup
import requests
import json
from flask import Flask, render_template, jsonify, request

global job_type_box
job_type_box = '1'
global URL



def get_last_page():
    result = requests.get(URL)

    # 뷰티풀숩을 사용해 Html을 전체 가져온다.
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class":"tplPagination newVer wide"}).find_all("li")
    if pagination is not None:
        last_page = pagination[-1].get_text()
        return int(last_page)
    else:
        return 0    

def extract_jobs(last_page):
    jk_jobs = []
    # for page in range(last_page):
    for page in range(1):
    #for page in range(1):
        print(f"Job-Koera page : {page+1}")
        result = requests.get(URL+f'&Page_No={page}')
        soup = BeautifulSoup(result.text, 'html.parser')
        list_default = soup.find("div", {"class":"list-default"})
        jobs_page = list_default.find_all("div", {"class":"post"})

        for job in jobs_page:
            #job = extract_job(jobs_page)
            companys_a = job.find("div", {"class":"post-list-corp"}).find("a")
            companys = companys_a.string
            if companys is not None:
                companys = companys
            else :
                companys = companys_a['title']
            positions = job.find("div", {"class":"post-list-info"}).find("a")["title"]
            locations = job.find("div", {"class":"post-list-info"}).find("p").find("span", {"class":"loc short"}).string
            # ##질문!!! 여기서 구, 동을 가져오고 싶다.
            # # job_type = job.find("div", {"class":"job_condition"}).find_all("span").string
            links = job.find("div", {"class":"post-list-info"}).find("a")["href"]
            links = f'http://www.jobkorea.co.kr{links}'


            # jobs_kind = {'company':companys, 'positions':positions, 'locations':locations, 'links':links, 'job_type':job_type}
            jobs_kind = {'companys':companys, 'positions':positions, 'locations':locations, 'links':links }

            # print(jobs_kind)
            jk_jobs.append(jobs_kind)
             
    return jk_jobs

def jk_get_jobs(input_keyword_recieve, input_location_recieve, input_jobtype_recieve):


    if input_jobtype_recieve == '전체(근무 형태)':
        input_jobtype = ''
    elif input_jobtype_recieve == '정규직':
        input_jobtype = 1
    elif input_jobtype_recieve == '계약직':
        input_jobtype = 2
    elif input_jobtype_recieve == '인턴':
        input_jobtype = 3
    elif input_jobtype_recieve == '아르바이트':
        input_jobtype = 7
    elif input_jobtype_recieve == '병역특례':
        input_jobtype = 9


    if input_location_recieve == '전체(희망 지역)':
        input_location = ''
    elif input_location_recieve == '서울':
        input_location = 'I000'
    elif input_location_recieve == '경기':
        input_location = 'B000'
    elif input_location_recieve == '인천':
        input_location = 'K000'
    elif input_location_recieve == '부산':
        input_location = 'H000'
    elif input_location_recieve == '대구':
        input_location = 'F000'
    elif input_location_recieve == '광주':
        input_location = 'E000'
    elif input_location_recieve == '대전':
        input_location = 'G000'
    elif input_location_recieve == '울산':
        input_location = 'J000'
    elif input_location_recieve == '세종':
        input_location = '1000'
    elif input_location_recieve == '강원':
        input_location = 'A000'
    elif input_location_recieve == '경남':
        input_location = 'C000'
    elif input_location_recieve == '경북':
        input_location = 'D000'
    elif input_location_recieve == '전남':
        input_location = 'L000'
    elif input_location_recieve == '전북':
        input_location = 'M000'
    elif input_location_recieve == '충남':
        input_location = 'O000'
    elif input_location_recieve == '충북':
        input_location = 'P000'
    elif input_location_recieve == '제주':
        input_location = 'N000'


    global URL
    global job_type_box

    URL = f'http://www.jobkorea.co.kr/Search/?stext={input_keyword_recieve}&local={input_location}&jobtype={input_jobtype}&tabType=recruit'

    print(URL)
    last_page = get_last_page()      # 최대 페이지를 정의하는 함수를 변수에 넣는다.
    jk_jobs = extract_jobs(last_page)      #최대 페이지를 정의하는 함수를 넣은 변수를 인자로 넣고 함수를 실행한다.

    return jk_jobs
    # return jsonify ({'result':'success','jk_jobs':jk_jobs})
    
