---
title: "Green your Code: Oaklean’s vision for sustainable Node.js projects 🇬🇧"
date: 2025-11-13T09:45:00+01:00
draft: false
bg_image : "images/bg/cta-bg.webp"
speaker_name: "Kay Makowsky"
speaker_company: "Hitabis"
speaker_image : "images/teams/kay-makowsky-small.webp"
speaker_link: "speaker/2025/kay-makowsky/"
talk_room: "Software & Hardware (So-Ha)"
talk_date: "13.11.2025 09:45"
type : "talk"
talk_label: "📌 Measuring"
outdated: false
---

Oaklean is an open-source tool that visualizes and optimizes the energy consumption of Node.js/JavaScript/Typescript applications.

In this talk, we demonstrate Oaklean’s technical workflow and share our broader vision: to build a community-driven database of software libraries rated by their environmental footprint.

The session is aimed at developers, technical decision-makers, and sustainability officers who want actionable strategies for greener software development.

Software development contributes substantially to global energy use (e.g. Internet traffic alone causes ~3.7% of global CO₂ emissions). In other words, “every line of code you write has an energy signature”.

Oaklean (https://www.oaklean.io) was created to help tackle this problem by bringing energy-awareness into the development process. It profiles Node.js and JavaScript/Typescript code to reveal how much CPU time and energy each function or dependency consumes. Developers can see the energy impact of their application in real time, helping to pinpoint and eliminate wasteful patterns.

Oaklean combines CPU energy measurements from hardware manufacturers with V8 engine instrumentation to deliver accurate, line-by-line energy profiling.

The tool integrates seamlessly into a developer’s workflow via a Visual Studio Code extension and a Jest testing environment.

As code is executed, Oaklean annotates each source line and library call with its estimated energy and time cost. This makes it easy to identify “hot spots,” such as an inefficient loop or a heavy library call, and to compare different commits or branches by their energy use.
