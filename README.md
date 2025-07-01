# HSU Example3 Common

HSU Repository Portability Framework - Approach 3 (Multi-Repository + Multi-Language)

This is the **common/shared components** repository for the HSU Example3 demonstration, showing how to structure shared code and API definitions that can be used across multiple service implementation repositories.

## Features

- Shared gRPC API definitions (protobuf)
- Common Go client and library implementations
- Common Python client and library implementations
- Cross-platform build system with HSU Universal Makefile
- Repository-portable code structure for multi-repo scenarios

## Related Repositories

This common repository works with these service implementation repos:
- `hsu-example3-srv-go` - Go server implementation
- `hsu-example3-srv-py` - Python server implementation

## Quick Start

### Go Components
```bash
# Build Go client and library
make go-build

# Run Go client (requires a running server)
make go-run-cli
```

### Python Components
```bash
# Install Python dependencies
make py-install

# Build Python components
make py-build

# Run Python client (requires a running server)
make py-run-cli
```

## Documentation

For comprehensive documentation, setup guides, and framework details, see:
https://github.com/Core-Tools/docs/blob/main/README.md

## Repository Structure

This repository demonstrates **Approach 3**: Multi-Repository + Multi-Language, specifically the **shared/common components** pattern that enables code reuse across multiple service implementation repositories while maintaining clean separation of concerns.