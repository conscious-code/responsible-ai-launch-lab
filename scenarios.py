PRINCIPLES = [
    "Fairness",
    "Reliability & Safety",
    "Privacy & Security",
    "Inclusiveness",
    "Transparency",
    "Accountability",
]

BUSINESS_PRESSURE = "Business Pressure"


SCENARIOS = [
    {
        "title": "Fairness in AI Screening",
        "primary_principle": "Fairness",
        "secondary_principles": ["Accountability", "Transparency"],
        "description": (
            "Your team is preparing to launch an AI résumé screening tool for enterprise customers. "
            "During testing, the system appears to rank candidates from certain universities higher, "
            "even when candidates have similar skills and experience. A major customer is waiting, "
            "and the business team wants to launch next week."
        ),
        "hint": (
            "Look for whether the option prevents unfair outcomes before users are affected, "
            "not just whether it explains the system after launch."
        ),
        "reflection_prompt": (
            "Which Responsible AI principle was most at risk in this scenario, and why?"
        ),
        "choices": [
            {
                "text": "Launch now and monitor complaints after release.",
                "impact": {
                    "Fairness": -20,
                    "Reliability & Safety": -5,
                    "Privacy & Security": 0,
                    "Inclusiveness": -10,
                    "Transparency": -5,
                    "Accountability": -15,
                    "Business Pressure": 15,
                },
                "feedback": (
                    "This reduces business pressure in the short term, but it weakens fairness and accountability. "
                    "Monitoring after launch does not prevent unequal treatment before candidates are affected."
                ),
            },
            {
                "text": "Delay launch and conduct a fairness review.",
                "impact": {
                    "Fairness": 20,
                    "Reliability & Safety": 10,
                    "Privacy & Security": 0,
                    "Inclusiveness": 10,
                    "Transparency": 10,
                    "Accountability": 15,
                    "Business Pressure": -10,
                },
                "feedback": (
                    "This is a stronger responsible AI decision. It creates time to investigate unequal outcomes, "
                    "document findings, and reduce harm before release."
                ),
            },
            {
                "text": "Remove university name from model inputs and retest.",
                "impact": {
                    "Fairness": 10,
                    "Reliability & Safety": 5,
                    "Privacy & Security": 0,
                    "Inclusiveness": 5,
                    "Transparency": 5,
                    "Accountability": 5,
                    "Business Pressure": -5,
                },
                "feedback": (
                    "This may help, but it may not fully solve the issue. Other variables could still act as proxies "
                    "for university background or social advantage."
                ),
            },
            {
                "text": "Add a disclaimer saying the AI is only advisory.",
                "impact": {
                    "Fairness": -5,
                    "Reliability & Safety": 0,
                    "Privacy & Security": 0,
                    "Inclusiveness": -5,
                    "Transparency": 10,
                    "Accountability": -5,
                    "Business Pressure": 5,
                },
                "feedback": (
                    "A disclaimer may improve transparency slightly, but it does not address the underlying fairness issue. "
                    "Responsible design requires fixing the risk, not only explaining it."
                ),
            },
        ],
    },
    {
        "title": "Reliability and Safety in AI Support",
        "primary_principle": "Reliability & Safety",
        "secondary_principles": ["Transparency", "Accountability"],
        "description": (
            "Your team is launching an AI customer support assistant. In testing, the assistant sometimes gives "
            "confident but incorrect advice for high-impact account issues, such as billing disputes and account recovery."
        ),
        "hint": (
            "Consider whether the AI should handle high-impact cases before its reliability has been validated."
        ),
        "reflection_prompt": (
            "How should a product team decide which AI use cases are safe enough for launch?"
        ),
        "choices": [
            {
                "text": "Launch fully because human agents can correct mistakes later.",
                "impact": {
                    "Fairness": 0,
                    "Reliability & Safety": -20,
                    "Privacy & Security": 0,
                    "Inclusiveness": -5,
                    "Transparency": -5,
                    "Accountability": -10,
                    "Business Pressure": 15,
                },
                "feedback": (
                    "This increases launch speed but creates safety risk. Human correction after harm occurs is not the same "
                    "as preventing unreliable AI behavior in high-impact situations."
                ),
            },
            {
                "text": "Limit the assistant to low-risk questions until further testing is complete.",
                "impact": {
                    "Fairness": 5,
                    "Reliability & Safety": 20,
                    "Privacy & Security": 5,
                    "Inclusiveness": 5,
                    "Transparency": 10,
                    "Accountability": 10,
                    "Business Pressure": -10,
                },
                "feedback": (
                    "This is a responsible staged-launch decision. It limits potential harm while the team gathers more evidence "
                    "about reliability and safety."
                ),
            },
            {
                "text": "Launch with a warning that answers may be imperfect.",
                "impact": {
                    "Fairness": 0,
                    "Reliability & Safety": -10,
                    "Privacy & Security": 0,
                    "Inclusiveness": 0,
                    "Transparency": 10,
                    "Accountability": -5,
                    "Business Pressure": 10,
                },
                "feedback": (
                    "The warning improves transparency, but it does not make the system reliable or safe. Transparency cannot replace "
                    "appropriate safeguards."
                ),
            },
        ],
    },
    {
        "title": "Privacy and Security in Model Improvement",
        "primary_principle": "Privacy & Security",
        "secondary_principles": ["Transparency", "Accountability"],
        "description": (
            "The product team wants to use customer chat logs to improve the AI model. The logs may include personal or sensitive "
            "information, and user consent for this use is unclear."
        ),
        "hint": (
            "Focus on consent, data minimization, access control, and secure handling before using customer data."
        ),
        "reflection_prompt": (
            "What data governance question should be answered before this model improvement work begins?"
        ),
        "choices": [
            {
                "text": "Use the data because it will improve the model.",
                "impact": {
                    "Fairness": 0,
                    "Reliability & Safety": 5,
                    "Privacy & Security": -25,
                    "Inclusiveness": 0,
                    "Transparency": -10,
                    "Accountability": -15,
                    "Business Pressure": 15,
                },
                "feedback": (
                    "Better model performance does not justify unclear data use. Responsible AI requires privacy, consent, "
                    "security, and governance before using sensitive user data."
                ),
            },
            {
                "text": "Pause the work until consent, retention, and access controls are clarified.",
                "impact": {
                    "Fairness": 0,
                    "Reliability & Safety": 5,
                    "Privacy & Security": 25,
                    "Inclusiveness": 0,
                    "Transparency": 15,
                    "Accountability": 20,
                    "Business Pressure": -10,
                },
                "feedback": (
                    "This strengthens privacy, transparency, and accountability. It ensures the team understands what data can be used, "
                    "who can access it, and how long it should be retained."
                ),
            },
            {
                "text": "Ask engineers to manually remove sensitive fields when they see them.",
                "impact": {
                    "Fairness": 0,
                    "Reliability & Safety": 0,
                    "Privacy & Security": -5,
                    "Inclusiveness": 0,
                    "Transparency": -5,
                    "Accountability": -5,
                    "Business Pressure": 5,
                },
                "feedback": (
                    "Manual cleanup is not a reliable privacy strategy. The team needs a clear process, not informal judgment during implementation."
                ),
            },
        ],
    },
    {
        "title": "Inclusiveness and Accessibility",
        "primary_principle": "Inclusiveness",
        "secondary_principles": ["Fairness", "Reliability & Safety"],
        "description": (
            "The AI feature works well for fluent English speakers but performs poorly for non-native speakers and users who rely "
            "on assistive technologies. The team is considering launching for the majority user group first."
        ),
        "hint": (
            "Ask whether launching now would exclude users who should have been considered during design and testing."
        ),
        "reflection_prompt": (
            "How can inclusive design reduce harm before launch rather than after complaints appear?"
        ),
        "choices": [
            {
                "text": "Launch for the majority user group first and improve later.",
                "impact": {
                    "Fairness": -10,
                    "Reliability & Safety": -10,
                    "Privacy & Security": 0,
                    "Inclusiveness": -25,
                    "Transparency": -5,
                    "Accountability": -10,
                    "Business Pressure": 15,
                },
                "feedback": (
                    "This treats inclusion as a later enhancement. Users with different language or accessibility needs may be excluded from the start."
                ),
            },
            {
                "text": "Expand testing with diverse users and assistive technology scenarios before launch.",
                "impact": {
                    "Fairness": 15,
                    "Reliability & Safety": 15,
                    "Privacy & Security": 0,
                    "Inclusiveness": 25,
                    "Transparency": 10,
                    "Accountability": 15,
                    "Business Pressure": -10,
                },
                "feedback": (
                    "This is a stronger inclusive design choice. It improves the chance that the AI feature works across diverse user needs before release."
                ),
            },
            {
                "text": "Add a note that the feature works best in English.",
                "impact": {
                    "Fairness": -5,
                    "Reliability & Safety": -5,
                    "Privacy & Security": 0,
                    "Inclusiveness": -10,
                    "Transparency": 10,
                    "Accountability": -5,
                    "Business Pressure": 5,
                },
                "feedback": (
                    "The note improves transparency but does not address the exclusion. Responsible AI should reduce barriers, not only disclose them."
                ),
            },
        ],
    },
    {
        "title": "Transparency and Accountability After Harm",
        "primary_principle": "Accountability",
        "secondary_principles": ["Transparency", "Reliability & Safety"],
        "description": (
            "After a pilot release, a user reports that the AI system made a harmful recommendation. The team is unsure who owns "
            "the response, explanation, investigation, and remediation."
        ),
        "hint": (
            "Look for a decision that creates ownership, escalation, investigation, and communication."
        ),
        "reflection_prompt": (
            "What does accountability require after an AI system causes or contributes to harm?"
        ),
        "choices": [
            {
                "text": "Let customer support handle the complaint as a normal ticket.",
                "impact": {
                    "Fairness": -5,
                    "Reliability & Safety": -10,
                    "Privacy & Security": 0,
                    "Inclusiveness": -5,
                    "Transparency": -10,
                    "Accountability": -25,
                    "Business Pressure": 10,
                },
                "feedback": (
                    "This minimizes the issue and weakens accountability. Harmful AI behavior may require escalation, investigation, and product-level action."
                ),
            },
            {
                "text": "Create an escalation path, assign ownership, investigate the issue, and communicate next steps.",
                "impact": {
                    "Fairness": 10,
                    "Reliability & Safety": 20,
                    "Privacy & Security": 5,
                    "Inclusiveness": 10,
                    "Transparency": 20,
                    "Accountability": 25,
                    "Business Pressure": -10,
                },
                "feedback": (
                    "This is the strongest accountable response. It assigns ownership, investigates the issue, communicates clearly, and supports remediation."
                ),
            },
            {
                "text": "Disable the feature immediately without explanation.",
                "impact": {
                    "Fairness": 5,
                    "Reliability & Safety": 15,
                    "Privacy & Security": 0,
                    "Inclusiveness": 5,
                    "Transparency": -15,
                    "Accountability": 5,
                    "Business Pressure": -15,
                },
                "feedback": (
                    "Disabling the feature may reduce immediate risk, but doing so without explanation weakens transparency and may reduce user trust."
                ),
            },
        ],
    },
]