# Profile assets

The banner is the supplied final artwork, preserved at its original 2172 × 724 resolution. Replace `assets/banner.png` with another PNG to change it. Keep the filename; the README needs no edit. Use an approximately 3:1 horizontal composition.

`tools/profile_assets.py` generates `assets/stats.svg` and `assets/featured-dataflow.svg` using only Python 3.12's standard library. SVGs contain inline shapes and text, with no scripts, external fonts or embedded HTML. The DataFlow chart is decorative and labelled as illustrative.

## Generate locally

Run from the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 tools/profile_assets.py --featured-only
```

For live statistics, set `GH_TOKEN` or `GITHUB_TOKEN` securely in your environment, then run `python3 tools/profile_assets.py`. Never put a token in a file or command argument. With an already authenticated GitHub CLI, no token copying is necessary:

```sh
python3 -c 'import sys; sys.path.insert(0, "tools"); from profile_assets import QUERY; print(QUERY)' > /tmp/profile-query.graphql
gh api graphql -F query=@/tmp/profile-query.graphql -f login=BarujaFe1 | python3 tools/profile_assets.py --input -
```

`--input path/to/response.json` also accepts a saved GraphQL response. Given the same input, output is byte-identical. Incomplete responses, API failures, mismatched accounts and invalid counts fail without replacing either card. There is no fabricated fallback or zero-filled error state.

## Automation

`profile-assets.yml` refreshes the cards each Monday at 09:23 UTC (06:23 São Paulo) and supports **Run workflow** on a selected branch. Scheduling starts after merge to the default branch. Only the two generated SVGs are staged, and a commit is made only if they changed. Concurrent branch changes cause a normal push rejection; nothing is force-pushed. The refresh has no push trigger, so asset commits cannot create a refresh loop.

The default `GITHUB_TOKEN` reads the API and commits cards with `contents: write`. An optional `PROFILE_STATS_TOKEN` secret can provide different read visibility; it is never used to push. No extra secret is required by the implementation. Do not add a more privileged token to bypass branch protection. If branch rules reject bot pushes, maintainers must choose an approved update process.

Statistics use GitHub's default annual contribution window and the visibility of the API token. Dates on the card are UTC. Commit/PR/issue/review counts are contribution categories, not a sum guaranteed to match the calendar total. These are activity signals, not productivity or code quality scores. The card records its date window and stays at its last successful snapshot if a later run fails; failures remain visible in Actions.

`validate.yml` runs deterministic tests on PRs and relevant pushes with read-only permissions. Tests use synthetic fixtures and never call the network. On trusted pushes, a separate step also generates cards in the runner's temporary directory using the default token to verify live API access. This does not commit assets or prove that the scheduled job has executed or that the production demo's full feature set works.

The previous README is preserved losslessly in `docs/archive/README-legacy.md.gz`. Read it with `gzip -dc docs/archive/README-legacy.md.gz`.

References: [GitHub token authentication](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token), [GraphQL reference](https://docs.github.com/en/graphql/reference).
