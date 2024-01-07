console.log(this)

$(document).ready(function(){
    // for deleting the product from the cart list
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
                console.log("Deleted")
            }
        })
    })


    // for updating the product from the cart list
    $(".update-product").on("click",function(){
        // from data-product attribute in html tag
        let product_id = $(this).attr("data-product")
        let this_val = $(this)

        // from html class
        let product_qty = $(".product-qty-"+product_id).val() 

        console.log("Product id:",product_id)
        console.log("Product qty:",product_qty)

        $.ajax({
            url:'/update-cart',
            data:{
                'id': product_id,
                'qty': product_qty,
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
                console.log("Updated")
            }
        })
    })
})