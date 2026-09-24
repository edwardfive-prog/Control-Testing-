# BSI.IT.6.C7.3 – DR Data Integrity Validation (DIV) – Evidence Repository

Control: IT DR team facilitates annual Data Integrity Validation testing performed by business line testers during actual DR testing for in-scope applications that store business data; business line management approves the results; evidence is documented in BCMS (BCiC).

Review period: 08/01/2025 – 06/01/2026 · Entity: BSI · Population tested: 10 in-scope applications / 56 DIV records · DR exercise: 11/15/2025 (prior cycle 10/19/2024).

## Workpaper

`BSI.IT.6.C7.3_E00_Workpaper_DR_DIV_INTEGRATED_APPLICATION_Evidence.xlsx` – tab **Application + Attribute Testing** holds the attribute testing for the 10 samples; every attribute cites the evidence Ref and its full location in this repository. Tab **BSI.IT.6.C7.3 Evidence Index** is the spreadsheet version of the index below (with samples and workpaper columns supported per file).

## Folder structure

| Folder | Prefix | Contents | Primary attributes supported |
|---|---|---|---|
| `01_Management_Attestation_In-Scope_Applications` | MA | BCiC in-scope applications screenshot (BSI In-Scope Applications-2026) | Applications in Scope Identified |
| `02_Business_Line_Approval_Results_Email` | BLA | Business line DR test scripts with the DIV results section (11/15/2025) and the Financial Analysis approval email | Business Line Approval of Results; DIV procedures; Business Data Validation |
| `03_DIV_Manager_Attestation_Email_Approvals` | DMA | Application-specific business line manager approval emails / signed attestations (signed PDFs extracted to `Signed_Attestations_extracted`) | Business Line Approval of Results; manager name / approval dates |
| `04_Data_Integrity_and_Email_Testing_Evidence` | E01–E10, E13, E16b | BCiC exports & screenshots, IT DR planning emails, data comparison files (attachments extracted to `E07_…` / `E08_Attachments_extracted`), backup/restore approval emails | All attributes |

## Evidence index

### 01 – Management Attestation / In-Scope Applications

| Ref | File | Date / owner | Content |
|---|---|---|---|
| MA01 | `MA01_BSI In-Scope Applications-2026.png` | 09/23/2026 – Cesar Vidal (BCiC walkthrough) | BC in the Cloud 'Applications In Scope for DR Test BSI' view (filter Scope Entity = BSI; 43 items). The 10 tested applications are selected (1822, 1867, 1868, 1903, 1917, 1937, 1936, 3301, 3299, 4052) and each shows 2025 DR Test Scope = True, 2025 Backup/Restore Test Scope = True and 2025 Backup/Restore DIV Scope = True. |

### 02 – Business Line Approval Results – Email

| Ref | File | Date / owner | Content |
|---|---|---|---|
| BLA01 | `BLA01_Client Back Office - FED Inclearing ACH & Cash Letter - DIV Test Results 11-15-2025.pdf` | 11/15/2025 – Client Back Office (operator Raimy Ayala) | DR test script with Data Integrity Validation section. Application in-scope: FedImport, FedExport, Imaging101, T24. Format / Headers / Content = Y – "No data discrepancy found". Steps include ACH Express import and Imaging101 validation screenshots (14 pages). |
| BLA02 | `BLA02_BSA_AML_OFAC Compliance - OFAC Verifier - DIV Test Results 11-15-2025.pdf` | 11/15/2025 – BSA/AML/OFAC Compliance (operator David Marquez) | OFAC Verifier test script. Application in-scope: T24, Imaging101, OFAC. DIV procedure instructions listed; production-day (11/14/2025) vs test-day (11/15/2025) screenshots for T24, Imaging101/ModeloIC and OFAC Report 64. NOTE: DIV Yes/No answer boxes on p.1 are blank. |
| BLA03 | `BLA03_Payments & Cash Management - Payments Script - DIV Test Results 11-15-2025.pdf` | 11/15/2025 – Payments & Position Management (operators Frank Puentes / Gustavo Bucaro) | Wire Transfer / Cash Mgt / Financial Messaging script. DIV application in-scope: T24, MQ Payment Monitor, OFAC – BSI, Fedlink – BSI, Swift Interface – BSI. Format / Headers / Content = yes; data from 11/14/2025 Fed & SWIFT reconciled. |
| BLA04 | `BLA04_Investment Operations - Treasury Hub & Derivatives Operations - DIV Test Results 11-15-2025.docx` | 11/15/2025 – Investment Operations (operator Michelle Oropesa) | Treasury Hub & Derivatives Operations script. Systems accessed: Swift Interface Monitor – BSI, T24, MS Office, DTCC. DIV application in-scope: T24 & Swift Interface – BSI. Incoming MT300 and FX S reports matched 11/14 vs 11/15; Format / Headers / Content = Yes. |
| BLA05 | `BLA05_Financial Analysis and Control - GL ReconXpert - DIV Test Results 11-15-2025.pdf` | 11/15/2025 – Finance & Accounting Reporting (operator Dunia Gonzalez Collado) | General ledger review script. DIV application in-scope: T24 & ReconXpert. Reconciliations passed; Format / Headers / Content = Yes, "No discrepancies found on the report". |
| BLA06 | `BLA06_RE_ Testing enviroment - Financial Analysis Manager Approval - Sadis Alvarenga 01-26-2026.msg` | 12/31/2025 & 01/26/2026 – Sadis Alvarenga | Sadis Alvarenga (Financial Analysis & Control manager) replies "Approved." on 12/31/2025 and again on 01/26/2026 to Elizabeth Noda's request to approve the submitted test script. |

