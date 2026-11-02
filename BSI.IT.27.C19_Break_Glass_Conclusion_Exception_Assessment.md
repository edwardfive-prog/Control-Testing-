# BSI.IT.27.C19 Break Glass Authorization: Exception Assessment and Conclusion

**Test period:** 03/31/2026 – 08/30/2026 (population timeframe in WP2)
**Prior cycle:** 10/01/2024 – 04/30/2025, rated *Not Tested* (population 0), CDA *Satisfactory*
**Risk:** BSI.IT.27.R6 Emergency Access. The inability to recover systems or operations due to a failure to manage emergency accounts may result in prolonged business disruptions, financial loss, and regulatory noncompliance.
**Control:** Prior to creation of a break glass account or entitlements by the access management team, either the S-CISO, CIO, Head of Infrastructure or delegate approves break glass access and invocation of the break glass procedure.

---

## 1. Bottom line

**The evidence does not support raising a performance exception (CPA deviation).**

The control has two triggers: (a) creation of a new break glass account or entitlement, and (b) invocation of the break glass procedure. All the evidence points to zero occurrences of either in the period. With no occurrence, the control never had to run, so there is nothing that could have failed. An exception needs an occurrence where the approval was missing, and none has been identified.

**Recommended rating:** CPA *Not Tested – control not executed (population = 0)*, consistent with the prior cycle. Keep the RCSA convention that it is treated as effective based on prior testing and the CDA.

**There are two conditions you need to document:**

1. **The "no events" evidence is weaker than it looks** (Section 3). The Splunk and ServiceNow queries are built so that they would probably return zero even if a break glass event had happened. Get a corrected query before signing off, or record the limitation in the CPA.
2. **There is a design gap between the procedure and the control statement** (Section 4). Procedure v6.0 uses a standing *pre-authorization* model, but the control statement and IAM Standard require *approval for each event*. This is a **CDA observation or recommendation, not a CPA exception.** It may justify downgrading the CDA from *Satisfactory* or raising an Action Driver.

---

## 2. What each piece of evidence actually proves

| # | Evidence | Who / date | Period covered | What it proves | What it does NOT prove |
|---|---|---|---|---|---|
| 1 | Email "CyberArk Break Glass – RCSA Evidence" | Zoila Rosario to Edward Morfa, 09/16/2026 | 03/31/2026 – 08/31/2026 | Management says there were no new break glass accounts (4 accounts unchanged: miabackup, MIAEVAULT, pws_root, root) and no break glass event | Inquiry only. On its own, it is not sufficient evidence for a Key control. |
| 2 | Splunk query #1 | Oscar Ortiz, email 10/22/2026 | 09/01/2025 – 09/30/2026 | 0 results for `EventCode=4720 user_name="*$*"` in `siem-na-authentication` | See 3.1. The query does not search for use of the break glass accounts. |
| 3 | Splunk query #2 | Evelio Heredia, email 10/19/2026 | 07/01/2026 – 09/30/2026 | Same query, 0 results | Only covers 2 of the 5 test-period months (Q3 2026 was requested, but the test period is 03/31 – 08/30/2026). |
| 4 | ServiceNow queries (3 screenshots) | Run by Oscar Ortiz, 10/15/2026 | 04/01/2025 – 09/30/2026; 07/01/2025 – 06/30/2026; 07/01/2026 – 10/15/2026 | No **Requested Items (sc_req_item)** for company SPB Miami with "break glass / breakglass / break-glass" in the short description or description, or with item name "Breakglass" | See 3.2. The procedure requires break glass events to be logged as **incidents**, and the incident table was not queried. |
| 5 | PAM0023 metric | Provider Oscar Ortiz, Approver Robert Burden | As-of 12/31/2025 – 08/31/2026 | Numerator 0 (Green). No break glass provisioning event was left un-deprovisioned past the SLA. | It does not show that zero events occurred. The denominator (V2) is blank, so the total number of events is not shown. This is a timeliness metric, not an approval metric. |
| 6 | CyberArk Break Glass Procedure v6.0 (10/06/2025) | Information Security | Current | A procedure exists. CISO is the owner. | Section 7.2 sign-off table is blank (no approval names or dates). See Section 4. |

---

## 3. Why the "zero population" is not fully evidenced

### 3.1 Splunk query has a scope problem

```
index="siem-na-authentication" ac="SPB Miami*" EventCode=4720 user_name="*$*"
```

