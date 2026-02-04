# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-04

### Added
- Initial release of the Keylogger project
- Main keylogger script (`src/keylogger.py`) with keystroke logging capabilities
- Web server (`src/server.py`) for viewing logs through a secure interface
- Configuration management via JSON config files and environment variables
- Command-line interface with flexible argument parsing
- Batch processing to reduce network overhead
- Basic authentication for the web interface
- Setup script (`setup.sh`) for easy installation
- Comprehensive documentation including README, SECURITY, and DISCLAIMER files
- GitHub Actions workflows for CI/CD and releases

### Security
- Password-protected web interface
- Environment variable support for sensitive credentials
- Security policy documentation (SECURITY.md)

## [Unreleased]

### Planned
- Enhanced encryption for log transmission
- Multi-platform support improvements
- Additional authentication methods
