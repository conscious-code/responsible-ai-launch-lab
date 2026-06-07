from scenarios import PRINCIPLES, BUSINESS_PRESSURE


INITIAL_SCORE = 50
MIN_SCORE = 0
MAX_SCORE = 100
RECOVERY_THRESHOLD = 40


PRINCIPLE_DEFINITIONS = {
    "Fairness": "AI systems should avoid unfair bias and unequal outcomes across people or groups.",
    "Reliability & Safety": "AI systems should work reliably and safely under expected and unexpected conditions.",
    "Privacy & Security": "AI systems should protect data, respect consent, and use secure handling practices.",
    "Inclusiveness": "AI systems should support diverse users, abilities, languages, and contexts.",
    "Transparency": "AI systems should be understandable, explainable, and clear about limitations.",
    "Accountability": "People and organizations should remain responsible for AI system decisions and impacts.",
}


def initial_scores():
    """
    Create the starting score state for all Responsible AI principles
    and the separate Business Pressure meter.
    """
    scores = {principle: INITIAL_SCORE for principle in PRINCIPLES}
    scores[BUSINESS_PRESSURE] = INITIAL_SCORE
    return scores


def clamp_score(value):
    """
    Keep scores between 0 and 100.
    """
    return max(MIN_SCORE, min(MAX_SCORE, value))


def apply_impact(scores, impact):
    """
    Apply a decision's score changes to the current score state.
    Returns a new score dictionary so the original is not modified directly.
    """
    updated_scores = scores.copy()

    for meter, change in impact.items():
        current_value = updated_scores.get(meter, INITIAL_SCORE)
        updated_scores[meter] = clamp_score(current_value + change)

    return updated_scores


def changed_meters(impact):
    """
    Return only the meters that changed.
    This supports the multimedia design principle of signaling:
    learners first see what changed, instead of processing all meters equally.
    """
    return {meter: change for meter, change in impact.items() if change != 0}


def responsible_ai_average(scores):
    """
    Calculate the average of only the six Responsible AI principles.
    Business Pressure is intentionally excluded because it is not a Responsible AI principle.
    """
    total = sum(scores[principle] for principle in PRINCIPLES)
    return total / len(PRINCIPLES)


def launch_readiness_profile(scores):
    """
    Convert the Responsible AI average score into a final profile.
    """
    avg = responsible_ai_average(scores)

    if avg >= 80:
        return "Responsible Launch Ready"
    if avg >= 65:
        return "Promising, but Needs Targeted Review"
    if avg >= 50:
        return "Needs Additional Responsible AI Review"
    return "High Responsible AI Risk"


def weakest_principles(scores, count=2):
    """
    Identify the lowest-scoring Responsible AI principles for the final debrief.
    """
    sorted_principles = sorted(PRINCIPLES, key=lambda principle: scores[principle])
    return sorted_principles[:count]


def lowest_principle(scores):
    """
    Identify the single lowest Responsible AI principle.
    """
    return min(PRINCIPLES, key=lambda principle: scores[principle])


def needs_recovery_support(scores):
    """
    Recovery support is triggered if any Responsible AI principle drops below 40.
    Business Pressure does not trigger recovery because it is not a Responsible AI principle.
    """
    return any(scores[principle] < RECOVERY_THRESHOLD for principle in PRINCIPLES)


def recovery_message(scores):
    """
    Create targeted recovery guidance based on the learner's weakest principle.
    """
    principle = lowest_principle(scores)
    definition = PRINCIPLE_DEFINITIONS[principle]

    return {
        "principle": principle,
        "definition": definition,
        "message": (
            f"Your lowest Responsible AI area is {principle}. "
            f"Before the next scenario, focus on how your next decision could better protect this principle."
        ),
    }


def summarize_choice_history(choice_history):
    """
    Create a short summary of player choices for the final debrief.
    """
    if not choice_history:
        return []

    summary = []
    for item in choice_history:
        summary.append(
            {
                "scenario": item["scenario_title"],
                "choice": item["choice_text"],
                "primary_principle": item["primary_principle"],
            }
        )
    return summary