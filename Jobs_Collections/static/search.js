
const header_input = document.querySelector("#header_input");
const input_div = header_input.querySelector("#input_div");
const search_btn = input_div.querySelector(".search_btn");

const Total_logo = document.querySelector(".Total_show")
const Job_Koera_logo = document.querySelector(".JobKorea_show")
const Saramin_logo = document.querySelector(".Saramin_show")
const Indeed_logo = document.querySelector(".Indeed_show")

const Total_class = document.querySelector("#section_total")
const Job_Koera_class = document.querySelector("#section_Job_Korea")
const Saramin_class = document.querySelector("#section_Saramin")
const Indeed_class = document.querySelector("#section_Indeed")


const section_recruit_info = document.querySelector("#section_total");
const section_news_info = document.querySelector("#hot_jobs");

const jobs_num_box = document.querySelector("#recruit_info_number")
const jobs_num = jobs_num_box.querySelector("h4")

const jobs_potal_div = document.querySelector("#recruit_info_box")
const jobs_potal_h = jobs_potal_div.querySelector("h2")
const jobs_potal = jobs_potal_h.querySelector("strong")


const input_keyword_box = document.querySelector(".input_company")
const input_potal_box = document.querySelector(".input_potal")
const input_location_box = document.querySelector(".input_location")
const input_jobtype_box = document.querySelector(".input_jobtype")

const pocket_bar = document.querySelector("#fixedbtn")

const like_list = document.querySelector("#like_list")

const like_list_LS = 'like_company';


const loadingbar = document.querySelector("#loadingbar_center")
const None_info = document.querySelector("#None_info")

let like_list_ar = []



function like_del(del_company, del_link){
    const del_btn = event.target;
    const li = del_btn.parentNode;  
    like_list.removeChild(li);

    localStorage.removeItem('test');
    // console.log(localStorage.getItem(like_list_LS))
    // console.log(like_list_ar.length)

    for(let i = 0; i <like_list_ar.length; i++){
        if (like_list_ar[i]['like_company'] === del_company){
            localStorage.removeItem(like_list_ar[i]);
            console.log(like_list_ar[i])
        }
    }


    // const loaded_like = localStorage.getItem(like_list_LS);
    
    // console.log(loaded_like)
    
    // if (loaded_like !== null) {
    //     const parsed_like = JSON.parse(loaded_like);
    //     parsed_like.forEach(function (like) {
    //         if (like['like_company']===del_company){
    //         console.log(like)
    //         console.log("삭제함수", del_company)
    //         localStorage.removeItem(like);
    //     }})
    // }


    // const like_del_LS = like_list_ar.filter(function(like_list_ar){
    //     return 
    // })

}



function handleClick_like(like_company, like_link) {
    const newId = like_list_ar.length + 1
    let like_html = `<li>
                        <a href="${like_link}">
                            <span id="like_list_span">
                              ${like_company}
                            </span>
                        </a>
                            <button id="like_del_btn" onclick="like_del('${like_company}', '${like_link}')">
                                 ❌
                            </button>
                    </li>`;
    // like_list.append(like_html);
    $('#like_list').append(like_html);

    const like_list_Obj = {
        'like_company': like_company,
        'like_link': like_link
        // id :newId
    };
    like_list_ar.push(like_list_Obj)
    save_like_list();

}




function handleClick_search() {

    let input_keyword = input_keyword_box.value
    let input_potal = input_potal_box.value
    let input_location = input_location_box.value
    let input_jobtype = input_jobtype_box.value

    console.log(`검색어 : ${input_keyword}, 포탈 : ${input_potal}, 위치 : ${input_location}, 고용 형태 : ${input_jobtype}`)

    if  (input_keyword == ''){
        alert("검색어를 입력하세요.")
        return 0
    }


    if (input_location == '전체 (희망 지역)') {
        input_location = ''
    }

    if (input_jobtype == '전체 (근무 형태)') {
        input_jobtype = ''
    }

    // console.log(`${input_keyword}를 검색합니다.`)

    if (input_potal == '전체 (포탈 선택)') {
        job_total_give(input_keyword, input_location, input_jobtype)
    }

    else if (input_potal == 'Job-korea') {
        job_korea_jobs_give(input_keyword, input_location, input_jobtype)
    }

    else if (input_potal == 'Saram-in') {
        saramin_jobs_give(input_keyword, input_location, input_jobtype)
    }

    else if (input_potal == 'Indeed') {
        indeed_jobs_give(input_keyword, input_location, input_jobtype)
    }

    section_recruit_info.classList.remove('hiding_class');
    section_news_info.classList.add('hiding_class');
    


}


