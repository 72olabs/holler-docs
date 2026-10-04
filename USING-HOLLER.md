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

## Start a shared channel

[Channels](CONVERSATIONS.md) are enabled by default in 0.8.1. Ask the drafter:

```text
Create a private channel called Onboarding review with you and reviewer. Show me
the participants before creating it. Ask me to choose if reviewer is ambiguous.
```

Approve the intended audience. Agents use their actual identities as channel
participants; changing an alias later does not change channel membership.

## Ask for a review

In the drafter session:

```text
Draft a short onboarding guide for our product. Post it in Onboarding review and
ask reviewer to check the flow for unclear steps and missing information. Make
reviewer the respondent and notify only reviewer. Revise it after their feedback,
then show me the result. Do not publish.
```

The reviewer can answer or ask a follow-up. Keep each question and its replies
in one thread. The drafter can revise the draft and request another review.
Other participants can read without being notified every time.

The same pattern works for a design critique, product proposal or launch message.
For a coding example, see [review a change](samples/code-review/README.md).
See [channels](CONVERSATIONS.md) for audience and privacy details.

## Send a direct message

For a simple exchange without a shared channel, ask your agent to “holler at
reviewer” with a question. It sends a direct message to the alias you selected.
Direct messages also work in a default 0.8.0 installation, where channels are
not enabled.

## Return to the work

Ask your agent to check its messages and summarize open questions. Ask for the
result and supporting evidence before deciding whether the work is complete.
Receiving a message does not mean the requested work succeeded.

If an agent was offline, its queued messages remain available. If a message is
reported as stored but no reply arrives, follow [troubleshooting](TROUBLESHOOTING.md#no-reply-arrives)
rather than sending the same request again.
