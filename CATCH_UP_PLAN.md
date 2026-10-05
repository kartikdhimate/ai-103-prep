# Catch-Up Plan

Rule: protect the **weighted core** (Foundry + models, RAG, agents, safety, observability) and the final review. Cut Optional first, then compress vision generation and speech, never the capstone spine.
Do not try to "double up" two days in one evening; that is how both stick poorly. Use the weekend buffer instead.

## Priority tiers

| Tier | Content | Cut order |
|---|---|---|
| P1 never cut | Days 2, 3, 5, 6, 7, 8, 9, 11, 12, 19, 20 | last |
| P2 compress | Days 4, 10, 13, 14, 16, 17, 18 | compress first, then cut Optional parts |
| P3 first to shrink | Day 15 (generation), Day 1 theory, Optional/Stretch sections everywhere | cut first |

## If you miss 1 day

| Missed | Action |
|---|---|
| Weekday | Do the **Hands-On Lab** only (skip Learn reading); read the Learn parts on the next weekend. Shift nothing else |
| Weekend day | Do the 90-minute **core path** (first lab steps plus validation) on Monday; finish the rest on the next weekend |

## If you miss 2 days

1. Merge them: do the P1 day fully, then only the lab validation of the other.
2. Drop Optional/Stretch from the next two weekdays.
3. Use the next weekend's last hour as buffer (every weekend day has a "buffer" line in its time budget).

Merge table (use the first matching row):

| Missed days | Merge instruction |
|---|---|
| 4-5 | Do Day 5 fully; do only Day 4 steps 1-3 (structured output) and read the async primer on the weekend |
| 9-10 | Do Day 9 fully; for Day 10 do only the single-agent Agent Framework example and read the orchestration section |
| 16-17 | Do Day 16 fully; for Day 17 do speech-to-text and text-to-speech only |
| 15 and any | Replace Day 15 with a reading-only pass (D3-01 to D3-05 are design/concept heavy) |

## If you miss 3 days

Reduce scope, not quality. Use this reduced plan:

| Instead of | Do |
|---|---|
| Day 13 + 14 (two long days) | One long day: Document Intelligence layout + one Content Understanding analyzer + 2 vision tasks via the multimodal model; skip video |
| Day 15 | Read the objectives and answer review questions only |
| Day 16 + 17 | One session: sentiment/PII plus speech-to-text; read the rest |
| Day 18 | Reduce to prompt-injection tests only |
| Days 19-21 | Keep Day 19 and 20 intact; shorten Day 21 (skip AI-500 bridge) |

If you are still more than 3 days behind: **move the exam date**. A rushed first attempt costs more than a delay. Retake rules: <https://learn.microsoft.com/en-us/credentials/support/retake-policy>.

## Recovery checklist

- [ ] Update [TRACKER.md](TRACKER.md): mark skipped items `Needs Review`, never `Completed`.
- [ ] Add every skipped objective ID to [WEAK_AREAS](exam-prep/WEAK_AREAS.md).
- [ ] Re-check the [COST_TRACKER](COST_TRACKER.md): idle resources still cost money.
- [ ] Confirm the day you reschedule to is a weekend if it is a long day.
- [ ] Do not skip Break/Fix on the next day; it is the part that makes the topic stick.

## Illness or travel pause (4+ days)

Delete or stop anything billable (the Free tiers are fine), keep `.env` local, and restart from the first missed day with a 20-minute recap of the previous capstone milestone.