function indeed_jobs_give(input_keyword, input_location, input_jobtype) {
    None_info.classList.add('hiding_class');
    loadingbar.classList.remove('hiding_class');
    $('#total_recruit_info').empty()
    $.ajax({
        type: "GET",
        url: `/api/indeed?input_keyword_give=` + input_keyword + `&input_location_give=` + input_location + `&input_jobtype_give=` + input_jobtype,
        data: {},
        error : function(){
            alert('일치하는 정보가 없습니다.');
            None_info.classList.remove('hiding_class')
            loadingbar.classList.add('hiding_class')
        },
        success: function (response) {
            let id_jobs = response['id_jobs'];
            // console.log(id_jobs.length)
            if (id_jobs.length === 0){
                alert('일치하는 정보가 없습니다.');
                None_info.classList.remove('hiding_class')
                loadingbar.classList.add('hiding_class')
            }
            


            for (let i = 0; i < id_jobs.length; i++) {
                let r_id_jobs = id_jobs[i]
                let company = r_id_jobs['companys']
                let position = r_id_jobs['positions']
                let location = r_id_jobs['locations']
                let link = r_id_jobs['links']

                let temp_html = ` <div id="total_recruit_info">
                <div id="recruit_post">
                    <div id="company_name">
                        <a href="${link}" class="a_companys_name">
                            <strong>
                                ${company}
                            </strong>
                        </a>
                    </div>
                    <div id="recruit_post_info">
                        <div id="position_name">
                            <span>
                                ${position}
                            </span>
                        </div>
                        <div id="other_name">
                            <div id="location_name">
                                <span> 위치 : ${location}</span>
                            </div>
                            <div id="income_name">
                                <span></span>
                            </div>
                        </div>
                    </div>
                    <div id="recruit_post_link">

                        <div id="support_btn">
                            <a href="${link}">
                                <button>지원하기</button>
                            </a>
                        </div>

                        <div id="like_btn">
                            <a>
                                <button class="pink_btn" id="like_click" onclick="handleClick_like('${company}', '${link}')">찜</button>
                            </a>
                        </div>

                    </div>
                </div>
            </div>`;
                $('#total_recruit_info').append(temp_html);
                jobs_num.innerText = `총 ${id_jobs.length}개의 채용정보`;
                jobs_potal.innerText = 'Indeed의 채용정보';
                loadingbar.classList.add('hiding_class');
                pocket_bar.classList.remove('hiding_class');
                

            }
        }
    })

}


function saramin_jobs_give(input_keyword, input_location, input_jobtype) {
    None_info.classList.add('hiding_class');
    loadingbar.classList.remove('hiding_class');
    $('#total_recruit_info').empty()
    $.ajax({
        type: "GET",
        url: `/api/saramin?input_keyword_give=` + input_keyword + `&input_location_give=` + input_location + `&input_jobtype_give=` + input_jobtype,
        data: {},
        error : function(){
            alert('일치하는 정보가 없습니다.');
            None_info.classList.remove('hiding_class')
            loadingbar.classList.add('hiding_class')
        },
        success: function (response) {
            let sa_jobs = response['sa_jobs'];
            for (let i = 0; i < sa_jobs.length; i++) {
                let r_sa_jobs = sa_jobs[i]

                let company = r_sa_jobs['companys']
                let position = r_sa_jobs['positions']
                let location = r_sa_jobs['locations']
                let link = r_sa_jobs['links']

                let temp_html = ` <div id="total_recruit_info">
                <div id="recruit_post">
                    <div id="company_name">
                        <a href="${link}" class="a_companys_name">
                            <strong>
                                ${company}
                            </strong>
                        </a>
                    </div>
                    <div id="recruit_post_info">
                        <div id="position_name">
                            <span>
                                ${position}
                            </span>
                        </div>
                        <div id="other_name">
                            <div id="location_name">
                                <span> 위치 : ${location}</span>
                            </div>
                            <div id="income_name">
                                <span></span>
                            </div>
                        </div>
                    </div>
                    <div id="recruit_post_link">

                        <div id="support_btn">
                            <a href="${link}">
                                <button>지원하기</button>
                            </a>
                        </div>

                        <div id="like_btn">
                            <a>
                            <button class="pink_btn" id="like_click" onclick="handleClick_like('${company}', '${link}')">찜</button>
                            </a>
                        </div>

                    </div>
                </div>
            </div>`;
                $('#total_recruit_info').append(temp_html);
                jobs_num.innerText = `총 ${sa_jobs.length}개의 채용정보`;
                jobs_potal.innerText = 'Saram-in의 채용정보';
                loadingbar.classList.add('hiding_class');
                pocket_bar.classList.remove('hiding_class');
            }
        }
    })
}


