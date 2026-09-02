# Repository agent instructions

<!-- BEGIN:clear-writing-standard -->
## Clear writing standard (hard rule)

Apply this standard to every reply and every piece of human-facing text you
draft or edit. This includes emails, messages, reports, proposals, posts,
scripts, instructions, documents, and technical explanations.

Write in this order:

1. Preserve the exact meaning.
2. Make the message easy to understand.
3. Remove words the reader does not need.

Use these rules:

- Lead with the answer, result, decision, or next action.
- Use common words and direct sentence structure.
- Keep most sentences short. Give each sentence one main idea.
- Split long or difficult sentences.
- Prefer active voice when it sounds natural.
- Name the person, team, or system responsible for an action.
- Remove filler, unnecessary adverbs, vague qualifiers, and repeated ideas.
- Remove stock AI phrases, fake enthusiasm, and inflated claims.
- Use contractions when they make the writing sound natural.
- Keep paragraphs short and use headings only when they help scanning.
- Explain an unfamiliar term the first time you use it.
- Prefer specific facts, names, dates, numbers, and examples.
- State risks, limits, assumptions, and unresolved questions clearly.
- Never use em dashes or en dashes in human-facing writing.

Aim for grade 9 or lower for normal explanations and internal writing. Aim for
grade 8 or lower for emails, buyer-facing copy, social posts, and scripts.
Treat the scores as guides. Accuracy matters more than a lower grade.

Do not simplify or change direct quotes, numbers, dates, evidence, legal
wording, code, commands, file paths, links, or required technical terms.
Explain required technical terms in plain language.

Before delivery, silently check the final draft. Put the main answer first,
rewrite hard sentences, remove filler, and confirm the next action is clear.
Return only the finished version unless the user asks to see the editing work.

For substantial prose, run:

~~~bash
printf '%s' "$FINAL_COPY" | python3 .agents/hooks/plain_language.py --profile standard
~~~

Use the sales profile for buyer-facing copy, emails, social posts, and
scripts. If the checker fails, rewrite once and return the clearer version.
Do not discuss the rule, refuse the task, or ask for permission to rewrite.
<!-- END:clear-writing-standard -->
