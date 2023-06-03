from aws_cdk import (
    core,
    aws_s3 as s3,
)
from azure_devops_utils import get_azure_devops_file_path


class MyStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket
        bucket = s3.Bucket(self, 'MyBucket',
                           bucket_name='cdkbucket',
                           # other bucket configuration options
                           )

        # Get the Azure DevOps file path
        azure_devops_file_path = get_azure_devops_file_path()

        # Add Azure DevOps file path as a tag
        core.Tags.of(bucket).add('AzureDevOpsFilePath', azure_devops_file_path)