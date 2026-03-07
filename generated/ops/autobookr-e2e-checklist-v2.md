# AutoBookr E2E Checklist v2

**Flow:** Missed Call → SMS → Stripe Checkout → Active Subscription

Strict pass/fail steps for verifying the complete no-wait conversion flow.

---

## 1. Missed Call Detection

| Step | Action | Pass Criteria | Fail Criteria |
|------|--------|---------------|---------------|
| 1.1 | External caller dials AutoBookr number (`+447700900000`) | Call connects | Line busy / not found |
| 1.2 | Call ends (no answer / busy / completed) | `CallStatus: completed` received at webhook | No webhook call |
| 1.3 | Call logged to DB | `logMissedCall` writes to `missed_calls` table | In-memory fallback only |
| 1.4 | A/B variant assigned | Variant logged (`control` or `a`/`b`) | No variant field |

---

## 2. SMS Trigger

| Step | Action | Pass Criteria | Fail Criteria |
|------|--------|---------------|---------------|
| 2.1 | Auto-reply SMS composed | Message body present | Empty/null |
| 2.2 | SMS sent via Twilio | `twilioClient.messages.create()` returns `MessageSid` | Twilio API error |
| 2.3 | SMS delivery confirmed | Status: `sent` / `delivered` | Status: `failed` / `undelivered` |
| 2.4 | SMS logged to DB | `logSmsDelivery` writes to `sms_log` table | DB write fails |

**SMS Retry Logic:** 3 attempts with exponential backoff (1s, 5s, 15s) → dead letter queue

---

## 3. Customer Response (Optional)

| Step | Action | Pass Criteria | Fail Criteria |
|------|--------|---------------|---------------|
| 3.1 | Customer replies to SMS | Inbound SMS webhook receives `Body` + `From` | No inbound webhook |
| 3.2 | Reply logged | Status: `replied` in dashboard | Not captured |

---

## 4. Stripe Checkout

| Step | Action | Pass Criteria | Fail Criteria |
|------|--------|---------------|---------------|
| 4.1 | Checkout initiated | `/api/checkout` returns `url` | 500 error / no URL |
| 4.2 | Customer on Stripe hosted page | Redirects to `checkout.stripe.com` | Wrong URL |
| 4.3 | Customer completes payment | `checkout.session.completed` event received | Payment abandoned |
| 4.4 | Customer enters email | Valid email captured in session | Guest checkout (no email) |

**Plans:**
- `starter` → £19/mo → `price_1T4j9PC5NyZYaa6HedL5ABxa`
- `growth` → £49/mo → `price_1T4jAyC5NyZYaa6HSP1sEKsX`
- `pro` → £99/mo → `price_1T4jE8C5NyZYaa6Hfq9TL8te`

---

## 5. Subscription Activation

| Step | Action | Pass Criteria | Fail Criteria |
|------|--------|---------------|---------------|
| 5.1 | `customer.subscription.created` received | Stripe webhook fires | Not received |
| 5.2 | Subscription `status: active` | `stripe.subscriptions.retrieve()` returns active | `past_due` / `canceled` |
| 5.3 | First invoice paid | `invoice.paid` event received | No payment |
| 5.4 | Customer dashboard accessible | `/api/dashboard` returns data with valid JWT | 401 unauthorized |

---

## 6. Post-Purchase Flow

| Step | Action | Pass Criteria | Fail Criteria |
|------|--------|---------------|---------------|
| 6.1 | Success redirect | `STRIPE_SUCCESS_URL` loads | 404 / error page |
| 6.2 | Customer can log in | `/api/auth/login` returns JWT | 400 / 500 |
| 6.3 | Dashboard shows subscription | Stats include `subscriptionId`, `plan` | Missing data |

---

## End-to-End Pass Criteria

**ALL steps must pass (1.1 → 6.3)** for a complete conversion.

| Metric | Target |
|--------|--------|
| SMS delivery rate | >95% |
| Checkout completion rate | >60% |
| Subscription activation | 100% of completed checkouts |
| Dashboard accessible | 100% of active subscriptions |

---

## Debug Commands

```bash
# Check missed calls
curl http://localhost:3000/api/dashboard -H "Authorization: Bearer <token>"

# Check Stripe subscription
stripe subscriptions list --email=<email>

# View dead letter queue
# (internal API - check source)

# Test SMS manually
curl -X POST http://localhost:3000/webhooks/twilio/call \
  -d "CallStatus=completed&From=+447700900001&To=+447700900000&CallSid=CAtest123"
```
