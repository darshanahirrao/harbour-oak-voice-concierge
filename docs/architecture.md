# Architecture

## The deployed demonstration

Twilio carries inbound phone audio to ElevenLabs Agents. The native agent handles speech recognition, conversation turns, interruptions, language-model reasoning, speech generation and a small fictional studio knowledge base. Native Google Calendar tools act only on a dedicated demo calendar. Post-call analysis retains structured enquiry and action outcomes for the operator.

There is no custom application server in this build. This repository does not contain deployable agent code or connect to any paid service.

## Configuration choices

| Layer | Current configuration | Purpose |
| --- | --- | --- |
| Voice | Lucy, Eleven v4 Turbo, expressive delivery | Friendly design conversation with measured contact read-backs |
| Recognition | Scribe v2 Realtime | Native live transcription |
| Conversation | Turn handling, interruption support and background filtering | Let callers finish, accommodate corrections and avoid acting on background speech |
| Reasoning | GPT-6.1 Sol | Scoped recommendations, contact confirmation and booking decisions |
| Actions | Native calendar availability and event creation | Check one dedicated calendar and create a clearly labelled demo consultation |
| Review | Structured post-call analysis | Preserve confirmed details, request summary, booking outcome and unresolved items |

The current voice configuration was published after the included phone recording. The complete scripted stories use Lucy with Eleven v4 TTS and a distinct caller voice. They illustrate the procedure with mocked outcomes. Neither the earlier phone excerpts nor the scripted TTS files measure the current deployed configuration's live latency.

## Action boundary

Booking creates a real demo calendar event. It requires confirmed contacts, an agreed valid time, approved project notes and explicit invitation consent. The assistant checks the returned result before reporting success. A repeated verbal confirmation must not cause another event.

The native structured procedure guides the language model through those steps. Its conditions remain model-evaluated. A production implementation should add deterministic validation, idempotency and reconciliation appropriate to the client's backend before relying on these behaviours as guarantees.

## Operator handoff

The native conversation record contains the caller's details and unresolved request for review. No CRM ticket, outbound callback, email follow-up or SMS is created by this handoff. It is an operator review record, not a connected human transfer.

## Public access

The website serves ordinary MP3 files and documentation. Neither the website nor this repository embeds a live agent, a phone dial link, an agent widget, an API proxy or a service credential. A prospective client can arrange a private walkthrough with the operator.
