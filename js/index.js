import 'bootstrap';
import $ from 'jquery';

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
