import json
import sys
from client import SlidingWindowFlowControl

sessions = {}

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "manage_window",
                        "description": "Send packets or acknowledge in a sliding window session",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "session_id": {"type": "string"},
                                "action": {"type": "string", "enum": ["send", "ack", "status"]},
                                "payload": {"type": "string"},
                                "ack_seq": {"type": "integer"}
                            },
                            "required": ["session_id", "action"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "manage_window":
            sid = args["session_id"]
            if sid not in sessions:
                sessions[sid] = SlidingWindowFlowControl(window_size=4)
            sw = sessions[sid]
            action = args["action"]
            if action == "send":
                ok, seq = sw.send_packet(args.get("payload", ""))
                res = {"sent": ok, "seq": seq, "state": sw.get_state()}
            elif action == "ack":
                new_base = sw.receive_ack(args["ack_seq"])
                res = {"new_base": new_base, "state": sw.get_state()}
            else:
                res = sw.get_state()
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res)}]}
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
