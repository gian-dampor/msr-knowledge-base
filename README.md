# MSR Knowledge Base

[![CI](https://github.com/gian-dampor/msr-knowledge-base/actions/workflows/ci.yml/badge.svg)](https://github.com/gian-dampor/msr-knowledge-base/actions/workflows/ci.yml)

A web-based knowledge base and reference guide designed for new PhD students and researchers in Mining Software Repositories (MSR)[cite: 2].

## Live Demo
You can access the live website deployed via GitHub Pages at:
[https://gian-dampor.github.io/msr-knowledge-base/](https://gian-dampor.github.io/msr-knowledge-base/)

## Project Overview
This project acts as an interactive reference guide to help researchers navigate data sources, collection methods, analysis methods, and publication venues in MSR[cite: 2, 5]. It was built following a structured software engineering process, including requirements analysis, project planning via GitHub milestones and issues, automated testing, and CI/CD deployment[cite: 1, 7].

## Implemented Features
- **Page Structure & Navigation:** Responsive layout with interactive tab switching between sections[cite: 5].
- **Data Sources Content:** Detailed tabular view of core MSR data sources (GitHub, Stack Overflow, JIRA, App Stores, Travis CI/Jenkins, Mailing Lists, and npm Registry) including data types and descriptions[cite: 3].
- **Automated Testing & CI/CD:** Unit tests verifying HTML structure and content integrity, executed automatically via GitHub Actions on every push and pull request[cite: 1, 7].

## Future Work (Remaining Milestones)
Per the project specifications, the following milestones are documented as future enhancements[cite: 6]:
- **Milestone 3: Collection Methods Content:** Documenting REST APIs, GraphQL, web scraping techniques, database dumps, and manual downloads with pros and cons[cite: 3, 6].
- **Milestone 4: Analysis Methods Content:** Organizing statistical analysis, regression, thematic analysis, machine learning, and visualization use cases[cite: 4, 6].
- **Milestone 5: Publication Venues Content:** Cataloging key conferences (ICSE, FSE, ASE, MSR, EASE, SANER) and journals (EMSE, TSE, TOSEM) with relevance levels[cite: 4, 6].
- **Milestone 6: Styling & Polish:** Advanced responsive design and professional visual enhancements[cite: 6].

## Project Structure
```text
/docs
  requirements.md        # Requirements analysis and user stories[cite: 7]
/src (or root)
  index.html             # Main webpage with tab navigation and data table[cite: 5, 7]
/tests
  test_page.py           # Automated unit tests[cite: 7]
/.github
  /workflows
    ci.yml               # GitHub Actions CI/CD workflow configuration[cite: 7]
