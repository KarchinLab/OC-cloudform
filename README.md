# OC-cloudform
Cloudformation template for OpenCravat automated AWS pipeline

Pre-requisites:
- A configured AWS account with permissions to create EC2, S3, CF, and IAM Resources
- An existing s3 bucket in your account to which you have write permissions
- Within that bucket should be an input file and a YAML file for OpenCravat configuration parameters
- NB : this will create cost on your amazon account and you are responsible for ensuring all components are deleted

To Do:
- DONE - Make sure s3 tools are installed in the base image for initial file download
- Watch instance for shutdown and destroy stack when triggered
- Stress test the disk mounting path
- Verify Metadata visuals not needed for CF pipeline
- Add multi-input processing path
- make the ami multi-regional and autoselecting
