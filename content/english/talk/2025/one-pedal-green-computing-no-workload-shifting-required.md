---
title: "One-pedal green computing: no (workload) shifting required 🇬🇧"
date: 2025-11-13T14:50:00+01:00
draft: false
bg_image : "images/bg/cta-bg.webp"
speaker_name: "Dr. Oleksiy Kozlov"
speaker_company: "HITS gGmbH"
speaker_image : "images/teams/oleksiy-kozlov-small.webp"
speaker_link: "speaker/2025/oleksiy-kozlov/"
talk_room: "Software & Hardware (So-Ha)"
talk_date: "13.11.2025 14:50"
type : "talk"
duration: "25 Minutes"
slide_link: "/files/slides_2025/01_Thursday/01_SoHa/10_Kozlov_Onepedal.pdf"
outdated: false
---

Classical carbon-aware computing approaches usually rely on shifting computational workloads in time (scheduling) and space (between datacenters) to follow the availability of renewable energy. This makes them difficult to use with jobs that  e.g., run for multiple days or depend on large amount of input data. 

But what if we could operate our computer like an electric car, applying "gas pedal" to modulate speed and energy consumption based on real-time carbon intensity or electricity price? 
  
Good news is that modern chips and operating systems do support dynamic power scaling, and often provide multiple ways to control it. Hence, this technique can be applied virtually anywhere, from Raspberry Pi to multi-node GPU cluster.

We recently evaluated carbon-aware power scaling using multiple real-world workloads and historical electricity market data. In this talk, I will present experimental results as well as discuss potential deployment scenarios in production systems.