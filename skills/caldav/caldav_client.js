import EventSource from 'eventsource';
import axios from 'axios';

// Configuration
const BRIDGE_URL = "http://100.88.191.63:3333/sse";
const BRIDGE_POST_URL = "http://100.88.191.63:3333/messages";

async function main() {
    const args = process.argv.slice(2);
    const command = args[0] || 'list_events';
    const param = args[1]; // e.g. date

    console.log(`Connecting to CalDAV Bridge at ${BRIDGE_URL}...`);

    // 1. establish SSE to get session? 
    // Actually, our bridge implementation (server.js from earlier) uses "sessionId" query param in POST
    // and sends "endpoint" event on SSE connection.
    // However, simplest way for *this* bridge (which we control) might be just to assume sending to /messages works?
    // Let's do the proper handshake.

    const es = new EventSource(BRIDGE_URL);

    let sessionId = null;
    let endpointUrl = null;

    es.onmessage = (event) => {
        // console.log("SSE Msg:", event.data);
        const data = JSON.parse(event.data);

        // Wait for JSON-RPC responses
        if (data.result) {
            console.log("Result received:");
            console.log(JSON.stringify(data.result, null, 2));
            process.exit(0);
        }
        if (data.error) {
            console.error("RPC Error:", data.error);
            process.exit(1);
        }
    };

    es.addEventListener('endpoint', (event) => {
        // Our bridge sends: event: endpoint, data: /messages?sessionId=...
        // Wait, standard is strictly URI relative or absolute.
        // Let's parse what we see.
        const ep = event.data;
        endpointUrl = `http://100.88.191.63:3333${ep}`;
        // console.log("Endpoint discovered:", endpointUrl);

        // Once we have the endpoint, send the request
        sendListEventsRequest(endpointUrl);
    });

    es.onerror = (err) => {
        // console.error("SSE Connection Error", err);
    };

    // If we don't get an endpoint event quickly (custom protocol), we might just POST.
    // server.js logic: 
    // res.write(`event: endpoint\ndata: /messages?sessionId=${sessionId}\n\n`);
}

async function sendListEventsRequest(url) {
    // Construct JSON-RPC 2.0 Request
    const payload = {
        jsonrpc: "2.0",
        id: 1,
        method: "tools/call",
        params: {
            name: "caldav_list_events", // Checking generic tool name. standard is usually namespaced or just name.
            arguments: {}
        }
    };

    try {
        const response = await axios.post(url, payload);
        // Response is usually "Accepted". The result comes via SSE.
    } catch (e) {
        console.error("Failed to post message:", e.message);
        process.exit(1);
    }
}

main();
