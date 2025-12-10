import csv
from typing import List, Iterator
from dataclasses import dataclass


@dataclass
class DeveloperRecord:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: str
    team: str
    experience_years: int


class CSVDataReader:
    def read_records(self, file_paths: List[str]) -> Iterator[DeveloperRecord]:
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    yield DeveloperRecord(
                        name=row['name'],
                        position=row['position'],
                        completed_tasks=int(row['completed_tasks']),
                        performance=float(row['performance']),
                        skills=row['skills'],
                        team=row['team'],
                        experience_years=int(row['experience_years'])
                    )


class DataProcessor:
    def __init__(self):
        self.data_reader = CSVDataReader()

    def get_all_records(self, file_paths: List[str]) -> List[DeveloperRecord]:
        return list(self.data_reader.read_records(file_paths))