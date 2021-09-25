$('a').click(function(event){
  event.preventDefault();
    var page_n = $(this).attr('href');
    console.log(page_n)
    $.ajax({
      url:"{% url 'spa_app:indexviews' %}",
      type: 'POST',
      data: {
        page_n:page_n,
        csrfmiddlewaretoken: '{{ csrf_token }}',
      },

      success: function(response) {
      	console.log(response)
          $('#items-list').html('')
        $.each(response.results, function(index, value) {           
            $('#items-list').append('<tr><td>' + value.title + '</td><td>' + value.quantity + '</td><td>' + value.distance + value.meter +'</td></tr>')
            }); 
        
      
      },
      error: function (response) {
        console.log("ERROR")
     
      }

    });

}); 

$('#filtering-form').submit(function(event){
	event.preventDefault();
    var data = $(this).serialize();
    
    $.ajax({
    	url:"{% url 'spa_app:filtering' %}",
    	type: 'POST',
    	data:data,

    	success: function(response) {
    	  	console.log(response)

    	  	$('#items-pagination-output').hide();
    	  	$('#items-data').show();
    	  	$('#items-filter').html('');
    	  	$("#filtering-form").trigger('reset');
    	  	
    	  	var varsearch = $('#search').val()
			var ItemSearch = response.results;
            if ( ItemSearch == 0) {
				$('#items-filter').html("search no found ");

			}else{
				$('#items-filter').html('');
				$.each(response.results, function(index, value){   
	            $('#items-filter').append('<tr><td>' + value.title + '</td><td>' + value.quantity + '</td><td>' + value.distance + value.meter +'</td></tr>');
            	
	            
            	}); 

			}

			
			
    	},

    	error: function (response) {
    		console.log("ERROR")
     
    	}
			

    });

}); 


