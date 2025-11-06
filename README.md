# Intelligent Cloud Resource Optimizer  
### *Open FinOps Template for Cloud Cost Efficiency*  
---

## Tech Stack 
**Terraform · Python · GitHub Actions · FinOps Simulation**

---

## Overview  
This project provides a **ready-to-extend FinOps automation framework** that helps organizations **monitor, analyze, and optimize cloud spend**.  
Built using **Terraform, Python, and GitHub Actions**, it demonstrates how businesses can integrate **Infrastructure-as-Code (IaC)** with **cost optimization logic** for measurable savings and improved infrastructure efficiency.

---

## What It Does  
- **Detects idle or underutilized resources** based on usage metrics (simulated in this template).  
- **Automates scaling and deallocation** actions to reduce waste.  
- **Generates cost visibility reports** (before/after comparison).  
- **Runs continuously** via GitHub Actions or any CI/CD platform.  

---

## Architecture  
<div style="text-align: center;">
    <img src="Cloud Optimization Flowchart.png" alt="Flowchart">
</div>

## Running the Simulation 
```bash
git clone https://github.com/JaithraSarma/cloud-resource-optimizer.git

cd cloud-resource-optimizer

pip install -r requirements.txt

python scripts/optimizer.py
```

---

## Quick Start (For Implementation Purposes)

### 1. Fork this repository 
Adapt it for your cloud provider (Azure, AWS, or GCP). Your DevOps team can customize the Terraform configuration `(terraform/main.tf)` for Azure, AWS, or GCP.

```bash
git clone https://github.com/<your-org>/cloud-resource-optimizer.git
cd cloud-resource-optimizer
```

### 2. Create a Service Principal or Access Key
Replace simulation logic with your provider’s SDK (Azure SDK, boto3, or GCP SDK) and store keys securely as GitHub Secrets or via a Vault.
Example for Azure is as below:
```bash
az ad sp create-for-rbac \
  --name "cloud-optimizer" \
  --role Contributor \
  --scopes /subscriptions/<YOUR_SUBSCRIPTION_ID> \
  --sdk-auth
```
Copy these values:
- tenantId
- subscriptionId
- clientId
- clientSecret

### 3. Define Policies
In `scripts/optimizer.py`, tune thresholds:
```python
if avg_cpu < 15: stop_vm()
if storage_utilization < 25: move_to_cold_tier()
```
### 4. Schedule Optimization runs
Use GitHub Actions cron triggers

```yaml
on:
  schedule:
    - cron: "0 2 * * *"   # Run daily at 2 AM
```
### 5. Monitor Reports and review Cost insights 
Generated Artifacts can be integrated into dashboards like Grafana, Power BI, FinOps Hub.
```pgsql
Under Reports folder
cost_before.json
actions.json
cost_after.json
```
---

## Summary
An end-to-end FinOps automation pipeline showcasing cloud cost optimization concepts using DevOps best practices — designed to reflect real-world cloud efficiency strategies in a safe, simulated environment.



