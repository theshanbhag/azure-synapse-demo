## Azure synapse

Azure Synapse is an enterprise analytics service that accelerates time to insight across data warehouses and big data systems. Azure Synapse brings together the best of SQL technologies used in enterprise data warehousing, Spark technologies used for big data, Data Explorer for log and time series analytics, Pipelines for data integration and ETL/ELT, and deep integration with other Azure services such as Power BI, CosmosDB, and AzureML.



### Content:
1. What is synapse:
2. Data integration for batch and real time processing using MongoDB Atlas and Synapse.
3. Setup MongoDB Atlas cluster.
4. Create a Synapse workspace.
5. Batch:
   1. Create Synapse pipeline to load data from Atlas to Blob storage.
   2. Read Table data in Avro format.
   3. Integrate/enrich the data using Apache spark (Databricks).
   4. Sink - MongoDB atlas, Synapse SQL datawarehouse 


## Setup MongoDB Atlas cluster:
* Log-on to your Atlas account and Navigate to your project.

* Create a cluster if you don't have one. This demo will also work with a free tier cluster. (To use a dedicated cluster, Use GETATLAS promo code to get the free credits).

* Create a new user by navigating to Database Access -> Add user and add the admin role to the user.

* Create Ip address whitelist for your cluster by navigating to Network access (For the demo purpose you can whitelist 0.0.0.0/0 - Not recommended on production clusters).

* Create a database named mdb-retails.

* Navigate to your cluster and click on connect. Choose the Standard connection. Click on Connect to you Application and make note of your connection string i.e. required for running further steps in this demo.


## 2. Create a Synapse workspace.
* Log-on to your azure portal.
* Create a resource group by navigating to resource with name of your preference.
![](images/synapse-01.png)

* Create a Synapse Workspace to create your pipelines That will read the data from Atlas using Atlas source connector and store the data to Azure blob storage/ SQL.
![](images/synapse-02.png)
* To create resources in your resource group, Click on Create button as shown below.
![](images/synapse-03.png)
* Search for Azure synapse analytics and click on Azure synapse analytics as shown below.
![](images/synapse-04.png)
* Create Azure Synapse Analytics workspace. Fill out the required fields and click on *Review+Create*
![](images/synapse-05.png)
![](images/synapse-06.png)
* Post creation of Synapse workspace. Click on the *Open Synapse Studio*
![](images/synapse-07.png)
* Click on Integrate from side pane and click on + to create a new pipeline.
![](images/synapse-08.png)


### Batch :

### Real Time : 

