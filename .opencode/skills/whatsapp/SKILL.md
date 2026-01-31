---
name: whatsapp_bridge
description: Control WhatsApp Business via wacli Bridge
---

# WhatsApp Control (wacli)

This skill provides access to WhatsApp via the `wacli` command-line tool installed on the connected Mac Node.

## Usage

To use this, execute the `wacli` command directly using `system.run` on the paired Node.

### Examples

- **Send Text:** `wacli send text --to "12345678" --message "Hello world"`
- **Send File:** `wacli send file --to "12345678" --file "/path/to/file.jpg" --caption "Look at this"`
- **List Messages:** `wacli sync --limit 5 --json`

**Note:** Ensure you target the connected Mac Node.