function job_korea_jobs_give(input_keyword, input_location, input_jobtype) {
    None_info.classList.add('hiding_class');
    loadingbar.classList.remove('hiding_class');
    $('#total_recruit_info').empty()
    $.ajax({
        type: "GET",
        url: `/api/job_korea?input_keyword_give=` + input_keyword + `&input_location_give=` + input_location + `&input_jobtype_give=` + input_jobtype,
        data: {},
        error : function(){
            alert('일치하는 정보가 없습니다.');
            None_info.classList.remove('hiding_class')
            loadingbar.classList.add('hiding_class')
        },
        success: function (response) {
            let jk_jobs = response['jk_jobs'];
            for (let i = 0; i < jk_jobs.length; i++) {
                let r_jk_jobs = jk_jobs[i]

                let company = r_jk_jobs['companys']
                let position = r_jk_jobs['positions']
                let location = r_jk_jobs['locations']
                let link = r_jk_jobs['links']

                let temp_html = ` <div id="total_recruit_info">
                <div id="recruit_post">
                    <div id="company_name">
                        <a href="${link}" class="a_companys_name">
                            <strong>
                                ${company}
                            </strong>
                        </a>
                    </div>
                    <div id="recruit_post_info">
                        <div id="position_name">
                            <span>
                                ${position}
                            </span>
                        </div>
                        <div id="other_name">
                            <div id="location_name">
                                <span> 위치 : ${location}</span>
                            </div>
                            <div id="income_name">
                                <span></span>
                            </div>
                        </div>
                    </div>
                    <div id="recruit_post_link">

                        <div id="support_btn">
                            <a href="${link}">
                                <button>지원하기</button>
                            </a>
                        </div>

                        <div id="like_btn">
                            <a>
                            <button class="pink_btn" id="like_click" onclick="handleClick_like('${company}', '${link}')">찜</button>
                            </a>
                        </div>

                    </div>
                </div>
            </div>`;
                $('#total_recruit_info').append(temp_html);
                jobs_num.innerText = `총 ${jk_jobs.length}개의 채용정보`;
                jobs_potal.innerText = 'Job-korea의 채용정보';
                loadingbar.classList.add('hiding_class');
                pocket_bar.classList.remove('hiding_class');
            }
        }
    })
}


