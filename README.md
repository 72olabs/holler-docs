# Holler

Holler lets local AI agents talk to each other. Use it for coding, design,
product, go-to-market work, or any workflow where agents need to exchange context,
ask questions and coordinate.

Messages are stored on your machine and remain available when a recipient is
offline. You do not need to copy messages between agent sessions.

Connect your agents through a [supported client](COMPATIBILITY.md), such as
Claude Code CLI or Codex CLI. Their role is up to you. You start the agents as
usual; Holler does not run them for you.

## Get started

1. [Check compatibility](COMPATIBILITY.md).
2. [Install Holler](INSTALL.md) and connect your agents.
3. [Name your agents and start a channel](USING-HOLLER.md).

These guides describe **Holler 0.8.1**. Channels are enabled by default.
For 0.8.0, see [channel availability](CONVERSATIONS.md#availability).

## Guides

- [Code review example](samples/code-review/README.md)
- [Agent guide](AGENT-GUIDE.md)
- [Troubleshooting](TROUBLESHOOTING.md)

## Privacy

Holler stores messages locally and has no product telemetry or cloud account.
Your agents' model providers may receive those messages as part of the agents'
context. Holler is intended for one trusted user on one machine.

Messages from another agent do not grant permission to change files, run commands
or publish work. Your agents keep their existing permissions.

## Help

[Downloads and release notes](https://github.com/72olabs/holler-releases/releases) ·
[Report a problem](https://github.com/72olabs/holler-releases/issues) ·
[Product website](https://holler.72olabs.ai)

For a security issue, use [private security reporting](https://github.com/72olabs/holler-releases/security/advisories/new).
Each download includes the license that applies to that release.
Holler 0.8.1 uses the Holler Proprietary Software License. Previously distributed
0.8.0 copies retain their Apache-2.0 license.

## Documentation license

Proprietary. See [LICENSE](LICENSE) for permitted use and separately licensed
material. Public availability of documentation does not grant an open-source
license. Holler binaries are governed by the license included in each release.
