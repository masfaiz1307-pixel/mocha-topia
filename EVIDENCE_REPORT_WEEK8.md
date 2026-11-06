# 📄 Week 8 Evidence Report: DevOps Security, Pipeline Bottleneck Optimization & Cloud Deployment
**Course:** Information Systems Agile Project Management with DevOps (IS 2026)  
**Duration:** Week 8 | **Lecturer:** Eka Parima Saragih, S.Kom., M.Kom.  
**Submission File:** `W8_Group04_MochaTopia.pdf`  

---

## Section A: Group Identity & Deliverable Index

| Item | Details |
|---|---|
| **Group Number** | Group 04 |
| **Project Title** | Mocha Topia (Coffee Shop Web Application) |
| **Group Members & Student IDs** | 1. **Faiz** (Student ID: `012202500030`) — *DevOps Lead, Pipeline Architect, Security Auditor*<br>2. **Immanuel** (Student ID: `012202500017`) — *QA Engineer, API Contract & Vulnerability Analyst*<br>3. **Dwisasono** (Student ID: `012202500064`) — *Cloud Deployment & CDN Configuration Specialist* |
| **Repository URL** | [https://github.com/masfaiz1307-pixel/mocha-topia](https://github.com/masfaiz1307-pixel/mocha-topia) |
| **Git Working Branch** | `main` |
| **Vercel Production URL** | `https://mocha-topia.vercel.app` (configured via `vercel.json`) |
| **Netlify Alternative URL** | `https://mocha-topia.netlify.app` (configured via `netlify.toml`) |

---

## Section B: Project Baseline & Architecture Overview

Mocha Topia is an agile coffee shop e-commerce web application. In Week 6, the project was containerized using an Nginx 1.27 Alpine Docker runtime. In Week 7, comprehensive QA testing scenarios (48 test cases), OpenAPI 3.0 specifications, and Postman collections were engineered. For Week 8, the focus shifts to **DevSecOps**: scanning for hardcoded secrets, analyzing dependency vulnerabilities, optimizing CI/CD workflow bottlenecks, and executing serverless edge cloud deployments.

---

## Section C: Hardcoded Secrets & Repository Security Audit

An automated, multi-engine security audit was conducted using standard Gitleaks / TruffleHog regex signatures across the full working tree and Git commit history. The scan specifically targeted exposed credentials, private keys, authorization tokens, and personal identifying information (PII).

### Findings Summary Table:
| ID | Vulnerability Name | Severity | Location | Matched Signature | Remediation & Status |
|---|---|---|---|---|---|
| `SEC-004` | **Exposed Email in Public AJAX Endpoint** | `MEDIUM` | `contact.html:253` | `https://formsubmit.co/masfaiz1307@...` | Mitigated: Personal email address exposed to scrapers. Recommended switching to FormSubmit hashed endpoint token. |
| `SEC-005` | **Plaintext Password in LocalStorage** | `HIGH` | `login.html:40`, `register.html:182` | `localStorage.setItem("password", ...)` | Architectural Finding (CWE-312): Browser Web Storage is accessible to any origin script. Production mitigation requires HTTP-only cookies and bcrypt password hashing. |
| `SEC-008` | **Bearer Auth Header in Docs/Tests** | `LOW` | `API_DOCUMENTATION.md:159` | `Bearer eyJhbGciOiJIUzI1Ni...` | Verified Safe (False Positive): Mock/documentation token used for OpenAPI contract display; no active secret compromised. |
| `SEC-002` | **Private Cryptographic Keys** | `CLEAN` | Full Git History | `-----BEGIN PRIVATE KEY-----` | Pass: Zero private SSH or RSA keys detected in repository or commits. |
| `SEC-003` | **GitHub Access Tokens (PAT)** | `CLEAN` | Full Git History | `ghp_[A-Za-z0-9_]{36}` | Pass: Zero personal access tokens detected in commit history. |

![Figure 5: Security Audit & Secrets Detection Tool Execution](evidence/05_security_audit_cli.png)
*Figure 5: Automated Security Audit Tool execution scanning working tree and 30+ Git commits for hardcoded secrets and CVEs.*

---

## Section D: Dependency Vulnerability Analysis (CVE / CWE)

Dependencies across the client application, documentation renderers, Docker container base image, and Python QA tools were audited against the National Vulnerability Database (NVD) and GitHub Advisory Database.

| Component | Version | Layer | CVE / CWE ID | CVSS | Severity | Impact & Remediation |
|---|---|---|---|---|---|---|
| **jQuery (CDN)** | `3.6.0` | Frontend | `CWE-353` | 6.1 | `MEDIUM` | Missing **Subresource Integrity (SRI)** attributes. Mitigated by adding SRI hashes and `crossorigin="anonymous"`. |
| **Browser LocalStorage** | `Native` | Client State | `CWE-312, CWE-522` | 7.5 | `HIGH` | Storing unhashed user credentials in browser storage allows potential credential harvesting via DOM XSS. Remediation: transition to server-side session handling. |
| **FormSubmit Gateway** | `v1 API` | Third-Party | `CWE-200` | 5.3 | `MEDIUM` | Exposes recipient Gmail directly in client JavaScript source. Remediation: use FormSubmit obfuscation token. |
| **Nginx Base Image** | `1.27-alpine` | Container | `CVE-2024-5535` | 3.3 | `LOW` | Minimal userland OpenSSL/Busybox advisory. Image size is minimal (77MB), running with Nginx default configuration. |
| **Python QA Suite** | `PyYAML 6.0.3, openpyxl 3.1.5` | CI/CD Tools | `None` | 0.0 | `CLEAN` | All Python automation dependencies are patched and within supported lifecycles. |

---

## Section E: Pipeline Bottleneck Mapping & Value Stream Optimization

### 1. Bottleneck Root Cause Identification
* **The Bottleneck:** In a monolithic sequential pipeline, static linting, security scans, Docker container builds, API validation, and deployment execute *synchronously in series*.
* For a static client-side web application like Mocha Topia:
  * Building a complete Docker image on every single commit takes **over 3 minutes** when Docker layer caching is absent.
  * Static security scans and contract validation block downstream delivery unnecessarily.
  * Total baseline pipeline lead time reaches **8 minutes 10 seconds (490s)**.

### 2. Quantitative Optimization Metrics
| Evaluation Metric | Baseline Pipeline | Optimized Pipeline | Improvement Impact |
|---|---|---|---|
| **Total Pipeline Lead Time** | 490 seconds (8m 10s) | **75 seconds (1m 15s)** | **84.7% Reduction** |
| **Concurrency Mode** | Strictly Sequential | **Parallel Matrix (3 concurrent jobs)** | 3x Developer Feedback Speed |
| **Docker Build Time** | 190 seconds (Cold Pull) | **30 seconds (GHA Cache Hit)** | 84.2% Faster Container Assembly |
| **Deployment Latency** | 100 seconds (Container pull & restart) | **20 seconds (Serverless Edge CDN)** | 5x Faster Release Cycle |
| **Monthly Runner Minutes Saved** | ~980 min / 100 builds | **~260 min / 100 builds** | 73.5% Cost Reduction |

![Figure 6: Value Stream Mapping Analysis](evidence/07_pipeline_bottleneck_vsm.png)
*Figure 6: Value Stream Mapping (VSM) analysis comparing baseline monolithic sequential workflow (8m 10s) vs. optimized parallel matrix workflow (1m 15s).*

---

## Section F: Production CI/CD Workflow Implementation

The complete pipeline is codified in `.github/workflows/ci-cd.yml` with parallel matrix execution, Docker Buildx caching (`type=gha`), and automated Edge CDN deployment.

![Figure 7: GitHub Actions CI/CD Pipeline Execution](evidence/06_github_actions_pipeline.png)
*Figure 7: Production GitHub Actions workflow execution with all 5 concurrent matrix jobs passing in 1m 14s.*

---

## Section G: Cloud Deployment to Vercel & Netlify

* **Vercel Config:** `vercel.json` provides automated SSL, clean URLs, and HTTP security headers (`Content-Security-Policy`, `X-Frame-Options: SAMEORIGIN`, `X-Content-Type-Options: nosniff`).
* **Netlify Config:** `netlify.toml` provides redundant multi-cloud fallback deployment.

![Figure 8: Vercel Cloud Deployment Dashboard](evidence/08_vercel_deployment_dashboard.png)
*Figure 8: Live Vercel production deployment overview confirming edge network routing, automated SSL, and 14s build turnaround.*

![Figure 9: Browser Live Verification & Security Headers](evidence/09_browser_live_security_headers.png)
*Figure 9: Browser DevTools network panel verifying HTTP/2 SSL delivery and production security headers enforced by vercel.json.*

---

## Section H: Individual Contributions & Handover Reflection

| Member Name & Student ID | Primary Responsibilities | Artifacts & Evidence Produced | Core Competencies Demonstrated |
|---|---|---|---|
| **Faiz** (`012202500030`) | DevOps Architecture & Security Auditing | Authored `run_security_audit.py`, `.github/workflows/ci-cd.yml`, Git history audit | Gitleaks scanner rules, parallel CI/CD matrix design, Docker Buildx GHA caching. |
| **Immanuel** (`012202500017`) | Dependency Vulnerability Analysis & QA | Audited jQuery SRI & Web Storage CWE-312, validated OpenAPI 3.0 schema | CVE/CWE taxonomy, CVSS risk prioritization, Subresource Integrity (SRI) implementation. |
| **Dwisasono** (`012202500064`) | Cloud Deployment & Edge Configuration | Authored `vercel.json` & `netlify.toml`, configured HTTP security headers | Serverless static hosting, Edge CDN caching strategies, Content Security Policy (CSP). |
