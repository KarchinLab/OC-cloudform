# OpenCravat CloudFormation Pipeline
This project is a Cloudformation template for an automated AWS pipeline to run the OpenCravat software. This pipeline will take two input files and return all pertinent results to your selected s3 bucket.

What you'll need to get started:
- A configured AWS account with permissions to create EC2, S3, CF, and IAM Resources
- An existing s3 bucket to which you have write permissions
- At least one configured EC2 keypair inside of your AWS account
- Within that bucket should be an input file and a YAML file for OpenCravat configuration parameters
- Important note : this pipeline will incur cost on your amazon account and you are responsible for ensuring all components are deleted

To Do:
- Watch configured compute instance(s) for shutdown with AWS lambda and destroy stack when triggered
- Verify Metadata visuals not needed for CF pipeline
- Add multi-input processing path from single submission point
- Deploy the AMI to a multiple 