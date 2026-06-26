def main():
    print("Hello from apply-job-ai-agent!")
    
    provider = GreenhouseProvider()
    resume_service = ResumeService()
    search_service = SearchService([provider])
    matching_service = MatchingService()

    agent = JobAgent(
        resume_service,
        search_service,
        matching_service
    )

    results = agent.run(
        "resume.pdf"
    )

    for match in results[:10]:
        print(
            match.score,
            match.job.company,
            match.job.title
        )

if __name__ == "__main__":
    main()
