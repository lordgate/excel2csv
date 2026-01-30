#!/usr/bin/env python3
import argparse
import sys
import os
import pandas as pd
import csv

VERSION = "1.0.0"

def get_sheet_names(file_path):
    """
    Excel 파일의 시트 이름 목록을 반환합니다.
    """
    try:
        xls = pd.ExcelFile(file_path)
        return xls.sheet_names
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        sys.exit(1)

def convert_sheet_to_csv(file_path, sheet_name, output_path, options):
    """
    특정 시트를 CSV로 변환합니다.
    """
    try:
        # Read Excel
        # Always assume header exists in Excel (row 0)
        df = pd.read_excel(file_path, sheet_name=sheet_name, header=0)
        
        # Write CSV
        # date_format is handled nicely by pandas to_csv if passed properly, 
        # but pandas to_csv doesn't have a direct 'date_format' equivalent for all columns globally easily for datetime objects only without affecting others potentially,
        # checking options. However, pandas `to_csv` `date_format` parameter sets format for datetime objects.
        
        df.to_csv(
            output_path, 
            index=False, 
            encoding=options.encoding,
            sep=options.separator,
            quotechar=options.quotechar,
            lineterminator=options.line_terminator,
            date_format=options.date_format,
            header=not options.no_header,
            quoting=csv.QUOTE_MINIMAL # Default needed behavior: quote only when needed
        )
        print(f"Converted '{sheet_name}' to '{output_path}'")
    except Exception as e:
        print(f"Error converting sheet '{sheet_name}': {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Convert Excel files to CSV.")
    
    parser.add_argument("input_file", help="Input Excel file (.xlsx, .xls)")
    parser.add_argument("sheet", nargs="?", help="Sheet index (1-based) or name. Optional if -a is used.")
    
    parser.add_argument("-a", "--all", action="store_true", help="Convert all sheets to CSV files.")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {VERSION}")
    
    # CSV Formatting Options
    parser.add_argument("-e", "--encoding", default="utf-8", help="Output encoding (default: utf-8)")
    parser.add_argument("-s", "--separator", default=",", help="Field separator (default: ,)")
    parser.add_argument("-q", "--quotechar", default='"', help="Quote character (default: \")")
    parser.add_argument("-l", "--line-terminator", default="\n", help="Line terminator (default: \\n)")
    parser.add_argument("-D", "--date-format", help="Date format (e.g., %%Y-%%m-%%d)")
    parser.add_argument("--no-header", action="store_true", help="Do not output the header row")
    parser.add_argument("-o", "--output", help="Output file name (ignored or used as prefix in batch mode)")

    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f"Error: File '{args.input_file}' not found.")
        sys.exit(1)

    sheet_names = get_sheet_names(args.input_file)

    # List sheets if no sheet is specified and not in all mode
    if args.sheet is None and not args.all:
        for idx, name in enumerate(sheet_names, 1):
            print(f"{idx}. {name}")
        return

    # Batch conversion
    if args.all:
        for idx, name in enumerate(sheet_names, 1):
            # Determine output filename
            # If -o is provided, maybe use it as directory or prefix?
            # Requirement says: "일괄 변환 시에는 무시되거나 디렉토리 지정용으로 사용될 수 있음"
            # Current logic: Original filename based: SheetName.csv 
            # Note: Requirement said "ExcelFile.xlsx(xls) 1 ... (파일명: Index_SheetName.csv)"
            # "시트 이름 지정 시 파일명: SheetName.csv"
            # Let's stick to safe default: SheetName.csv
            
            out_name = f"{name}.csv"
            # If output is a directory, join it
            if args.output and os.path.isdir(args.output):
                 out_name = os.path.join(args.output, out_name)
            
            convert_sheet_to_csv(args.input_file, name, out_name, args)
        return

    # Single sheet conversion
    target_sheet_name = None
    output_filename = args.output

    # Try to interpret sheet argument as index (int)
    try:
        idx = int(args.sheet)
        if 1 <= idx <= len(sheet_names):
            target_sheet_name = sheet_names[idx-1]
            if not output_filename:
                output_filename = f"{idx}_{target_sheet_name}.csv"
        else:
            print(f"Error: Index {idx} out of range.")
            sys.exit(1)
    except ValueError:
        # Not an integer, treat as sheet name
        if args.sheet in sheet_names:
            target_sheet_name = args.sheet
            if not output_filename:
                output_filename = f"{target_sheet_name}.csv"
        else:
             print(f"Error: Sheet '{args.sheet}' not found.")
             sys.exit(1)

    convert_sheet_to_csv(args.input_file, target_sheet_name, output_filename, args)

if __name__ == "__main__":
    main()
