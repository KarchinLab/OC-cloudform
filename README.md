# OpenCravat CloudFormation Pipeline
This project is a Cloudformation template for an automated AWS pipeline to run the OpenCravat software. This pipeline will take two input files and return all pertinent results to your selected s3 bucket.

What you'll need to get started:
- A configured AWS account with permissions to create EC2, S3, CF, and IAM Resources
- An existing s3 bucket to which you have write permissions
- At least one configured EC2 keypair inside of your AWS account
- Within that bucket should be an input file and a YAML file for OpenCravat configuration parameters
- Important note : this pipeline will incur cost on your amazon account and you are responsible for ensuring all components are deleted

To get started, click this link: ![CloudFormation Quick Start](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=OpenCravatRunner-v2&templateURL=http://oc-auto-wflow-testing.s3.amazonaws.com/oc-cf-template.yml "CF Quickstart" target="_blank")

At this first screen, you'll only need to confirm with the "Nex" button. The template selection and file locations have been processed with the link.

![First Screen](https://github.com/hynesgra/OC-cloudform/blob/master/images/First-Screen.png)

The second screen is where you will provide all necessary values for the pipeline run. The ImageID and machine type values will already be populated from default, but the rest will require completion. The InputFile and OCYMLFile values should be the names of files within your S3 bucket. 

If your files are nested in a within a "directory", that should be included in your OCS3Bucket values  "<bucket-name>/<folder-name>" 

If you don't see any values for keypairs, follow these instructions <insert link>

If you don't have an s3 bucket configured, follow these instructions <inssert link>



![Second Screen](https://github.com/hynesgra/OC-cloudform/blob/master/images/SecondScreen.png)

![Third Screen](https://github.com/hynesgra/OC-cloudform/blob/master/images/ThirdScreen.png)

![Fourth Screen](https://github.com/hynesgra/OC-cloudform/blob/master/images/FourthScreen.png)

To Do:
- Watch configured compute instance(s) for shutdown with AWS lambda and destroy stack when triggered
- Verify Metadata visuals not needed for CF pipeline
- Add multi-input processing path from single submission point
- Deploy the AMI to a multiple regions and make the template self selecting