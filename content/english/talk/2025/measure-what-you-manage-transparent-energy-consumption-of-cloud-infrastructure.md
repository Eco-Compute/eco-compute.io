---
title: "Measure what you manage: Transparent Energy consumption of cloud infrastructure 🇬🇧"
date: 2025-11-13T10:55:00+01:00
draft: false
bg_image : "images/bg/cta-bg.webp"
speaker_name: "Josefine Kipke"
speaker_company: "Open Source Business Alliance"
speaker_image : "https://cfp.eco-compute.io/media/avatars/9T7HJS_9jwdXPV.JPG"
speaker_link: "speaker/josefine-kipke/"
talk_room: "Data Centers / Infrastructure / Management (DIM)"
talk_date: "13.11.2025 10:55"
type : "talk"
outdated: false
---

The ECO:DIGIT research project develops open-source methods for the holistic measurement of the ecological footprint  of digital systems. This talk presents the eco-digit balancer, a sustainability runtime monitoring system for OpenStack based SCS compliant cloud infrastructure. It links software workloads with actual source usage and provides both lifecycle and runtime reporting for cloud admins and tenants. The monitoring solution integrates bills of material from asset management tools, hardware sensors, and exporters. Technical challenges such as heterogenous hardware, attribution of consumption to tenants and workloads, and proportional allocation to control plane components will be addressed. Participants will see a highly technical talk with a live demo, our architecture blueprint, and learn how to apply these methods to make their own infrastructure more transparent.

The ECO:DIGIT research project is developing methods for measuring the ecological footprint of digital systems in a holistic way. The aim is to correlate software workload with actual resource consumption, and quantify the resulting impact.  As part of this work, we have created a sustainability runtime monitoring solution for Sovereign Cloud Stack (SCS)-compliant Infrastructure as a Service (IaaS) clouds.

In this talk, we will present ECO:DIGIT Balancer, our open-source sustainability monitoring solution for OpenStack-based IaaS environments. We will also present our technology-stack agnostic architecture blueprint, which can be applied across distributed cloud environments.

We will demonstrate its implementation, including load tests and resulting reports, to illustrate the blueprint's practical application. The blueprint is intended as a reusable model for sustainability monitoring, providing a clear separation between metric definition and collection. This enables operators to select the most suitable sensors, exporters, or database systems for their environment.

Our monitoring solution combines data from hardware sensors and asset management sources, such as NetBox and Snipe-IT, with runtime exporters to generate consistent power and energy metrics. Device bills of material, created using asset management tools, are used to integrate life-cycle data for the manufacturing and disposal phases. We will address technical challenges such as heterogeneous hardware, attributing energy and resource consumption to tenant workloads and proportionally allocating control plane overhead in detail. Next to this we will focus on reporting strategies.

This will be a highly technical talk where participants can expect to gain concrete insights into the current architecture and implementation status. Learn from our experience and find out how you can follow our lead to make infrastructure more transparent from an environmental perspective.
