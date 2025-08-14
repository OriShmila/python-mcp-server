# Python MCP Server Template

A production-ready Python template for building Model Context Protocol (MCP) servers. This template provides a complete foundation with schema validation, comprehensive testing, and a reference implementation using the Weather API.

## 🎯 Purpose

This template serves as a starting point for building your own MCP servers in Python. It includes:
- Complete MCP server setup with `uv` package manager
- JSON Schema-based tool definitions
- Comprehensive input/output validation
- Extensive test suite framework
- Error handling and logging
- Example implementation (Weather API)

## 🏗️ Template Structure

```
python-mcp-server/
├── mcp_server/              # Main package directory
│   ├── __init__.py         # Package initialization
│   ├── __main__.py         # Entry point for the MCP server
│   ├── server.py           # Core MCP server implementation
│   ├── handlers.py         # Tool function implementations
│   └── tools.json          # Tool schemas and definitions
├── main.py                 # Compatibility wrapper for testing
├── test_server.py          # Comprehensive test framework
├── test_cases.json         # Test case definitions
├── pyproject.toml          # Project dependencies and metadata
├── uv.lock                 # Locked dependencies
└── README.md               # This file
```

## 🚀 Quick Start

### Using This Template

1. **Clone or fork this repository:**
   ```bash
   git clone https://github.com/yourusername/python-mcp-server.git my-mcp-server
   cd my-mcp-server
   ```

2. **Install dependencies with uv:**
   ```bash
   uv sync
   ```

3. **Customize for your use case:**
   - Replace tool implementations in `mcp_server/handlers.py`
   - Update tool schemas in `mcp_server/tools.json`
   - Modify test cases in `test_cases.json`
   - Update project metadata in `pyproject.toml`

4. **Run tests to verify:**
   ```bash
   uv run python test_server.py
   ```

## 📋 Core Components

### 1. Server Implementation (`mcp_server/server.py`)

The core MCP server that:
- Loads tool schemas from `tools.json`
- Handles MCP protocol communication
- Routes tool calls to handler functions
- Manages server lifecycle

**Key functions:**
- `load_tool_schemas()` - Loads tool definitions from JSON
- `handle_list_tools()` - Returns available tools to MCP clients
- `handle_call_tool()` - Executes tool functions with validation
- `run_server()` - Main server loop

### 2. Tool Handlers (`mcp_server/handlers.py`)

Implement your tool functions here. The template includes Weather API handlers as examples:

```python
# Example tool function structure
async def your_tool_function(param1: str, param2: int = None) -> dict:
    """Your tool implementation."""
    # Validate inputs
    if not param1:
        raise ValueError("param1 is required")
    
    # Process request
    result = await process_data(param1, param2)
    
    # Return structured response
    return {"status": "success", "data": result}

# Register in TOOL_FUNCTIONS mapping
TOOL_FUNCTIONS = {
    "your_tool": your_tool_function,
    # Add more tools here
}
```

### 3. Tool Schemas (`mcp_server/tools.json`)

Define your tools using JSON Schema:

```json
{
  "name": "YourServer",
  "tools": [
    {
      "name": "your_tool",
      "description": "Tool description",
      "inputSchema": {
        "type": "object",
        "properties": {
          "param1": {
            "type": "string",
            "description": "Parameter description"
          }
        },
        "required": ["param1"]
      },
      "outputSchema": {
        "type": "object",
        "properties": {
          "status": {"type": "string"},
          "data": {"type": "object"}
        }
      }
    }
  ]
}
```

### 4. Testing Framework (`test_server.py`)

Comprehensive testing with:
- Schema structure validation
- Input/output validation
- Tool function testing
- Error case handling
- Performance monitoring

### 5. Test Cases (`test_cases.json`)

Define test scenarios:

```json
{
  "test_cases": [
    {
      "name": "test_name",
      "tool": "your_tool",
      "arguments": {
        "param1": "test_value"
      },
      "description": "Test description",
      "expected_fields": ["status", "data"],
      "should_succeed": true
    }
  ]
}
```

## 🔧 Customization Guide

### Step 1: Define Your Tools

Edit `mcp_server/tools.json`:
1. Update the server name
2. Define your tool schemas
3. Specify input/output validation rules

### Step 2: Implement Tool Functions

