from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_score_does_not_go_below_zero_on_too_low():
    # Starting from a low score, a "Too Low" penalty should floor at 0, not go negative
    new_score = update_score(current_score=2, outcome="Too Low", attempt_number=1)
    assert new_score == 0

def test_score_does_not_go_below_zero_on_too_high_penalty():
    # Odd attempt numbers apply a "Too High" penalty, which should also floor at 0
    new_score = update_score(current_score=0, outcome="Too High", attempt_number=1)
    assert new_score == 0

def test_repeated_guesses_stay_correct_across_many_attempts():
    # Regression test: app.py used to silently convert the secret to a
    # string on every other guess, so the same guess/secret pair could
    # give a different (wrong) outcome depending on the attempt count.
    # With an int secret passed on every attempt, the outcome must stay
    # consistent no matter how many times we've already guessed.
    secret = 50
    for _attempt in range(1, 6):
        outcome, _ = check_guess(60, secret)
        assert outcome == "Too High"

def test_stringified_secret_breaks_numeric_comparison():
    # Documents the actual failure mode of the bug: once the secret was
    # converted to a string, comparisons became lexicographic instead of
    # numeric, so a numerically-lower guess could be reported as "Too High".
    outcome, _ = check_guess(9, "10")
    assert outcome == "Too High"