### 03 – DIV Manager Attestation Email Approvals

| Ref | File | Date / owner | Content |
|---|---|---|---|
| DMA01 | `DMA01_RE_ Management Attestation – DIV – Client Back Office - Claudia Romero 08-18-2026.msg` | 08/18/2026 – Claudia Romero | Claudia Romero (Client Back Office Manager VP) returns signed attestation (DMA01a). |
| DMA01a | `Signed_Attestations_extracted/DMA01a_Client Back Office - Data_Integrity_Attestation_Santander-BCiC (002).pdf` | 08/18/2026 – Claudia Romero | Signed Management Attestation – Client Back Office. |
| DMA02 | `DMA02_RE_ Management Attestation – DIV – BSA-AML-OFAC Compliance - David Marquez 08-19-2026.msg` | 08/19/2026 – David Marquez | Cesar Vidal request to Department Managers (08/17/2026; DR exercises 11/15/2025 and 02/21/2026; BCiC export attached) and David Marquez (OFAC Manager) reply returning the signed attestation. |
| DMA02a | `Signed_Attestations_extracted/DMA02a_BSA-AML-OFAC Compliance - Data_Integrity_Attestation_Santander-BCiC (005) - BSA-AML-OFAC Compliance.pdf` | 08/19/2026 – David Marquez | Signed attestation – OFAC Manager, VP, BSA/AML-OFAC Compliance, dated 8/19/2026. §1 states the IT DR team facilitates DIV annually; §2 lists 63 entries / 13 applications, all Y/Y/Y; §3.5 retention in BCMS/BCiC; §3.6 contemporaneous approval going forward. |
| DMA03 | `DMA03_RE_ Management Attestation – DIV – Payments & Cash Management - Frank Puentes 08-18-2026.msg` | 08/18/2026 – Frank Puentes | Frank Puentes returns signed attestation (DMA03a). |
| DMA03a | `Signed_Attestations_extracted/DMA03a_Payments & Cash Management - 4069_001.pdf` | 08/18/2026 – Frank Puentes | Scanned signed attestation – Executive Director, Payments & Cash Management. |
| DMA04 | `DMA04_RE_ Management Attestation – DIV – Investment Operations - Michelle Oropesa 08-17-2026.msg` | 08/17/2026 – Michelle Oropesa | Michelle Oropesa (Investment Operations Director) returns signed attestation (DMA04a). |
| DMA04a | `Signed_Attestations_extracted/DMA04a_Investment Operations - Data_Integrity_Attestation_Santander-BCiC.pdf` | 08/17/2026 – Michelle Oropesa | Signed attestation – Investment Operations Director, VP, dated 8/17/2026. |
| DMA05 | `DMA05_RE_ Management Attestation – DIV – Operations (Governance & Static Data, Multi-Family Office) - Maria Teresa Del Cerro 08-19-2026.msg` | 08/19/2026 – Maria Teresa (Mayte) Del Cerro | Signed attestation + BCiC export (E16b) returned by Senior Director of Operations. |
| DMA05a | `Signed_Attestations_extracted/DMA05a_Operations (Governance & Static Data, Multi-Family Office) - Data_Integrity_Attestation_Santander-BCiC.pdf` | 08/19/2026 – Maria Teresa Del Cerro Hontanilla | Signed attestation – Director of Operations, dated 08/19/2026. |
| DMA06 | `DMA06_RE_ Management Attestation – DIV – Trading & Capital Markets (AIS, Portfolio Advisory, P&I Tech) - Ricardo Garcia-Marques 08-18-2026.msg` | 08/18/2026 – Ricardo Garcia-Marques | Attestation and approval from Trading & Capital Markets (covers BCiC records approved by Ricardo Garcia). |
| DMA06a | `Signed_Attestations_extracted/DMA06a_Trading & Capital Markets (AIS, Portfolio Advisory, P&I Tech) - Data_Integrity_Attestation_Santander-BCiC_signed.pdf` | 08/18/2026 11:45 AM EDT – Ricardo Garcia Marques | e-signed attestation – MD, Head of Trading & Capital Markets. |
| DMA07 | `DMA07_RE_ Management Attestation – DIV – Treasury & Capital Planning - Martha Sullivan 08-18-2026.msg` | 08/18/2026 – Martha Sullivan | Martha Sullivan returns signed attestation (DMA07a). |
| DMA07a | `Signed_Attestations_extracted/DMA07a_Treasury & Capital Planning - Data_Integrity_Attestation_Santander-BCiC.pdf` | 08/18/2026 – Martha Sullivan | Signed attestation – Balance Sheet Manager, Treasury. |
| DMA08 | `DMA08_RE_ Management Attestation – DIV – Solvency & Market Risk (Financial Risk) - Ivan Caisapanta 08-18-2026.msg` | 08/18/2026 – Ivan Caisapanta | "Hi Elizabeth, You have my approval" – Financial Risk (BCiC Department Manager recorded as Xavier Caisapanta). |
| DMA09 | `DMA09_RE_ Management Attestation – DIV – General Services (Marketing & General Services) - Clara De Castro 08-18-2026.msg` | 08/18/2026 – Clara G. De Castro | Clara De Castro (Director, General Services & Facilities) returns signed attestation (DMA09a). |
| DMA09a | `Signed_Attestations_extracted/DMA09a_General Services (Marketing & General Services) - Data_Integrity_Attestation_Santander-BCiC.pdf` | 08/18/2026 – Clara G. De Castro | Signed attestation – General Services. |
| DMA10 | `DMA10_RE_ Management Attestation – DIV – Digital Wealth - Victoria Fernandez 08-21-2026.eml` | 08/21/2026 – Victoria Fernandez | "Approved" – Digital Wealth. |
| DMA11 | `DMA11_RE_ Management Attestation – DIV – Commercial Middle Office - Miguel Orozco 09-09-2026.eml` | 09/09/2026 – Miguel Orozco | "I approve the integrity validation for the testing performed by the Commercial Middle Office." |
| DMA12 | `DMA12_RE_ Management Attestation – DIV – Client Servicing Unit - Liliana Vizhnay 09-09-2026.eml` | 09/09/2026 – Liliana Vizhnay | "I approve." – Client Servicing Unit. |
| DMA13 | `DMA13_RE_ Management Attestation – DIV – IT Unified Communication - Cisco Call Manager - Elizabeth Noda 09-09-2026 (out of scope).eml` | 09/09/2026 – Elizabeth Noda | "approve" – Cisco Call Manager (IT). Cisco Call Manager is NOT one of the 10 tested applications – retained for completeness only. |

