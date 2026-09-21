# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Start Game | 1 - 100 number as the answer|Negative answer|none |       
|Restart button| Restarts the game, clears history of last game | Does nothing|none | 
|Difficulties |Hard mode is 1-100 while medium is 1-50 |Hard mode is 1-50 while medium is 1-100 |none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

--- I used Claude only as my AI tool. Claude made a suggestion that it should verify that the test it made catches the bug by reverting what it fixed.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---The pytest and actually rerunning the code. Tested for if the target guess could still go negative.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- Each time you change something in the code, the script reruns itself so that you dont have to.
## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

--- One habit I want to take from this lab is reviewing what the agent is coming up with and not just accepting what its giving me. This is something I will use is future projects because the code that is produced is never a guaranteed thing to work, so you need to read through it to make sure it's doing what you want.