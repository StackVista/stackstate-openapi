import boto3

# based on https://stackoverflow.com/questions/35803027/retrieving-subfolders-names-in-s3-bucket-from-boto3

#needed?
session = boto3.Session(
  aws_access_key_id='<your_access_key_id>',
  aws_secret_access_key='<your_secret_access_key>'
)

bucket = 'my-bucket'
# should end with /
prefix = 'dir_name/'
# should end with /
url = "http://link-to-s3-bucket/folder/"
s3 = boto3.client('s3')
result = s3.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')

# debug/test
# url = "http://link-to-s3-bucket/"
# result = ["4.0.0", "4.1.0", "4.2.0", "4.3.0" ]
# print(result)

folders = {}
for o in result.get('CommonPrefixes'):
  oname = o.get('Prefix’)
  olink = url + oname
  folders[oname] = olink

# debug/test
# for o in result:
#   oname = o
#   olink = url + oname
#   folders[oname] = olink
#   print(folders)

text_begin = '''
<html>
  <body>
    <h1>StackState OpenAPI documentation</h1>
    <p>Select a StackState version below to view the associated OpenAPI documentation.</p>
    <ul>
'''

text_end = '''
    </ul>
  </body>
</html>
'''

file = open("index.html","w")

file.write(text_begin)

for f in folders:
    line = f'      <li>OpenAPI docs for <a href="{folders[f]}">StackState version {f}</a></li>\n'
    file.write(line)

file.write(text_end)
