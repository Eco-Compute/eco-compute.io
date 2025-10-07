---
title: "Built to Last: The Art of Sustainable Software Design 🇬🇧"
date: 2025-11-14T11:10:00+01:00
draft: false
bg_image : "images/bg/cta-bg.webp"
speaker_name: "Wilco Burggraaf"
speaker_company: ""
speaker_image : "https://cfp.eco-compute.io/media/avatars/SAVYPK_M6oDnfV.jpg"
speaker_link: "speaker/wilco-burggraaf/"
talk_room: "Data Centers / Infrastructure / Management (DIM)"
talk_date: "14.11.2025 11:10"
type : "talk"
outdated: false
---

What if we built software to last not just for the next sprint but across changing hardware, energy constraints, and unpredictable demands? In this talk, we will explore how thoughtful coding can extend hardware lifespan, cut energy consumption, and enable systems to adapt gracefully without constant rewrites. Inspired by the enduring design of the pyramids, we will examine timeless principles like separation of concerns, graceful degradation, and green coding that make software both resilient and resource-conscious. From architectural decisions to everyday developer practices, we will dive into practical strategies for reducing thermal stress, managing network congestion, and aligning with renewable energy availability. Whether you are writing code or architecting distributed systems, you will walk away with actionable techniques to build smarter, leaner, and longer-lasting technology. Sustainability is not just a challenge for systems it is a mindset that every developer can embrace.

This presentation explores how software design choices affect energy efficiency, hardware longevity, and overall system sustainability. The following concepts will be discussed:

Thermal stress and its impact on hardware lifespan, including how spiky or inconsistent CPU usage can accelerate degradation, while stable, predictable software can extend the life of computing infrastructure. Runtime traces, CPU utilization graphs, and thermal metrics are used to illustrate these effects.

A universal approach to energy efficiency that emphasizes minimizing energy use regardless of time, location, or energy grid composition. This approach avoids dependency on renewable availability and supports equitable energy-conscious development in all environments.

A green-aware CI/CD integration testing framework that identifies inefficiencies such as idle CPU time, underutilized resources, and spiky usage patterns. These findings are presented using system metrics and prerecorded demonstrations involving containerized environments.

The impact of asynchronous execution and programming language design on sustainability. Comparisons across languages and paradigms are analyzed using execution time, energy consumption, and compute efficiency to highlight real-world trade-offs.

Graceful degradation techniques and architecture that enable systems to adapt under resource constraints by selectively disabling non-essential features. These strategies maintain a usable experience while reducing overall system demand.

A conceptual model called the one micro-operation to one hertz approach, used to reason about the energy cost of code at the line and function level. This model introduces energy as a fundamental design consideration alongside latency, memory, and network usage, with examples and a sustainable coding playbook included.
