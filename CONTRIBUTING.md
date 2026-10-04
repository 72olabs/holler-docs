# Contributing to the docs

Read the [documentation policy](DOCUMENTATION-POLICY.md) before editing.
The goal is concise, correct guidance for everyday use by humans and agents.

Edit the Markdown in this repository. Add new pages to `docs-manifest.json` and
link them from an appropriate guide. Keep the product version in the manifest
and the instructions consistent.

Run:

```sh
python3 scripts/check_docs.py
git diff --check
```

The checker validates relative file links, JSON examples, the document list and
common accidental disclosures. It does not verify external URLs, heading anchors,
all possible sensitive text or product behavior. Review those separately.

A change should explain what the reader needs to do, with a working command or
example where appropriate. Report documentation problems with a link to the page
and a suggested correction. Keep credentials and private conversations out of
issues and pull requests.
