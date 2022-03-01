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
