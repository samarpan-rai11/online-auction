console.log("This is working")

const monthNames = [
    "Jan", "Feb", "Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"
];


//This is for dynamic review of the product 
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



// Add to cart button
$(".add-to-cart-btn").on("click", function(){

    let this_val = $(this)
    let _index = this_val.attr("data-index")

    let qunatity = $(".product-quantity-"+_index).val()
    let product_title = $(".product-title-"+_index).val()
    let product_id = $(".product-id-"+_index).val()
    let product_pid = $(".product-pid-"+_index).val()
    let product_image = $(".product-image-"+_index).val()
    let product_price = $(".current-price-"+_index).text()

    console.log("Quantity:", qunatity)
    console.log("product title:", product_title)
    console.log("product id:", product_id)
    console.log("product pid:", product_pid)
    console.log("Index:", _index)
    console.log("product image:", product_image)
    console.log("product price:", product_price)
    console.log("This is:", this_val)

    $.ajax({
        url: '/add-to-cart',
        data: {
            'id': product_id,
            'pid': product_pid,
            'image': product_image,
            'qty': qunatity,
            'title': product_title,
            'price': product_price
        },
        dataType: 'json',
        beforeSend:function(){
            console.log("Adding product to cart...")
        },
        success:function(response){
            this_val.html("✓")
            console.log("Added product to cart")
            $(".cart-items-count").text(response.totalcartitems)
            // this_val.attr('disabled',false);
        }
    });

})


$(document).on("submit", "#contact-form", function(e){
    e.preventDefault()
    console.log("Submited")
    let full_name = $("#full_name").val()
    let email = $("#email").val()
    let phone = $("#phone").val()
    let subject = $("#subject").val()
    let message = $("#message").val()

    console.log("Full name:", full_name)
    console.log("Email:", email)
    console.log("Phone:", phone)
    console.log("Subject:", subject)
    console.log("Message:", message)

    $.ajax({
        url: '/ajax-contact-form',
        data: {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "subject": subject,
            "message": message,
        },
        dataType: 'json',
        beforeSend:function(){
            console.log("Sending data to sercer..");
        },
        success:function(response){
            console.log("Sent data successfully");
            $("#contact-form").hide()
            $("#message-after").html("Message sent Successfully")
        }
    })
})