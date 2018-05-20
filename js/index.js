import 'bootstrap';
import $ from 'jquery';
import jQuery from 'jquery';

let oContent = $('#content');

$('#sidebar-collapsible').on('hide.bs.collapse', function () {
  console.log('hi')
  oContent.removeClass('col-md-8')
  oContent.addClass('col-md-12')
    $('#sidebar-switcher').html('Показать сайдбар')
})

$('#sidebar-collapsible').on('show.bs.collapse', function () {
  oContent.removeClass('col-md-12')
  oContent.addClass('col-md-8')
    $('#sidebar-switcher').html('Убрать сайдбар')
})


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$('.js-article-like').on('click', function () {
    let btn = $(this);
    let csrftoken = getCookie('csrftoken');
    let question_id = btn.data('id');

    // через промисы
    $.ajax({
        method: "POST",
        url: "/like/",
        data: {
          "question_id" : question_id,
          "csrfmiddlewaretoken" : csrftoken
        },
        dataType: 'json'
    }).done(function (data) {
      $('#article-count-id-' + question_id).text(data.count)
    });
    // еще есть: success(f(d) {}), error(f() {})

    /*
    в JSON'ы правильный подход - добавлять "status"
     */

    return false;
});


// по-старому
// let xhr = new XMLHttpRequest();
// xhr.open('POST', '/xhr/test.html', true);   // блокирующий
// xhr.onreadystatechange = function () {      // callback
//     if (xhr.readyState === 4) {             // успешно выполнен
//         if(xhr.status === 200) {
//             alert(xhr.responseText);
//         }
//     }
// };
// xhr.send("a=5");                            // urlencoded