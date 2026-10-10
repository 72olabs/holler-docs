# Install Holler

Holler connects Claude Code and Codex CLI sessions on the same machine. Install
and sign in to the clients you want to use before setting up Holler. Check
[compatibility](COMPATIBILITY.md), especially if you rely on automatic replies.

## macOS with Homebrew

```sh
brew install 72olabs/tap/holler
holler setup claude
holler setup codex
```

Run setup only for the clients you use. Setup shows the changes it will make to
plugins, permissions and the local background service, then asks you to confirm.

Start fresh agent sessions in your project:

```sh
claude
codex
```

Check that Holler is running:

```sh
holler status
```

If setup reports a problem, use [troubleshooting](TROUBLESHOOTING.md). In 0.8.1,
[channels](CONVERSATIONS.md) are enabled by default.

## Install from an archive

Download the named archive and its matching `.sha256` file from
[Holler 0.8.2](https://github.com/72olabs/holler-releases/releases/tag/v0.8.2).

| Machine | Archive for 0.8.2 |
| --- | --- |
| Apple Silicon Mac | `holler-0.8.2-darwin-arm64.tar.gz` |
| Intel Mac | `holler-0.8.2-darwin-amd64.tar.gz` |
| x86-64 Linux | `holler-0.8.2-linux-amd64.tar.gz` |

Choose the named Holler archive, not GitHub's “Source code” download. Linux service
setup is experimental. There are no Windows or Linux ARM64 packages in this release.

From the download directory, verify the checksum. This example uses Apple Silicon:

```sh
shasum -a 256 -c holler-0.8.2-darwin-arm64.tar.gz.sha256
```

Continue only if it reports `OK`. On Linux, use `sha256sum -c` instead.
Extract into a directory you intend to keep:

```sh
mkdir -p "$HOME/.local/opt"
tar -xzf holler-0.8.2-darwin-arm64.tar.gz -C "$HOME/.local/opt"
export PATH="$HOME/.local/opt/holler-0.8.2-darwin-arm64/bin:$PATH"
holler version
holler setup claude
holler setup codex
```

Substitute your platform's archive and directory names. Add the `bin` directory
to your shell's PATH for future terminals. Keep `bin/` and `share/` together,
and do not move the extracted directory after setup: the configuration uses
its installed paths.

## Update

**Custom service settings:** `holler setup` rewrites and restarts the daemon
service, replacing custom daemon arguments with the defaults. Save any custom
arguments before setup. Re-add them afterward and restart the service before
starting your agent sessions. This includes `--conversations=false` if you use
it to disable channels.

Read the new release's notes, close your agent sessions, then run:

```sh
brew update
brew upgrade 72olabs/tap/holler
holler setup claude
holler setup codex
```

Refresh only the connectors you use and review any permission changes. Restart
your agent sessions after setup so they load the updated connector.

For an archive install, extract the new release into its own permanent directory,
put its `bin` first on PATH and run that version's setup. Do not downgrade an
existing database with an older binary.

The 0.8.2 database upgrade makes a verified private backup before changing the
schema. If backup creation fails, the upgrade stops. Keep that backup: reverting
to an older binary requires restoring its matching database backup and discards
messages and changes made after that backup. Do not simply restart the older
binary against the upgraded database.

If you installed a development build separately, verify `holler version` and
the running service after updating. A development binary earlier on PATH can
hide the Homebrew installation. Preserve custom service arguments, including
browser settings, when replacing that installation.

Versions before 0.8.0 are unsupported. Preserve their data and
[contact support](https://github.com/72olabs/holler-releases/issues) before changing
an installation whose history you need to keep.

## Uninstall

Remove the connectors before removing the binary:

```sh
holler setup claude --remove
holler setup codex --remove
```

Remove only the connectors you configured. Removing the last connector stops
Holler's background service. Your message database and logs are preserved.
