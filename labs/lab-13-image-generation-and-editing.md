# Lab 13: Image Generation and Editing (Video as Concept)

Full steps: [Day 15](../week-03/day-15.md).

## 1. Scenario
Marketing wants generated illustrations with edits to specific regions, delivered safely with an AI-generated marker. Video generation is evaluated for feasibility only.

## 2. Objectives
Generate and edit images; apply masks; compare quality settings; gate and watermark outputs; design a video generation job flow.

## 3. AI-103 objectives
D3-01, D3-02, D3-03, D3-04, D3-05, D3-16.

## 4. Prerequisites
[Lab 12](lab-12-vision-understanding.md) `check_image`.

## 5. Services
Image model deployment (availability and access vary), Content Safety.

## 6. SDKs
`openai` (`images.generate`, `images.edit`), `pillow`.

## 7. Duration
75 minutes.

## 8. Resources
Image deployment (if available); output images; provenance log.

## 9. Cost and risk
About EUR 1.00 for at most 10 images. Risks: gated model access, large or high-quality images, unmanaged outputs. Video: EUR 0 unless you deliberately run one short job after verifying price.

## 10. Steps
Check availability; generate; mask edit; prompt-only edit; quality comparison; gate plus watermark plus provenance; video notes.

## 11. Expected result
`gen1.png`, `edit1.png`, watermarked outputs, provenance records, and a written video job flow.

## 12. Validation
See Day 15 section 11.

## 13. Break/fix
Blocked prompt; inverted mask; unsupported size; 11th image attempt.

## 14. Common mistakes
No image cap; wrong mask polarity; dropping provenance; assuming watermarking is automatic.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| Model not deployable | Access request, region |
| Edit returns unexpected region | Mask transparency |
| 400 errors | Parameter values and size allowlist |

## 16. Capstone relevance
M11 extension: optional generation module passing the visual policy gate.

## 17. Cleanup
Delete the image deployment if unused; remove sensitive outputs.
