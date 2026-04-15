"""Hardcoded-credential test cases. All values are inert documentation examples."""

# CASE: plain hardcoded API key — must be flagged CRITICAL
ANTHROPIC_API_KEY = "sk-ant-api03-0000000000000000000000000000000000000000000000000000000000000000"

# CASE: AWS access key (canonical AWS docs example) — must be flagged CRITICAL
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"

# CASE: valid inline suppression — must NOT be flagged
GITHUB_PAT = "ghp_000000000000000000000000000000000000"  # claude-ignore: test fixture - inert placeholder for scanner regression suite

# CASE: invalid suppression (no reason given) — must STILL be flagged CRITICAL
SLACK_TOKEN = "xoxb-0000000000xx-000000000000-000000000000000000000000"  # claude-ignore
