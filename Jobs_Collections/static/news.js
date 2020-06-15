


$(document).ready(function () {
    listing();
});




  function listing() {
    $.ajax({
      type: "GET",
      url: "./news.py",
      data: {},
      success: function (response) {
          console.log(news_card)
        let news_card = response['news_card'];
        for (let i = 0; i < news_card.length; i++) {
            make_news_card(news_card[i]['news_img'], news_card[i]['news_title'], news_card[i]['news_link'])
        }
      }
    })
  }

function make_news_card(news_img, news_title, news_link) {
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
                Title
            </div>
        </a>
    </div>`;
    $('#recruit_news').append(temp_html);
    print(news_img)
}



// function is_long(obj) {
//     let content = $(obj).val();
//     if (content.length > 140) {
//         alert('리뷰는 140자까지 기록할 수 있습니다.');
//         $(obj).val(content.substring(0, content.length - 1));
//     }
// }