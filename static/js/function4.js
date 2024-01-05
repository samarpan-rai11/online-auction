console.log("This is working")

const monthNames = ["Jan", "Feb", "Mar","Apr","May","Jun","Jul",      
                    "Aug","Sept","Oct","Nov","Dec"];

$(document).ready(function(){
    $("#commentForm").submit(function(e){
        e.preventDefault();

        let dt = new Date();
        let time = dt.getDay() + " " + monthNames[dt.getUTCMonth()] + "," + dt.getFullYear();

        $.ajax({
            data: $(this).serialize(),

            method: $(this).attr("method"),
            url: $(this).attr("action"),

            dataType: "json",

            success: function(response){
                console.log('done');

                //this will add text and remove the review form after submitting the form
                if(response.bool == true){
                    $("#review").html("Review added successfully.");
                    $(".hide_form").hide()
                }

                let _html='<div class="mt-3 bg-white p-4 rounded-xl">'
                    _html+='<img src="https://cvhrma.org/wp-content/uploads/2015/07/default-profile-photo.jpg" alt="profile" style="max-width: 50px;" class="rounded-full">'

                    _html+='<div class="flex">'
                    _html+='<h2 class="text-left mr-6 text-emerald-500 underline">'+ response.user +'</h2>'
                    _html+='<span class="text-gray-400">'+ time +'</span>'
                    _html+='</div>'

                    for(let i = 1; i<=response.rating; i++){
                        _html += '<i class="fas fa-star text-warning" style="color: #FFB534;"></i>'
                    }

                    _html+='<p>'+ response.review +'</p>'
                    _html+='</div>'

                    $(".comment").prepend(_html)
            }

        })
    });
});
