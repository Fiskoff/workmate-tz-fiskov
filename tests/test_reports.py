from app.analyzer import DeveloperRecord
from app.reports import PerformanceReport


class TestPerformanceReport:

    def test_generate_report_single_position(self):
        records = [
            DeveloperRecord(
                name="John", position="Backend Developer", completed_tasks=10,
                performance=4.5, skills="Python", team="Team A", experience_years=3
            ),
            DeveloperRecord(
                name="Jane", position="Backend Developer", completed_tasks=8,
                performance=4.7, skills="Python", team="Team A", experience_years=2
            )
        ]

        result = PerformanceReport.generate(records)

        assert len(result) == 1
        assert result[0]['position'] == "Backend Developer"
        assert result[0]['avg_performance'] == 4.6

    def test_generate_report_multiple_positions(self):
        records = [
            DeveloperRecord(
                name="John", position="Backend Developer", completed_tasks=10,
                performance=4.5, skills="Python", team="Team A", experience_years=3
            ),
            DeveloperRecord(
                name="Jane", position="Frontend Developer", completed_tasks=8,
                performance=4.7, skills="React", team="Team B", experience_years=2
            ),
            DeveloperRecord(
                name="Bob", position="Backend Developer", completed_tasks=12,
                performance=4.9, skills="Java", team="Team A", experience_years=5
            )
        ]

        result = PerformanceReport.generate(records)

        assert len(result) == 2
        assert result[0]['position'] == "Backend Developer"
        assert result[0]['avg_performance'] == 4.7
        assert result[1]['position'] == "Frontend Developer"
        assert result[1]['avg_performance'] == 4.7

    def test_generate_report_empty_list(self):
        result = PerformanceReport.generate([])
        assert result == []

    def test_generate_report_single_record(self):
        records = [
            DeveloperRecord(
                name="John", position="Backend Developer", completed_tasks=10,
                performance=4.5, skills="Python", team="Team A", experience_years=3
            )
        ]

        result = PerformanceReport.generate(records)

        assert len(result) == 1
        assert result[0]['position'] == "Backend Developer"
        assert result[0]['avg_performance'] == 4.5