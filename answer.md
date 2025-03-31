1. Giving Read-Only Access to S3 for a Group of Students in AWS IAM
To provide read-only access to S3 buckets for a group of students in AWS IAM, follow these steps:

Create a Group in IAM called S3ReadOnlyStudents.

Attach the AWS-Managed Policy called AmazonS3ReadOnlyAccess to this group.

Add Students to the Group, so they inherit the read-only permissions.

2. What is VPC and Its Use?
A VPC (Virtual Private Cloud) is a private network in AWS where you can launch resources like EC2 instances securely.

Use of VPC:

Isolates your cloud environment for security.

Allows you to define IP ranges and subnets.

Connects to the internet through a gateway or VPN.

Controls traffic using security groups and network ACLs.

3. What is the Use of an S3 Bucket?
Amazon S3 (Simple Storage Service) is used to store and retrieve any amount of data securely in the cloud.

Uses of S3 Bucket:

Stores files, images, videos, and backups.

Provides high availability and scalability.

Supports versioning to track changes.

Integrates with other AWS services (e.g., Lambda, CloudFront).


4. What is IAM Role?
An IAM Role is a permission set in AWS that allows AWS services or users to perform actions on your behalf.

Key Points:

Unlike IAM Users, roles do not have passwords or keys.

Temporary credentials are issued when needed.

Used for cross-account access, EC2, and Lambda.

Example: We can assign an IAM Role to an EC2 instance so it can access an S3 bucket without storing credentials in the instance

5. Difference Between Public and Private Subnets in AWS VPC

Public Subnets
The subnet that has a route table which contains a route to an Internet gateway is referred to as a Public subnet. EC2 instances that are started in a public subnet can access the internet directly and so is the appropriate place for resources that need to be available to the general internet population such as web servers.

Private Subnets
A private subnet is one that has no route to an Internet gateway The specific characteristic is that of having no path to the Internet Gateway. In private subnet, we have instances that are not exposed to the internet hence making it more secure. Individual subnets are normally utilized for systems, which do not require a connection with other systems from the Internet, for instance, databases or internal application servers.