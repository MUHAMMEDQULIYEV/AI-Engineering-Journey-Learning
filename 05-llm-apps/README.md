# 05 · LLM apps (Block 4)
Goal: first LLM apps with APIs, structured output, tool calling and vector search. Main course: Ed Donner *AI Engineer Core Track*.
Plan: [roadmap/plan.md → Block 4](../roadmap/plan.md#block-4--llm-apps-4-weeks-main-course--ed-donner-ai-engineer-core-track)

≤30 min of video per day at 1.5×. LEARN = watch + predict · BUILD = rebuild *without the video* · SHIP = my variation + push · REVIEW = 🧠 one older topic.

## Weeks
- [ ] 1 · course Week 1: LLM APIs, first app → the course app adapted to my language · REVIEW: tentative flagship idea + data source
  - done when: app answers in my language, pushed
- [ ] 2 · prompting + structured output (system prompt, few-shot, JSON validated by **Pydantic**) → extractor: text in → Pydantic object out
  - done when: 5 test inputs, all parse
- [ ] 3 · course Week 2: Gradio UI, tool calling → assistant with 1 real tool in a Gradio UI
  - done when: the tool is called on 3 test prompts
- [ ] 4 · **embeddings + vector search** (multilingual embedder) → top-3 search over ~20 flagship docs · REVIEW: confirm or switch the flagship idea
  - done when: the right doc is in the top 3 for 4 of 5 test questions

## Done when
- [ ] 3 small apps pushed (API app, Pydantic extractor, tool assistant)
- [ ] top-3 search works on my docs
- [ ] flagship idea confirmed
- [ ] 🔒 explain the tool-calling loop in 5 sentences, then write cosine top-3 search in ≤20 lines, no notes

## Suggested layout (I create the files)
- `01-api-app/`
- `02-extractor/`
- `03-tool-assistant/`
- `04-embeddings-search/`
- `notes.md`: in my own words
