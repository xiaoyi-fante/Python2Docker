import argparse
# import docker
import subprocess
import os


class Python2docker:

    # Generate the Docker run command
    def get_docker_command(self, name, age):
        age = str(age)
        x = 'echo Hi ' + name + ', age ' + age
        y = 'sleep ' + age + ';'
        z = 'docker run alpine:3 /bin/sh -c '
        command = z + '"' + y + x + '"'
        return command

    # Run the Docker command using os.popen
    def exec_docker(self, command):
        print('docker run ...')
        tmp = os.popen(command).readlines()
        tmp = "".join(tmp)
        return tmp

    # Get the running result of docker command
    def get_logs(self, name, age):
        command = self.get_docker_command(name, age)
        logs = self.exec_docker(command)
        return logs

# Parsing parameters from the command line
def get_parser():
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument('-n', '--name', required=True,
                        help="input the docker name")
    parser.add_argument('-a', '--age', type=int, required=True,
                        help="input the age that the docker will run")
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    name = args.name
    age = args.age

    python2docker = Python2docker()
    logs = python2docker.get_logs(name, age)
    print(logs)
