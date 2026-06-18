import streamlit as st

from scenarios import PRINCIPLES, BUSINESS_PRESSURE
from scoring import PRINCIPLE_DEFINITIONS


def page_setup():
    """
    Configure the Streamlit page.
    """
    st.set_page_config(
        page_title="Responsible AI Launch Lab",
        page_icon="🧭",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def apply_custom_styles():
    """
    Light CSS styling to make the prototype feel like a clean dashboard.
    This supports the multimedia design direction from the storyboard:
    clear hierarchy, limited clutter, and separated Business Pressure.
    """
    st.markdown(
        """
        <style>
        .main-title {
            font-size: 2.4rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            font-size: 1.05rem;
            color: #4a5568;
            margin-bottom: 1.5rem;
        }
        .small-note {
            font-size: 0.9rem;
            color: #5f6b7a;
        }
        .principle-pill {
            display: inline-block;
            padding: 0.25rem 0.55rem;
            margin: 0.15rem;
            border-radius: 999px;
            background-color: #e8f1ff;
            color: #174ea6;
            font-size: 0.85rem;
            font-weight: 600;
        }
        .business-pill {
            display: inline-block;
            padding: 0.25rem 0.55rem;
            margin: 0.15rem;
            border-radius: 999px;
            background-color: #fff2df;
            color: #a85b00;
            font-size: 0.85rem;
            font-weight: 600;
        }
        .callout {
            padding: 1rem;
            border-radius: 0.75rem;
            background-color: #f7f9fc;
            border: 1px solid #dbe3ef;
            margin-bottom: 1rem;
        }
        .success-callout {
            padding: 1rem;
            border-radius: 0.75rem;
            background-color: #eef9f0;
            border: 1px solid #b9e6c3;
            margin-bottom: 1rem;
        }
        .warning-callout {
            padding: 1rem;
            border-radius: 0.75rem;
            background-color: #fff8e6;
            border: 1px solid #f2d27b;
            margin-bottom: 1rem;
        }
        .risk-callout {
            padding: 1rem;
            border-radius: 0.75rem;
            background-color: #fff0f0;
            border: 1px solid #f0b5b5;
            margin-bottom: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_title():
    st.markdown(
        '<div class="main-title">Responsible AI Launch Lab</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="subtitle">Practice responsible AI decisions before they become real-world consequences.</div>',
        unsafe_allow_html=True,
    )


def render_principle_pills():
    """
    Short principle labels only. This supports coherence by avoiding long definitions
    on the main decision screens.
    """
    pill_html = ""
    for principle in PRINCIPLES:
        pill_html += f'<span class="principle-pill">{principle}</span>'
    pill_html += f'<span class="business-pill">{BUSINESS_PRESSURE}</span>'

    st.markdown(pill_html, unsafe_allow_html=True)
    st.caption("Business Pressure is a contextual constraint, not a Microsoft Responsible AI principle.")


def render_principle_overview():
    """
    Principle overview used on the introduction screen and in Beginner Mode.
    """
    st.subheader("Microsoft Responsible AI Principles")

    cols = st.columns(2)
    for index, principle in enumerate(PRINCIPLES):
        with cols[index % 2]:
            st.markdown(f"**{principle}**")
            st.write(PRINCIPLE_DEFINITIONS[principle])

    st.markdown("---")
    st.markdown(f"**{BUSINESS_PRESSURE}**")
    st.write(
        "Represents launch pressure, customer commitments, time constraints, or business urgency. "
        "It creates realistic tension, but it is not a Responsible AI principle."
    )


def render_scores(scores, compact=False):
    """
    Render the Responsible AI meters and Business Pressure separately.
    This implements the dashboard separation from the multimedia design storyboard.
    """
    st.subheader("Responsible AI Impact Meters")

    for principle in PRINCIPLES:
        score = scores[principle]
        st.write(f"**{principle}: {score}/100**")
        st.progress(score / 100)

        if not compact:
            st.caption(PRINCIPLE_DEFINITIONS[principle])

    st.markdown("---")
    st.subheader("Contextual Constraint")
    business_score = scores[BUSINESS_PRESSURE]
    st.write(f"**{BUSINESS_PRESSURE}: {business_score}/100**")
    st.progress(business_score / 100)
    st.caption("Shown separately because it is not a Responsible AI principle.")


def render_changed_meters(changes):
    """
    Show only changed meters first, supporting the signaling principle.
    """
    st.subheader("What changed?")

    if not changes:
        st.write("No meter changed for this choice.")
        return

    for meter, change in changes.items():
        direction = "+" if change > 0 else ""
        if meter == BUSINESS_PRESSURE:
            st.markdown(f"🟧 **{meter}: {direction}{change}**")
        else:
            st.markdown(f"🟦 **{meter}: {direction}{change}**")


def render_mode_card(title, bullets):
    """
    Small helper for mode selection display.
    """
    with st.container(border=True):
        st.markdown(f"### {title}")
        for bullet in bullets:
            st.write(f"- {bullet}")


def render_scenario_header(scenario, scenario_number, total_scenarios):
    """
    Scenario header with principle signaling.
    """
    st.caption(f"Scenario {scenario_number} of {total_scenarios}")
    st.header(scenario["title"])

    st.markdown(
        f'<span class="principle-pill">Primary: {scenario["primary_principle"]}</span>',
        unsafe_allow_html=True,
    )

    secondary_html = ""
    for principle in scenario["secondary_principles"]:
        secondary_html += f'<span class="principle-pill">Secondary: {principle}</span>'

    st.markdown(secondary_html, unsafe_allow_html=True)

def render_scenario_brief(scenario):
    """
    Render scenario information in smaller content blocks.
    This reduces text density and creates a more immersive workplace role-play feel.
    Falls back to the original description if structured fields are not available.
    """
    role = scenario.get("role")
    context = scenario.get("context")
    tension = scenario.get("tension")
    decision_point = scenario.get("decision_point")

    if role or context or tension or decision_point:
        if role:
            st.markdown(f"**Your role:** {role}")

        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container(border=True):
                st.markdown("#### Context")
                st.write(context or "Not provided.")

        with col2:
            with st.container(border=True):
                st.markdown("#### Tension")
                st.write(tension or "Not provided.")

        with col3:
            with st.container(border=True):
                st.markdown("#### Decision Point")
                st.write(decision_point or "Not provided.")
    else:
        st.write(scenario["description"])
        
def render_planning_prompt(scenario):
    """
    SRL planning prompt. The SRL blueprint says players should predict
    the principle at risk before options appear.
    """
    st.subheader("Planning Prompt")
    st.write("Before seeing the decision options, predict which Responsible AI principle is most at risk.")

    selected = st.radio(
        "Which principle is most at risk?",
        PRINCIPLES,
        index=None,
        key=f"planning_{scenario['title']}",
    )

    return selected


def render_planning_feedback(predicted, scenario):
    """
    Shows comparison between learner prediction and scenario's primary principle.
    This creates a planning-monitoring connection.
    """
    if predicted == scenario["primary_principle"]:
        st.success(
            f"Good planning. This scenario primarily involves **{scenario['primary_principle']}**."
        )
    else:
        st.info(
            f"You selected **{predicted}**. The primary principle in this scenario is "
            f"**{scenario['primary_principle']}**, but your choice may still connect to the broader trade-off."
        )


def render_reflection_box(prompt):
    """
    Reflection prompt supports SRL reflection/metacognition.
    """
    st.subheader("Reflection")
    st.write(prompt)

    response = st.text_area(
        "Write a short reflection. One or two sentences is enough.",
        key=f"reflection_{prompt}",
        placeholder="Example: Fairness was most at risk because the decision could create unequal outcomes before users are protected.",
    )

    return response


def render_footer_note():
    st.caption(
        "Prototype note: This first version focuses on functionality, learning alignment, and usability rather than visual polish."
    )