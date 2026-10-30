# BSI.IT.27.C7 – Response to process owner: "accounts pass because they are active in Fieldglass"

Hello,

Thank you for the Fieldglass evidence provided by BSI Procurement on 10/29/2026. We reviewed it against each sampled account.

**Where we agree.** Fieldglass is the authoritative HR source for contractors (SUS.IAMS.4.2.1.1). It shows open engagements to 2027-02-28, so the SanIAM termination date of 12/31/2024 is stale data, not a termination. On that basis:

- **MIA25104, MIA25105, MIA25106 – PASS.** The termination date was the only issue, and these accounts were enabled and in use when they were approved.
- **MIA25103, MIA25249, MIA25250** – the termination-date issue (E2) is cleared. For MIA25249 and MIA25250 the 2025 Q3 sample now passes.

**Why active status does not clear the remaining exceptions.** An active contract shows the person is still engaged. Under SUS.IAMS.4.2.5.1, the recertification also has to confirm that the *privileged access* is still valid and follows least privilege. The open exceptions are about the access, not the contract:

- **MIA25103 (FAIL, both samples):** CISCO/ISE admin access was approved on 8/28/2025 and 4/30/2026. Over that time the AD account was disabled, with no logon since 10/15/2023. Fieldglass shows the contractor has been working continuously since 2024-01-01 without using this admin account. That supports revoking the access, not approving it (4.2.5.1, 4.2.3.1).
- **MIA25249 / MIA25250 (FAIL, 2026 Q1):** privileged access was approved on 4/30/2026, but the AD accounts had been disabled since 4/2/2026 and 4/3/2026, and the reviewer did not address that. Both accounts were later re-enabled, and no request or approval is on file (4.2.3.4). Being active in Fieldglass does not explain why the accounts were disabled, and it does not authorize the re-enable.

**What could change the 2026 Q1 conclusion for MIA25249 / MIA25250:**

1. The reason for the 4/2–4/3/2026 disablement.
2. The approved request (ServiceNow ticket) for the re-enable.
3. The Fieldglass worker detail ("Go to Details", work order revision history Rev.0–Rev.18) showing status as of 4/30/2026 and confirming there was no gap in April 2026. The screenshots we received show only the current period, with no report date or parameters, and the current work orders start on 2026-09-29.

**Please also confirm:** the Fieldglass search returned active *Employee* (Hiring Manager) profiles with the same names: Richard Harris (n222712), Kevin Ackley (n67450) and Ashish Rimal (n600486). Are these the same individuals as the contractors, for example after conversion to FTE?

The 2025 Q3 removals of MIA25142, MIA25172, MIA25175 and X453396 were not sustained, and access was later re-granted without a request. Fieldglass does not affect those exceptions.

**Result unchanged: 3 PASS / 7 FAIL.**

Kind regards,
Edward Morfa
