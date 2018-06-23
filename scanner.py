import os
from argparse import ArgumentParser

parser = ArgumentParser()

#parser.add_argument("-f", "--file", dest="filename", help="Dockerfile", metavar="FILE")
parser.add_argument("-i", "--image",
                    help="Docker image name with the tag", metavar="ubuntu:latest")
args = parser.parse_args()

docker_img = args.image

docker_run_cmd = "docker run  -u root  --rm -v $(pwd)/container_data:/container_data {} cp -rf /* /container_data".format(docker_img)
result_file_name = "result-"+docker_img
scan_cmd = "clamscan -r -i $(pwd)/container_data > {}".format(result_file_name)

os.system(docker_run_cmd)
os.system(scan_cmd)
print (open(result_file_name, 'r').read())