---
name: automator_bridge
description: Run AppleScript and JXA via Automator Bridge
---

# Automator Control (AppleScript)

This skill allows execution of AppleScript and JXA (JavaScript for Automation) on the connected Mac Node.

## Usage

Execute scripts directly using `system.run` with `osascript`.

### Examples

- **AppleScript:** `osascript -e 'tell application "Finder" to activate'`
- **JXA:** `osascript -l JavaScript -e 'Application("Finder").activate()'`

**Note:** The command runs on the paired Mac Node.
