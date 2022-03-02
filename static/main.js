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

  // --------------------------------------------------------
  const allButtons = $('.btn');
  const randbutton = allButtons[Math.floor(Math.random()*allButtons.length)];
  $(randbutton).css('transform', 'scale(1.5, 1.5)');

    const colors = [
      '#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
		  '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
		  '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
		  '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
		  '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
		  '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
		  '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
		  '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
		  '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
		  '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'];

    $(".btn").hover(function(){
        $(this).css("background", colors[Math.floor(Math.random()*colors.length)]);
    },
    function(){
        $(this).css("background", colors[Math.floor(Math.random()*colors.length)]);
    });

    $(".card").hover(function(){
        $(this).css("border-color", colors[Math.floor(Math.random()*colors.length)]);
    },
    function(){
        $(this).css("border-color", colors[Math.floor(Math.random()*colors.length)]);
    });
});
