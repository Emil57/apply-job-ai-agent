# Roadmap

This document is the development plan for the job application assistant. Work is tracked as GitHub issues:

- **Epics** (label `epic`): one per sprint. Each epic lists its stories as sub-issues.
- **Stories** (label `story`): one unit of work, usually one pull request.
- **Sprint labels** (`sprint-0` … `sprint-7`): filter the issue list by sprint.

## Approach: a pipeline, not a free-roaming agent

The system is a fixed pipeline. AI is used only where judgment is needed, and a human approves every application before it is sent.

```text
preferences.yaml + resume.pdf
        │
        ▼
 1. Profile ──► 2. Search ──► 3. Filter ──► 4. AI score ──► 5. Review (you)
                (job boards)   (rules)        (+ reasons)       approve / reject
                                                                   │
                                                                   ▼
                       8. Track ◄── 7. Apply (Playwright) ◄── 6. Tailor (AI)
                                       dry run first          cover letter + answers
```

| Step | Uses AI? | Why |
|------|----------|-----|
| Profile | Yes (once) | Turn a resume PDF into structured data |
| Search | No | Public job-board feeds give structured data |
| Filter | No | Cheap rules remove obvious mismatches |
| Score | Yes | Judging fit needs reading comprehension |
| Review | No — **you** | Keeps you in control |
| Tailor | Yes | Writing cover letters and answers |
| Apply | Partly | Unfamiliar form fields are mapped by AI; uncertain ones are flagged |
| Track | No | Plain database records |

### Job sources

We use the public job-board feeds of company application systems instead of scraping LinkedIn, whose terms forbid automation and which restricts accounts that use it.

| Board | Public feed |
|-------|-------------|
| Greenhouse | `https://boards-api.greenhouse.io/v1/boards/{company}/jobs?content=true` |
| Lever | `https://api.lever.co/v0/postings/{company}?mode=json` |
| Ashby | `https://api.ashbyhq.com/posting-api/job-board/{company}` |

## How we work together

1. Pick the next story in sprint order.
2. Create a branch, implement it with tests, open a pull request that says `Closes #<story>`.
3. Review and run it locally with real data (your resume, API key and preferences stay in git-ignored files).
4. Merge when the story's acceptance criteria are checked.
5. A sprint is done when every story in its epic is closed and the epic's "Definition of done" holds.

**Safety rules for the whole project**

- `DRY_RUN=true` is the default. Nothing is submitted unless you turn it off.
- No application goes out without your explicit approval.
- AI never invents experience: tailoring uses only `profile.json` and `answers.yaml`.
- CAPTCHAs or unexpected pages stop the run; the system never tries to get around them.
- Secrets live only in `.env`, never in code or commits.

## Sprints

### Sprint 0 — Foundation · epic #1

Goal: a runnable, tested skeleton.

| # | Story |
|---|-------|
| #9 | Restructure code into `src/job_agent` package and fix broken imports |
| #10 | Fix pyproject: Python version, runtime dependencies and CLI entry point |
| #11 | Settings loaded from `.env` with pydantic-settings |
| #12 | Code quality tooling and GitHub Actions CI |
| #13 | Decide open product questions |

### Sprint 1 — Profile & preferences · epic #2

Goal: capture who you are and what you want.

| # | Story |
|---|-------|
| #14 | Preferences model and `preferences.yaml` |
| #15 | AI client wrapper with structured (typed) output |
| #16 | Parse resume PDF into a Candidate profile |
| #17 | CLI command: `job-agent profile` |

### Sprint 2 — Job search · epic #3

Goal: real openings from your target companies, stored without duplicates.

| # | Story |
|---|-------|
| #18 | SearchProvider interface and richer Job model |
| #19 | Greenhouse job board provider |
| #20 | Lever job board provider |
| #21 | Ashby job board provider |
| #22 | SQLite storage for jobs with de-duplication |
| #23 | CLI command: `job-agent search` |

### Sprint 3 — Filtering & AI scoring · epic #4

Goal: a short, ranked list with reasons you agree with.

| # | Story |
|---|-------|
| #24 | Rule-based job filters |
| #25 | AI match scoring with reasons (MatchingService) |
| #26 | Cache match scores in SQLite |
| #27 | CLI command: `job-agent rank` + scoring evaluation set |

### Sprint 4 — Review & approval · epic #5

Goal: nothing moves forward without your approval.

| # | Story |
|---|-------|
| #28 | CLI review: approve / reject / skip ranked jobs |
| #38 | (Optional) Local web review page with FastAPI |

### Sprint 5 — Tailoring · epic #6

Goal: everything an application needs, grounded in your real background.

| # | Story |
|---|-------|
| #29 | Answer bank for standard application questions |
| #30 | Cover letter generation per approved job |
| #31 | Answers to job-specific screening questions |

### Sprint 6 — Automated applying · epic #7

Goal: fill and submit forms safely, dry run first.

| # | Story |
|---|-------|
| #32 | Greenhouse form filler in dry-run mode |
| #33 | Submit approved applications with safeguards |
| #34 | Lever (and Ashby) form fillers |

### Sprint 7 — Tracking & scheduling · epic #8

Goal: daily runs and a clear record of every application.

| # | Story |
|---|-------|
| #35 | Application status tracking |
| #36 | Daily scheduled pipeline run |
| #37 | Daily digest notification |

## Open decisions (story #13)

| Question | Options | Decision |
|----------|---------|----------|
| AI provider | OpenAI / Claude | _pending_ |
| Target companies | 20–50 companies with their job board | _pending_ |
| First job board | Greenhouse (proposed) | _pending_ |
| Where it runs | Locally / scheduled in the cloud | _pending_ |
| Review interface | Terminal first, web page later (proposed) | _pending_ |

## Optional: GitHub milestones and project board

The issues are ready to drop into GitHub's planning tools:

- **Milestones:** Issues → Milestones → New milestone, one per sprint ("Sprint 0 — Foundation", …). Then filter issues by `label:sprint-0`, select all, and set the milestone.
- **Project board:** Projects → New project → Board. Add items with the filter `repo:Emil57/apply-job-ai-agent is:issue`, then group by label or by milestone to see one column per sprint.
