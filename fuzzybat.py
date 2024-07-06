#!/usr/bin/env python3
import os
import subprocess
import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.styles import Style

def get_files(directory="."):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def fuzzy_search(query, file_list):
    process = subprocess.Popen(
        ["fzf", "--filter", query],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )
    stdout, _ = process.communicate(input="\n".join(file_list))
    return stdout.strip().split("\n")

def display_file_with_bat(file_path):
    try:
        result = subprocess.run(
            ["bat", "--color=always", "--style=full", file_path],
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError:
        print(f"Error: Unable to display file {file_path}")

def main():
    file_list = get_files()
    completer = FuzzyWordCompleter(file_list)
    
    style = Style.from_dict({
        'completion-menu.completion': 'bg:#008888 #ffffff',
        'completion-menu.completion.current': 'bg:#00aaaa #000000',
    })

    session = PromptSession(
        completer=completer,
        style=style,
        complete_while_typing=True
    )

    while True:
        try:
            query = session.prompt(HTML('<b>FuzzyBat></b> '))
            if query.lower() in ('quit', 'exit', 'q'):
                break

            matches = fuzzy_search(query, file_list)
            
            if not matches or matches[0] == '':
                print("No matches found.")
                continue

            for i, match in enumerate(matches[:5], 1):
                print(f"{i}. {match}")

            choice = input("Enter the number of the file to view (or press Enter to search again): ")
            if choice.isdigit() and 1 <= int(choice) <= len(matches):
                selected_file = matches[int(choice) - 1]
                display_file_with_bat(selected_file)
            elif choice == '':
                continue
            else:
                print("Invalid choice. Please try again.")

        except KeyboardInterrupt:
            continue
        except EOFError:
            break

    print("Thank you for using FuzzyBat!")

if __name__ == "__main__":
    main()
