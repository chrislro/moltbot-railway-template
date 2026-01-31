---
name: peekaboo_bridge
description: Control the remote Mac UI via Peekaboo Bridge
---

# Peekaboo (Screen Capture)

This skill allows capturing the screen of the connected Mac Node using the `peekaboo` CLI.

## Usage

Execute `peekaboo` directly using `system.run`.

### Examples

- **Take Screenshot:** `peekaboo see --json` (Returns base64 image analysis)
- **Record:** `peekaboo record --duration 10`

**Note:** Requires `screen_record` permission on the Mac (already configured).
