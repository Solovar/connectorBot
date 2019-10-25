$(document).ready(function() {
//alert("test alert")
// for showing modals

    $(".modalButton").click(function () {
        let itemID = $(this).attr('id');
        $("#" + itemID + "Modal").modal('show');
    });

    $(".modalClose").click(function () {
        $(".modal").modal('hide');
    });

// loading data on to locations
/*
    function legalData(name) {
        let legalData =["settings", "twitter"];
        return legalData.includes(name)
    }
*/
    $.ajax({
        url: 'static/Json/test.json',
        dataType: 'json',
        success: function (data) {
            var items = [];

            $.each(data, function (key, val) {

                items.push('<li id="' + key + '">' + val + '</li>');

            });

            var item = items.join('');
            $('#settings-block div').append(item)
        }
    });

/*
    function loadData(loc) {
        if(legalData(loc))
        {
            if(loc == "settings") {
                $.ajax({
                    url: '../Json/test.json',
                    dataType: 'json',
                    success: function (data) {
                        var items = [];

                        $.each(data, function (key, val) {

                            items.push('<li id="' + key + '">' + val + '</li>');

                        });

                        $('<ul/>', {
                            'class': 'interest-list',
                            html: items.join('')
                        }).appendTo('.settings-block');

                    }
                });
            }
        }
    }
*/
});