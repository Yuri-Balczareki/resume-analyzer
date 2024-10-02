from tinydb import TinyDB, Query


class AnalyzeDatabase(TinyDB):
    def __init__(self, db_path='db.json'): 
        super().__init__(db_path)
        
        self.jobs = self.table('jobs')
        self.resumes = self.table('resumes')
        self.analysis = self.table('analysis')
        self.files = self.tables('files')

    def get_job_by_name(self, name): 
        job = Query()
        result = self.jobs.search(
            job.name == name
        )
        return result[0] if result else None 
    