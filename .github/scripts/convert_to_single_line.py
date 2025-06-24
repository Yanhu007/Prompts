#!/usr/bin/env python3
"""
Convert multi-line files to single-line format with \\r\\n separators
"""
import os

def convert_file_to_single_line(file_path):
    """Convert a multi-line file to single line with \\r\\n separators"""
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Remove trailing newlines from each line and join with \\r\\n
        cleaned_lines = [line.rstrip('\n\r') for line in lines]
        single_line_content = '\\r\\n'.join(cleaned_lines)
        
        # Write back to the same file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(single_line_content)
        
        print(f"✓ Converted {file_path}")
        return True
    except Exception as e:
        print(f"✗ Error converting {file_path}: {e}")
        return False

def main():
    """Main function to process all files"""
    base_path = ".outputs"
    successful = 0
    failed = 0
    
    # Process files from 01 to 50
    for i in range(1, 51):
        file_name = f"edge_src_structure_part_{i:02d}.txt"
        file_path = os.path.join(base_path, file_name)
        
        if os.path.exists(file_path):
            if convert_file_to_single_line(file_path):
                successful += 1
            else:
                failed += 1
        else:
            print(f"✗ File not found: {file_path}")
            failed += 1
    
    print(f"\nSummary:")
    print(f"Successfully converted: {successful} files")
    print(f"Failed: {failed} files")

if __name__ == "__main__":
    main()
