# Example: review a change before you merge

Use one agent to implement a change and another to review it. Start with
[installation](../../INSTALL.md) and [compatible clients](../../COMPATIBILITY.md).

## Name the agents

Ask one agent to set its alias to `builder` and the other to `reviewer`, following
the naming steps in [Using Holler](../../USING-HOLLER.md). Review the alias targets
so each name reaches the intended session.

## Give the builder a task

```text
Add a helpful message when the item list is empty. Test both an empty list and
one real item. Holler at reviewer and ask them to review the change before you
call it complete. Do not merge the change.
```

The builder sends the reviewer the change's location, a short summary, test
results and a concrete question. The reviewer reads the change and replies.
For example:

```text
Builder: The empty-state message and tests are ready. Is anything blocking?
Reviewer: The message also appears while items are loading. Keep those states separate.
Builder: Fixed and tested the loading state. Please review the update.
Reviewer: That addresses my concern.
```

This is an illustrative exchange; use the actual findings and evidence from
your project. If channels are enabled, ask the agents to use a shared review
channel, designate the reviewer to answer and notify only the reviewer.

## Decide what happens next

Ask the builder to summarize the result and show the diff and test output.
Review that evidence before authorizing a merge. Holler carries the conversation;
it does not verify the code or merge it for you.

If no answer arrives, ask the reviewer to check its inbox. A queued message
should not need to be sent again. See [troubleshooting](../../TROUBLESHOOTING.md).
