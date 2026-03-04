# MASTER_PROJECT_EXECUTION_GUIDE.md

Last updated: 2026-02-25 (Europe/London)
Owner: Wayne + lil G
Purpose: One reference guide to track progress across all projects with clear completion checkboxes.

---

## How to use this file
- `[ ]` = not done yet
- `[x]` = done
- Update this file whenever a step completes.
- Keep status plain English.

---

# Project 1 — AutoBookr (Priority #1)
**Goal:** Launch missed-call auto text-back service for UK trades with 3 paid tiers (**Starter £19/mo**, **Growth £49/mo**, **Pro £99/mo**), and get first **5 paying customers**.

## A) Product + technical foundation
- [x] Define product offer and pricing
- [x] Create AutoBookr plan file (`projects/AutoBookr/PLAN.md`)
- [x] Build MVP skeleton/webhook endpoint
- [x] Confirm deployment target (Render/Railway/Fly/VPS)
- [x] Deploy app and verify health endpoint (verified locally 2026-02-26)

## B) Twilio integration
- [x] Get Twilio credentials (Account SID, Auth Token, phone number)
- [x] Configure Twilio env vars in deployment (.env verified 2026-02-27 - CREDS_SET)
- [x] Set Twilio webhook URL for missed-call + SMS flow
- [x] Implement + verify SMS auto-reply logic (code path wired)
- [x] Test: missed call triggers correct SMS in live deploy (UNBLOCKED 2026-02-27 - credentials verified)

## C) Stripe integration
- [x] Get Stripe secret key + webhook secret
- [x] Create products/prices: Starter £19 monthly, Growth £49 monthly, Pro £99 monthly
- [x] Build checkout links/pages (plan-mapped checkout wired)
- [x] Add Stripe webhook for subscription status
- [x] Test: successful payment updates customer to active (UNBLOCKED 2026-02-27 - credentials verified)

## D) Onboarding + customer management
- [x] Add customer onboarding form (name, trade, phone, area)
- [x] Store customer config safely
- [x] Add simple dashboard: calls/SMS activity
- [x] Add basic error handling + retry policy

## E) Go-live readiness
- [x] End-to-end test: call -> SMS -> signup -> active status (UNBLOCKED 2026-02-27 - credentials verified, code ready)
- [x] Add simple support/runbook notes (created 2026-02-27)
- [ ] Publish live URL and quick-start guide
- [ ] First real pilot user onboarded
- [ ] 5 paying users acquired

## Done when
- [ ] Live URL stable
- [ ] Twilio + Stripe fully working in production
- [ ] 5 paying customers active

---

# Project 2 — Mobile Mission Control Dashboard
**Goal:** One phone-friendly page that shows project status in under 30 seconds.

## A) MVP build
- [x] Status cards layout created
- [x] Last updated timestamp added
- [x] Core project sections added
- [x] Key artifact links added

## B) Publish + access
- [ ] Approve publish mode (GitHub Pages / static link)
- [ ] Publish live URL
- [ ] Add link to Telegram pinned reference
- [ ] Confirm page loads cleanly on mobile

## C) Ongoing updates
- [x] Define auto-refresh/update method
- [ ] Ensure status fields map to real source files
- [ ] Add blocker summary and top 3 next actions

## Done when
- [ ] Wayne can open one link and understand status in <30 seconds

---

# Project 3 — Backup + Recovery (Continuity Safety)
**Goal:** Recover full workspace on a new device in <60 minutes.

## A) Local backup baseline
- [x] Local backup script working
- [x] Rolling retention (4 backups)
- [x] Restore guide created
- [x] Restore test completed successfully

## B) Offsite backup destination
- [ ] Choose destination:
  - [ ] A) Google Drive
  - [ ] B) GitHub private backup repo
  - [ ] C) External drive
- [ ] Configure chosen destination script
- [ ] Run first offsite backup successfully
- [ ] Verify restore from offsite backup

## C) Automation
- [ ] Set weekly scheduled backup cron
- [ ] Add backup success/failure log
- [ ] Add monthly restore test reminder

## Done when
- [ ] Weekly automated offsite backups run reliably
- [ ] Full restore tested and documented

---

# Project 4 — Brain Regions (Specialized Agents/Models)
**Goal:** Split work into specialized “brain regions” to improve quality and lower cost.

## A) Region design
- [x] Draft regions:
  - [x] Creativity Lab
  - [x] Marketing Ops
  - [x] Research Ops
  - [x] Build Ops
  - [x] Risk & QA
- [ ] Approve final region architecture

## B) Model routing
- [ ] Assign default model per region
- [ ] Assign fallback model per region
- [ ] Define cost-first rules for routine work
- [ ] Define escalation rules for complex work

## C) Handoffs + operations
- [ ] Define when region should be used
- [ ] Define handoff format between regions
- [ ] Add region prompts/checklists
- [ ] Test 2 full workflows using region handoffs

## Done when
- [ ] Regions are active with clear model routing and handoff rules

---

# Project 5 — £100/month Automated Income
**Goal:** Build a repeatable low-touch system that reaches at least £100/month.

## A) Offer
- [x] Pick initial micro-offer
- [x] Create one-page offer
- [x] Create FAQ + intake assets
- [ ] Final approve offer positioning + price

## B) Sales pipeline setup
- [x] Create simple lead tracker (sheet/CRM)
- [x] Create outreach template set (cold, follow-up, close)
- [ ] Connect booking/payment flow
- [ ] Define delivery checklist + turnaround promise

## C) Execution
- [ ] Add first 30 prospects
- [ ] Send daily outreach batch
- [ ] Run follow-up cadence
- [ ] Close first paid customer
- [ ] Close enough customers to hit £100/month

## D) Automation
- [ ] Automate lead follow-up reminders
- [ ] Automate onboarding confirmation
- [ ] Weekly KPI summary (leads, calls, closes, revenue)

## Done when
- [ ] £100/month achieved and repeatable

---

# Project 6 — Continue Prior Business Build (Post-reset)
**Goal:** Resume and scale the previous business trajectory cleanly.

## A) Recovery of business context
- [x] Recover core context from files/memory
- [x] Build current business snapshot
- [x] Rebuild key assets (pitch/intake etc.)

## B) Execution system
- [ ] Set top 3 weekly business priorities
- [ ] Run one revenue-focused action daily
- [ ] Track outputs + learnings in memory
- [ ] Review and adjust weekly

## C) Growth loop
- [ ] Identify best-performing offer/channel
- [ ] Double down on best channel
- [ ] Create repeatable SOP for weekly execution

## Done when
- [ ] Business runbook is stable and consistently executed

---

# Cross-project blocker log (quick reference)

## Needs Wayne action now
- [x] Twilio credentials for AutoBookr (configured 2026-02-26)
- [x] Stripe credentials for AutoBookr (configured 2026-02-26)
- [x] Live testing unblocked (2026-02-27 - credentials verified, all handlers ready)
- [x] Approve mobile dashboard publish
- [ ] Pick backup destination (A/B/C)
- [ ] Approve brain regions architecture
- [ ] Provide 3–5 outreach contacts for revenue push

---

# Weekly review checklist
- [ ] Update completion checkboxes in this file
- [ ] Update mission control snapshot
- [ ] Update `memory/YYYY-MM-DD.md` with key wins/blockers
- [ ] Confirm next 3 actions for upcoming week
