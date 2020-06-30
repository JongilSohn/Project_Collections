
from bs4 import BeautifulSoup
import requests
import json
from flask import Flask, render_template, jsonify, request

from news import news_card
from indeed import id_get_jobs
from saramin import sa_get_jobs
from job_korea import jk_get_jobs

app = Flask(__name__)


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('Jobs_collection.html')


@app.route('/api/news', methods=['GET'])
def get_news():
    return news_card()


@app.route('/api/saramin', methods=['GET'])
def get_saramin_jobs():
    input_keyword_recieve = request.args.get('input_keyword_give')
    input_location_recieve = request.args.get('input_location_give')
    input_jobtype_recieve = request.args.get('input_jobtype_give')
    # print(input_keyword_recieve)
    # print(input_location_recieve)
    # print(input_jobtype_recieve)
    sa_jobs = sa_get_jobs(input_keyword_recieve, input_location_recieve, input_jobtype_recieve)
    # return sa_get_jobs()
    # return id_get_jobs()
    return jsonify ({'result':'success','sa_jobs':sa_jobs})
    


@app.route('/api/indeed', methods=['GET'])
def get_indeed_jobs():
    input_keyword_recieve = request.args.get('input_keyword_give')
    input_location_recieve = request.args.get('input_location_give')
    input_jobtype_recieve = request.args.get('input_jobtype_give')
    # print(input_keyword_recieve)
    # print(input_location_recieve)
    # print(input_jobtype_recieve)
    id_jobs = id_get_jobs(input_keyword_recieve, input_location_recieve, input_jobtype_recieve)
    # return sa_get_jobs()
    # return id_get_jobs()
    return jsonify ({'result':'success','id_jobs':id_jobs})
    
    

@app.route('/api/job_korea', methods=['GET'])
def get_job_korea_jobs():
    input_keyword_recieve = request.args.get('input_keyword_give')
    input_location_recieve = request.args.get('input_location_give')
    input_jobtype_recieve = request.args.get('input_jobtype_give')
    # print(input_keyword_recieve)
    # print(input_location_recieve)
    # print(input_jobtype_recieve)
    jk_jobs = jk_get_jobs(input_keyword_recieve, input_location_recieve, input_jobtype_recieve)
    # return sa_get_jobs()
    # return jk_get_jobs()
    return jsonify ({'result':'success','jk_jobs':jk_jobs})

@app.route('/api/total', methods=['GET'])
def get_total_jobs():
    # return sa_get_jobs()
    input_keyword_recieve = request.args.get('input_keyword_give')
    input_location_recieve = request.args.get('input_location_give')
    input_jobtype_recieve = request.args.get('input_jobtype_give')
    print(input_keyword_recieve)
    print(input_location_recieve)
    print(input_jobtype_recieve)
    jk_jobs = jk_get_jobs(input_keyword_recieve, input_location_recieve, input_jobtype_recieve)
    sa_jobs = sa_get_jobs(input_keyword_recieve, input_location_recieve, input_jobtype_recieve)
    id_jobs = id_get_jobs(input_keyword_recieve, input_location_recieve, input_jobtype_recieve)
    # print(type(jk_jobs), jk_jobs)
    # print(type(b))
    
    return jsonify ({'result':'success','jk_jobs':jk_jobs, 'sa_jobs':sa_jobs, 'id_jobs':id_jobs})

    
if __name__ == '__main__':
    app.run('localhost', port=10038, debug=True)
# print(news_craw())