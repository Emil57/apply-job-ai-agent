from pathlib import Path

from data_models.candidate import Candidate


class ResumeService:

    def parse_resume(
            self,
            path: Path
    ) -> Candidate:

        ...