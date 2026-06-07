# Responsible AI Launch Lab

Responsible AI Launch Lab is a scenario-based educational game prototype designed for game-based learning. Players take on the role of a product lead preparing an AI-powered feature for launch. Across five scenarios, players make decisions aligned with Microsoft Responsible AI principles and observe how those decisions affect the product’s Responsible AI readiness.

## Learning Goal

The goal of the game is to help learners move beyond memorizing Responsible AI principles and practice applying them under realistic product launch pressure.

## Microsoft Responsible AI Principles

The game uses six Responsible AI meters:

- Fairness
- Reliability & Safety
- Privacy & Security
- Inclusiveness
- Transparency
- Accountability

The game also includes Business Pressure as a separate contextual constraint. Business Pressure is not treated as a Responsible AI principle.

## Game-Based Learning Design

The core gameplay loop is:

Scenario challenge → planning prediction → player decision → impact meters update → feedback → reflection → next scenario

This supports learning through decision-making, consequences, and reflection rather than passive content delivery.

## Self-Regulated Learning Integration

The prototype includes four SRL dimensions:

- Planning: players predict which Responsible AI principle is most at risk before seeing options.
- Monitoring: players track impact meters and written feedback.
- Control: players adjust decisions as scenarios become more complex.
- Reflection: players write short reflections and review decision patterns at the end.

## Adaptivity and Personalization

The game includes simple rule-based adaptivity:

- Beginner Mode: definitions, optional hints, and guided feedback.
- Challenge Mode: fewer hints and more independent reasoning.
- Recovery support: if a Responsible AI principle score drops below 40, the game provides targeted support.

## Multimedia and Cognitive Design

The interface uses a clean dashboard layout, short scenario text, separated Business Pressure, highlighted changed meters, and step-by-step feedback. These design choices reduce extraneous cognitive load and support focused decision-making.

## How to Run the Prototype

Install dependencies:

```bash
pip install -r requirements.txt