- **EventCode 4720 means "A user account was created".** The query only detects account *creation*. It does not detect *use* of the existing break glass accounts. Use is the main event: an invocation means someone logs on as miabackup or MIAEVAULT. Use would show up as 4624 (logon), 4648 (logon with explicit credentials) or 4672 (special privileges assigned).
- **`user_name="*$*"` only matches account names that contain a `$`.** None of the four break glass accounts (miabackup, MIAEVAULT, pws_root, root) contains a `$`. The query could not return them even if they had been used or recreated.
- **It does not catch new entitlements.** The control also covers "entitlements". Granting break glass privilege, for example adding an account to Domain Admins or Enterprise Admins, appears as 4728, 4732 or 4756. These events are not in the query.
- **Unix/Linux is not covered.** pws_root (T24 core banking, Miasx1) and root (e-Banking, miaecowas) are Unix accounts. Their activity would not appear in a Windows authentication index.

**Result:** "0 events" from this query is expected whatever happened. It does not corroborate "no break glass event".

### 3.2 ServiceNow query searched the wrong table

- Procedure v6.0, §4.2 step 2 says: *"The IT Operations representative will create an **incident** on ServiceNow to document the BreakGlass event."* §4.3 step 3 says: *"…document and close the BreakGlass **incident** in ServiceNow."*
- The screenshots query `sc_req_item` (Requested Items / RITM). They do not query `incident`. A properly logged break glass event would therefore not appear in these results.
- The search is keyword-only. A ticket titled, for example, "CyberArk outage – emergency access" would be missed. Add the account names (miabackup, MIAEVAULT, pws_root) and "CyberArk" with "outage" or "unavailable".
- **Strength:** the screenshots show the full filter, the run date (10/15/2026) and the user who ran them, and the date ranges cover the test period.

### 3.3 Corroboration you can rely on today

- Management attestation (inquiry), plus
- PAM0023 at 0 for every month-end in the period, approved by a second person (Burden), plus
- No RITMs for break glass creation or access requests.

Taken together, these are consistent with zero population. They are the same type of evidence the prior cycle accepted, which also used Netwrix and Linux tickets. However, the prior cycle **also** had Netwrix AD privileged-account-creation logs (C19.04) and Linux privileged account tickets (C19.05). This cycle has no equivalent of those yet.

### 3.4 What to request so you can close cleanly (send to Oscar Ortiz / Evelio Heredia)

1. Splunk (Windows), 03/31/2026 – 08/30/2026:
   `index="siem-na-authentication" ac="SPB Miami*" (user_name="miabackup" OR user_name="MIAEVAULT") (EventCode=4624 OR EventCode=4648 OR EventCode=4672)`. Also run `EventCode IN (4720,4728,4732,4756)` without the `*$*` filter.
2. Linux/Unix authentication logs (or CyberArk session logs) for `root` on miaecowas and `pws_root` on Miasx1 that show only CyberArk-brokered access. Alternatively, CyberArk PSM/vault audit showing the passwords were checked out only by the vault.
3. ServiceNow **incident** table query with the same filters (company SPB Miami, period dates, keywords plus account names). Screenshot the filter, the run date and the result.
4. Netwrix report of privileged AD group membership changes for the period. This is the equivalent of prior-cycle C19.04.
5. *(Optional, procedure compliance)* Evidence of the quarterly break glass password rotation (§4.3), for Q2 and Q3 2026.

**If management cannot provide items 1–3:** do not raise an exception. Instead, record in the CPA Summary that completeness of the zero population relies on management attestation and PAM0023, and that the Splunk and ServiceNow queries were not designed to detect break glass use or incidents.

---

## 4. Policy / procedure review: design observations (CDA, not CPA)

### 4.1 What the policies require

| Source | Requirement (quoted) |
|---|---|
| **CUSO IAM Standard v11.0 (07/28/2026), SUS.IAMS.4.2.1.6 Temporary Access** (same text in v10.0, 09/29/2025) | "Break glass access must be approved by s-CISO or Chief Information Officer ("CIO") Infrastructure or delegate **through a ticket request or incident ticket**. Break glass activity **must be monitored**. Access must be removed when it is no longer needed." |
| **IAM Standard, Privileged Access definition** | "Privileged accounts include 'super users,' service accounts, local administration accounts, **emergency accounts**…". So break glass accounts are in scope of the privileged account review. |
| **PAM Definition of Privilege, Reporting and Escalation/Exceptions** | "The office of CIO / CISO will **review and approve break glass requests based on the incident**. Key Performance Indicator (KPI) Reporting is included in the monthly Operational Risk Management Dashboard…" (this KPI is PAM0023) |
| **CyberArk Break Glass Procedure v6.0 (10/06/2025), §4.1** | "The IT Operations Manager or delegate has been **pre-authorized by the CISO** to utilize the privilege accounts for each platform in the event of a CyberArk outage. Information Security will monitor the use of these accounts." |
| **Procedure v6.0, §4.2 step 1** | "IT Operations Manager will access his corporate mobile phone to retrieve the passwords… The CISO/CIO **will be notified** of the event." |
| **Procedure v6.0, §4.2 step 3** | "The IAM/PAM Cybersecurity representative will monitor the use of these privilege accounts passwords… to ensure they were used for a valid CyberArk outage event." |
| **Procedure v6.0, §4.3** | Reset passwords after the event, rotate quarterly even if there is no event, and close the ServiceNow incident. "All evidences will be collected and provided to the Cybersecurity Compliance Officer." |

