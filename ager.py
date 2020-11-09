import argparse
# import docker
import subprocess
import os


class Python2docker:
    # Parsing parameters from the command line
    def get_parser(self):
        parser = argparse.ArgumentParser(description="Demo of argparse")
        parser.add_argument('-n', '--name', required=True,
                            help="input the docker name")
        parser.add_argument('-a', '--age', type=int, required=True,
                            help="input the age that the docker will run")
        return parser

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
        # print(command)
        tmp = os.popen(command).readlines()
        tmp = ".".join(tmp)
        return tmp

    # Get the running result of docker command
    def get_logs(self, name: str, age: int):
        command = self.get_docker_command(name, age)
        logs = self.exec_docker(command)
        return logs


if __name__ == '__main__':
    python2docker = Python2docker()
    parser = python2docker.get_parser()
    args = parser.parse_args()
    name = args.name
    age = args.age
    logs = python2docker.get_logs(name, age)
    print(logs)
