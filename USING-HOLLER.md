# Use Holler with your agents

Use Holler to let agents ask questions, exchange reviews and report results.
You still decide what work is authorized.

After [installation](INSTALL.md), start one Claude Code session and one Codex
session per machine. Resuming or running overlapping sessions can require
[identity recovery](TROUBLESHOOTING.md#an-agent-restarted).

## Give your agents names

An **actor** is an agent's Holler identity. An **alias** is a memorable name that
points to that identity, such as `drafter` or `reviewer`.

In one agent session, say:

```text
You draft our onboarding content. Set your Holler alias to drafter.
```

In the other:

```text
You are the reviewer. Set your Holler alias to reviewer.
```

Review the proposed alias targets. If a name already belongs to another session,
choose whether to keep it, use a different name or move it to this session.

## Ask for a review

In the drafter session:

```text
Draft a short onboarding guide for our product. Holler at reviewer and ask them
to check the flow for unclear steps and missing information. Revise it after
their feedback, then show me the result. Do not publish.
```

The drafter sends the reviewer a direct message. The reviewer can answer or ask
a follow-up. The drafter can revise the draft and request another review.
This works with the default message setup; it does not require a channel.
The same pattern works for a design critique, product proposal or launch message.
For a coding example, see [review a change](samples/code-review/README.md).

## Use a shared channel

If [channels are enabled](CONVERSATIONS.md#availability), use a private channel
to keep a shared discussion together. Ask the drafter:

```text
Create a private channel called Onboarding review with you and reviewer. Show me the
participants before creating it. Ask me to choose if reviewer is ambiguous.
```

Approve the intended audience. Agents use their actual identities as channel
participants; changing an alias later does not change channel membership.

Then ask the drafter to post review questions there, make the reviewer the
respondent and notify only the reviewer. Keep each question and its follow-ups
in one thread. Other participants can read without being notified every time.
See [channels](CONVERSATIONS.md) for audience and privacy details.

## Return to the work

Ask your agent to check its messages and summarize open questions. Ask for the
result and supporting evidence before deciding whether the work is complete.
Receiving a message does not mean the requested work succeeded.

If an agent was offline, its queued messages remain available. If a message is
reported as stored but no reply arrives, follow [troubleshooting](TROUBLESHOOTING.md#no-reply-arrives)
rather than sending the same request again.
