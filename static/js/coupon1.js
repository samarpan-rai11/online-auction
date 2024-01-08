if (coupon_discount) {
    if (product_amount >= 500) {
        cal_discount = product_amount - (product_amount * coupon_discount / 100) - 20;
        document.getElementById("total").innerHTML = "$" + cal_discount;
        console.log(cal_discount);
    } else {
        cal_discount = product_amount - (product_amount * coupon_discount / 100);
        document.getElementById("total").innerHTML = "$" + cal_discount;
        console.log(cal_discount);
    }
}