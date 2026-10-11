# Security Incident Process

Company: Contoso Field Services (CFS)
Document ID: security_incident_process
Owner: David Okafor, Information Security Manager
Effective date: January 1, 2026
Review date: December 15, 2026

1. Purpose and scope

This procedure defines how Contoso Field Services identifies, reports, contains, investigates, and closes security incidents. It covers suspected malware, lost devices, unauthorized account access, data disclosure, phishing compromises, and physical security breaches.

All employees and contractors must report suspected incidents, even when the evidence is incomplete.

2. Reporting requirements

Employees must report suspected security incidents immediately using one of these channels:

Security mailbox: security@contoso.example.
Emergency hotline: +358 9 5550 1299.
CFS Support Portal, category Security Incident.

An employee who loses a company laptop must report the loss within 15 minutes of discovering it whenever reasonably possible. Suspected unauthorized disclosure of customer information must be reported immediately and must not be investigated independently by the reporting employee.

Reports should include the discovery time, affected system, observed symptoms, device identifier if known, and any action already taken.

3. Severity classification

The Information Security team assigns one of three severity levels.

SEV-1 — Critical: Confirmed unauthorized access to sensitive customer data, active ransomware, or compromise affecting multiple customer sites. Initial acknowledgment target: 15 minutes.

SEV-2 — High: A compromised employee account, suspected malware on a company endpoint, or a lost device that may contain sensitive information. Initial acknowledgment target: 30 minutes.

SEV-3 — Moderate: Suspicious email, blocked malware, or a policy violation without evidence of successful compromise. Initial acknowledgment target: four business hours.

These are internal response targets. Legal notification deadlines, where applicable, must be assessed separately.

4. Containment and investigation

The on-call security analyst must create an incident record and assign an incident commander for every SEV-1 and SEV-2 incident.

The security team may disable accounts, revoke authentication sessions, isolate affected endpoints, or block malicious network traffic. Actions affecting customer operations must be coordinated with Service Operations when doing so does not create an unacceptable security risk.

Employees must not delete suspicious files, wipe devices, or forward suspected phishing messages to personal accounts. Evidence must be preserved in approved storage with timestamps and access records.

David Okafor must be notified of every SEV-1 incident within 30 minutes of classification.

5. Recovery and closure

The incident commander must document containment, root cause, affected assets, recovery actions, and follow-up tasks. SEV-1 incidents require a written post-incident review within five business days of containment. SEV-2 incidents require review within 10 business days.

Corrective actions must have a named owner and due date. Any external notification must be coordinated with Legal and the Data Protection Officer.

Contact: security@contoso.example