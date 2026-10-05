"""Day 1 compatibility gate: reports which AI-103 SDK packages import on this interpreter."""
import importlib
import importlib.metadata as md
import sys

# (pip name, import name, tier)
PACKAGES = [
    ("azure-ai-projects", "azure.ai.projects", "A"),
    ("azure-identity", "azure.identity", "A"),
    ("openai", "openai", "A"),
    ("agent-framework", "agent_framework", "A"),
    ("azure-monitor-opentelemetry", "azure.monitor.opentelemetry", "A"),
    ("pydantic", "pydantic", "A"),
    ("python-dotenv", "dotenv", "A"),
    ("azure-search-documents", "azure.search.documents", "B"),
    ("azure-ai-contentsafety", "azure.ai.contentsafety", "B"),
    ("azure-ai-evaluation", "azure.ai.evaluation", "B"),
    ("azure-ai-documentintelligence", "azure.ai.documentintelligence", "B"),
    ("azure-ai-contentunderstanding", "azure.ai.contentunderstanding", "B"),
    ("azure-ai-vision-imageanalysis", "azure.ai.vision.imageanalysis", "B"),
    ("azure-ai-textanalytics", "azure.ai.textanalytics", "B"),
    ("azure-ai-translation-text", "azure.ai.translation.text", "B"),
    ("azure-cognitiveservices-speech", "azure.cognitiveservices.speech", "B"),
]


def check(pip_name: str, import_name: str) -> tuple[str, str]:
    try:
        version = md.version(pip_name)
    except md.PackageNotFoundError:
        return "NOT INSTALLED", "-"
    try:
        importlib.import_module(import_name)
    except Exception as exc:  # report any import failure, not only ImportError
        return "IMPORT FAILED", f"{version} ({type(exc).__name__}: {exc})"
    return "OK", version


def main() -> int:
    print(f"Python {sys.version.split()[0]} at {sys.executable}\n")
    print(f"{'package':34} {'tier':4} {'status':14} version")
    tier_a_failed = False
    for pip_name, import_name, tier in PACKAGES:
        status, version = check(pip_name, import_name)
        print(f"{pip_name:34} {tier:4} {status:14} {version}")
        if tier == "A" and status != "OK":
            tier_a_failed = True
    print("\nTier A failures block the plan. Tier B failures: use the fallback venv listed in README.md.")
    return 1 if tier_a_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
