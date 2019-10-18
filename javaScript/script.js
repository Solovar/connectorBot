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

// for switching content and navigating
    var currentLocation = 'console';
    swapContent(false);

    $("html").on('click', '.content-btn', function () {
        let itemID = $(this).attr('id');
        swapContent(itemID)
    });

    function swapContent(swap) {
        let getFrom = '#' + currentLocation + '-block';
        const contentArea = '#content-area';
        $(contentArea).empty();

        if (swap !== false) {
            getFrom = '#' + swap + '-block';
            set_location(swap)
        }
        loadData(currentLocation);
        let data = $(getFrom).html();
        $(contentArea).prepend(data);
    }

    function set_location(posis) {
        currentLocation = posis
    }

// loading data on to locations

    function legalData(name) {
        let legalData =["settings", "twitter"];
        return legalData.includes(name)
    }

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

});