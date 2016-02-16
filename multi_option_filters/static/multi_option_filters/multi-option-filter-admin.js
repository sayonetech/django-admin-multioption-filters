if (!$) {
    $ = django.jQuery;
}

$(function() {
    $('.multi-filter-form').submit(function(event){
        var values = []
        $(this).closest('div.multi-filter-div').find('input[type="checkbox"]:checked').each(function()
    {
        values.push(this.value);
    });
        if (values.length != 0)
        {
            $(this).find('.lookup-field').val(values.join(','))
        }

        else
        {
            var clear = $(this).closest('.multi-filter-div').find('ul.filter-choices li').first().find('a').attr('href')
            window.location.href = clear;
            event.preventDefault()
        }


    });
})