### 04 – Data Integrity & Email Testing Evidence

| Ref | File | Date / owner | Content |
|---|---|---|---|
| E01 | `BSI.IT.6.C7.3_E01_Applications In Scope for DR Test BSI (13).xlsx` | BCiC – Applications In Scope for DR Test BSI | BCiC export of the BSI DR-scope population (43 applications) with Exercise Date and 2025 DR / Backup-Restore / DIV scope flags. |
| E02 | `BSI.IT.6.C7.3_E02_screenshot BCiC apps in scope for DR Testing.jpg` | 09/10/2026 – Cesar Vidal | BCiC Applications screen with view 'Applications In Scope for DR Test BSI' selected (1–20 of 43 items). |
| E03 | `BSI.IT.6.C7.3_E03_All Data Integrity Validation Testing_FV.xls` | BCiC – Data Integrity Validation Testing (62 records) | BCiC DIV export incl. Business Tester, Business Data Validation Date, Department Manager, Department Manager Approval Date, Y/N Format/Headers/Content, Attestation Date / Provided By. Row numbers quoted are Excel rows. |
| E04 | `BSI.IT.6.C7.3_E04_BCiC_Screenshot for Data Integrity Validation report.jpg` | 09/10/2026 – Cesar Vidal | BCiC 'Data Integrity Validation Testing' screen (1–20 of 66 items) showing tester, validation date, manager, approval date, Y/N results and attestation fields. |
| E05 | `BSI.IT.6.C7.3_E05_IT BIA Results Review and preparation for DR .msg` | 09/15/2025 – Elizabeth Noda | IT DR meeting to review the 2025 BIA results and applications list ahead of the DR exercise. |
| E06 | `BSI.IT.6.C7.3_E06_IT BIA Results Review and preparation for DR  1 (1).msg.eml` | 09/18/2025 – Elizabeth Noda | Follow-up IT BIA results / DR preparation meeting (applications list review). |
| E07 | `BSI.IT.6.C7.3_E07_DATA INTERITY FILS FROM 111425.msg` | 11/15/2025 – Frank Puentes | Pre-DR (11/14/2025) source reports: Fedlink, OFAC ACH/FED/SWIFT, Payment Monitor, SWIFT Interface Monitor, outgoing Fedwire/SWIFT. Attachments extracted to E07_Attachments_extracted. |
| E08 | `BSI.IT.6.C7.3_E08_FILES FROM 111525 DR TEST - DATA COMPARISON FROM 111425.msg` | 11/15/2025 – Frank Puentes | DR test-day (11/15/2025) re-run of the same reports for comparison with 11/14/2025 source. Attachments extracted to E08_Attachments_extracted. |
| E09 | `BSI.IT.6.C7.3_E09_RE_ Yearly Backup and restore exercise- client back office sign off-ACH,ACH Express, FedExport, FedImport,Imagi.msg` | 03/03/2026 – 05/05/2026 – Claudia Romero | Client Back Office test evidence (Mariorly Morales, Ilumel Rodriguez, Rolando Bonilla) and Claudia Romero "Approved." 05/05/2026. Thread maps ACH Express, FedExport, FedImport, Imaging101 to Client Back Office / Claudia Romero. |
| E10 | `BSI.IT.6.C7.3_E10_RE_ Yearly Backup and restore exercise-- re-run- Finance approval-T24-ReconXpert.msg` | 03/09/2026 – Lina Acuna | Finance DIV results chart (Jose Acero) and Lina Acuna "Approved" 03/09/2026 (T24 / ReconXpert backup-restore). |
| E13 | `BSI.IT.6.C7.3_E13_miasx2 T24 environment(s)  miaeod miabed01 refreshed correctly.msg` | 11/13/2024 – T24 backup user | T24 environment refresh log – prior period (outside review period); supplemental only. |
| E16b | `BSI.IT.6.C7.3_E16b_All Data Integrity Validation Testing-BSI 2025-26.xlsx` | 08/2026 – BCiC export sent with attestation request | BCiC DIV export 2025-26 (64 rows; no manager columns) sent to managers with the attestation request and returned by M. T. Del Cerro (DMA05). Row numbers are Excel rows. |

