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

// for switching content
    var currentLocation = 'console';
    swapContent(false);

    $("html").on('click', '.content-btn', function () {
        let itemID = $(this).attr('id');
        alert(itemID)
        swapContent(itemID)
    });

    /*$(".content-btn").on('click', function () {
        let itemID = $(this).attr('id');
        alert(itemID)
        swapContent(itemID)
    });*/

    function swapContent(swap) {
        let getFrom = '#' + currentLocation + '-block';
        const contentArea = '#content-area';
        $(contentArea).empty();

        if (swap !== false) {
            getFrom = '#' + swap + '-block';
        }
        // alert(getFrom)
        let data = $(getFrom).html();
        $(contentArea).prepend(data);
    }
});