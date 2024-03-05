import os
import sys

def latex_diff(original_dir, revised_dir, diff_dir):
    # Check if the output directory exists, if not, create it
    if not os.path.exists(diff_dir):
        os.makedirs(diff_dir)

    # Get the list of directories in the original directory
    original_files = [f for f in os.listdir(original_dir) if f.endswith('.tex')]
    revised_files = [f for f in os.listdir(revised_dir) if f.endswith('.tex')]
    # Iterate through main directories
    for file in revised_files:
        print("================================================")
        print(f"Processing {file}")

        original_file = os.path.join(original_dir, file)
        revised_file = os.path.join(revised_dir, file)
        diff_file = os.path.join(diff_dir, file)

        if file not in original_files:
            original_file = "empty.tex"
            
        cmd = f"latexdiff '{original_file}' '{revised_file}' > '{diff_file}'"

        os.system(cmd)

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python3 latexdiff.py original_dir revised_dir diff_dir")
        sys.exit(1)

    original_dir = sys.argv[1]
    revised_dir = sys.argv[2]
    diff_dir = sys.argv[3]

    latex_diff(original_dir, revised_dir, diff_dir)