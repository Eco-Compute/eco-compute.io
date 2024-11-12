---
title: "Call for Speakers"
date: 2019-09-10T13:51:25+06:00
draft: true
description: "Call for Speakers for the EcoCompute Conference 2025 in Berlin, Germany"
bg_image : "images/bg/cta-bg.webp"
socialmedia_preview: "images/social-media-previews/call-for-speakers.webp"

---

## Call for Speakers: Share Your Expertise!

{{< alert >}}
The call for Call for Speakers for <b>software-only</b> related talks is <b>closed</b> as of 31.01.2024 ❌
<br>We are still accepting <b>hardware</b> ✅ and / or <b>datacenter</b> ✅ related talks. 
<br>Also, if you have been invited by us individually to submit a talk please still use the form. 
{{</ alert >}}

We're excited to invite dynamic and knowledgeable speakers to submit their talks for our upcoming conference. This is your opportunity to inspire, engage, and impart wisdom to a diverse audience eager for new insights and perspectives.

Under our [about](/about) page you find some details what the conference will focus on. In short: We are looking for talks that focus on sustainablity engineering solutions in hardware and software to reduce resource consumption of digital infrastructure.

Here are some examples of topics that we deem matching to the conference topic, but please also suggest talks that broaden the scope and address sustainability topics that are not listed here:

- Case studies with customers and/or companies around implementing sustainability in hardware products / software products / datacenters
- Academic research projects or industry R&D on sustainability in hardware products / software products / datacenters
- Identification of problems why sustainability features/techniques are not used in tech companies and the cloud
- Identification of problems why sustainabilty / efficiency features in hardware are not taken up by software
- New hardware / hardware-features / software / tools to save resources (energy, CO2, extended hardware refresh cycles)
- Saving energy through thermal management / energy monitoring / power converters / SoC power management / battery management (e.g. optimizing heat dissipation, material selection, power rail measurement, NPUs, network adapters)
- Expertise in AI models that focus on techniques contributing to the minimization of carbon emissions

**We accept talks in English and German.**


{{< alert >}}
The call for Call for Speakers for <b>software-only</b> related talks is <b>closed</b> as of 31.01.2024 ❌
<br>We are still accepting <b>hardware</b> ✅ and / or <b>datacenter</b> ✅ related talks. 
<br>Also, if you have been invited by us individually to submit a talk please still use the form. 
{{</ alert >}}

<form
  id="speaker-form"
  action="https://formspree.io/f/mgejgkbv"
  method="POST"
>
<div class="col-lg-6">
<div class="contact-form pl-4 mt-5 mt-lg-0">
<form method="post" action="#">
<div class="form-row">
<div class="col-lg-6">
<div class="form-group">
<input type="text" placeholder="Your Name" class="form-control" name="name" id="name" required>
</div>
</div>

<div class="col-lg-6">
<div class="form-group">
<input type="email" placeholder="Your Email" class="form-control" name="email" id="email" required>
</div>
</div>

<div class="col-lg-12">
<div class="form-group">
<input type="text" placeholder="Company (optional)" class="form-control" name="company" id="company">
</div>
</div>


<div class="col-lg-12">
<div class="form-group">
<input type="text" placeholder="Title of your talk" class="form-control" name="title" id="title" required>
</div>
</div>

<div class="col-lg-12">
<div class="form-group">
<input type="text" placeholder="Language of your talk" class="form-control" name="language" id="language" required>
</div>
</div>

<div class="col-lg-12">
<div class="form-group">

<select class=" form-control"  value="" id="length" name="length">
    <option value="30">20 Min. + Q&A (30 Min. total)</option>
    <option value="45" selected>30 Min. + Q&A (45 Min. total)</option>
    <option value="60">50 Min. + Q&A (60 Min. total)</option>
</select>
</div>
</div>


<div class="col-lg-12">
<div class="form-group">
    <textarea rows="6" placeholder="Your bio" class="form-control" name="bio" id="bio"></textarea>
</div>
</div>

<div class="col-lg-12">
<div class="form-group">
    <textarea rows="6" name="abstract" id="abstract" class="form-control" placeholder="A 500 word abstract"></textarea>
</div>
</div>
<div class="col-lg-12">Supporting files:
<div class="form-group">
    <input type="file" name="attachment" accept="image/png, image/jpeg">
</div>
</div>


<div class="mt-4">
<button type="submit" id="contact-submit" class="btn btn-hero btn-rounded " value="Send Message">Apply now</button>
</div>

</form>

<div class="alert alert-info d-none" role="alert" id="form-status">
</div>


<script>
  var form = document.getElementById("speaker-form");

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
        status.innerHTML = "Thanks for handing in a talk. We will evaluate all proposals by start of Feb. 2024";
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
