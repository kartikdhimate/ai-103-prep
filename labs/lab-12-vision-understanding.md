# Lab 12: Vision Understanding, Content Understanding for Images/Video and Visual Safety

Full steps: [Day 14](../week-02/day-14.md).

## 1. Scenario
Users upload images. The assistant must describe them, answer questions grounded in what is visible, produce alt text, and refuse unsafe or injected images.

## 2. Objectives
Generate captions and alt text with a multimodal model; enforce evidence-based Q&A; use Image Analysis for OCR, objects and tags; run Content Understanding on images (and optionally video); build an image safety and policy gate.

## 3. AI-103 objectives
D3-06 through D3-16 (see Day 14), D1-13.

## 4. Prerequisites
[Lab 11](lab-11-document-extraction.md); [Lab 04](lab-04-safety-and-guardrails.md) safety module.

## 5. Services
Multimodal model, Azure AI Vision Image Analysis, Content Understanding, Content Safety.

## 6. SDKs
`azure-ai-vision-imageanalysis`, `azure-ai-contentsafety`, `azure-ai-contentunderstanding==1.1.0`, `openai`, `pillow`.

## 7. Duration
270 minutes.

## 8. Resources
Vision resource (F0 if offered); sample images including a poisoned image.

## 9. Cost and risk
About EUR 1.00. Risks: image token cost, video cost, region feature availability, personal images.

## 10. Steps
Create resource; prepare images; caption and alt-text variants; grounded Q&A; Image Analysis; Content Understanding; image safety and rule checks; Week 2 checkpoint.

## 11. Expected result
Scored captions and alt text; low hallucination on unanswerable questions; OCR text from the poisoned image blocked by the guard; rule violations reported with evidence.

## 12. Validation
See Day 14 section 11.

## 13. Break/fix
Poison obeyed; oversized image; invented answers; region availability.

## 14. Common mistakes
Treating embedded text as trusted; writing alt text that starts with "image of"; not resizing images; running video without a cost cap.

## 15. Troubleshooting
| Symptom | Check |
|---|---|
| Feature unavailable | Region availability for Image Analysis |
| Large cost per call | Image size and detail |
| Safety API errors | Image format and size limits in docs |

## 16. Capstone relevance
M11: image intake with injection guard.

## 17. Cleanup
Remove sensitive images; keep Vision F0.