Edit `mcp_server/handlers.py`:
1. Remove example Weather API functions
2. Add your tool implementations
3. Update the `TOOL_FUNCTIONS` mapping

### Step 3: Configure Dependencies

Edit `pyproject.toml`:
1. Update project name and description
2. Add/remove dependencies as needed
3. Update the console script name if desired

### Step 4: Update Tests

Edit `test_cases.json`:
1. Remove example Weather API tests
2. Add test cases for your tools
3. Include both success and failure scenarios

### Step 5: Environment Variables

If your server needs configuration:
1. Create a `.env` file for local development
2. Add environment variable handling in `handlers.py`
3. Document required variables in README

## 📦 Packaging and Distribution

### Option 1: Install from Git

Users can install directly from your repository:

```bash
uvx --from git+https://github.com/yourusername/your-mcp-server your-server-name
```

### Option 2: Publish to PyPI

1. Update `pyproject.toml` with your package details
2. Build the package: `uv build`
3. Publish: `uv publish`

### Option 3: Use with MCP Clients

Configure in Claude Desktop or other MCP clients:

```json
{
  "mcpServers": {
    "your-server": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/yourusername/your-mcp-server",
        "your-server-name"
      ],
      "env": {
        "YOUR_ENV_VAR": "value"
      }
    }
  }
}
```

## 🌟 Example Implementation: Weather API

This template includes a complete Weather API implementation as a reference showing:

- **Multiple tool types** - Various weather-related queries
- **Complex schemas** - Nested objects and arrays
- **Error handling** - Invalid inputs and API errors
- **Async operations** - HTTP client integration
- **Environment configuration** - API key management
- **Comprehensive testing** - 45+ test cases

### Available Example Tools

| Tool | Description |
|------|-------------|
| `get_weather` | Weather forecasts (1-3 days) |
| `get_weather_history` | Historical weather data |
| `get_weather_airquality` | Air quality information |
| `get_astronomy_data` | Sunrise, sunset, moon phases |
| `search_locations` | Location search |
| `get_timezone` | Timezone information |
| `get_sport_events` | Sports event weather |

To use the Weather API example:
1. Get a free API key from [WeatherAPI.com](https://www.weatherapi.com/)
2. Set `WEATHER_API_KEY` in your `.env` file
3. Run tests: `uv run python test_server.py`

## 🧪 Testing Your Server

The template includes a comprehensive test framework:

```bash
# Run all tests
uv run python test_server.py

# Test output includes:
# - Schema validation
# - Tool function tests  
# - Error handling
# - Performance metrics
# - Success/failure summary
```

### Test Features

- **Schema Validation** - Validates all tool schemas
- **Input Validation** - Tests parameter constraints
- **Output Validation** - Verifies response structure
- **Error Cases** - Tests invalid inputs
- **Performance** - Measures response times

## 🛠️ Development Workflow

1. **Define schemas** in `tools.json`
2. **Implement handlers** in `handlers.py`
3. **Write tests** in `test_cases.json`
4. **Run tests** with `test_server.py`
5. **Test with MCP client** (Claude Desktop, etc.)
6. **Package and distribute**

## 📚 MCP Protocol Basics

This template implements the MCP protocol:

- **Communication**: JSON-RPC 2.0 over stdio
- **Tool Discovery**: Clients call `list_tools` to discover available tools
- **Tool Execution**: Clients call `call_tool` with tool name and arguments
- **Validation**: Input/output validated against JSON schemas
- **Error Handling**: Structured error responses

## 🤝 Contributing

Contributions to improve this template are welcome:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

This template is provided as open source for use in your MCP server projects.

## 🔗 Resources

- [MCP Documentation](https://github.com/modelcontextprotocol)
- [UV Package Manager](https://github.com/astral-sh/uv)
- [JSON Schema](https://json-schema.org/)
- [Python Async/Await](https://docs.python.org/3/library/asyncio.html)

## 🎯 Next Steps

1. **Customize** - Replace the example implementation with your own tools
2. **Test** - Ensure comprehensive test coverage
3. **Document** - Update this README with your specific details
4. **Deploy** - Share your MCP server with the community

---

*This template provides a solid foundation for building MCP servers in Python. The Weather API implementation serves as a comprehensive example of how to structure tools, handle validation, and implement testing.*