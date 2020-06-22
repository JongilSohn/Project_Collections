
$(document).ready(function () {
    news_readey();
    console.log('준비완료');
});

// const loadingbar_news = document.querySelector("#loading_news")   질문 1번

function news_readey() {
    $('#recruit_news').empty()
    $.ajax({
        type: "GET",
        url: "/api/news",
        data: {},
        success: function (response) {
            $(loading_news).addClass("hiding_class");
            // loadingbar_news.classList.add('hiding_class')  질문 1번
            let news_card = response['news_card'];
            for (let i = 0; i < news_card.length; i++) {
                let r_news_card = news_card[i]

                let news_content = r_news_card['news_content']
                let news_link = r_news_card['news_link']
                let news_img = r_news_card['news_img']
                let news_title = r_news_card['news_title']

                let temp_html = `<div id="news_box">
                                  <a href="${news_link}" class="news_class">
                                      <div id="news_img">
                                         <img src="${news_img}"
                                          class="" width="178" height="120" onerror="this.parentNode.style.display='none';">
                                     </div>
                                 <div id="news_title">
                                      ${news_title}
                                </div>
                                  <div id="news_content">
                                    ${news_content}
                                 </div>
                                </a>
                            </div>`;
                $('#recruit_news').append(temp_html);
                
            }
        }
    })
}