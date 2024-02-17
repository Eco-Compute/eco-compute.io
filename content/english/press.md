---
title: "Press"
date: 2019-09-10T13:51:25+06:00
draft: false
description: "Press accreditation for the EcoCompute Conference 2024 in Munich, Germany"
bg_image : "images/bg/cta-bg.webp"
---


## Presse Akkreditierung

Sie möchten über die erste Tech-Konferenz zur digitalen Nachhaltigkeit in Hardware und Software berichten?

Bitte nutzen Sie das untenstehende Formular oder kontaktieren Sie uns via E-Mail an [info@eco-compute.io](mailto:info@eco-compute.io). 

Für Journalisten bieten wir eine begrenzte Menge an kostenlosen Tickets an.

Wir melden uns schnellstmöglich zurück.

<div class="alert alert-info d-none" role="alert" id="form-status">
</div>

<div class="container">
    <div class="row">
        <div class="col">
            <form id="press-form" action="https://formspree.io/f/xrgnqyqy" method="POST"  style="margin-bottom: 50px;">
                <div class="contact-form pl-4 mt-5 mt-lg-0">
                    <div class="form-row">
                        <div class="col-lg-6">
                            <div class="form-group">
                                <input type="text" placeholder="Vorname" class="form-control" name="fname" id="fname" required>
                            </div>
                        </div>
                        <div class="col-lg-6">
                            <div class="form-group">
                                <input type="text" placeholder="Nachname" class="form-control" name="sname" id="sname" required>
                            </div>
                        </div>
                        <div class="col-lg-12">
                            <div class="form-group">
                                <input type="email" placeholder="E-mail" class="form-control" name="email" id="email" required>
                            </div>
                        </div>
                        <div class="col-lg-12">
                            <div class="form-group">
                                <input type="text" placeholder="Unternehmen" class="form-control" name="company" id="company" required>
                            </div>
                        </div>
                        <div class="col-lg-12">
                            <div class="form-group">
                                <textarea placeholder="Ihre Nachricht" class="form-control" name="message" id="message" rows=10 required></textarea>
                            </div>
                        </div>
                        <div class="mt-4">
                            <button type="submit" id="contact-submit" class="btn btn-hero btn-rounded " value="Absenden">Absenden</button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
        <div class="col">
            <div class="container">
                <div class="row">
                    <div class="col">
                        <h3>Medienkontakt</h3>
                        <h4>Petra Rulsch</h4>
                        <p>Kontakt: <a href="mailto:pr@petra-rulsch.com">E-Mail</a> / <a href="https://www.linkedin.com/in/petrarulsch/">LinkedIn</a></p>
                    </div>
                    <div class="col">
                        <div class="time-table">
                            <div class="content-img text-lg-right">
                                <img src="https://www.green-coding.io/img/team/petra.webp" alt="" class="img-fluid" loading="lazy">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script>
    var form = document.getElementById("press-form");

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
                status.innerHTML = "Vielen Dank für Ihre Anfrage! Wir melden uns umgehend.";
                form.reset()
            } else {
                response.json().then(data => {
                    if (Object.hasOwn(data, 'errors')) {
                        status.innerHTML = data["errors"].map(error => error["message"]).join(", ")
                    } else {
                        status.innerHTML = "Oops! Es gab ein Problem mit dem Absenden des Formulars. Bitte wenden Sie sich an info@eco-compute.io"
                    }
                })
            }
        }).catch(error => {
            status.innerHTML = "Oops! Es gab ein Problem mit dem Absenden des Formulars. Bitte wenden Sie sich an info@eco-compute.io"
        });
    }
    form.addEventListener("submit", handleSubmit)
</script>