### 4.2 Gaps

| # | Observation | Why it matters |
|---|---|---|
| D1 | **Pre-authorization vs. per-event approval.** The control statement says approval happens *prior to* invocation. The IAM Standard and the PAM Definition of Privilege say approval is *per ticket / per incident*. Procedure v6.0 instead gives standing pre-authorization to the IT Ops Manager and only *notifies* the CISO/CIO. | No approval artifact is produced for each invocation. If an event does happen, the attribute "CISO/CIO approval of invocation" in the CPA may not be testable as written. The control statement, procedure and standard need to be aligned. Either reword the control (pre-authorization plus after-the-fact CISO review of the incident) or add an approval step to the procedure. |
| D2 | **The prior CDA describes an older procedure.** The 06/26/2025 CDA says "an email or any kind of written authorization from the CISO or CIO is required" and refers to two scenarios (network available / not available). v6.0 removed the scenario-1 content and relies on pre-authorization. | The CDA narrative is out of date. Refresh the CDA walkthrough against v6.0. |
| D3 | **Procedure covers invocation only, not creation of new break glass accounts or entitlements.** | The first trigger in the control statement, "prior to creation of a break glass account or entitlements", has no documented approval step in the procedure. |
| D4 | **v6.0 sign-off table (§7.2) is blank.** There are no names or dates for CISO, CIO or IT Ops Manager approval. | The 2025 CDA states that the procedure "is reviewed/approved on an annual basis by CISO, CIO, ITOps Manager". Request evidence of that approval. |
| D5 | **Break glass passwords are stored on corporate mobile phones** (CISO, CIO, IT Ops Manager). The vault was removed in v6.0. | This is a credential-custody risk. It is not part of C19's statement, but it is relevant to R6. Raise it as an observation for the CISO. |
| D6 | **Monitoring evidence is weak.** The IAM Standard says break glass activity must be monitored. The monitoring evidence provided (Splunk) does not target the break glass accounts (see 3.1). | This supports a CDA question 6 answer of "Moderately Reliable" and a recommendation to set up a saved Splunk alert on the four accounts. |

**How these affect the rating:** D1–D4 are **design** points. None is a deviation in performance during the period, because nothing happened that the control would have had to act on. Put them in the CDA comments, and, if your methodology allows, rate the CDA *Needs Improvement* or raise an Action Driver or recommendation to align the procedure with SUS.IAMS.4.2.1.6 and the control statement. Do **not** put them in the CPA as a failed sample.

---

## 5. Suggested CPA wording

**Population / Sample:** 0 / 0. Timeframe 03/31/2026 – 08/30/2026.

**Summary of Results:**
> Management (Zoila Rosario, Sr. Cybersecurity Compliance Officer, 09/16/2026) confirmed that no new Break Glass accounts were created and no Break Glass event occurred during 03/31/2026 – 08/31/2026. The Break Glass account population (miabackup, MIAEVAULT, pws_root, root) is unchanged from the prior year (BSI.IT.27.C19.03). This was corroborated by: (i) the PAM0023 metric, which reported 0 break glass provisioning events not de-provisioned within SLA for each month-end from 12/31/2025 to 08/31/2026 (Approved, Green) (BSI.IT.27.C19.04); (ii) ServiceNow Requested Item queries for SPB Miami covering 04/01/2025 – 09/30/2026 that returned no break glass requests (run 10/15/2026); and (iii) Splunk queries for 09/01/2025 – 09/30/2026 that returned no results.
>
> Limitation: the Splunk query (EventCode 4720, user_name containing "$") and the ServiceNow query (Requested Items table) were not designed to detect use of the existing break glass accounts or break glass incidents. Completeness of the zero population therefore relies mainly on management attestation and the PAM0023 metric. *[Remove this paragraph if the corrected queries in Section 3.4 are received and also return zero.]*
>
> Because there were no Break Glass events or new Break Glass accounts, CISO/CIO approval of break glass access and invocation could not be tested. The control was not executed during this testing cycle (population and sample size of 0). The control has been previously tested and has not substantially changed. IT RCSA therefore expects the control to continue working, and control performance is considered Effective for the test period based on prior testing and the CDA. **No exceptions noted.**

**CDA comment to add:** D1–D4 above, with a recommendation to align CyberArk Break Glass Procedure v6.0 with SUS.IAMS.4.2.1.6 (approval through a ticket or incident ticket) and the control statement (approval prior to invocation and prior to account or entitlement creation), and to obtain documented approval of v6.0.
