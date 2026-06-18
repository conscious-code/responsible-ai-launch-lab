import streamlit as st

from scenarios import SCENARIOS, PRINCIPLES, BUSINESS_PRESSURE
from scoring import (
    initial_scores,
    apply_impact,
    changed_meters,
    launch_readiness_profile,
    weakest_principles,
    needs_recovery_support,
    recovery_message,
    summarize_choice_history,
)
from ui import (
    page_setup,
    apply_custom_styles,
    render_title,
    render_principle_pills,
    render_principle_overview,
    render_scores,
    render_changed_meters,
    render_mode_card,
    render_scenario_header,
    render_scenario_brief,
    render_planning_prompt,
    render_planning_feedback,
    render_reflection_box,
    render_footer_note,
)


TOTAL_SCENARIOS = len(SCENARIOS)


def initialize_state():
    """
    Initialize all game state values.
    This supports the functioning prototype requirement:
    the game remembers mode, scenario progress, scores, choices, feedback, and reflections.
    """
    defaults = {
        "screen": "welcome",
        "mode": None,
        "scenario_index": 0,
        "scores": initial_scores(),
        "planning_done": False,
        "predicted_principle": None,
        "answered": False,
        "selected_choice": None,
        "selected_impact": None,
        "feedback": None,
        "choice_history": [],
        "reflection_history": [],
        "recovery_shown_for_index": False,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_game():
    """
    Clear the session and restart the game.
    """
    st.session_state.clear()
    st.rerun()


def go_to(screen_name):
    st.session_state.screen = screen_name
    st.rerun()


def welcome_screen():
    render_title()

    st.markdown(
        """
        <div class="callout">
        <strong>Your role:</strong> You are the product lead preparing an AI-powered feature for launch.
        Your decisions will affect the product's Responsible AI readiness.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write(
        "You will move through five realistic product launch scenarios. "
        "Each scenario asks you to identify the responsible AI risk, make a decision, "
        "review the consequences, and reflect before moving forward."
    )

    render_principle_pills()

    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Start Game", type="primary", use_container_width=True):
            go_to("mode_selection")

    with col2:
        with st.expander("View Microsoft Responsible AI Principles"):
            render_principle_overview()

    render_footer_note()


def mode_selection_screen():
    render_title()
    st.header("Choose Your Learning Mode")

    st.write(
        "Select how much support you want during gameplay. "
        "This is a simple personalization feature based on prior knowledge and confidence."
    )

    col1, col2 = st.columns(2)

    with col1:
        render_mode_card(
            "Beginner Mode",
            [
                "Responsible AI definitions visible",
                "Optional hints enabled",
                "Guided feedback and reflection",
            ],
        )

        if st.button("Choose Beginner Mode", type="primary", use_container_width=True):
            st.session_state.mode = "Beginner"
            go_to("principle_overview")

    with col2:
        render_mode_card(
            "Challenge Mode",
            [
                "Definitions hidden by default",
                "Hints minimized",
                "More open-ended reflection",
            ],
        )

        if st.button("Choose Challenge Mode", use_container_width=True):
            st.session_state.mode = "Challenge"
            go_to("principle_overview")


def principle_overview_screen():
    render_title()
    st.header("Responsible AI Dashboard")

    st.write(
        "The game tracks six Microsoft Responsible AI principles. "
        "Business Pressure is shown separately because it is a contextual constraint, not a principle."
    )

    render_principle_overview()

    if st.button("Continue to Scenario 1", type="primary"):
        go_to("scenario")


def scenario_screen():
    scenario = SCENARIOS[st.session_state.scenario_index]
    scenario_number = st.session_state.scenario_index + 1

    render_title()

    left, right = st.columns([1.5, 1])

    with left:
        render_scenario_header(scenario, scenario_number, TOTAL_SCENARIOS)

        render_scenario_brief(scenario)  

        if st.session_state.mode == "Beginner":
            with st.expander("Need a hint?"):
                st.write(scenario["hint"])
        else:
            st.caption("Challenge Mode: hints are minimized. Use the principle labels and scenario evidence to reason through the decision.")

        if not st.session_state.planning_done:
            predicted = render_planning_prompt(scenario)

            if st.button("Confirm Prediction", type="primary", disabled=predicted is None):
                st.session_state.predicted_principle = predicted
                st.session_state.planning_done = True
                st.rerun()

        else:
            render_planning_feedback(st.session_state.predicted_principle, scenario)

            st.subheader("Decision")
            st.write("Choose one action.")

            if not st.session_state.answered:
                for idx, choice in enumerate(scenario["choices"]):
                    if st.button(choice["text"], key=f"choice_{st.session_state.scenario_index}_{idx}", use_container_width=True):
                        st.session_state.selected_choice = choice
                        st.session_state.selected_impact = choice["impact"]
                        st.session_state.feedback = choice["feedback"]
                        st.session_state.scores = apply_impact(
                            st.session_state.scores,
                            choice["impact"],
                        )
                        st.session_state.answered = True

                        st.session_state.choice_history.append(
                            {
                                "scenario_title": scenario["title"],
                                "choice_text": choice["text"],
                                "primary_principle": scenario["primary_principle"],
                                "predicted_principle": st.session_state.predicted_principle,
                                "impact": choice["impact"],
                            }
                        )

                        st.rerun()

            else:
                go_to("feedback")

    with right:
        render_scores(st.session_state.scores, compact=True)


def feedback_screen():
    scenario = SCENARIOS[st.session_state.scenario_index]

    render_title()
    st.header("Feedback & Impact")

    st.markdown(f"**You chose:** {st.session_state.selected_choice['text']}")

    changes = changed_meters(st.session_state.selected_impact)
    render_changed_meters(changes)

    st.markdown("---")
    st.subheader("Feedback")

    if st.session_state.mode == "Beginner":
        st.info(st.session_state.feedback)
    else:
        st.write(st.session_state.feedback)
        st.caption("Challenge Mode: consider whether this decision solved the root issue or only reduced visible risk.")

    reflection = render_reflection_box(scenario["reflection_prompt"])

    if st.button("Save Reflection and Continue", type="primary"):
        st.session_state.reflection_history.append(
            {
                "scenario_title": scenario["title"],
                "prompt": scenario["reflection_prompt"],
                "response": reflection,
            }
        )

        if needs_recovery_support(st.session_state.scores) and not st.session_state.recovery_shown_for_index:
            st.session_state.recovery_shown_for_index = True
            go_to("recovery")

        move_to_next_scenario()


def recovery_screen():
    render_title()
    st.header("Targeted Recovery Support")

    recovery = recovery_message(st.session_state.scores)

    st.warning(recovery["message"])
    st.markdown(f"**Principle focus:** {recovery['principle']}")
    st.write(recovery["definition"])

    st.write(
        "This support appears because one of your Responsible AI principle scores dropped below 40. "
        "Use the next scenario to actively protect this principle while still considering the full trade-off."
    )

    if st.button("Continue with this focus", type="primary"):
        move_to_next_scenario()


def move_to_next_scenario():
    """
    Move to the next scenario or final screen.
    Reset per-scenario state while preserving scores and history.
    """
    st.session_state.scenario_index += 1

    st.session_state.planning_done = False
    st.session_state.predicted_principle = None
    st.session_state.answered = False
    st.session_state.selected_choice = None
    st.session_state.selected_impact = None
    st.session_state.feedback = None
    st.session_state.recovery_shown_for_index = False

    if st.session_state.scenario_index >= TOTAL_SCENARIOS:
        st.session_state.screen = "final"
    else:
        st.session_state.screen = "scenario"

    st.rerun()


def final_screen():
    render_title()
    st.header("Final Launch Readiness Profile")

    profile = launch_readiness_profile(st.session_state.scores)
    weakest = weakest_principles(st.session_state.scores, count=2)

    if profile == "Responsible Launch Ready":
        st.success(profile)
    elif profile == "Promising, but Needs Targeted Review":
        st.warning(profile)
    elif profile == "Needs Additional Responsible AI Review":
        st.warning(profile)
    else:
        st.error(profile)

    col1, col2 = st.columns([1, 1])

    with col1:
        render_scores(st.session_state.scores, compact=True)

    with col2:
        st.subheader("Learning Debrief")
        st.markdown(f"**Top improvement areas:** {', '.join(weakest)}")

        st.write(
            "Your final profile is based only on the six Responsible AI principles. "
            "Business Pressure is shown separately because it represents contextual pressure, not responsible AI quality."
        )

        st.markdown("### Recommended Next Step")
        st.write(
            f"Review your decisions involving **{weakest[0]}** and consider what earlier safeguard, review, "
            "or escalation path could have improved the outcome."
        )

    st.markdown("---")
    st.subheader("Your Decision Pattern")

    summary = summarize_choice_history(st.session_state.choice_history)

    for idx, item in enumerate(summary, start=1):
        st.markdown(f"**{idx}. {item['scenario']}**")
        st.write(f"Primary principle: {item['primary_principle']}")
        st.write(f"Your choice: {item['choice']}")

    with st.expander("View Reflection History"):
        if not st.session_state.reflection_history:
            st.write("No reflections were entered.")
        else:
            for item in st.session_state.reflection_history:
                st.markdown(f"**{item['scenario_title']}**")
                st.write(f"Prompt: {item['prompt']}")
                st.write(f"Response: {item['response'] or 'No response entered.'}")

    st.markdown("---")

    col_a, col_b = st.columns(2)

    with col_a:
        if st.button("Restart Game", type="primary", use_container_width=True):
            reset_game()



def main():
    page_setup()
    apply_custom_styles()
    initialize_state()

    if st.session_state.screen == "welcome":
        welcome_screen()
    elif st.session_state.screen == "mode_selection":
        mode_selection_screen()
    elif st.session_state.screen == "principle_overview":
        principle_overview_screen()
    elif st.session_state.screen == "scenario":
        scenario_screen()
    elif st.session_state.screen == "feedback":
        feedback_screen()
    elif st.session_state.screen == "recovery":
        recovery_screen()
    elif st.session_state.screen == "final":
        final_screen()
    else:
        welcome_screen()


if __name__ == "__main__":
    main()