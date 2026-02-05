#!/bin/bash
# Script to create a release for the Keylogger project
# This script creates a Git tag and pushes it to trigger the release workflow

set -e

# Default version from VERSION file
DEFAULT_VERSION=$(cat VERSION 2>/dev/null || echo "1.0.0")

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}   Keylogger Release Creator${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Get version from argument or prompt
if [ -n "$1" ]; then
    VERSION="$1"
else
    echo -e "Current version in VERSION file: ${YELLOW}${DEFAULT_VERSION}${NC}"
    read -p "Enter release version (e.g., v1.0.0) [v${DEFAULT_VERSION}]: " VERSION
    VERSION=${VERSION:-"v${DEFAULT_VERSION}"}
fi

# Ensure version starts with 'v'
if [[ ! "$VERSION" =~ ^v ]]; then
    VERSION="v${VERSION}"
fi

# Validate version format
if [[ ! "$VERSION" =~ ^v[0-9]+\.[0-9]+\.[0-9]+(-[a-zA-Z0-9.]+)?$ ]]; then
    echo -e "${RED}Error: Version must follow semantic versioning (e.g., v1.0.0 or v1.0.0-beta.1)${NC}"
    exit 1
fi

echo ""
echo -e "Creating release: ${GREEN}${VERSION}${NC}"
echo ""

# Check if tag already exists locally
if git tag -l | grep -q "^${VERSION}$"; then
    echo -e "${YELLOW}Warning: Tag ${VERSION} already exists locally${NC}"
    read -p "Do you want to delete and recreate it? (y/n) [n]: " DELETE_TAG
    if [[ "$DELETE_TAG" =~ ^[Yy]$ ]]; then
        git tag -d "$VERSION"
        echo -e "${GREEN}Deleted local tag ${VERSION}${NC}"
    else
        echo "Aborting."
        exit 1
    fi
fi

# Check if tag exists on remote
if git ls-remote --tags origin | grep -q "refs/tags/${VERSION}$"; then
    echo -e "${RED}Error: Tag ${VERSION} already exists on remote${NC}"
    echo "Please use a different version number."
    exit 1
fi

# Create the tag
echo -e "Creating tag ${GREEN}${VERSION}${NC}..."
git tag -a "$VERSION" -m "Release ${VERSION}"

# Push the tag
echo -e "Pushing tag to origin..."
git push origin "$VERSION"

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}   Release Created Successfully!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "The GitHub Actions release workflow has been triggered."
echo "Check the Actions tab on GitHub to monitor the build progress."
echo ""
echo "Release URL (once complete):"
echo "  https://github.com/Stalin-143/Keylogger/releases/tag/${VERSION}"
echo ""
