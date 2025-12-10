import argparse
import sys

from tabulate import tabulate

from app.analyzer import DataProcessor
from app.reports import report_generator


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Анализ эффективности работы разработчиков'
    )
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Пути к файлам с данными'
    )
    parser.add_argument(
        '--report',
        required=True,
        help='Тип отчета для генерации'
    )
    return parser.parse_args()


def main():
    try:
        args = parse_arguments()

        if args.report != 'performance':
            print(f"Error: Unsupported report type '{args.report}'. Supported: 'performance'", file=sys.stderr)
            sys.exit(1)

        if not args.files:
            print("Error: No files provided", file=sys.stderr)
            sys.exit(1)

        processor = DataProcessor()
        records = processor.get_all_records(args.files)

        if not records:
            print("No data found in provided files", file=sys.stderr)
            sys.exit(1)

        report_data = report_generator.generate_report(args.report, records)

        headers = ['Position', 'Average Performance']
        table_data = [[item['position'], item['avg_performance']] for item in report_data]

        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid data format - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()