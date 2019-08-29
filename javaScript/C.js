//alert("test alert")

$('.content-block').hide();

$(".modalButton").click(function () {
    let itemID = $(this).attr('id');
    $("#" + itemID + "Modal").modal('show');
});

$(".modalClose").click(function () {
    $(".modal").modal('hide');
});