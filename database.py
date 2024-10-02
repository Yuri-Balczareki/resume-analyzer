from tinydb import TinyDB, Query
from typing import Optional, List, Any


class AnalyzeDatabase(TinyDB):
    def __init__(self, db_path: str = 'db.json'):
        super().__init__(db_path)
        
        self.jobs = self.table('jobs')
        self.resumes = self.table('resumes')
        self.analysis = self.table('analysis')
        self.files = self.table('files')

    def _query(self) -> Query:
        return Query()

    def get_job_by_name(self, name: str) -> Optional[dict]:
        job = self._query()
        result = self.jobs.search(job.name == name)
        return result[0] if result else None

    def get_resume_by_id(self, resume_id: int) -> Optional[dict]:
        resume = self._query()
        result = self.resumes.search(resume.id == resume_id)
        return result[0] if result else None
    
    def get_analysis_by_job_id(self, job_id: int) -> List[dict]:
        analysis = self._query()
        return self.analysis.search(analysis.job_id == job_id)

    def get_resumes_by_job_id(self, job_id: int) -> List[dict]:
        resumes = self._query()
        return self.resumes.search(resumes.job_id == job_id)
    
    def delete_all_resumes_by_job_id(self, job_id: int) -> None:
        resumes = self._query()
        self.resumes.remove(resumes.job_id == job_id)

    def delete_all_analysis_by_job_id(self, job_id: int) -> None:
        analysis = self._query()
        self.analysis.remove(analysis.job_id == job_id)

    def delete_all_files_by_job_id(self, job_id: int) -> None:
        file = self._query()
        self.files.remove(file.job_id == job_id)
