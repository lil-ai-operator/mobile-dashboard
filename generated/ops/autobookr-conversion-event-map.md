# AutoBookr Conversion Event Map

Mapping of all CTA, tier, and checkout events with naming conventions and payload fields.

---

## Event Naming Convention

**Format:** `{service}.{resource}.{action}`

| Component | Values |
|-----------|--------|
| `service` | `twilio`, `stripe`, `autobookr` |
| `resource` | `call`, `sms`, `checkout`, `subscription`, `customer` |
| `action` | `received`, `sent`, `completed`, `failed`, `created`, `updated`, `deleted` |

**Example:** `twilio.call.missed`, `stripe.checkout.completed`

---

## Twilio Events

### Inbound Call

**Webhook:** `POST /webhooks/twilio/call`

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| `CallSid` | string | Twilio | Unique call ID |
| `CallStatus` | string | Twilio | `completed`, `no-answer`, `busy` |
| `From` | string | Twilio | Caller's phone number |
| `To` | Twilio | Business phone number | |

**Event:** `twilio.call.received` (on `CallStatus === 'completed'`)

### SMS Sent

**Internal:** `sendSMS()` in `services/twilio.ts`

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| `MessageSid` | string | Twilio | Unique message ID |
| `to` | string | Request | Recipient phone |
| `from` | string | Config | Business Twilio number |
| `body` | string | Request | Message content |
| `status` | string | Twilio Response | `sent`, `delivered`, `failed` |

**Event:** `twilio.sms.sent` / `twilio.sms.delivered` / `twilio.sms.failed`

### SMS Received (Reply)

**Webhook:** `POST /webhooks/twilio/sms`

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| `MessageSid` | string | Twilio | Unique message ID |
| `From` | string | Twilio | Replier's phone number |
| `To` | string | Twilio | Business number |
| `Body` | string | Twilio | Reply content |

**Event:** `twilio.sms.received`

---

## Stripe Events

### Checkout Session Created

**API:** `POST /api/checkout`

**Request Payload:**
```json
{
  "priceId": "price_1T4jAyC5NyZYaa6HSP1sEKsX",
  "customerEmail": "customer@example.com"
}
```

**Response:**
```json
{
  "url": "https://checkout.stripe.com/..."
}
```

**Event:** `stripe.checkout.created`

### Checkout Completed

**Webhook:** `POST /webhooks/stripe`

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| `id` | string | Stripe | Session ID (`cs_...`) |
| `payment_status` | string | Stripe | `paid`, `unpaid` |
| `customer_email` | string | Stripe | Customer email |
| `subscription` | string | Stripe | Subscription ID (`sub_...`) |
| `metadata.plan` | string | Stripe | Price ID |

**Event:** `stripe.checkout.completed`

### Subscription Created

**Webhook:** `POST /webhooks/stripe`

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| `id` | string | Stripe | Subscription ID (`sub_...`) |
| `customer` | string | Stripe | Customer ID (`cus_...`) |
| `status` | string | Stripe | `active`, `past_due`, `canceled`, `trialing` |
| `current_period_start` | int | Stripe | Unix timestamp |
| `current_period_end` | int | Stripe | Unix timestamp |
| `items.data.price.id` | string | Stripe | Price ID |

**Event:** `stripe.subscription.created`

### Subscription Updated

**Event:** `stripe.subscription.updated`

### Subscription Deleted

**Event:** `stripe.subscription.deleted`

### Invoice Paid

**Webhook:** `POST /webhooks/stripe`

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| `id` | string | Stripe | Invoice ID (`in_...`) |
| `customer` | string | Stripe | Customer ID |
| `subscription` | string | Stripe | Subscription ID |
| `amount_paid` | int | Stripe | Amount in pence |
| `status` | string | Stripe | `paid`, `open`, `void` |

**Event:** `stripe.invoice.paid`

---

## AutoBookr Internal Events

### Missed Call Logged

**Function:** `logMissedCall()` in `services/twilio.ts`

| Field | Type | Source | Description |
|-------|------|--------|-------------|
| `callSid` | string | Twilio | Call ID |
| `callerNumber` | string | Request | Caller phone |
| `calledNumber` | string | Request | Business number |
| `status` | string | Twilio | `no-answer`, `busy`, `failed` |
| `variantId` | string | A/B Logic | `control`, `a`, `b` |
| `timestamp` | datetime | Auto | UTC timestamp |

**Event:** `autobookr.call.missed`

### Customer Onboarded

**API:** `POST /api/onboarding`

**Request Payload:**
```json
{
  "name": "John Doe",
  "trade": "Plumber",
  "phone": "+447700900000",
  "area": "London"
}
```

**Event:** `autobookr.customer.onboarded`

### Customer Logged In

**API:** `POST /api/auth/login`

**Request:**
```json
{
  "phoneNumber": "+447700900000",
  "customerId": "cus_xxx"
}
```

**Response:**
```json
{
  "token": "eyJ...",
  "expiresIn": "7d"
}
```

**Event:** `autobookr.auth.login`

---

## Pricing Tiers

| Tier | Price ID | Amount | Interval | Price ID (Env Var) |
|------|----------|--------|----------|-------------------|
| Starter | `price_1T4j9PC5NyZYaa6HedL5ABxa` | £19 | Monthly | `STRIPE_PRICE_STARTER` |
| Growth | `price_1T4jAyC5NyZYaa6HSP1sEKsX` | £49 | Monthly | `STRIPE_PRICE_GROWTH` |
| Pro | `price_1T4jE8C5NyZYaa6Hfq9TL8te` | £99 | Monthly | `STRIPE_PRICE_PRO` |

---

## Conversion Funnel Events

| Funnel Stage | Event | Key Metrics |
|--------------|-------|-------------|
| Lead In | `twilio.call.received` | Call volume |
| Lead Engaged | `twilio.sms.sent` | SMS delivery rate |
| Lead Responded | `twilio.sms.received` | Response rate |
| Checkout Started | `stripe.checkout.created` | Checkout initiation rate |
| Payment Completed | `stripe.checkout.completed` | Conversion rate |
| Subscription Active | `stripe.subscription.created` | MRR |
| Renewed | `stripe.invoice.paid` | Retention rate |

---

## Webhook Endpoints

| Service | Endpoint | Raw Body |
|---------|----------|----------|
| Twilio Call | `POST /webhooks/twilio/call` | Form URL-encoded |
| Twilio SMS | `POST /webhooks/twilio/sms` | Form URL-encoded |
| Stripe | `POST /webhooks/stripe` | `application/json` (raw) |

**Note:** Stripe webhook requires `express.raw({ type: 'application/json' })` middleware for signature verification.
