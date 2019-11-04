$(document).ready(function() {
   setInterval(function () {
        clear_area('#settings-block div');
        do_stuff('#settings-block div');
    },1000);

    function do_stuff(add_to) {
        $.get( "/AJAX/Settings", function( data ) {
            $(add_to).html( data );
            console.log( "Load was performed." );
        });
        /*
        $.ajax({
            url: '/AJAX/Settings',
            dataType: 'get',
            success: function (xhr) {
                console.log("it happend");
                $(add_to).append(xhr['responseText'])
            },
            error: function(xhr) {
                console.log('error');
                console.log(xhr);
            }
        }); */
    }

    function clear_area(id) {
        $(id).empty();
    }
});