---
title: "cat /proc/energy: Power and Carbon Awareness Made Simple 🇬🇧"
date: 2025-11-13T15:45:00+01:00
draft: false
bg_image : "images/bg/cta-bg.webp"
speaker_name: "Geerd-Dietger Hoffmann"
speaker_company: "Green Coding Solutions"
speaker_image : "images/teams/didi-hoffmann-small.webp"
speaker_link: "speaker/2025/geerd-dietger-hoffmann/"
talk_room: "Software & Hardware (So-Ha)"
talk_date: "13.11.2025 15:45"
type : "talk"
duration: "25 Minutes"
slide_link: "/files/slides_2025/01_Thursday/01_SoHa/11_Hoffmann_Didi_ProcPower.pdf"
outdated: false
---

Energy efficiency is no longer a niche concern—it is a first-class systems metric alongside performance and scalability. Yet, developers and operators still lack lightweight, fine-grained tools to observe how individual processes and containers consume energy. In this talk, we present procpower a Linux kernel module that exposes per-PID runtime, I/O, and energy-related statistics directly via /proc and debugfs. By integrating Intel RAPL counters with kernel task accounting, the module enables high-frequency sampling of CPU, memory, disk, and network usage at less than 0.3 % overhead on modern hosts. These metrics power an extensible linear energy model whose weights can be retrained to reflect local hardware characteristics or external carbon-intensity signals.
Crucially, the module is container-aware: when run on the host, the same per-cgroup metrics become securely visible inside Docker containers, making energy monitoring a first-class citizen in multi-tenant environments
