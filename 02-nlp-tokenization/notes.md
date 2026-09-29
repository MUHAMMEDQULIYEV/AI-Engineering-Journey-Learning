# 02 · NLP Tokenization

**Week 2 (Oct 5–11, 2026), started early Sep 29** · Source: Krish Naik bootcamp, Section 51

> Write every answer in my own words, as if explaining to a friend.

## Basic terms (lecture 307)
- Corpus: all the text I work with (e.g. a whole paragraph or dataset)
- Document: one piece of the corpus (e.g. one sentence, one email)
- Vocabulary: the **unique** words/tokens in the corpus — repeats count once
- Words / tokens: every piece after cutting, repeats included
- Example: `"I love NLP. I love AI."` → 2 sentences, 6 tokens, 4 vocab (unique words)

## Tokenization
- Token = one piece of text. Tokenization = cutting text into pieces.
- Levels: corpus → documents → sentences → words → subwords (LLMs, BPE)
- Tokenization is NOT only old NLP — every LLM starts with it (Claude counts everything in tokens).
- NLTK splits into words (`"I love NLP"` → `I`, `love`, `NLP`); LLMs split into subwords (`tokenization` → `token` + `ization`).
- Why don't LLMs just use whole words? → answer in Week 2 (BPE)

## My practice (tokenization.ipynb, Azerbaijani corpus)
- `sent_tokenize` splits on `.` `!` `?` (sentence-ending punctuation). Commas and new lines do NOT split → without `.` I got 1 sentence, after adding `.` I got 2.
- Different tokenizers give different tokens for the same text:

| Tokenizer | `that's` | `varsan.` |
|---|---|---|
| `word_tokenize` | `that`, `'s` | `varsan`, `.` |
| `wordpunct_tokenize` | `that`, `'`, `s` | `varsan`, `.` |
| `TreebankWordTokenizer` | `that's` | `varsan.` (one token) |

- Treebank = fewer tokens, but messier vocab: `varsan` and `varsan.` (or `like` and `like.`) become 2 different vocab entries for the same word.
- So splitting `.` off is better: the word stays one entry, `.` is one shared entry.
- Note: "stopwords" ≠ `.` — stopwords are very common words like *the, is, a* (lecture 311).

## Stemming vs Lemmatization
- `"he likes apple i like orange"` → vocab 6 without merging, 5 with merging (`likes` → `like`)
- Trade-off: smaller vocab vs losing information (tense, he/she)

## NLP vs LLM
- NLP = the field (computers + human language); LLM = one method inside it, currently the strongest.
- LLM next-token prediction = classification over the vocabulary (GPT-2: 50,257 scores per position) — same `argmax` idea as FashionMNIST `[64, 10]`.

## Questions I still have

