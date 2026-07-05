# Copilot Instructions for Awesome-Evolution

## Repository Context

This is an **awesome list** repository curating evolution-related resources. The repository follows the [awesome-list standards](https://github.com/sindresorhus/awesome).

## Markdown Guidelines

### Format & Structure
- Use **bold** (`**text**`) for resource names/titles when introducing them
- Use **blockquotes** (`>`) for definitions and descriptive text
- Maintain consistent two-space indentation
- Use bullet lists (`-`) for all list items, not mixed with numbered lists

### Line Length
- Lines can exceed 400 characters—this is intentional and configured in `.markdownlint.yaml`
- Long descriptive paragraphs and URLs are acceptable
- Code blocks are excluded from line-length validation

### URL Formatting
- Place URLs directly in markdown link syntax: `[Text](https://example.com)`
- Include trailing slashes for domain-level URLs when appropriate
- Check `.lycheeignore` for URLs that are intentionally excluded from link validation

### Sections
- Use `##` for main sections (e.g., `## Evolution Blogs`)
- Use `###` for subsections (e.g., `### Large Scale Genome Sequencing Projects`)
- Maintain the Table of Contents (auto-generated via doctoc)

## Content Style

### Writing Style
- Keep descriptions concise but informative
- Include relevant credentials or context for authors/contributors
- Add links to papers, websites, or documentation when available
- Use parentheses for supplementary information: `[ [paper-YEAR](url) | [web](url) ]`

### Resource Categories
- **Blogs/Content**: Short bio + mission statement
- **Projects/Tools**: Purpose + scope description
- **Databases/Browsers**: What it offers + key features
- **Related Awesome Lists**: Link only with no description

### Attribution
- Include author credentials when available (education, credentials, affiliations)
- Link to personal sites/portfolios when provided by content creators

## Linting & CI/CD

### Super-Linter Configuration
- The repo uses `super-linter v8.7.0` with markdown validation enabled
- Configuration file: `.markdownlint.yaml`
- Configured to allow lines up to 700 characters
- Code blocks are included in line-length rules (MD013 `code_blocks: true`)

### Link Checking
- Lychee validates all URLs on push/PR
- `.lycheeignore` file contains patterns for excluded URLs
- Some URLs may be intentionally ignored if they have accessibility issues

## Before Committing

- Run `npm run lint` locally if available, or rely on GitHub Actions
- Verify all new links are valid and accessible
- Update the Table of Contents if adding/removing sections
- Keep formatting consistent with existing entries

## Key Files
- `README.md` — Main content (this is the awesome list)
- `.markdownlint.yaml` — Markdown linting configuration
- `.lycheeignore` — URL validation exclusions
- `.github/workflows/linter.yml` — CI/CD linting workflow
