# MEMORY.md

## 2026-02-23

- **Ship-check CI mode**: `scripts/ship-check.sh` now supports `--non-interactive` / `--auto-pass` flags for automated/CI runs (found via acceptance-domain dry run).
- 8-stage project closeout workflow complete; moved to first project sprint execution.
- Wayne prefers morning readiness summaries via Telegram.

## 2026-02-24

- **Wayne execution pattern**: Phased delivery with explicit sign-off confirmation in writing (chat screenshot/file), then immediate artifact update. Efficient for external dependency unblocking.
- **Cron optimization**: Routine cron jobs switched to `openrouter/minimax/minimax-m2.5` to reduce OpenAI token burn.

## 2026-02-25

- **Mobile-first execution style**: Wayne often works from phone; best results come from one-step-at-a-time instructions with exact taps.
- **Signal quality preference**: Wayne does not want repetitive/noisy status pings; prefers only relevant updates (changes, blockers, needed actions).
- **AutoBookr pricing locked**: 3 paid tiers selected — Starter £19/mo, Growth £49/mo, Pro £99/mo.
- **AutoBookr setup progress**: Twilio test number and Stripe test products/webhooks configured; backend mapping updated.

## 2026-02-27

- **Root cause found - Memory bug**: I was NOT loading SESSION_START.md + memory files at session start. This caused "amnesia" - I had no continuity between sessions.
- **Fixed**: Cron jobs disabled (dashboard-backup, autobookr-e2e, brain-regions, revenue-business)
- **Mobile dashboard published**: https://lil-ai-operator.github.io/mobile-dashboard/
- **AutoBookr landing published**: https://lil-ai-operator.github.io/autobookr-landing/
- **Brave API key added**: Now have web search capability
- **Root cause - Stale cron validation**: The cron job kept saying "needs Wayne to publish" because it only checked LOCAL files, not the live GitHub Pages URL. Never detected the publish action.

## 2026-02-28

- **Memory features added**: Created scripts for quick capture, decisions, todos, and context recall (`memory-capture.sh`, `memory-decision.sh`, `memory-todo.sh`, `memory-context.sh`). Added `memory/PEOPLE.md` for people & preferences.
- **Qwen subagent crash root cause**: Qwen 3.5 via OpenRouter (`openrouter/qwen/qwen3.5-plus-02-15`) is unstable when used for subagent spawning - causes crashes. Marked as AVOID in BURN_GUARDRAILS.md, COMMAND_PACK.md, AGENT_UPGRADE_MASTER_PLAN.md.
- **Revenue runner automated**: Built `scripts/run-revenue-day.py` with seeded decorator lead pool + automated 5-lead outreach queue generation.

## 2026-03-02 (Weekly Curated)

- **Published landing pages**: Mobile dashboard and AutoBookr landing both live on GitHub Pages
- **Brain regions architecture documented**: Full routing logic, JSON handoff contracts between regions, cost caps per region, auto-escalation rules
- **Revenue assets complete**: LEADS.md, TRACKER.md, OUTREACH_CALENDAR.md, INDUSTRY_TEMPLATES.md, FIRST_10_BATCH.md all created
- **Business rebuild assets**: SUBAGENT_WORKFLOWS.md, EXPERIMENT_BACKLOG.md, SALES_SCRIPT.md, DAILY_MOMENTUM_PROTOCOL.md, WEEKLY_SCORECARD.md
- **AutoBookr auth live**: JWT-based auth implemented, dashboard protected with Bearer token
- **Backup prep complete**: rclone + GPG installed, scripts validated, ready for OAuth flow
- **Ongoing blockers**: 
  - Backup needs Google Drive OAuth + passphrase
  - Revenue outreach needs Wayne to send (2/10 done)
- **Key lesson**: Always validate against LIVE URLs, not local files (fixed stale cron issue)
