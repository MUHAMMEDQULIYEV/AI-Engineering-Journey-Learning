# 🤖 How to use Claude (or any AI assistant) on this roadmap

**Main rule:** the AI is your **tutor, reviewer and planner**. It is not your homework machine. If it writes your code, you learn nothing.

I use [Claude Code](https://claude.com/claude-code) opened inside my learning repo. A `CLAUDE.md` file there tells it my plan and how to teach me (see [../CLAUDE.md](../CLAUDE.md)). Any assistant that can read your files works the same way.

---

## The daily loop

| When | You type | The AI does |
|---|---|---|
| **Start** (2 min) | `Start session` | Reads your `NEXT.md` + today's row in the plan. Asks you **1 recall question** about an old topic and **1 predict question** about today's topic. |
| **During** | your questions | Gives a **hint first**, never the full solution. Answers with small examples and one question at a time. |
| **Stuck 15 min** | *"I'm on <today's row>. I did X. I'm stuck on Y. What's my next 30-minute step?"* | Gives one small next step. |
| **End** (5 min) | `End session` | Reads your notebook, names **skipped exercises and open bugs**, writes your NEXT line, gives a date to re-test today's topic, and reminds you to commit. |

Put `Start session` in your calendar event so the first step needs no thinking.

## Weekly and monthly

| When | You type | The AI does |
|---|---|---|
| Last study day of the week | `Weekly check-in` + what you did, blockers, energy 1–10, **proof** (commit links) | Writes it as one Sunday row in the session log, compares with the plan and writes next week's days |
| Last review of the month | `Monthly review` | Writes next month's daily rows and checks the plan against the mlabonne map and real job posts |

---

## Copy-paste prompts

**Learn a concept**
```
Explain <concept> like I know <thing I know>. Keep it short.
Then give me 3 questions. Don't give answers until I reply.
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
Quiz me on <topic>: 5 questions. 2 concept, 2 "predict the output", 1 "find the bug".
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
- ❌ Ask for a new course in the middle of a block (write it in `IDEAS.md`)
- ❌ Hide a bad week. Bad weeks are the most important check-ins.

> Okay to ask for code: boilerplate you already understand (configs, plotting), or after you've tried yourself and want to compare.

## The AI is also a skill for your CV
From Block 4 on, call the Claude API (or another LLM API) **inside your own projects**: tool use, structured output, MCP.
Using AI to *learn* is good. Building *with* AI is what gets you hired.
