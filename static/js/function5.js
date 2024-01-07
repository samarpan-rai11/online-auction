console.log(this)

$(document).ready(function(){
    $(".delete-product").on("click",function(){
        console.log("You pressed trash button")
        let product_id = $(this).attr("data-product")
        let this_val = $(this)
        console.log("Product id:",product_id)

        $.ajax({
            url:'/delete-from-cart',
            data:{
                'id': product_id,
            },
            dataType: 'json',
            beforeSend:function(){
                this_val.hide()
            },
            success:function(response){
                console.log(response)
                this_val.show()
                $(".cart-items-count").text(response.totalcartitems)
                $("#cart-list").html(response.data)
            }
        })
    })
})