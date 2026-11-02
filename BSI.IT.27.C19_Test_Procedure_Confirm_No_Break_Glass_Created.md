# BSI.IT.27.C19: How to confirm no break glass account was created or used (03/31/2026 – 08/30/2026)

## What counts as a "break glass account"

A break glass account is a privileged account that can be used **outside CyberArk** in an emergency (Procedure v6.0 §4.1). In practice, it is any account that:

- is in **Domain Admins, Enterprise Admins, Schema Admins or Administrators** (Windows/AD), or
- has **UID 0, root-equivalent sudo (`ALL=(ALL) ALL`)** or the T24 admin user (Unix/Linux/AIX), and
- is **not** managed or rotated by CyberArk.

**Known baseline (prior year, C19.03 / C19.06):** miabackup (Domain Admin), MIAEVAULT (Enterprise Admin), pws_root (Miasx1, T24), root (miaecowas, e-Banking).

**Test logic:** if (1) the end-of-period inventory still equals the baseline, (2) no creation or privileged-group-add events occurred in the period, and (3) the existing four accounts were not used, then no break glass account was created or invoked.

---

## Step 1 – Windows/AD inventory (who is privileged today, and when were they created)

Ask the AD admin to run these and share the output with the command visible (screen-share is preferred so you can observe it):

```powershell
# All members of privileged groups, with creation, password and logon dates
"Domain Admins","Enterprise Admins","Schema Admins","Administrators" | ForEach-Object {
  $g = $_
  Get-ADGroupMember $g -Recursive | Where-Object objectClass -eq 'user' |
  Get-ADUser -Properties whenCreated,pwdLastSet,lastLogonTimestamp,Enabled,Description |
  Select-Object @{n='Group';e={$g}},SamAccountName,Enabled,whenCreated,
    @{n='pwdLastSet';e={[datetime]::FromFileTime($_.pwdLastSet)}},
    @{n='lastLogon';e={[datetime]::FromFileTime($_.lastLogonTimestamp)}},Description
} | Export-Csv C19_Privileged_Inventory.csv -NoTypeInformation
```

```powershell
# Any account that is or was in a protected group (adminCount=1), with creation dates
Get-ADUser -LDAPFilter "(adminCount=1)" -Properties whenCreated,pwdLastSet,lastLogonTimestamp,memberOf |
  Select SamAccountName,whenCreated,@{n='pwdLastSet';e={[datetime]::FromFileTime($_.pwdLastSet)}},
         @{n='lastLogon';e={[datetime]::FromFileTime($_.lastLogonTimestamp)}}
```

```powershell
# Any user account created during the test period
Get-ADUser -Filter 'whenCreated -ge "2026-03-31" -and whenCreated -le "2026-08-30"' -Properties whenCreated,memberOf,adminCount
```

**Pass criteria**
- Every privileged account is either one of the 4 known break glass accounts, a named admin account that is vaulted in CyberArk, or a service account. Cross-check against the CyberArk onboarded accounts list or the PAM recertification population used for C7.
- No account has `whenCreated` in the period and also has `adminCount=1` or membership in a privileged group.
- miabackup and MIAEVAULT have a `whenCreated` date before the period.
- `lastLogon` for miabackup and MIAEVAULT is before 03/31/2026. `lastLogonTimestamp` can lag by up to about 14 days, so confirm with Step 3.
- *Bonus:* `pwdLastSet` shows the quarterly rotation required by §4.3.

## Step 2 – AD change events in the period (Splunk or Netwrix)

Use the index that holds **WinEventLog:Security** from the domain controllers. Confirm the index name with Evelio, because `siem-na-authentication` may not hold group-change events.

```spl
index=<windows_security_index> ac="SPB Miami*"
  (EventCode=4720 OR EventCode=4728 OR EventCode=4732 OR EventCode=4756 OR EventCode=4738)
  earliest="03/31/2026:00:00:00" latest="08/30/2026:23:59:59"
| table _time EventCode src_user user Group_Name ComputerName Message
| sort _time
```

| EventCode | Meaning |
|---|---|
| 4720 | User account created |
| 4728 / 4732 / 4756 | Member added to global / local / universal security group |
| 4738 | User account changed |

Do **not** use the `user_name="*$*"` filter. It excludes every normal account name.

**Alternative:** the Netwrix report "Changes to privileged group membership" for 03/31/2026 – 08/30/2026. This is the same type of evidence as prior-cycle C19.04.

