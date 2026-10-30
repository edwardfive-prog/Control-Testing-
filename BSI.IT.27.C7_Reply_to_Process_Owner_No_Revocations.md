# BSI.IT.27.C7 – Reply to process owner: "no revocations, approved by manager, no SLA, consultants were extended"

Hello,

Thank you for the clarification. We agree with two of your points, and both are already reflected in our results:

1. **No SLA where nothing was revoked – agreed.** The 30-business-day SLA (SUS.IAMS.4.2.5.21) applies only to revoked access. We have raised no SLA exception for the contractor accounts.
2. **The consultants were extended – agreed.** The Fieldglass evidence from 10/29/2026 shows open engagements to 2027-02-28, so the SanIAM termination date of 12/31/2024 is stale. That is why **MIA25104, MIA25105 and MIA25106 pass**.

However, these points do not resolve the remaining 7 exceptions, for two reasons.

**A. "No revocations" does not match the 2025 Q3 certification for 4 sampled accounts.** In the 2025 Q3 certification (decided 8/28/2025), the manager **revoked** these accounts, and AD shows they were removed:

| Account | 2025 Q3 decision | Removed from AD | Status by 11/25/2025 |
|---|---|---|---|
| MIA25142 – Miguel Nieves Nieves | Revoked (CISCO Network Administrators, ISEAdmin) | 9/2/2025 | Back in both groups |
| MIA25172 – Juan Hernandez Ruiz | Revoked (CISCO Network Administrators) | 9/2/2025 | Back in the group; also newly in ISEAdmin |
| MIA25175 – Carlos Hernandez Acevedo | Revoked (CISCO Network Administrators) | 9/8/2025 | Back in the group; also newly in ISEAdmin |
| X453396 – Juan Fernando Perez Peralta | Revoked (CISCO Network Administrators, ISEAdmin) | 9/8/2025 | Back in both groups |

The removals were on time, so the SLA was met. The exception is that the access came back without an approved request (SUS.IAMS.4.2.3.4, PAM Procedure 4.1.1 C4 and 4.2). It was then approved again on 4/30/2026. A manager's approval in a later certification does not replace the request and approval that re-granting revoked access requires. If your records show these were not revocations, please send the 2025 Q3 certification extract for these accounts and the ServiceNow requests for the re-adds.

**B. For the contractor accounts, the exception is about the approval, not about revocations or SLA.** SUS.IAMS.4.2.5.1 requires each approval to confirm that the privileged access is still valid and needed. Manager approval is the control we are testing, so the approval itself has to be appropriate:

- **MIA25103:** approved on 8/28/2025 and 4/30/2026, but the AD account was disabled and had not been used since 10/15/2023. The contractor works from an enabled personal account (x223865), so the admin access was not needed. It should have been revoked.
- **MIA25249 / MIA25250:** approved on 4/30/2026 while the AD accounts were disabled (since 4/2/2026 and 4/3/2026). The reviewer did not address that. The accounts were later re-enabled with no request on file.

The contract extension explains why these people are still engaged. It does not explain approving privileged access on disabled or unused accounts, or the re-grants and re-enables that have no requests.

**C. Re-enabling a disabled account requires an approved request, however long it was disabled.** Re-enabling MIA25249 and MIA25250 restored their privileged access (CISCO Network Administrators, ISEAdmin, CyberArk safes). That is provisioning, so it needs a request, manager validation and second-level approval (SUS.IAMS.4.2.3.4). The policy gives no exemption for short disablements. If a disabled account can be re-enabled without a request, the inactivity control in 4.2.3.1 has no effect.

The disablement also does not appear to have been short:

| Account | Last logon | Disabled | Status at 4/30/2026 approval | Seen enabled again |
|---|---|---|---|---|
| MIA25249 – Richard Harris | 11/17/2025 | 4/2/2026 | Disabled | 10/13/2026 (exact date unknown) |
| MIA25250 – Kevin Ackley | 11/07/2025 | 4/3/2026 | Disabled | 10/13/2026 (exact date unknown) |

Both accounts went about 4.5 months without a logon before they were disabled. That pattern points to an inactivity disablement (4.2.3.1), not a short break.

If the IAM Standard or the PAM Procedure has a specific reactivation process, for example a service-desk re-enable with manager approval, and it was followed for these accounts, please send that evidence and we will reassess the re-enable point. Separately, the 4/30/2026 approval of accounts that were disabled at the time remains an exception under 4.2.5.1 either way.

**What would change the result:**
- ServiceNow requests and approvals for the re-grants (MIA25142, MIA25172, MIA25175, X453396) and the re-enables (MIA25249, MIA25250).
- The reason MIA25249 and MIA25250 were disabled on 4/2–4/3/2026 (for example, the automated 90-day inactivity job).
- The date each account was re-enabled (Netwrix or AD event), and the reactivation procedure followed, if one exists.
- For MIA25103, any evidence that the admin access was needed while the account was disabled.

**Result unchanged: 3 PASS / 7 FAIL.**

Kind regards,
Edward Morfa
