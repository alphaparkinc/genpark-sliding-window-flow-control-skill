# genpark-sliding-window-flow-control-skill

[![GitHub Stars](https://img.shields.io/github/stars/alphaparkinc/genpark-sliding-window-flow-control-skill?style=social)](https://github.com/alphaparkinc/genpark-sliding-window-flow-control-skill)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-0%20(pure%20standard%20library)-brightgreen.svg)](client.py)
[![MCP Ready](https://img.shields.io/badge/MCP-Ready-purple.svg)](mcp_server.py)

> **TCP sliding window flow control protocol with cumulative ACK and buffer management**

Part of the **GenPark Autonomous Agent Matrix**, developed for production AI agents operating across local and distributed enterprise networks.

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A[Agent Application / Network Stack] --> B[genpark-sliding-window-flow-control-skill]
    B --> C[Pure Python Standard Library Engine]
    C --> D[Validated Network Output / Route Vector]
    B --> E[MCP Protocol Endpoint stdio]
    E --> F[Cursor / Claude Desktop / Windsurf Integration]
```

## 🚀 Quickstart

### Native Python Execution
```bash
python example_usage.py
```

### Standard Library Verification
```python
from client import *
```

### MCP Server (Claude Desktop / Cursor)
```json
{
  "mcpServers": {
    "genpark-sliding-window-flow-control-skill": {
      "command": "python",
      "args": ["-m", "genpark_sliding_window_flow_control_skill.mcp_server"]
    }
  }
}
```

## 📄 License
MIT License.
