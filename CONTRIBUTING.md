# Contributing

Your contributions are always welcome!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Contents

- [Contribute via Git](#contribute-via-git)
- [I want to suggest a change](#i-want-to-suggest-a-change)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Contribute via Git

Use the standard open source fork-and-pull-request model.

- Fork this repository to your GitHub account.
- Clone your fork locally and create a feature branch.
  - Example branch name: `add-new-evolution-resource`.
- Make your changes.
  - Add a new section if needed.
  - Add a section description.
  - If the content has special access requirements, mention it in bullet points under the entry.
  - Follow this entry format: `- **[resource-name](http://example.com/)** - A short description ends with a dot.`
- Check for duplicates by searching existing entries and discussions.
- Review your edits.
  - Check spelling and grammar.
  - Make sure your text editor removes trailing whitespace.
- Commit and push your branch to your fork.
- Open a Pull Request from your fork branch to this repository.
- In the Pull Request description, add a short explanation of why the project/resource/tool is awesome.

Copy-paste Git commands (replace placeholders):

```bash
# 1) Clone your fork (replace YOUR-USERNAME)
git clone https://github.com/YOUR-USERNAME/awesome-evolution.git
cd awesome-evolution

# 2) Add upstream remote
git remote add upstream https://github.com/timtyler/awesome-evolution.git

# 3) Create a branch for your change
git checkout -b add-new-evolution-resource

# 4) Edit files, then stage and commit
git add README.md CONTRIBUTING.md
git commit -m "Add resource: resource-name"

# 5) Push your branch to your fork
git push -u origin add-new-evolution-resource

# 6) Keep your fork branch up to date (run before new work)
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

Helpful GitHub guides:

- [Fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
- [Creating a pull request from a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

## I want to suggest a change

If you are not ready to open a Pull Request, suggest changes through a GitHub Discussion.

- Open a new Discussion topic in this repository.
- Use a clear title, for example: `Suggestion: Add [resource-name] to [section-name]`.
- Include:
  - What should be added, removed, or revised.
  - Why it belongs in this awesome list.
  - Relevant links and references.
  - Optional draft entry using this format: `- **[resource-name](http://example.com/)** - A short description ends with a dot.`
- If maintainers agree, you can follow up with a Pull Request or request help from another contributor.

Helpful GitHub guide:

- [About discussions](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions)