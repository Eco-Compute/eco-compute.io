---
title: "Deep Sleep by Design - Building Linux Products that truly Sleep - Workshop"
date: 2025-08-25T10:51:25+06:00
draft: false
description: "A workshop to engineer low power linux systems to be used in mobile or embedded systems"
bg_image : "images/bg/cta-bg.webp"
type : "workshop"
icon: "tf-tools-2"
outdated: false
name: "Arne Tarara"
image : "images/teams/arne-tarara.webp"

---

### Goals of the workshop

- Get to know concepts of power saving and hardware design that result in altered power consumption
- Deep dive into the linux kernel to learn settings that contribute to system sleep and wake states which result in energy consumption

---


### Key info
- **Target Group**: Hardware developers, hardware vendors, low-level software developers, engineers interested in power efficiency
- **Duration**: 3 hours
- **Format**: Presentation & Hands-On

---


### Description
Power is one of the tightest resource in embedded systems. This hands-on workshop
shows how to combine modern ARM SoC and Intel capabilities with Linux power-management
subsystems so your device spends as much time as possible in deep sleep—yet
wakes quickly and predictably to get work done. 
We'll align on 
- shutdown vs. throttling
- power/clock domains
- state retention
- and wake sources

then walk the key Linux building blocks: 
- CPUIdle/C-states
- CPUFreq (DVFS)
- Runtime PM
- System Suspend
- PM QoS
- wakelocks
- and opportunistic sleep with tickless idle

We start our hands-on workshop from a deliberately poor baseline and, step by
step, turn it into a system with high sleep residency and low power draw.
You’ll learn how to connect essential hardware capabilities to the right Linux
power-management building blocks, focusing on what matters. 

Each improvement is validated with simple measurements so progress is repeatable and
trustworthy. You leave with a concise sleep-first checklist and the confidence
to apply the same method to your own products, from early prototypes to
production.