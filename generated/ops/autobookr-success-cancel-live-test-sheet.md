# AutoBookr Success/Cancel Live Test Sheet

## Objective
Verify Stripe checkout returns correctly to `/success` and `/cancel` in live flow.

## Test matrix
1. Starter plan -> complete payment -> expect `/success` page
2. Growth plan -> cancel at Stripe -> expect `/cancel` page
3. Pro plan -> complete payment -> expect `/success` page

## Pass/Fail criteria
- PASS: route loads with no 404, clear message shown, session completes.
- FAIL: 404, blank page, wrong route, or broken redirect.

## Evidence to capture
- Screenshot of URL + page content for each case.
- Timestamp and plan used.

## Notes
- Run in private tab once to avoid cache.
- If fail: capture exact URL path and send to fix queue.
