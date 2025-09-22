# Invoice Processing Pipeline on Azure  

## 📌 Project Overview  
This project demonstrates an **end-to-end invoice processing pipeline** built on **Azure cloud services**, designed to automate ingestion, transformation, and reporting of financial invoice data.  

The pipeline uses **Power Automate, SharePoint, Azure Data Lake Storage (ADLS Gen2), Azure Data Factory, Databricks, Synapse Analytics, and Power BI** to build a robust **ETL/ELT architecture** with Bronze–Silver–Gold layers, real-time triggers, and business-ready dashboards.  

---

## 🎯 Business Problem  
Finance and procurement teams often face challenges in **managing vendor invoices**:  
- Manual processing is slow and error-prone.  
- Invoices arrive in multiple formats (PDF, CSV, Excel).  
- Lack of central visibility on vendor spend, overdue payments, and SLAs.  

This pipeline automates the **end-to-end lifecycle**: from receiving invoices in email to delivering validated, aggregated, and analytics-ready data for decision-making.  

---

## 🔹 End-to-End Data Flow  

1. **Invoice Arrival (Source)**  
   - Vendors send invoices via email.  
   - Power Automate monitors Outlook → saves attachments to **SharePoint**.  

2. **Staging in SharePoint**  
   - Invoices centralized in an **Incoming Invoices folder**.  
   - Optional: consolidate multiple attachments into a single batch file.  

3. **Raw Zone – ADLS Gen2**  
   - Power Automate/Event Grid copies new files to **ADLS Gen2 Raw container**.  
   - Metadata (file name, size, source, timestamp) logged into **Azure SQL/Log Analytics**.  

4. **Cleansing & Structuring – Silver Zone**  
   - **Azure Data Factory** / **Databricks Autoloader** parses files.  
   - Schema normalization (invoice_id, vendor_id, amount, due_date, etc.).  
   - Deduplication, error handling, and validation.  
   - Cleansed data stored in **Parquet/Delta** format in Silver zone.  

5. **Business Transformations – Gold Zone**  
   - Aggregations: monthly spend, vendor totals, payment aging.  
   - Joins with **vendor master data** from SQL/ERP.  
   - Outputs business-ready datasets in Gold zone + **Synapse SQL Pool**.  

6. **Analytics & Reporting**  
   - **Power BI** dashboards for Finance & Procurement:  
     - Spend analysis  
     - On-time vs overdue payments  
     - Forecast trends  

7. **Automation & Monitoring**  
   - **Event Grid** triggers pipelines on file arrival.  
   - **Logic Apps / Power Automate** send alerts for failed loads or SLA breaches.  
   - **Azure Monitor + Log Analytics** track pipeline health & performance.  

8. **Optional Add-Ons**  
   - **OCR with Form Recognizer** → parse unstructured PDF invoices.  
   - **Purview** for data catalog & lineage tracking.  
   - **Key Vault** for secrets management.  
   - **Databricks ML** for predicting late payments.  

---

## 🛠️ Tech Stack  

- **Automation & Ingestion**: Power Automate, SharePoint, Event Grid  
- **Storage**: ADLS Gen2 (Bronze, Silver, Gold architecture)  
- **ETL/ELT**: Azure Data Factory, Databricks (Autoloader, Delta Lake)  
- **Analytics**: Synapse Analytics, Power BI  
- **Monitoring**: Azure Monitor, Log Analytics, Logic Apps  
- **Optional Enhancements**: Form Recognizer, Purview, Key Vault, ML (Databricks)  

---

## 🚀 Business Value  

- **Automation**: Eliminates manual invoice entry.  
- **Data Quality**: Cleanses and validates data with robust error handling.  
- **Scalability**: Event-driven, cloud-native architecture handles large invoice volumes.  
- **Insights**: Finance teams gain real-time dashboards for spend analysis, SLA monitoring, and payment forecasting.  
- **Extensibility**: Easily integrates with ERP systems (SAP, Dynamics, etc.).  

---

## 📊 Architecture Diagram  

<img width="768" height="59" alt="invoice_pipeline_diagram" src="https://github.com/user-attachments/assets/b6985d3e-3437-4b0c-b4c6-feee91f0e361" />


