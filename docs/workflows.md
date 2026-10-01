# Process & Control Flows

## End-to-end operating flow

```mermaid
flowchart LR
 A["Source Data"] --> B["Quality & Feature Engineering"]
 B --> C["Model Training / Scoring"]
 C --> D["Validation & Risk Controls"]
 D --> E["Monitoring / Reporting"]
 E --> F["Audit / Evidence Layer"]
 F -. "feedback & remediation" .-> B
```

## Control lifecycle

```mermaid
flowchart TD
 I["Input / Event"] --> V{"Validation Passed?"}
 V -- "No" --> Q["Quarantine / Exception"]
 Q --> R["Review & Remediate"]
 R --> V
 V -- "Yes" --> P["Process / Analyse"]
 P --> C{"Control Threshold Met?"}
 C -- "No" --> A["Alert / Escalate"]
 A --> E["Evidence / Audit Record"]
 C -- "Yes" --> O["Approved Output"]
 O --> E
```

## Engineering expectations

- Inputs remain traceable to source.
- Validation occurs before downstream processing.
- Exceptions are explicit states rather than silent failures.
- Material actions produce evidence suitable for review.
- Metrics are derived from the same governed state used by operational workflows.
- Production deployment requires environment-specific identity, authorization, secrets management and observability.
