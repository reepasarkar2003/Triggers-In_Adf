# Azure Pricing Calculator Configuration

This document provides detailed steps to configure the Azure Pricing Calculator for the given data integration scenario.

## 1. Azure Data Factory

### Configuration
- **Region**: East US
- **Data movement**: 85 GB per month
- **Number of pipeline activities**: Estimated based on workflow

### Steps
1. Go to the [Azure Pricing Calculator](https://azure.microsoft.com/en-us/pricing/calculator/).
2. Add "Azure Data Factory" to the calculator.
3. Select the region (e.g., East US).
4. Estimate the number of activities per month.
5. Input 85 GB for data movement per month.

## 2. Azure Data Lake Storage

### Configuration
- **Region**: East US
- **Storage capacity**: 170 GB (85 GB raw + 85 GB processed)

### Steps
1. Add "Azure Data Lake Storage Gen2" to the calculator.
2. Select the region (e.g., East US).
3. Input 170 GB for storage capacity.

## 3. Azure SQL Database or Azure Synapse Analytics

### Configuration
- **Region**: East US
- **Database service level**: As required
- **Storage**: 85 GB

### Steps
1. Add "Azure SQL Database" or "Azure Synapse Analytics" to the calculator.
2. Select the region (e.g., East US).
3. Configure the database service based on the required performance level.
4. Input 85 GB for storage.

## 4. Azure Blob Storage

### Configuration
- **Region**: East US
- **Archive storage capacity**: 85 GB

### Steps
1. Add "Azure Blob Storage" to the calculator.
2. Select the region (e.g., East US).
3. Input 85 GB for archive storage capacity.

## Azure Pricing Calculator Estimate

You can view the detailed cost estimate using the following link:
[Azure Pricing Calculator Estimate](https://azure.microsoft.com/en-us/pricing/calculator/)
