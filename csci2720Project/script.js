// NAME: Cheung ******; Tseung ******; KWOK Chun Kiu
// SID: sid, sid, 1155141911
const data = [{"event_ics": "https://ogcef.one.gov.hk/event-psi/psi/171695_en.ics", "event_desc":"More than 600 invaluable items of Bruce Lee memorabilia will be showcased to create an exhibition that looks at Bruce Lee from a more comprehensive, in-depth and independent perspective.","event_id":171695,"event_summary":"Bruce Lee：Kung Fu‧Art‧Life","event_location":"Hong Kong Heritage Museum","event_date":"20 Jul 2013 - 20 Jul 2020","event_duration":"","event_org":"Presented by the Leisure and Cultural Services Department Jointly organised by Bruce Lee Foundation and Hong Kong Heritage Museum Sponsored by Fortune Star Media Limited","event_url":"http://www.lcsd.gov.hk/ce/Museum/Heritage/en_US/web/hm/exhibitions/data/exid209.html","event_status":"B"}]

$(document).ready(function() {
    $('#navbarDropdown').click(function() {
        $(this).parent().toggleClass('show');
        $(this).siblings('div').toggleClass('show');
        if ($(this).siblings('div').css('display') !== 'none')
            {$(this).attr('aria-expanded', 'true')}
        else {$(this).attr('aria-expanded', 'false')}
    });

    $('body').on('click', 'a.dropdown-item', null, function() {
        $(this).parent().toggleClass('show');
        $(this).closest('ul').toggleClass('show');
        $('#navbarDropdown').attr('aria-expanded', 'false');
    });

    $('#forgot-pw').click(function() {
        alert('sdf');
        // $('#forgetForm').attr('action','http://csci2720-g8.cse.cuhk.edu.hk/forget/checkUserExist');
        // $('#forgetForm').attr('method','post');
        // $.getJSON('http://csci2720-g8.cse.cuhk.edu.hk/forget/checkUserExist',function(data){
        //   if ('error' in data) {
        //     alert("error");
        //   }
        //   else{
        //     alert(data);
        //   }
        // }).fail(function(err) {
        //     $("#error").text("Error: Cannot connect to the server.");
        // });
    });

    $('#login').click(function (e) {
        e.preventDefault();
        alert("Don't know what to do");
        $(this).closest('div').hide();
        $('#app').show();
    });

    $('#myTab a').on('click', function (e) {
        e.preventDefault();
        $(this).tab('show');
    });

    // FIXME: Make this work -- it should show ALL events at once.
    $.ajax({
        url: 'https://ogcef.one.gov.hk/event-api/eventList/',
        dataType: 'jsonp',
        type: 'GET',
        data: {}
    }).done(function (data) {
        $.each(data, function () {
            $('#event-list').append('<tr>' +
                '<td>' + data['event_date'] + '</td>' +
                '<td>' + data['event_summary'] + '</td>' +
                '<td>' + data['event_org'] + '</td>' +
                '<td>' + data['event_location'] + '</td>' +
                '</tr>'
            );
        });
    });
});