## Application → key evidence

| Sample | Application | E03 row(s) | Results document (02) | Business line approval (02/03/04) |
|---|---|---|---|---|
| 1822 | ACH Express | 47 | BLA01 | E09, DMA01/DMA01a |
| 1867 | FedExport - BSI | 9 | BLA01 | E09, DMA01/DMA01a |
| 1868 | FedImport - BSI | 10 | BLA01 | E09, DMA01/DMA01a |
| 3299 | Imaging101 | 5, 11, 13, 51, 53, 57 | BLA01, BLA02 | DMA02, E09, DMA01, DMA11, DMA05 |
| 4052 | Interface Monitor | 61 | BLA04 | DMA04/DMA04a |
| 3301 | MQ Payment Monitor | 25, 29 | BLA03 | DMA03/DMA03a |
| 1903 | OFAC - BSI | 6, 26, 30, 34, 58 | BLA02, BLA03 | DMA02, DMA03, DMA05 |
| 1917 | ReconXpert | 17 | BLA05 | BLA06 (E10 supplemental) |
| 1936 | Swift Interface - BSI | 7, 60 | BLA03, BLA04 | DMA02, DMA04 |
| 1937 | T24 | 36 records (see workpaper) | BLA01–BLA05 | E09, BLA06, DMA01–DMA12 |

