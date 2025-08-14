"""Compatibility entrypoint for tests and local tooling.

Exposes `load_tool_schemas` and `TOOL_FUNCTIONS` as expected by `test_server.py`.

🎯 TEMPLATE INSTRUCTIONS - Update import when you rename the folder!
When you rename "mcp_server" folder to your unique name (e.g., "weather_server"):
Change line 6: from mcp_server.server import...
to: from your_folder_name.server import...
"""

from mcp_server.server import (
    load_tool_schemas,
    TOOL_FUNCTIONS,
)  # 👈 CHANGE: Update "mcp_server" to your folder name

__all__ = [
    "load_tool_schemas",
    "TOOL_FUNCTIONS",
]
