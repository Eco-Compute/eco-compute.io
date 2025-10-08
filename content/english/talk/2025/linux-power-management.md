---
title: "Linux Power Management"
date: 2025-11-13T17:15:00+01:00
draft: false
bg_image : "images/bg/cta-bg.webp"
speaker_name: "Marco Liess"
speaker_company: "TU Munich"
speaker_image : "images/teams/marco-liess-small.webp"
speaker_link: "speakers/2025/marco-liess/"
talk_room: "Software & Hardware (So-Ha)"
talk_date: "13.11.2025 17:15"
type : "talk"
duration: "50 Minutes"
outdated: false
---

Webservers are inherently demand driven and request rates can fluctuate
significantly, both throughout the day but also in the order of milliseconds
and less. 

Dynamic Voltage/Frequency Scaling (DVFS) is a popular hardware
mechanisms to reduce the power consumption of CPUs and scale their performance
to match the required demand. 

Modern operating systems such as Linux perform
power management based on recent thread activity, some CPUs support autonomous
DVFS control based on processor utilization. However, changes in performance
state incur a certain switching latency and finding the optimal state is not
trivial. 

Therefore, many servers always operate on the highest performance
level to ensure responsiveness and low-latency request handling. 

This talk will provide a background on the hardware aspects of DVFS and the interaction
with Linux power governors, illustrate challenges of DVFS management in
request-driven networking applications and explore potential solutions using
the help of SmartNICs. 

SmartNICs can monitor incoming network traffic and aid
in system-level tasks such as load balancing and power management, thereby
offering potential to improve server utilization and energy-efficiency. 


The
presentation will cover recent research progress in this area, including
measurement results from a testbed with FPGA-based SmartNICs and comparison to
state-of-the-art solutions.