## Duplicate files removed

The received packages contained the same evidence more than once. Each duplicate below was removed and one copy retained; the workpaper cites only the retained copy.

| Removed ref | Removed file | Retained ref | Reason |
|---|---|---|---|
| MA02 | `MA02_RE_ Management Attestation – DIV Testing (Nov 2025 & Feb 2026) – Payments & Cash Management – Frank Puentes 08-18-2026.msg` | DMA03 | same email message (subject, sent 08/18/2026 14:50, attachment 4069_001.pdf) |
| DMA05b | `DMA05b_Operations (Governance & Static Data, Multi-Family Office) - All Data Integrity Validation Testing-BSI 2025-26.xlsx` | E16b | byte-identical file (MD5 match) |
| E11 | `BSI.IT.6.C7.3_E11_BSI.IT.6.C7.3 Manager Approval.msg` | E10 | same email message (sent 03/09/2026 18:43) saved twice |
| E12 | `BSI.IT.6.C7.3_E12_RE_ Testing enviroment Financial Analysis manager approval.msg` | BLA06 | same email message (sent 01/26/2026 20:43) |
| E14 | `BSI.IT.6.C7.3_E14_RE_ Management Attestation – Data Integrity Validation Testing (November 2025 & February 2026 Exercises) (1).msg.eml` | DMA02 | same email message saved as .eml |
| E14a | `BSI.IT.6.C7.3_E14a_Data_Integrity_Attestation_Santander-BCiC (005) - BSA-AML-OFAC Compliance.pdf` | DMA02a | byte-identical file (MD5 match) |
| E15 | `BSI.IT.6.C7.3_E15_RE_ Management Attestation – Data Integrity Validation Testing (November 2025 & February 2026 Exercises) 1 (1).msg.eml` | DMA04 | same email message saved as .eml |
| E15a | `BSI.IT.6.C7.3_E15a_Data_Integrity_Attestation_Santander-BCiC.pdf` | DMA04a | byte-identical file (MD5 match) |
| E16 | `BSI.IT.6.C7.3_E16_RE_ Management Attestation – Data Integrity Validation Testing (November 2025 & February 2026 Exercises) 2 (1).msg.eml` | DMA05 | same email message saved as .eml |
| E16a | `BSI.IT.6.C7.3_E16a_Data_Integrity_Attestation_Santander-BCiC.pdf` | DMA05a | byte-identical file (MD5 match) |
| E17 | `BSI.IT.6.C7.3_E17_RE_ Management Attestation – Data Integrity Validation Testing (November 2025 & February 2026 Exercises) 3 (1).msg.eml` | DMA03 | same email message saved as .eml |
| E17a | `BSI.IT.6.C7.3_E17a_4069_001.pdf` | DMA03a | byte-identical file (MD5 match) |

## Notes

- File names carry a reference prefix (MA/BLA/DMA/E) so each workpaper citation resolves to exactly one file. Original received names are recorded in the Evidence Index tab. `BSI In-Scope Applications-20206.png` was renamed to `MA01_BSI In-Scope Applications-2026.png` (year typo in the received name).
- E-numbers were kept stable after the duplicate removal (gaps at E11, E12, E14–E17 are intentional and logged above) so earlier references remain traceable.
- `Signed_Attestations_extracted` and `E07_/E08_Attachments_extracted` hold attachments extracted from the emails so they can be opened directly; they are not separate evidence items.
- E13 (11/13/2024) is prior-period and supplemental. DMA13 (Cisco Call Manager) is not one of the 10 tested applications.
- Observations raised in the workpaper: approval timing (33 of 56 records approved via retrospective attestation after 06/01/2026; 13 more confirmed retrospectively), self-approval in several business lines, BCiC data-entry inconsistencies (FedExport approval date, BSA T24 attestation date), blank Yes/No boxes on BLA02.
