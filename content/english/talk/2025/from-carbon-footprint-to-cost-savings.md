---
title: "From Carbon Footprint to Cost Savings: Sustainable Optimization of AI Systems with GAISSA-Optimizer 🇬🇧"
date: 2025-11-14T09:00:00+01:00
draft: false
bg_image : "images/bg/cta-bg.webp"
speaker_name: "Joel Castaño Fernández, Alexandra González Álvarez, Violeta Bonet Vila"
speaker_company: "Universitat Politècnica de Catalunya"
talk_room: "Data Centers / Infrastructure / Management (DIM)"
talk_date: "14.11.2025 09:00"
type : "talk"
duration: "50 Minutes"
outdated: false
---

All the investments in building highly accurate Artificial Intelligence (AI) systems have led to a dramatic growth in data volume, model size, and infrastructure capacity. Training costs, measured in computing resources, have skyrocketed, rising by orders of magnitude in just a few years, while inference has become the dominant contributor to AI’s energy footprint, accounting for up to 90% of total Machine Learning costs. To illustrate, a single Large Language Model (LLM) query can consume around ten times more energy than a traditional web search and translate into hundreds of thousands of euros per year in hardware expenditure.

In this talk, we present GAISSA-Optimizer as the culmination of several strands of research in the GAISSA project on green AI-based systems. We first show how large-scale repository mining of Hugging Face models revealed the current carbon footprint and poor adoption of sustainable practices in real AI ecosystems, and how these insights led to GAISSALabel, our tool for generating standardized energy labels for AI models. We then summarize empirical results on AI optimization tactics (e.g., quantization, pruning, compilation, and training tricks such as early stopping and layer freezing) that achieve up to 75% reductions in energy consumption and operational costs with limited impact on correctness.

Building on this foundation, we introduce GAISSA-Optimizer: a tool that (i) integrates these sustainable practices into AI development and deployment workflows, (ii) performs what-if and ROI analysis to quantify the economic benefits of energy-aware decisions, and (iii) issues energy efficiency labels aligned with emerging ISO and GSF standards. We close with a preview of ongoing work on a static and fine-grained energy consumption of Python code execution prediction model, outlining how these upcoming capabilities will further enrich GAISSA-Optimizer’s cost and sustainability analytics.
