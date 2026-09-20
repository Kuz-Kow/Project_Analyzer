from typing import NoReturn


PROJECT_TITLE = "File Analyzer"

FILEDS= [
    "Analyze extensions",
    "Group files",
    "Show larges files",
    "Show resent files",
    "Search files",
    "Exit"
]

def main() -> NoReturn:
    
    while True:
        print("="*len(PROJECT_TITLE)*3)
        print(" "*len(PROJECT_TITLE),PROJECT_TITLE.upper()," "*len(PROJECT_TITLE))
        print("="*len(PROJECT_TITLE)*3, "\n")
    
        for number, title in enumerate(FILEDS):
            print(f"{number+1}. {title}")
        
        choice = input("\nChoice: ")
        

if __name__ == "__main__":
    main()