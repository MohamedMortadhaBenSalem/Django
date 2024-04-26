$(document).ready(function () {
    $('.increment-btn').click(function (e) {
        e.preventDefault();
        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function (e) {
        e.preventDefault();
        var dec_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value, 10);
        value = isNaN(value) ? 1 : value;
        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.addToCartBtn').click(function (e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status); // Display success message
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
                alertify.error(xhr.responseText); // Display error message
            }
        });
    });

    $('.changeQuantity').click(function (e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
            }
        });
    });


    
    $(document).on('click','.delete-cart-item',function (e) {
        e.preventDefault();
        
        // Get the product ID from the DOM
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        
        // Get the CSRF token from the hidden input field
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        // Send an AJAX request to delete the cart item
        $.ajax({
            method: "POST",
            url: "/delete-cart-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                // Handle the success response here
                alertify.success(response.status);
                
                // Reload the cart data after successful deletion
                $('.kartdata').load(location.href + ' .cartdata');
            },
            error: function (xhr, status, error) {
                // Handle the error response here
                console.error(xhr.responseText);
            }
        });
    });

    $('.addToWishlist').click(function (e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status)
            }
        });
    });
     


    $(document).on('click','.delete-wishlist-item',function (e) {
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val(); 
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
                $(".wishlistdata").load(location.href + " .wishlistdata");
            }
        });
    });
    
    


    
});
