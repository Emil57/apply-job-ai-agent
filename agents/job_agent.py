class JobAgent:
    def __init__(self, resume_service, search_service,matching_service):
        self.resume_service = resume_service
        self.search_service = search_service
        self.matching_service = matching_service