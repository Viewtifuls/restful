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
			$("#tags").html('<h1 style="color: #f9f9f9;" c>' + data.number + '</h1>');
			}

		});
	});
})
