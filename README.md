# apply-job-ai-agent
AI Agent to apply jobs in LinkedIn

# Job Agent

AI-powered job search and application assistant.

The goal of this project is to:

- Parse a resume/CV
- Search for relevant job opportunities
- Match jobs against the candidate profile
- Generate tailored resumes and cover letters
- Automate job applications
- Track application status

## Tech Stack

### Backend

- Python 3.13
- uv
- FastAPI
- SQLAlchemy
- SQLite

### AI

- OpenAI
- LangGraph

### Automation

- Playwright

### Development Tools

- Ruff
- MyPy
- Pytest

---

## Prerequisites

Install:

- Python 3.13+
- uv

Verify installation:

```bash
python --version
uv --version
```

---

## Project Setup

### Clone Repository

```bash
git clone <repository-url>
cd job-agent
```

### Create Virtual Environment

```bash
uv venv
```

### Activate Virtual Environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

#### macOS/Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

Dependencies are managed through `pyproject.toml`.

Install all dependencies:

```bash
uv sync
```

Verify installation:

```bash
pip list
```

---

## Install Playwright Browsers

```bash
uv run playwright install
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
OPENAI_API_KEY=your_api_key_here

DATABASE_URL=sqlite:///data/job_agent.db

PLAYWRIGHT_HEADLESS=true
```

---

## Project Structure

```text
job-agent/

├── data/
├── tests/
│
├── src/
│   └── job_agent/
│       ├── agents/
│       ├── automation/
│       ├── jobs/
│       ├── storage/
│       ├── config/
│       ├── models/
│       ├── services/
│       └── main.py
│
├── .env
├── pyproject.toml
└── README.md
```

---

## Running the Project

Run the application:

```bash
uv run python -m job_agent.main
```

---

## Code Quality

### Ruff

Check linting:

```bash
uv run ruff check .
```

Auto-fix issues:

```bash
uv run ruff check . --fix
```

### MyPy

Run static type checking:

```bash
uv run mypy src
```

### Pytest

Run tests:

```bash
uv run pytest
```

---

## Development Roadmap

### Phase 1

- [ ] Resume upload
- [ ] Resume parsing
- [ ] Candidate profile extraction
- [ ] Job search integration
- [ ] Job storage

### Phase 2

- [ ] Job matching
- [ ] Resume tailoring
- [ ] Cover letter generation

### Phase 3

- [ ] Playwright automation
- [ ] Job application workflow

### Phase 4

- [ ] Agent orchestration with LangGraph
- [ ] Daily autonomous job search
- [ ] Application tracking dashboard

---

## License

MIT
