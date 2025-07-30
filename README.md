# GitHub Fork Deleter

This project provides a simple Python script to delete forked repositories from your GitHub account using the GitHub API.

## Features
- Delete multiple forked repositories in bulk
- Uses GitHub API for secure and automated deletion
- Customizable list of repositories to delete

## Requirements
- Python 3.8+
- `requests` library
- (Optional) `python-dotenv` for loading environment variables from a `.env` file

## Setup
1. **Clone this repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or manually:
   ```bash
   pip install requests python-dotenv
   ```
3. **Create a `.env` file** in the project root with your GitHub personal access token:
   ```env
   GITHUB_ACCESS_TOKEN=your_github_token_here
   ```
   - The token must have `delete_repo` and `repo` permissions.

## Usage
1. Edit `main.py` and update the `repos_to_delete` list with the repositories you want to delete (format: `username/repo`).
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will attempt to delete each listed repository and print the result.

## Safety
- **Be careful!** Deleting a repository is permanent and cannot be undone.
- The script only deletes repositories listed in `repos_to_delete`.

## License
MIT License