function job_total_give(input_keyword, input_location, input_jobtype) {
    None_info.classList.add('hiding_class');
    loadingbar.classList.remove('hiding_class');
    $('#total_recruit_info').empty()
    $.ajax({
        type: "GET",
        url: `/api/total?input_keyword_give=` + input_keyword + `&input_location_give=` + input_location + `&input_jobtype_give=` + input_jobtype,
        data: {},
        error : function(){
            alert('일치하는 정보가 없습니다.');
            None_info.classList.remove('hiding_class')
            loadingbar.classList.add('hiding_class')
        },
        success: function (response) {
            let jk_jobs = response['jk_jobs'];
            let id_jobs = response['id_jobs'];
            let sa_jobs = response['sa_jobs'];
            // console.log(jk_jobs)
            for (let i = 0; i < jk_jobs.length; i++) {
                let r_jk_jobs = jk_jobs[i]

                let company = r_jk_jobs['companys']
                let position = r_jk_jobs['positions']
                let location = r_jk_jobs['locations']
                let link = r_jk_jobs['links']

                let temp_html = ` <div id="total_recruit_info">
                <div id="recruit_post">
                    <div id="company_name">
                        <a href="${link}" class="a_companys_name">
                            <strong>
                                ${company}
                            </strong>
                        </a>
                    </div>
                    <div id="recruit_post_info">
                        <div id="position_name">
                            <span>
                                ${position}
                            </span>
                        </div>
                        <div id="other_name">
                            <div id="location_name">
                                <span> 위치 : ${location}</span>
                            </div>
                            <div id="income_name">
                                <span></span>
                            </div>
                        </div>
                    </div>
                    <div id="recruit_post_link">

                        <div id="support_btn">
                            <a href="${link}">
                                <button>지원하기</button>
                            </a>
                        </div>

                        <div id="like_btn">
                            <a>
                            <button class="pink_btn" id="like_click" onclick="handleClick_like('${company}', '${link}')">찜</button>
                            </a>
                        </div>

                    </div>
                </div>
            </div>`;
                $('#total_recruit_info').append(temp_html);
                jobs_num.innerText = `총 ${jk_jobs.length + id_jobs.length + sa_jobs.length}개의 채용정보`;
                jobs_potal.innerText = '전체포탈의 채용정보';
                loadingbar.classList.add('hiding_class');
                pocket_bar.classList.remove('hiding_class');
            }

            for (let i = 0; i < sa_jobs.length; i++) {
                let r_sa_jobs = sa_jobs[i]

                let company = r_sa_jobs['companys']
                let position = r_sa_jobs['positions']
                let location = r_sa_jobs['locations']
                let link = r_sa_jobs['links']

                let temp_html = ` <div id="total_recruit_info">
                <div id="recruit_post">
                    <div id="company_name">
                        <a href="${link}" class="a_companys_name">
                            <strong>
                                ${company}
                            </strong>
                        </a>
                    </div>
                    <div id="recruit_post_info">
                        <div id="position_name">
                            <span>
                                ${position}
                            </span>
                        </div>
                        <div id="other_name">
                            <div id="location_name">
                                <span> 위치 : ${location}</span>
                            </div>
                            <div id="income_name">
                                <span></span>
                            </div>
                        </div>
                    </div>
                    <div id="recruit_post_link">

                        <div id="support_btn">
                            <a href="${link}">
                                <button>지원하기</button>
                            </a>
                        </div>

                        <div id="like_btn">
                            <a>
                            <button class="pink_btn" id="like_click" onclick="handleClick_like('${company}', '${link}')">찜</button>
                            </a>
                        </div>

                    </div>
                </div>
            </div>`;
                $('#total_recruit_info').append(temp_html);
            }

            for (let i = 0; i < id_jobs.length; i++) {
                let r_id_jobs = id_jobs[i]

                let company = r_id_jobs['companys']
                let position = r_id_jobs['positions']
                let location = r_id_jobs['locations']
                let link = r_id_jobs['links']

                let temp_html = ` <div id="total_recruit_info">
                <div id="recruit_post">
                    <div id="company_name">
                        <a href="${link}" class="a_companys_name">
                            <strong>
                                ${company}
                            </strong>
                        </a>
                    </div>
                    <div id="recruit_post_info">
                        <div id="position_name">
                            <span>
                                ${position}
                            </span>
                        </div>
                        <div id="other_name">
                            <div id="location_name">
                                <span> 위치 : ${location}</span>
                            </div>
                            <div id="income_name">
                                <span></span>
                            </div>
                        </div>
                    </div>
                    <div id="recruit_post_link">

                        <div id="support_btn">
                            <a href="${link}">
                                <button>지원하기</button>
                            </a>
                        </div>

                        <div id="like_btn">
                            <a>
                            <button class="pink_btn" id="like_click" onclick="handleClick_like('${company}', '${link}')">찜</button>
                            </a>
                        </div>

                    </div>
                </div>
            </div>`;
                $('#total_recruit_info').append(temp_html);
            }
        }
    })
}

function print_like(like) {
    let like_company_LS = like['like_company']
    let like_link_LS = like['like_link']

    let like_html = `<li>
                        <a href="${like_link_LS}">
                            <span id="like_list_span">
                                ${like_company_LS}
                            </span>
                        </a>
                         <button id="like_del_btn" onclick="like_del('${like_company_LS}', '${like_link_LS}')">
                            ❌
                         </button>
                    </li>`;
    // like_list.append(like_html);
    $('#like_list').append(like_html);

    const like_list_Obj = {
        'like_company': like_company_LS,
        'like_link': like_link_LS
        // id :newId
    };
    like_list_ar.push(like_list_Obj)
    save_like_list();

}

function save_like_list() {
    localStorage.setItem(like_list_LS, JSON.stringify(like_list_ar));
}

function load_like() {
    const loaded_like = localStorage.getItem(like_list_LS);
    if (loaded_like !== null) {
        const parsed_like = JSON.parse(loaded_like);
        parsed_like.forEach(function (like) {
            // console.log(like)
            print_like(like)
        })
    }
}




function init() {

    search_btn.addEventListener("click", handleClick_search);


    load_like();

    // Total_logo.addEventListener("click", handleClick_search);   
    // Job_Koera_logo.addEventListener("click", handleClick_Job_Korea);
    // Saramin_logo.addEventListener("click", handleClick_Saramin);
    // Indeed_logo.addEventListener("click", handleClick_Indeed);
}
init();

