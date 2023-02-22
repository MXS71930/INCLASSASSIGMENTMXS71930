import boto3
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('staticwebimage')

for bucket in s3.buckets.all():
 print(bucket.name)

