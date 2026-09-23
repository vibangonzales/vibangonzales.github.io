import os
import re
import subprocess
import shutil
import tempfile

def extract_and_convert_mermaid():
    """Extract Mermaid code blocks, convert to SVG, and replace with image refs."""
    docs_dir = "docs"
    output_dir = os.path.join(docs_dir, "assets", "mermaid")
    os.makedirs(output_dir, exist_ok=True)
    
    # Create temporary directory and copy entire docs directory
    temp_dir = tempfile.mkdtemp()
    temp_docs_dir = os.path.join(temp_dir, "docs")
    shutil.copytree(docs_dir, temp_docs_dir)
    
    mermaid_count = 0  # Counter for unique SVG filenames
    print ("temp_dir", temp_dir);
    return temp_dir

def run_mkdocs_with_pdf(temp_dir):
    """Run mkdocs build with with-pdf using temporary Markdown files."""
    print("Generating PDF...")
    env = os.environ.copy()
    env["EXPORT_PDF"] = "1"

    env["FONTCONFIG_FILE"] = "C:/Users/mannyinsignares/Documents/fonts.conf"
    
    # Temporarily replace docs directory
    orig_docs = "docs"
    shutil.move(orig_docs, "docs_orig")
    shutil.move(os.path.join(temp_dir, "docs"), orig_docs)
    
    try:
        subprocess.run(["mkdocs", "build", "--clean"], env=env, check=True)
    finally:
        # Restore original docs directory
        shutil.move(orig_docs, os.path.join(temp_dir, "docs"))
        shutil.move("docs_orig", orig_docs)
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    print("Converting Mermaid diagrams to images...")
    temp_dir = extract_and_convert_mermaid()
    run_mkdocs_with_pdf(temp_dir)
    print("PDF generated at pdf/document.pdf")