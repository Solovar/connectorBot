$(document).ready(function() {
    setInterval(function () {
        clear_area('#settings-block div')
        do_stuff('#settings-block div')
    },1000);

    function do_stuff(add_to) {
        $.ajax({
            url: 'static/Json/test.json',
            dataType: 'json',
            success: function (data) {
                var items = [];

                $.each(data['persons'], function (key, val) {
                    console.log('----------')
                    console.log(key);
                    console.log(val['age']);
                    items.push('<li>' + key + ' is: ' + val['age'] + ' years old</li>');

                });

                var item = items.join('');
                $(add_to).append(item)
            }
        });
    }

    function clear_area(id) {
        $(id).empty();
    }
});