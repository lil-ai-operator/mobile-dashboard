# PROJECTS_BACKLOG_WAYNE.md

Last updated: 2026-02-25 (Europe/London)
Owner: Wayne + lil G

## How to read this
- **Now** = we can start immediately
- **Next** = planned after current item
- **Later** = queued

---

## 0) AutoBookr launch track (Now - priority)
**Goal (plain English):** Launch AutoBookr (missed call → auto text-back) and start first revenue.

### Core targets
- [x] Pricing model locked: 3 paid tiers (Starter £19/mo, Growth £49/mo, Pro £99/mo)
- [ ] Offer live with 3 paid tiers
- [ ] Twilio connected for missed-call + SMS
- [ ] Stripe connected for payments
- [ ] First 5 paying customers

### Next actions
- [x] Deploy MVP endpoint/app ⭐ DONE 2026-02-25
- [x] Configure Twilio test number + webhook routes
- [x] Create Stripe products/prices (Starter/Growth/Pro) + webhook destination
- [x] Wire backend routes for `/api/twilio/*`, `/api/stripe/webhook`, and plan-based checkout mapping
- [x] Create deployment guide (Render/Railway/Fly options) ⭐ DONE 2026-02-25 22:15
- [ ] Run end-to-end test: missed call -> SMS -> paid signup

### Working file
- `projects/AutoBookr/PLAN.md`

---

## 1) Build execution pack for current project (Now)
**Goal (plain English):** Start real product build work in clear steps and keep Wayne updated simply.

### Tasks
- [x] NS-001: Define notification data structure (what data we store, and where)
- [x] NS-002: Set up message pipeline (Redis pub/sub)
- [x] NS-003: Build service skeleton
- [x] NS-005: Build core API endpoints
- [x] NS-004: Security sign-off ✅ (Wayne approved)
- [x] NS-006: User Preference API
- [x] NS-007: Webhook Payload Schema
- [x] NS-008: Database Migration (PostgreSQL 16)
- [x] NS-009: WebSocket Server
- [x] NS-010: Notification Delivery Queue

### Done when
- [x] NS-001 + NS-002 done and documented
- [x] Checkpoint quality pass is green
- [x] Update sent to Wayne in plain English
- ✅ **PHASE 1 COMPLETE - All 10 tasks done!**

---

## 2) Mobile Mission Control dashboard (Now)
**Goal (plain English):** A phone-friendly status page Wayne can open anytime.

### MVP scope
- [x] Single page status (Done / In progress / Blockers / Next)
- [x] Last update timestamp
- [x] Project health cards
- [x] Links to key artifacts (mission-control.md, sprint folder, reports)

### Delivery options
- [x] Publish prep artifacts created (GitHub Actions workflow + local serve script + checklist)
- [x] Option A approved by Wayne (GitHub Pages/simple publish)
- [ ] Option B: Notion-style dashboard (easy editing)
- [x] Option C: Static page in repo + Telegram quick link ✅ MVP DONE

### Done when
- [ ] Wayne can open one link on phone and understand status in under 30 seconds
- ⏳ In progress: approval received; publish live link next.

---

## 3) Full backup + recovery plan (Now)
**Goal (plain English):** If Mac breaks, restore lil G/workspace quickly on another device.

### Backup plan
- [x] Weekly encrypted backup archive of workspace + config exports
- [x] Keep 4 rolling weekly backups (backup-simple.sh)
- [x] Write step-by-step restore guide (RESTORE_GUIDE.md)
- [x] ✅ LOCAL BACKUP WORKING - 53MB tested and verified!
- [x] Option A prep complete (Google Drive script hardened + readiness checker + env template)
- [ ] Upload to Google Drive (needs Wayne to pick destination)
- [ ] OR: Upload to GitHub private repo (needs Wayne repo URL)
- [ ] OR: External drive backup (needs Wayne mount point)

### Restore target
- [x] New device can restore to working state in <60 minutes ✅ TESTED

### Status
- ⚠️ **BLOCKED: Waiting for Wayne to pick A/B/C destination**

---

## 4) Brain regions via specialized agents/models (Next)
**Goal (plain English):** Use focused "sub-brains" for different tasks to improve quality and reduce cost.

### Proposed regions
- [x] Creativity Lab (ideation, naming, concepts)
- [x] Marketing Ops (offers, copy, funnel tasks)
- [x] Research Ops (fact finding, competitor scan)
- [x] Build Ops (execution plans, implementation checklists)
- [x] Risk & QA (ship-check and safety gates)

### Done when
- [ ] Each region has a clear role, model preference, and handoff rules
- ⚠️ **BLOCKED: Need Wayne approval on architecture**

---

## 5) Build to £100/month mostly automated (Next)
**Goal (plain English):** Launch a simple income system with minimum manual work.

### Initial strategy (practical)
- [x] Pick 1 micro-offer we can deliver fast (AI Workflow Automation Pack)
- [x] Create 1-page offer + payment link + intake form
- [x] Build delivery checklist template
- [x] Create outreach template pack (cold + follow-up + close + runbook + tracker)
- [ ] Set light outreach + follow-up automation (needs Wayne contacts)
- [ ] Weekly KPI review (leads, closes, £)

### Done when
- [ ] First paid customer closed
- [ ] Repeatable flow documented
- [ ] £100/month baseline reached
- ⚠️ **BLOCKED: Need Wayne to approve offer + provide outreach contacts**

---

## 6) Continue previous business build (Next)
**Goal (plain English):** Reconstruct where we left off before reset/reinstall and continue cleanly.

### Tasks
- [x] Rebuild business context from memory/docs/repo
- [x] Create current business state snapshot
- [x] Re-prioritize top 3 revenue actions
- [ ] Execute one action per day (needs Wayne outreach contacts)

### Status
- ✅ Pitch deck + intake form created
- ⚠️ **BLOCKED: Need Wayne to provide 3-5 outreach contacts**

---

## Operating rules for all projects
- Keep updates plain English first
- Keep costs low by default (cheap models for routine work)
- Send Wayne concise updates: what changed, what's next, any blocker
- Write key decisions to memory files

---

## Tomorrow morning recommended start order
1. Project execution pack (NS-001 + NS-002)
2. Mobile mission control MVP link
3. Backup/recovery automation draft
4. £100/month micro-offer selection
