# FuzzyBat

FuzzyBat is a command-line application that combines the power of fzf (fuzzy finder) and bat (syntax highlighter) into a single, easy-to-use tool. It allows users to search for files using fuzzy matching and then view the contents of the selected file with syntax highlighting.

## Features

- Fuzzy file search across directories
- Syntax-highlighted file preview
- Interactive command-line interface
- Combines functionality of popular tools fzf and bat

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- fzf
- bat
- macOS (Note: This tool is designed for macOS but may work on other Unix-like systems with modifications)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/fuzzybat.git
   cd fuzzybat
   ```

2. Install the required Python package:
   ```
   pip3 install -r requirements.txt
   ```

3. Ensure you have fzf and bat installed. If not, you can install them using Homebrew:
   ```
   brew install fzf bat
   ```

4. Make the script executable:
   ```
   chmod +x fuzzybat.py
   ```

## Usage

To run FuzzyBat, navigate to the directory containing the script and run:

```
./fuzzybat.py
```

Once the application is running:

1. Enter a search query to find files.
2. Select a file from the list of matches by entering its number.
3. The contents of the selected file will be displayed with syntax highlighting.
4. Press Enter to search again, or type 'quit', 'exit', or 'q' to exit the application.

## Contributing

Contributions to FuzzyBat are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## License

This project uses the [MIT License](LICENSE.md).

## Acknowledgements

- [fzf](https://github.com/junegunn/fzf) - Command-line fuzzy finder
- [bat](https://github.com/sharkdp/bat) - A cat(1) clone with syntax highlighting and Git integration
- [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) - Library for building powerful interactive command-line applications
