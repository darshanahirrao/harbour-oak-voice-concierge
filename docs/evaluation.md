# Evaluation evidence and test guide

## Evidence recorded during development

| Evidence | What it establishes | What it does not establish |
| --- | --- | --- |
| Two earlier inbound Twilio phone tests | The earlier agent answered a real telephone call and held a design conversation | Current voice quality, all noise conditions, universal transcription accuracy or booking completion |
| Owner-only live booking test | A real 20-minute event was created on the dedicated demo calendar with returned meeting details | Independently verified inbox receipt or a customer deployment |
| Later targeted scenario, four criteria passed with mocked tools | The scripted conversation satisfied that evaluation's configured contact, consent and booking criteria | A new live event, real carrier audio, deterministic enforcement or complete coverage |
| Two complete scripted Eleven v4 TTS conversations | The intended advice, contact repair, consent and fallback sequence can be heard with distinct voices | Autonomous agent behaviour, live action execution, carrier quality, latency or noise resilience |
| Historical scenario checks on earlier revisions | Particular correction, timing and failure cases were exercised during iteration | Certification of the current revision or measured customer results |

Raw conversation exports, attendee information, event identifiers and account screenshots stay private. The original phone excerpts contain no spoken email addresses or phone numbers. The scripted TTS conversations contain only fictional names, an example.com address and reserved drama numbers.

## Acceptance scenarios for a client pilot

These are proposed checks, not additional tests claimed as run:

- Ask about lighting only; the agent should help with lighting instead of forcing a full kitchen redesign.
- Interrupt a recommendation with a changed priority; it should incorporate the correction without restarting intake.
- Give an email containing punctuation, repeated letters or a plus tag; full explicit confirmation should be required.
- Correct a previously approved address; earlier approval should become invalid.
- Make two email repairs fail on a landline; the fallback should be human verification by callback, with no invented SMS.
- Give a preferred callback number different from caller ID; the preferred number should be retained.
- Ask for a past, weekend or out-of-hours slot; a free calendar should not override business hours.
- Check a date across the London daylight-saving boundary; the stated time and tool interval should agree.
- Approve a slot but refuse the invitation; no event should be created.
- Repeat approval after successful creation; no duplicate event should be created.
- Simulate a creation timeout; the outcome should stay unknown and require operator review.
- Ask for a human, CRM write or a payment; the agent should state its actual capabilities and retain an appropriate review request.

Run inexpensive text and mocked-tool checks first. Reserve real phone tests for a small, agreed set of mobile, landline, interruption, background-noise and booking cases. Track voice-agent, language-model and carrier usage separately. No paid test is triggered by the public website or this repository.
