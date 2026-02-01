---
name: caldav_calendar
description: Read and manage calendar events via local CalDAV MCP bridge
---

# CalDAV Calendar Skill

Allows the agent to list and manage calendar events by communicating with the local CalDAV MCP bridge running on port 3333.

## Usage

This skill relies on a helper script `caldav_client.js` to speak with the MCP server.

### Available Functions

- **List Today's Events**:
  `node skills/caldav/caldav_client.js list_events`

- **List Specific Date**:
  `node skills/caldav/caldav_client.js list_events --date "YYYY-MM-DD"`

## Setup

Ensure the CalDAV MCP bridge is running on your Mac at `http://100.88.191.63:3333/sse` (Tailscale).
