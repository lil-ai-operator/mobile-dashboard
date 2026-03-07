# AutoBookr Customer Portal MVP Specification

## Overview
Self-service portal for AutoBookr customers to manage their account, SMS templates, and view activity.

---

## User Stories

1. **As a tradesperson**, I want to log in so I can access my dashboard securely
2. **As a tradesperson**, I want to edit my SMS auto-reply template so customers get the right message
3. **As a tradesperson**, I want to set my business hours so I only get notifications when open
4. **As a tradesperson**, I want to see my plan and billing status so I know what I'm paying for
5. **As a tradesperson**, I want to view my missed calls and SMS activity so I can follow up on leads
6. **As a tradesperson**, I want to change my notification number so texts go to my mobile

---

## Screens & Features

### 1. Login Screen
- Email input
- Password input
- "Forgot password?" link
- "Sign in" button
- Background: branded gradient

### 2. Dashboard (Home)
- **Header**: Welcome message + current plan badge
- **Stats cards**:
  - Total missed calls (this month)
  - SMS sent (this month)
  - Active leads
- **Recent activity feed**: Last 5 missed calls/SMS
- **Quick actions**: Edit template, View all activity

### 3. Settings - Business Profile
- Business name (text)
- Trade type (dropdown: Plumbing, Electrical, Building, etc.)
- Service area (text - e.g., "Manchester & Surrounding")
- Notification phone number (tel - where SMS replies go)

### 4. Settings - SMS Template
- Preview of incoming SMS to customer
- Editable template text (with variable placeholders)
- Variables available: `{customer_name}`, `{business_name}`, `{our_number}`
- "Test template" button - sends test SMS to your number
- Character count / SMS length indicator

### 5. Settings - Business Hours
- Day-by-day toggle: Open/Closed
- If open: Start time + End time (time pickers)
- Timezone display (auto-set to UK)
- Preview: "We'll only send notifications during your open hours"

### 6. Billing & Plan
- Current plan display (Starter/Growth/Pro)
- Price per month
- Features included (checklist)
- "Change plan" button → Stripe checkout
- Payment method on file (last 4 digits)
- Next billing date
- "Cancel subscription" link (with confirmation)

### 7. Activity Log
- Table view: Date | Time | Customer Phone | SMS Sent | Reply
- Filters: Date range, Has reply / No reply
- Pagination: 20 per page
- Export to CSV button

---

## Technical Implementation

### Authentication
- JWT-based auth (already implemented in auth.ts)
- Token stored in localStorage
- Auto-logout after 30 days inactivity
- Refresh token flow

### API Endpoints Needed

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/login | Authenticate user |
| GET | /api/user/profile | Get user profile |
| PUT | /api/user/profile | Update business profile |
| GET | /api/user/sms-template | Get current SMS template |
| PUT | /api/user/sms-template | Update SMS template |
| POST | /api/user/test-sms | Send test SMS |
| GET | /api/user/business-hours | Get hours config |
| PUT | /api/user/business-hours | Update hours |
| GET | /api/user/plan | Get current plan info |
| GET | /api/user/activity | Get activity log |

### Database Schema (Supabase)

```sql
-- users table (extends auth)
profiles:
  - id (uuid, FK to auth.users)
  - email (text)
  - business_name (text)
  - trade_type (text)
  - service_area (text)
  - notification_phone (text)
  - sms_template (text)
  - business_hours (jsonb)
  - plan_id (text)
  - stripe_customer_id (text)
  - created_at (timestamp)

activity_log:
  - id (uuid)
  - user_id (uuid, FK to profiles)
  - caller_phone (text)
  - sms_sent (boolean)
  - sms_content (text)
  - customer_reply (text)
  - created_at (timestamp)
```

---

## UI/UX Guidelines

### Layout
- Sidebar navigation (left, 240px wide)
- Main content area (right)
- Mobile: Hamburger menu, full-width content

### Colors (use brand kit)
- Sidebar: Surface color (#1E293B)
- Active nav item: Primary blue (#1E40AF)
- Buttons: Primary blue
- Success states: Secondary green (#22C55E)
- Error states: Red (#EF4444)

### Components
- Cards with subtle shadow (0 4px 6px rgba(0,0,0,0.1))
- Input fields: Full-width, 48px height, rounded 8px
- Buttons: 48px height, rounded 8px, bold text
- Tables: Striped rows, sticky header
- Toast notifications: Bottom-right corner

---

## Build Priority

### Phase 1 (MVP - Launch)
1. Login screen
2. Dashboard with stats
3. Business profile edit
4. SMS template edit
5. Activity log view

### Phase 2 (After first 5 customers)
1. Business hours
2. Billing/plan display
3. Change plan flow

### Phase 3 (Growth)
1. Real-time SMS notifications (WebSocket)
2. Export activity to CSV
3. Multi-user accounts (team members)

---

## Success Metrics

- [ ] Customer can log in and see dashboard
- [ ] Customer can edit SMS template and it sends correctly
- [ ] Customer can change notification phone number
- [ ] Activity log shows real missed call data
- [ ] Plan and billing info is accurate

---

*Specification created: 2026-03-04*