**Pass criteria:** no 4720 event followed by a 4728/4732/4756 add into Domain Admins, Enterprise Admins, Schema Admins or Administrators. If any add exists, it must trace to an approved ticket and a CyberArk-vaulted named admin account.

## Step 3 – Use of the existing Windows break glass accounts

```spl
index=<windows_security_index> ac="SPB Miami*"
  (user="miabackup" OR user="MIAEVAULT" OR user_name="miabackup" OR user_name="MIAEVAULT")
  (EventCode=4624 OR EventCode=4625 OR EventCode=4648 OR EventCode=4672)
  earliest="03/31/2026:00:00:00" latest="08/30/2026:23:59:59"
| table _time EventCode user src_ip ComputerName Logon_Type
```

**Pass criteria:** 0 events, or every event is a CyberArk CPM password rotation or reconciliation (source = CyberArk CPM server) that ties to the quarterly rotation.

## Step 4 – Unix / AIX break glass accounts (Miasx1 – pws_root, miaecowas – root)

Ask the Unix admin to run these and send the output with the hostname and date visible:

```bash
hostname; date
awk -F: '$3==0 {print}' /etc/passwd                 # all UID-0 accounts
ls -l --time-style=full-iso /etc/passwd /etc/shadow /etc/sudoers /etc/sudoers.d/ 2>/dev/null
grep -RhE 'ALL=\(ALL(:ALL)?\)' /etc/sudoers /etc/sudoers.d/ 2>/dev/null   # root-equivalent sudo
last -F root pws_root | head -50                    # direct logons
sudo chage -l root; sudo chage -l pws_root           # last password change (Linux)
```

If Miasx1 is **AIX**, use:

```bash
lsuser -a id time_last_login time_last_unsuccessful_login root pws_root
lsuser ALL | awk '/ id=0 /'
last root pws_root
```

**Pass criteria:** the set of UID-0 and sudo-ALL accounts equals the baseline. There are no direct logons as root or pws_root in the period other than those brokered by CyberArk PSM (check the source IP against the PSM server). Password changes match the CPM rotation dates.

## Step 5 – CyberArk (shows whether credentials left the vault)

- **Safe or account activity report** for the safes holding the 4 accounts, 03/31/2026 – 08/30/2026. Look for "Retrieve password", "Show password" and "Use password" activities, and check who performed them.
- **Account list** of the 4 accounts showing "Last modified / CPM last changed" dates. These confirm the quarterly rotation.
- **CyberArk availability:** confirm there was no CyberArk outage incident in the period. An outage is the only trigger for invoking break glass.

## Step 6 – ServiceNow (incident and request tables)

Run the query on **both** `incident` and `sc_req_item` (and `change_request` if account creation goes through change), company = SPB Miami, opened 03/31/2026 – 08/30/2026, where short description or description contains any of: `break glass`, `breakglass`, `break-glass`, `emergency access`, `CyberArk outage`, `CyberArk unavailable`, `miabackup`, `MIAEVAULT`, `pws_root`.

**Pass criteria:** no records. If records exist, test each one for CISO/CIO approval **before** the account was used or created.

---

## Evidence quality checks (IPE)

For every report, make sure it shows:
1. the exact query, filter or command,
2. the run date/time and who ran it,
3. the full result population (row count),
4. the system or host it ran on.

Observing the run live (screen-share) is the strongest option. Reconcile the account list from Step 1 with Step 5 (CyberArk) and with the C7 PAM recertification population, so you can see that the inventory is complete.

## Conclusion matrix

| Result | Conclusion |
|---|---|
| Steps 1–6 all clean, and the inventory equals the baseline of 4 accounts | **No break glass account created or used.** CPA population = 0, *Not Tested / no exceptions*. Keep the CDA design observations. |
| A new privileged or break glass account, or a use event, **with** a CISO/CIO approval ticket dated before the creation or use | Population ≥ 1. Test it as a sample. It **passes**. |
| A new account or use event **without** prior CISO/CIO approval | **CPA exception.** The control failed. Raise an Action Driver. |
| Management cannot produce Steps 1–4 | **Monitoring finding** under SUS.IAMS.4.2.1.6 ("break glass activity must be monitored") and Procedure v6.0 §4.2(3). Record that the completeness of the zero population could not be verified. |
