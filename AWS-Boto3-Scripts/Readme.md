# 🐍 AWS Infrastructure Automation with Python (Boto3)

This directory contains a collection of Python scripts to automate various AWS services using the **Boto3 SDK**. 

The goal is to move away from manual console actions and embrace **Infrastructure as Code (IaC)** principles.

## 🛠️ Prerequisites for all scripts
Before running any script in this folder, ensure you have the following setup:

1. **Install Boto3:**
   pip install boto3

2.Configure AWS Credentials (Important): You need to authenticate your local environment with AWS. Run the following command and enter your Access Key ID and Secret Access Key:

aws configure
AWS Access Key ID:  ****************
AWS Secret Access Key:  ****************
(Note: Ensure your IAM user has the required permissions, e.g., AmazonEC2ReadOnlyAccess).
