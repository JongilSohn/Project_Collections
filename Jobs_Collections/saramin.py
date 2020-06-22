
from bs4 import BeautifulSoup
import requests
import json
from flask import Flask, render_template, jsonify, request

global URL
global URL_op 


def get_last_page():
    result = requests.get(URL)

    # 뷰티풀숩을 사용해 Html을 전체 가져온다.
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class":"pagination"}).find_all("span")

    if pagination is not None:
        last_page = pagination[-1].get_text()
        return int(last_page)
    else :
        return 0

def extract_jobs(last_page):
    sa_jobs = []
    # for page in range(last_page):
    for page in range(1):
    #for page in range(1):
        print(f"Saramin page : {page+1}")
        result = requests.get(URL+f'&recruitPage={page+1}'+URL_op)
        print(URL+f'&recruitPage={page+1}'+URL_op)
        soup = BeautifulSoup(result.text, 'html.parser')
        jobs_page = soup.find_all("div", {"class":"item_recruit"})


        for job in jobs_page:
            #job = extract_job(jobs_page)
            companys = job.find("strong", {"class":"corp_name"}).find("a")["title"]
            positions = job.find("h2", {"class":"job_tit"}).find("a")["title"]
            locations = job.find("div", {"class":"job_condition"}).find("a").string
            ##질문!!! 여기서 구, 동을 가져오고 싶다.
            #job_type = job.find("div", {"class":"job_condition"}).find_all("span")[3].string
            links = job.find("h2", {"class":"job_tit"}).find("a")["href"]
            links = f'http://www.saramin.co.kr{links}'           
            jobs_kind = {'companys':companys, 'positions':positions, 'locations':locations, 'links':links }

            
            #print(jobs_kind)
            sa_jobs.append(jobs_kind)
             
    # print(sa_jobs)
    return sa_jobs

def sa_get_jobs(input_keyword_recieve, input_location_recieve, input_jobtype_recieve):
    
    

    if input_jobtype_recieve == '전체(근무 형태)':
        input_jobtype = ''
    elif input_jobtype_recieve == '정규직':
        input_jobtype = 1
    elif input_jobtype_recieve == '계약직':
        input_jobtype = 2
    elif input_jobtype_recieve == '인턴':
        input_jobtype = 4
    elif input_jobtype_recieve == '아르바이트':
        input_jobtype = 5
    elif input_jobtype_recieve == '병역특례':
        input_jobtype = 3


    if input_location_recieve == '전체(희망 지역)':
        input_location = ''
    elif input_location_recieve == '서울':
        input_location = 101000
    elif input_location_recieve == '경기':
        input_location = 102000
    elif input_location_recieve == '인천':
        input_location = 108000
    elif input_location_recieve == '부산':
        input_location = 106000
    elif input_location_recieve == '대구':
        input_location = 104000
    elif input_location_recieve == '광주':
        input_location = 103000
    elif input_location_recieve == '대전':
        input_location = 105000
    elif input_location_recieve == '울산':
        input_location = 107000
    elif input_location_recieve == '세종':
        input_location = 118000
    elif input_location_recieve == '강원':
        input_location = 109000
    elif input_location_recieve == '경남':
        input_location = 110000
    elif input_location_recieve == '경북':
        input_location = 111000
    elif input_location_recieve == '전남':
        input_location = 112000
    elif input_location_recieve == '전북':
        input_location = 113000
    elif input_location_recieve == '충남':
        input_location = 115000
    elif input_location_recieve == '충북':
        input_location = 114000
    elif input_location_recieve == '제주':
        input_location = 116000

    print("검색어는", input_keyword_recieve)
    print("근무형태 입력은", input_jobtype)
    print("위치 입력은", input_location)

    global URL
    global URL_op

    URL_op = f'&recruitSort=relation&recruitPageCount=40&inner_com_type=&quick_apply='
    URL = f'http://www.saramin.co.kr/zf_user/search/recruit?searchType=search&searchword={input_keyword_recieve}&company_cd=0,1,2,3,4,5,6,7,9&loc_mcd={input_location}&job_type={input_jobtype}&panel_type=&search_optional_item=y&search_done=y&panel_count=y'
    

    last_page = get_last_page()      # 최대 페이지를 정의하는 함수를 변수에 넣는다.
    sa_jobs = extract_jobs(last_page)      #최대 페이지를 정의하는 함수를 넣은 변수를 인자로 넣고 함수를 실행한다.
    # print(sa_jobs)
    # return sa_jobs

    return sa_jobs
    # return jsonify ({'result':'success','sa_jobs':sa_jobs})