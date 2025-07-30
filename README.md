# Manage GitHub with Python

>This project demonstrates how to manage your GitHub repositories programmatically using Python and the GitHub API.

## Features
- Delete repositories (including forked repos) in bulk
- Easily customize which repositories to manage
- Secure authentication using environment variables
- Foundation for automating other GitHub tasks (extend as needed)

## Requirements
- Python 3.8 or higher
- `requests` library
- (Optional) `python-dotenv` for loading environment variables from a `.env` file

## Setup
1. **Clone this repository**
2. **Install [uv](https://github.com/astral-sh/uv) (if not already installed):**
   ```bash
   pip install uv
   ```
3. **Install dependencies with uv:**
   ```bash
   uv pip install -r requirements.txt
   # or, to use pyproject.toml/uv.lock:
   uv pip install --all-extras .
   ```
4. **Create a `.env` file** in the project root:
   ```env
   GITHUB_ACCESS_TOKEN=your_github_token_here
   ```
   - Your token must have `delete_repo` and `repo` permissions.

## Usage
1. Edit `main.py` and update the `repos_to_delete` list with the repositories you want to delete (format: `username/repo`).
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will attempt to delete each listed repository and print the result.

## Extending
This project is a starting point for managing GitHub with Python. You can extend it to:
- List all your repositories
- Archive or unarchive repositories
- Update repository settings
- Manage issues, pull requests, and more

See the [GitHub REST API documentation](https://docs.github.com/en/rest) for more ideas.

## Safety
- **Warning:** Deleting a repository is permanent and cannot be undone.
- The script only deletes repositories listed in `repos_to_delete`.

## License
MIT License
