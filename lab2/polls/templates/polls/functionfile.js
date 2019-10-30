console.log('functionfile')
$('.apireq').click( function() {
    $.ajax({
             url : "http://localhost:8000/studentsapi",
             dataType: "json",
             success : function (data) {
                      $('#first_name').text( data[0].first_name);
                      $('#last_name').text( data[0].last_name);
                      $('#age').text( data[0].age);
                      $('#gender').text( data[0].gender);
                    }
                 });
             });
