fetch("/gallery/cart/checkout-config-view")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);

  const btn = document.querySelector("#submitBtn");
  if (btn) {
    btn.addEventListener("click", () => {
      // Get Checkout Session ID
      fetch("/gallery/cart/create-checkout-session")
      .then((result) => { return result.json(); })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      });
    });
  }
});



$(document).ready(function() {
  $('#order-btn-submit').on('click', function (event) {
      const form = $('#order-form').parsley();
      if (form.validate()) {
        $('#order-form').submit();
      }
    });

  $('#singup-form-submit').on('click', function (event) {
      const form = $('#singup-form').parsley();
      if (form.validate()) {
        $('#singup-form').submit();
      }
    });

  $('.add-remove-to-cart').on('click', function (event) {
    const itemId = $(event.target).data('id');
    const action = $(event.target).data('action');
    $.get("/gallery/cart/add-remove-to-cart?id=" + itemId + '&action=' + action, function(data, status) {
      if (status === 'success') {
        alert(data.message);
        window.location.href = $('#cart-link').attr('href');
      }
      else {
        alert("Something Went wrong");
      }
    });
  });
});
