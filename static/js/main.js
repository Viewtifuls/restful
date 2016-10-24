// DOM is ready
$(document).ready(function() {
	$("#url_search").keypress(function(event){
    if(event.keyCode == 13){
        event.preventDefault();
        $('button').click();
    }
	});
	$('button').click(function() {
        $.ajax({
			url: "/data?" + $('form').serialize(),
			success: function(data){
			var row_html = 
				'<tr><td>' + data.url + '</td>' +
				'<td>' + data.number + '</td></tr>';

			// Append our row
			$('.ourtable > tbody').append(row_html);
			}

		});
	});
})
