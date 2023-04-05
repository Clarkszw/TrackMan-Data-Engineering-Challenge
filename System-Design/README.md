# System-Design-Challenge

The TrackMan Data Engineering System Design Challenge aims to gauge your familiarity with designing cloud based applications and solutions.

This challenge is as much about the ability to communicate and justify the decisions as it is the specifics of the design itself.

## Data Lake Infrastructure

For this task, you will design a pipeline in AWS for ingesting data into a data lake in S3.

the existance of the following resources:

* A relation database called trackman-backend.
* An s3 bucket called trackman-lake.

do the following

* Read data from multiple different tables in trackman-backend.
* Ingest the data into a different relational database (dataengineering-db) which will be used as the backend for an internal application. You do not need to make considerations for what this application does.
* Load the data into trackman-lake in a suitable format.

## Answer

* A description of the solution approach taken.
* A description of each component. There is no need to provide code for any component, but for each that would contain code, you should give an overview of what the code would do any technical details about the implementation that you think are relevant.
* Any other notes that you think are valuable for us to know.

## requirements

* Is the solution fit for purpose?
* Scalability
* Maintainability
* Reliability
* Cost