from typing import List, Dict, Any

from app.analyzer import DeveloperRecord


class ReportGenerator:
    def __init__(self):
        self._reports = {}

    def register_report(self, name: str, handler):
        self._reports[name] = handler

    def generate_report(self, report_type: str, records: List[DeveloperRecord]) -> List[Dict[str, Any]]:
        if report_type not in self._reports:
            raise ValueError(f"Unknown report type: {report_type}")

        return self._reports[report_type](records)


class PerformanceReport:
    @staticmethod
    def generate(records: List[DeveloperRecord]) -> List[Dict[str, Any]]:
        position_data = {}
        for record in records:
            position = record.position
            if position not in position_data:
                position_data[position] = []
            position_data[position].append(record.performance)

        results = []
        for position, performances in position_data.items():
            avg_performance = sum(performances) / len(performances)
            results.append({
                'position': position,
                'avg_performance': round(avg_performance, 2)
            })

        results.sort(key=lambda x: x['avg_performance'], reverse=True)

        return results


report_generator = ReportGenerator()
report_generator.register_report('performance', PerformanceReport.generate)