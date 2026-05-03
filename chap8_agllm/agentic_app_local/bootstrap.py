import os
# import sys

# sys.modules["agents.tracing"] = None
# sys.modules["agents._tracing"] = None

# ===== 强制关闭 OpenAI 云端 Tracing / Telemetry =====
os.environ["OPENAI_TRACING"] = "false"
os.environ["OPENAI_TRACE"] = "0"
os.environ["OPENAI_TELEMETRY"] = "off"
os.environ["OPENAI_DISABLE_TELEMETRY"] = "1"

# ===== Ollama OpenAI-compatible endpoint =====
os.environ["OPENAI_BASE_URL"] = "http://localhost:11434/v1"
os.environ["OPENAI_API_KEY"] = "ollama"
