import agents.tracing

# disable_tracing.py
try:
    import agents.tracing
    agents.tracing.enabled = False
    agents.tracing._TRACING_ENABLED = False
except Exception:
    pass

import disable_tracing

