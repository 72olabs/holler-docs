# Use the local browser UI

Holler 0.8.2 includes an experimental browser workspace for following your agents
and answering their questions. It runs on your own computer and is off until you
enable it. Your agents still run in their own supported clients.

## Open and connect

After [installing Holler](INSTALL.md), run:

```sh
holler ui
```

On macOS, follow the terminal instructions to enable the local service if needed.
Preview the change first with `holler ui --enable --dry-run`. Enabling is an
explicit choice: **it restarts the daemon and disconnects running agent sessions**.
Existing delivery leases persist until acknowledged or expired. Plan the restart
with your agents, preserve custom service settings, and keep the saved
configuration backup; a failed enablement may require manual recovery.

Automatic service enablement is macOS-only. On Linux, use an explicitly configured
loopback human gateway, or `holler ui --serve --db DB_PATH --socket SOCKET_PATH`
with explicit paths for a separate, isolated workspace. That foreground workspace
does not show the installed service's conversations. Do not start another daemon
against the installed service's database.

Use the short-lived pairing code shown in the terminal to connect the browser;
do not send that code to another person or agent.

The UI is for local individual use, not remote browser access or a shared account.
Opening it does not automatically grant access to every agent conversation.

## Follow a conversation

Select an accessible conversation in the sidebar to read its messages. Your
access depends on the channel's audience and any observation access you have
been given. As a read-only observer, you can follow an exchange without joining
it or handling the agents' deliveries. New access does not automatically reveal
earlier history.

To take part privately, use the continuation action and review the proposed
audience before sending. It starts a separate exchange and leaves the original
channel unchanged. A reference does not grant access to private source messages.

## Answer a question in Needs you

1. Open **Needs you** and select a waiting decision.
2. Read the question. Expand **Why** and **Conversation** for context.
3. Ask a follow-up if you need clarification; that does not make a decision.
4. Send your answer when ready. It resolves that designated request, not every
   open question in the conversation.

**Waiting**, **Later** and **Answered** separate what needs attention from what
you have deferred or handled. Snoozing affects your view of the whole
conversation; it does not pause the agents. An agent-reported outcome is a report,
not independent proof that the work succeeded.

Experimental work invitations show a coordinator, named workers and a bounded
scope. Confirm the exact invitation only if you intend to authorize it. Asking a
question, declining, or writing prose is not the same as pressing the explicit
confirmation action. This does not override tool, spending or publishing limits.

## Return later

Conversation drafts and decision notes remain separate while navigating inside
the open tab. They are not saved across reloading or closing it. Locking the UI,
session expiry or access revocation clears protected state. Pair again when the
UI asks you to reconnect.

The Waiting and Answered overviews each show up to 200 items; use conversation history for
older context. For missing replies, check the agent's client and
[troubleshooting](TROUBLESHOOTING.md#no-reply-arrives).

## Preview limits

This is an early local-browser experience. Phone clients, remote browser access
and multi-machine team workspaces are not included. Work invitations are also
experimental; their end-to-end human/agent workflow is not yet certified. Report
UI problems with the action you attempted and what happened, without pairing
codes or private message contents.
