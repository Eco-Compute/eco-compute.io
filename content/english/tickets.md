---
title: "Get your ticket now"
date: 2019-09-10T13:51:25+06:00
draft: false
description: "Ticket sales for the EcoCompute Conference 2024 in Munich, Germany"
bg_image : "images/bg/cta-bg.webp"
---

## Buy a ticket

You can now buy a ticket for the early bird price of 150 Euro. As the location is not confirmed we will be sending out
invoices in Q1 2024

We have a limited amount of [Grant Tickets](/grants/) available.

<div class="alert alert-info d-none" role="alert" id="form-status">asd
</div>

<form id="ticket-form" action="https://formspree.io/f/xyyqrdoa" method="POST">
<div class="col-lg-6">
<div class="contact-form pl-4 mt-5 mt-lg-0">
<form method="post" action="#">
<div class="form-row">
<div class="col-lg-6">
<div class="form-group">
<input type="text" placeholder="Your First Name" class="form-control" name="fname" id="fname" required>
</div>
</div>

<div class="col-lg-6">
<div class="form-group">
<input type="text" placeholder="Your Second Name" class="form-control" name="sname" id="sname" required>
</div>
</div>

<div class="col-lg-12">
<div class="form-group">
<input type="email" placeholder="Your Email" class="form-control" name="email" id="email" required>
</div>
</div>

<div class="col-lg-12">
<div class="form-group">
<input type="text" placeholder="Company" class="form-control" name="company" id="company" required>
</div>
</div>

<div class="col-lg-12">
<div class="form-group">
<input type="text" placeholder="(optional) Billing address" class="form-control" name="address" id="address">
</div>
</div>

<div class="col-lg-12">
<div class="form-group">
<label>
  <input type="checkbox" name="photos" value="photos" required>
  I hereby agree that I accept videos and pictures of my person can be made according to our <a href="/agb">terms & privacy policy</a>
</label>
</div>
</div>

<div class="col-lg-12">
<div class="form-group">
<label>
  <input type="checkbox" name="terms" value="terms" required>
  I hereby agree to the <a href='/agb'>Terms and Conditions</a>
</label>
</div>
</div>

<div class="col-lg-12">
<div class="form-group">
<label>
  <input type="checkbox" name="ticketing" value="ticketing" required>
  I hereby agree that the Green Coding Solutions GmbH can use my Data for ticketing purposes.
</label>
</div>
</div>

<div class="mt-4">
<button type="submit" id="contact-submit" class="btn btn-hero btn-rounded " value="Buy Now">Buy Now</button>
</div>

</form>

<script>
    var form = document.getElementById("ticket-form");

    async function handleSubmit(event) {
      event.preventDefault();
      var status = document.getElementById("form-status");
      var data = new FormData(event.target);
      fetch(event.target.action, {
        method: form.method,
        body: data,
        headers: {
            'Accept': 'application/json'
        }
      }).then(response => {
        status.classList.remove("d-none");

        if (response.ok) {
          status.innerHTML = "Thanks for being part of this amazing event! We will be in touch soon with more information.";
          form.reset()
        } else {
          response.json().then(data => {
            if (Object.hasOwn(data, 'errors')) {
              status.innerHTML = data["errors"].map(error => error["message"]).join(", ")
            } else {
              status.innerHTML = "Oops! There was a problem submitting your form"
            }
          })
        }
      }).catch(error => {
        status.innerHTML = "Oops! There was a problem submitting your form"
      });
    }
    form.addEventListener("submit", handleSubmit)
</script>