from streamlit.testing.v1 import AppTest


def test_secret_regenerates_within_range_when_difficulty_changes():
    # Regression test: switching difficulty used to leave the old secret in
    # place while the guess range shrank/grew, so guesses could never reach
    # it (e.g. secret stayed in the 1-100 Normal range after switching to
    # Easy's 1-20 range, making every guess report "Too Low").
    at = AppTest.from_file("../app.py")
    at.run()

    at.selectbox[0].set_value("Easy").run()

    assert at.session_state["difficulty"] == "Easy"
    assert 1 <= at.session_state["secret"] <= 20


def test_attempts_and_score_reset_when_difficulty_changes():
    at = AppTest.from_file("../app.py")
    at.run()

    at.text_input[0].set_value("50").run()
    at.button[0].click().run()
    assert at.session_state["attempts"] > 0

    at.selectbox[0].set_value("Hard").run()

    assert at.session_state["attempts"] == 0
    assert at.session_state["score"] == 0
    assert at.session_state["status"] == "playing"
    assert at.session_state["history"] == []


def test_guess_above_difficulty_range_is_rejected():
    at = AppTest.from_file("../app.py")
    at.run()

    at.selectbox[0].set_value("Easy").run()
    at.text_input[0].set_value("500").run()
    at.button[0].click().run()

    assert at.error[0].value == "Enter a number between 1 and 20."
    assert at.session_state["history"] == ["500"]
    assert at.warning == []


def test_guess_within_difficulty_range_is_accepted():
    at = AppTest.from_file("../app.py")
    at.run()

    at.selectbox[0].set_value("Easy").run()
    at.text_input[0].set_value("10").run()
    at.button[0].click().run()

    assert at.error == []
    assert at.session_state["history"] == [10]
