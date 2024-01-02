console.log("This is working")

$(document).ready(function(){
    $("#commentForm").submit(function(e){
        e.preventDefault();

        $.ajax({
            data: $(this).serialize(),

            method: $(this).attr("method"),
            url: $(this).attr("action"),

            dataType: "json",

            success: function(response){
                console.log('done');

                if(response.bool == true){
                    $("#review").html("Review added successfully.");
                    $(".hide_form").hide()
                }
            }
        })
    });
});