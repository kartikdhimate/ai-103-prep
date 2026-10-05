# KnowledgeDesk CLI: Architecture

Six diagrams that evolve over the three weeks. Update the "Status" column as you build; the diagrams show the **target** end state, with labels telling you when each part arrives.

| Diagram | Week 1 | Week 2 | Week 3 |
|---|---|---|---|
| 1 High-level architecture | Foundry client, safety, search | Agent, tools, telemetry, extraction, vision | Text, speech, generation, red team |
| 2 Request/data flow | Question -> grounded answer | Tools, approval, traces | Voice, image intake, gates |
| 3 RAG pipeline | Push ingestion, hybrid, citations | Layout-aware ingestion, extraction | Final tuned settings |
| 4 Agent/tool interaction | - | Function, search, MCP, approval | Hardened policy, rules router |
| 5 Auth and security | Keyless local | Tool policy, identity matrix, network design | Red-team controls |
| 6 Azure deployment | Local only + resources | Target production design | Cost-checked final design |

## 1. High-level architecture

```mermaid
flowchart TB
    U[User - CLI, files, images, audio] --> CLI[KnowledgeDesk CLI - Python 3.14]
    CLI --> SG[Safety gate - Content Safety, rules]
    SG --> ORCH[Orchestrator: rules router, agent, workflow]
    ORCH --> FM[Foundry project - chat and embedding deployments]
    ORCH --> TOOLS[Tools: search, tickets, extraction, MCP]
    TOOLS --> AIS[(Azure AI Search)]
    TOOLS --> DI[Document Intelligence / Content Understanding]
    CLI --> VIS[Vision: multimodal model, Image Analysis]
    CLI --> SPE[Speech and Translator, Language]
    ORCH --> TEL[OpenTelemetry to Application Insights]
    ORCH --> EV[Offline evaluation and red team]
```

## 2. Request and data flow (grounded question)

```mermaid
sequenceDiagram
    participant U as User
    participant CLI as CLI
    participant S as Safety gate
    participant R as Retrieval
    participant M as Model (agent)
    participant O as Output check
    U->>CLI: question
    CLI->>S: check input
    S-->>CLI: allowed
    CLI->>R: hybrid + semantic search (top 4)
    R-->>CLI: chunks with sources
    CLI->>S: check retrieved chunks as untrusted data
    CLI->>M: instructions + question + sources
    M-->>CLI: answer with citations
    CLI->>O: check output, attach provenance
    O-->>U: answer, sources, trace id
```

## 3. RAG pipeline

```mermaid
flowchart LR
    subgraph Ingest
        F[Files: md, PDF, scans] --> L[Layout/OCR to markdown]
        L --> C[Chunk by heading, overlap 100]
        C --> E[Embed: text-embedding-3-small]
        E --> UP[Upload with merge_or_upload]
        UP --> IDX[(Index: text + vector + semantic config)]
    end
    subgraph Query
        Q[Question] --> QE[Embed question]
        Q --> KW[Keyword BM25]
        QE --> VQ[Vector query]
        KW --> HY[Hybrid fusion]
        VQ --> HY
        HY --> SR[Semantic ranker]
        SR --> TOP[Top 4 chunks]
    end
    IDX --> KW
    IDX --> VQ
    TOP --> ANS[Cited answer]
```

Record your final values here: chunk size ___, overlap ___, top k ___, search mode ___, index name ___.

## 4. Agent and tool interaction

```mermaid
sequenceDiagram
    participant A as Agent
    participant P as Tool policy (code)
    participant T as Tool
    participant H as Human approval
    participant L as Audit log
    A->>P: call tool(name, args)
    P->>P: allowlist, call limit, risk class
    alt read-only tool
        P->>T: execute
    else write tool
        P->>H: request approval
        H-->>P: approve or reject
        P->>T: execute if approved
    end
    T-->>P: result
    P->>P: safety check on result (untrusted data)
    P->>L: decision + argument digest
    P-->>A: result or error
```

Tools: `search_knowledge` (read), `get_ticket_status` (read), `create_ticket` (write, approval), `extract_invoice` (read, restricted folder), optional MCP documentation tool (approval).

## 5. Authentication and security flow

```mermaid
flowchart LR
    DEV[Developer az login] -->|Entra token| SDK[SDK DefaultAzureCredential]
    SDK -->|Azure AI User role| FND[Foundry project]
    SDK -->|Search Index Data roles| SRCH[AI Search]
    SDK -->|Cognitive Services User| CS[Content Safety, Document Intelligence, Vision, Language]
    EXC[Exceptions: Translator key, Speech key] -.->|documented in SECURITY.md| ENV[.env, gitignored]
    CI[CI workflow] -->|OIDC federated identity| SDK
    APP[Production app] -->|managed identity| FND
    INPUT[Untrusted input: text, files, images, audio, tool results] --> GATE[Safety gate fail closed]
    GATE --> FND
```

## 6. Azure deployment (target design)

```mermaid
flowchart TB
    subgraph RG[Resource group]
        subgraph VNET[Virtual network]
            APP[Container App - managed identity]
            PE1[Private endpoint Foundry]
            PE2[Private endpoint Search]
            PE3[Private endpoint Storage and Key Vault]
        end
        FND[Foundry resource and project]
        SRCH[AI Search - Basic or higher for private endpoints]
        ST[Storage - source documents]
        KV[Key Vault]
        AI[Application Insights and Log Analytics]
        SAFE[Content Safety, Document Intelligence, Language, Speech, Vision]
    end
    APP --> PE1 --> FND
    APP --> PE2 --> SRCH
    APP --> PE3 --> ST
    PE3 --> KV
    APP --> AI
    APP --> SAFE
    CI[CI pipeline OIDC] --> APP
```

Prep reality: the course uses a local CLI and Free/F0 tiers; this diagram is the design target you can explain on the exam, not something you deploy on a EUR 25 budget (Free Search does not support private endpoints).

## Design records (fill during the course)

### Model decision matrix (Day 3)

| Task | Model | Reason | Estimated cost per 1,000 requests |
|---|---|---|---|
| Grounded answer | | | |
| Classification | | | |
| Embeddings | | | |
| Image understanding | | | |

### Service decision table (Day 16)

| Need | Language service | LLM | Translator |
|---|---|---|---|
| Sentiment at scale | | | |
| Custom schema extraction | | | |
| Translation with tone | | | |

### Network design notes (Day 12)

Private endpoints needed: ___. Private DNS zones: ___. Developer access path: ___. Free Search consequences: ___.

### Pull pipeline design (Day 13)

Data source ___, indexer ___, skillset (layout, split, embed) ___, projections ___, schedule ___.
