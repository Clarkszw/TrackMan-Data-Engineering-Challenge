# System Design Challenge

## Data Lake Infrastructure

### Components

* **AWS Glue**

    AWS Glue is a fully-managed extract, transform, and load (ETL) service that makes it easy to move data between data stores. I propose using AWS Glue as the primary ETL service in our pipeline. AWS Glue provides a simple and cost-effective way to crawl, transform and move data between relational databases and S3. It also has built-in support for parallelism and job scheduleing, which will help us to optimize the ETL process.

    AWS Glue job reads data from multiple tables in the trackman-backend database, The data is ingested into a relational database (dataengineering-db) through `AWS Database Migration Service(DMS)` within 30 minutes of its first insertion into trackman-backend.

    Another AWS Glue job transforms and loads the data into trackman-lake in a suitable formant within 1 hour of its first insertion into trackman-backend. `AWS Redshift` could be used as a data warehouse to make data available to analysts in the future.

    It's important to ensure that the AWS Glue jobs and DMS instances are properly configured to handle data from a production database. For example, AWS Glue job workers can be increased to handle larger datasets or parallel processing, and DMS can be configured to handle schema changes or schema mapping.

    It could be usefule to implement a monitoring and alerting system to ensure that data is being ingested, transformed, and loaded within the specified timeframes. For example, `Glue job bookmarks` can be used to keep track of the progress of a Glue ETL job. Bookmarks can be used to resume a job run from where it left off in case of a failure, and also to track the completion of a job run. Bookmarks can be queried using the AWS Glue API or console to build custom monitoring solutions.

* **AWS EC2**

* **AWS ESC**

* **AWS Redshift**

* **AWS Lambda**

    AWS Lambda is a serverless compute service that allow us to run code without provisioning or managing servers. I propose using AWS Lambda to trigger the ETL process whenever new data is inserted into the trackman-backend database. AWS Lambda will listen to the database for new data using a trigger, and then call the AWS Glue job to extract, transform, and load the data into the dataengineering-db and trackman-lake.

* **AWS Step Function**

    AWS Step Function is a fully-managed workflow service that makes it easy to build and run multi-step applications. i propose using AWS Step Functions to orchestrate the ETL process. The workflow will consist of multiple steps, including the ingestion data from the trackman-backend database, the transformation of data, and the loading of data into both dataengineering-db and trackman-lake. AWS Step Functions will provide us with a way to monitor the progress of the ETL process and handle any errors that occur.

* **Amazon S3**

    Amazon S3 is an object storage service that provides industry-leading scalability, data availability, security, and performance. I propose using AWS S3 as the primary data store for our data lake. The dataengineering-db will also store the ingested data for the internal application. AWS S3 will provide a scalable and cost-effective storage solution that can handle the growing volumn of data that will be ingested from variou sources in the furture.

### Aspects of the Solution

* To achieve high scalability, I recommend  

  * Partitioning the data in S3 based on the data and time of ingestion. This will help optimize queries and reduce the cost of scanning the entire dataset.
  * Using AWS EC2 instances to host the Glue jobs and DMS instances. EC2 instances can be easily scaled up or down based on the workload demands of the jobs.
  * Using AWS ECS to run the Glue jobs in containerized environments. This allows us to easily scale the jobs horizontally to handle larger data sets and processing loads.
  * Using AWS S3's built-in capabilities, such as enabling automatic multi-part uploads, increasing the number of storage buckets, or optimizing the storage configuration to scale the data lake horizontally.

* To achieve high reliability, I recommend

  * Designing the system with fault tolerance in mind. This means designing the pipeline to handle failure gracefully and automatically retrying failed operations. For example, using `AWS Glue Bookmarks` to keep track of the progress of a Glue ETL job.
  * Considering backup and disaster recovery solutions for the data lake and data warehouse to ensure data availability and continuity in case of any issues.
  * Considering monitoring and alerting using AWS CloudWatch to monitor the health of the Glue jobs and DMS instances, as well as the data lake and dataengineering-db. This allows us to proactively address any issues before they impact the end users.
  * Using AWS Elastic Load Balancers to distribute traffic across multiple instances of our Glue jobs and DMS instances, This ensures that if one instance fails, traffic can be automatically routed to a healthy instance without any service interruption.

* To achieve high maintainability, I recommend

  * Using a serverless architecture that reduces the need for manual intervention and maintenance.
  * Using Infrastructure as Code (IaC) to manage the AWS resources in a repeatable and consistent way. (AWS CloudFormation or Terraform)
  * Considering AWS CodePipline to automate the building, testing, and deployment of our Glue jobs and DMS instances. This ensures that the deployment process is consisitent, repeatable, and reliable.
  * Considering logging and tracing by AWS CloudTrail and AWS X-Ray to track and analyze te execution of our Glue jobs and DMS instances. This allows us to easily debug issues and optimize the performance of our data processing pipelines.

* Cost is a critical factor in any cloud-based solution, and I recommend designing the pipline to optimize cost. To optimize the cost of a pipeline, there are several best practices that can be followed:

  * Use cost-effective services: AWS offers a variety of services that are priced differently based on their features and usage. For example, choosing a more cost-effective data storage service, such as Amazon S3, instead of a more expensive database service can help to reduce costs. AWS Reserved Instances for the EC2 instances and Redshift cluster, S3 Glacier Deep Archive for infrequently accessed data, S3 intelligent-Tiering for data that has changing access patterns.

  * Right-size resources: Use resources that are appropriately sized for the workload. This means selecting resources that are neither too small nor too large for the workload, and that can efficiently handle the expected volume of data. For example, configuring Glue job workers to use minimum required hardware specifications to reduce compute costs, using spot instances for Glue job workers.

  * Leverage serverless architectures: AWS offers serverless architectures, such as AWS Lambda and AWS Step Function, that can help to reduce costs by allowing you to pay only for the compute time used.

  * Use monitoring and analysis tools: Use tools such as AWS Cost Explorer and AWS Trusted Advisor to monitor resource usage and identify cost-saving opportunities.

## Technical Requirements and Considerations

* trackman-backend is a production database, and in order to ensure high availability and prevent service interruptions, I recommend to use AWS Elastic Load Balancers to distribute traffic across multiple instances of Glue jobs and DMS instances. This will allow for automatic failover to healthy instances in the event of a failure, which will help to minimize any potential downtime. By using an Elastic Load Balancer, traffic can be balanced across multiple instances, which can improve the overall performance and reliability of the system. Additionally, Elastic Load Balancers can be configured to automatically scale up or down based on demand, which can help to optimize cost and ensure that the system can handle fluctuating workloads.

* To ensure data arrives in trackman-lake no later than 1 hour after it is first inserted into trackman-backend, we can schedule Glue jobs to run periodically (e.g. every 15 minutes) to check for new data in trackman-backend and load it into trackman-lake. We can also use Lambda functions to trigger Glue jobs in response to events, such as new data being inserted into trackman-backend.

* To ensure data arrives in dataengineering-db no later than 30 minutes after it is first inserted into trackman-backend, we can use DMS to replicate data from trackman-backend to dataengineering-db in near-real-time.

* To accommodate ingesting data from other data sources in the future, we can configure Glue jobs and DMS tasks to read from and write to multiple sources and destinations, respectively.

* To optimize costs, we can use AWS Cost Explorer to monitor and optimize our AWS costs. We can also leverage cost-saving strategies such as using reserved instances, spot instances, and auto-scaling to optimize our compute resources.