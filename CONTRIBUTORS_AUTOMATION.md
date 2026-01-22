# Contributors Automation Guide

## Overview

This repository uses an automated system to maintain a Contributors Hall of Fame with GitHub profile photos. When anyone contributes to the project through merged pull requests, they will be automatically added to the [CONTRIBUTORS.md](CONTRIBUTORS.md) file.

## How It Works

1. **Automatic Detection**: When a pull request is merged to the main branch, the GitHub Actions workflow automatically detects all contributors.

2. **Profile Photos**: The system fetches GitHub profile photos for each contributor and displays them in the Contributors Hall of Fame.

3. **Automatic Updates**: The CONTRIBUTORS.md file is automatically updated with new contributors, maintaining a beautiful gallery of everyone who has helped the project.

## Features

- ✨ Automatic detection of new contributors
- 📸 GitHub profile photos displayed in the hall of fame
- 🔄 Automatic updates on every merged PR
- 👥 Recognition for all types of contributions (code, documentation, ideas, etc.)

## The Contributors Workflow

The automation is powered by a GitHub Actions workflow located at `.github/workflows/contributors.yml`. This workflow:

1. Triggers when:
   - A pull request is merged to main
   - Code is pushed to the main branch
   - Manually triggered via workflow_dispatch

2. Automatically:
   - Fetches all contributors from the repository
   - Updates the CONTRIBUTORS.md file with profile photos
   - Commits the changes back to the repository

## Manual Triggering

Repository maintainers can manually trigger the contributors update by:
1. Going to Actions tab in GitHub
2. Selecting "Add Contributors" workflow
3. Clicking "Run workflow"

## Configuration

The contributors system is configured in:
- `.github/workflows/contributors.yml` - The automation workflow
- `.all-contributorsrc` - Configuration for the all-contributors system

### Customization Options

You can customize the appearance by editing `.github/workflows/contributors.yml`:
- `image_size`: Size of profile photos (default: 100px)
- `columns_per_row`: Number of contributors per row (default: 6)

## For Contributors

When you contribute to this project:
1. Your GitHub profile will automatically appear in the Contributors Hall of Fame
2. Your profile photo will be displayed
3. You'll be recognized for your contributions

## Requirements

- GitHub Actions must be enabled for the repository
- The workflow requires `contents: write` permission to update files

## Troubleshooting

If contributors are not being added automatically:
1. Check that GitHub Actions is enabled
2. Verify the workflow has necessary permissions
3. Ensure the main branch name matches the configuration
4. Manually trigger the workflow to force an update

## Credits

This automation uses:
- [contributors-readme-action](https://github.com/akhilmhdh/contributors-readme-action) by akhilmhdh
- GitHub Actions for automation

---

For questions about the contributors system, please open an issue on GitHub.
