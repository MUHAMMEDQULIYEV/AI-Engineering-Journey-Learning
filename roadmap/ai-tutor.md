# 🤖 How to use Claude (or any AI assistant) on this roadmap

**Main rule:** the AI is your **tutor, reviewer and planner**. It is not your homework machine. If it writes your code, you learn nothing.

I use [Claude Code](https://claude.com/claude-code) opened inside my learning repo. A `CLAUDE.md` file there tells it my plan and how to teach me (see [../CLAUDE.md](../CLAUDE.md)). Any assistant that can read your files works the same way.
> Note: my `CLAUDE.md` points to private files in my home folder (`~/Claude_KNow_About_me/…`). That's just my setup. Use your own paths for `NEXT.md`, the session log and check-ins.

---

## The daily loop

| When | You type | The AI does |
|---|---|---|
| **Start** (2 min) | `Start session` | Reads your `NEXT.md`, today's row and your session log. Asks **1 recall question** on the oldest due topic in the whole log (the "next due" column). After you answer, **1 predict question** about today's topic. Then the first tiny step. |
| **During** | your questions | Gives a **hint first**, never the full solution. Answers with small examples and one question at a time. Picks the method for the situation from [learning-methods.md](learning-methods.md). |
| **Stuck 15 min** | *"I'm on <today's row>. I did X. I'm stuck on Y. What's my next 30-minute step?"* | Gives one small next step. |
| **End** (5 min) | `End session` | The 5 steps below. |

**End session** (the same steps as in my `CLAUDE.md`):
1. Read the notebook on disk. Name skipped exercises and open bugs plainly.
2. Add one row to your session log ([template](templates/session-log.md)): date, plan row, output (commit), skipped/open, 🧠 recalled (✅/partial/❌) → next due. The next due date follows the [gap ladder](learning-methods.md#the-gap-ladder-spaced-recall): 1 → 3 → 7 → 21 → 60 days, a miss resets to 1.
3. **You write the NEXT line yourself.** The AI only critiques it (too vague? too big?). Deciding the next step is part of the learning, so don't hand it over.
4. Optional: add the next study day's task to your to-do app (I use Notion). Skip it on rest days.
5. Remind you to commit + push.

**Minimum day (15 min):** End session is 2 lines: your NEXT line + commit + push. No log row needed.

**One question at a time.** When a command has several questions (Start session, a quiz), the AI asks them in order and waits for each answer. Only End session, the weekly check-in and the monthly review may give a multi-part answer.

Put `Start session` in your calendar event so the first step needs no thinking.

## Weekly and monthly

| When | You type | The AI does |
|---|---|---|
| Last study day of the week (REVIEW day) | first **AI-off**: recall + rebuild one piece from a blank file, alone. Then `Weekly check-in` | Checks your rebuild afterwards (what was missing, what goes back to 1 day on the ladder). Fills the 3-line [check-in](templates/weekly-checkin.md) with you: proof link, energy 1–10, one change for next week. Links it from that day's session-log row |
| Last review of the month | `Monthly review` | Writes next month's daily rows and checks the plan against the mlabonne map and real job posts |

---

## Copy-paste prompts

**Learn a concept**
```
Explain <concept> like I know <thing I know>. Keep it short.
Then ask me 3 questions, one at a time. Wait for my answer before the next.
```

**Check my understanding**
```
Here is my explanation of <concept>: "…"
What is wrong or missing? Don't rewrite it, ask me questions.
```

**Error**
```
I got this error: <full error>
Code: <paste or @file>
Explain WHY it happens. Hint first, not the fix.
```

**Code review**
```
Review @<file>. Don't rewrite it. Tell me what a professional would do differently.
```

**Quiz**
```
Quiz me on <topic>: 5 questions, one at a time. 2 concept, 2 "predict the output", 1 "find the bug".
```

**Bad week**
```
I did almost nothing this week because <reason>. Shrink next week's plan so I can restart.
```

---

## Tips
1. **Give context:** "Block 3, causal mask" gets a far better answer than "how does attention work?"
2. **Show real things:** paste the full error, or point to the file. Don't describe it from memory.
3. **Ask it to ask you questions** before planning or designing something.
4. **Say "I already know this"? Prove it:** ask for a cold recall question.
5. **One topic per conversation.** Start a fresh chat for a new topic.
6. **Verify important facts** (deadlines, prices, requirements) in the official source.

## Don'ts
- ❌ "Write section 3 for me" / "Build my mini-GPT"
- ❌ Copy code you can't explain line by line
- ❌ Ask for a new course in the middle of a block (write it in your `IDEAS.md` parking list)
- ❌ Hide a bad week. Bad weeks are the most important check-ins.

> Okay to ask for code: boilerplate you already understand (configs, plotting), or after you've tried yourself and want to compare.

## The AI is also a skill for your CV
From Block 4 on, call the Claude API (or another LLM API) **inside your own projects**: tool use, structured output, MCP.
Using AI to *learn* is good. Building *with* AI is what gets you hired.
