# for any questions see http://parallel-ssh.readthedocs.io/en/latest/index.html
# Github link: https://github.com/ParallelSSH/parallel-ssh

from pprint import pprint
from pssh.pssh_client import ParallelSSHClient
from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, \
  UnknownHostException, ConnectionErrorException
from password import username1, password1, password2

def telemetryServer(customCommand):
    config = {
        "hosts" : ['10.4.114.208', '10.4.115.111'],
        "user" : username1,
        "pass" : password1
    }
    mainServer(config,customCommand)

def rabbitmqServer(customCommand):
    config = {
        "hosts" : ['10.125.148.34', '10.125.148.35', '10.125.148.25'],
        "user" : username1,
        "pass" : password2
    }
    mainServer(config,customCommand)

def checkmkServer(customCommand):
    config = {
        "hosts" : ['10.125.148.32', '10.125.148.29', '10.125.148.33', '10.125.148.34', '10.125.148.35', '10.125.148.25', '10.125.148.30'],
        "user" : username1,
        "pass" : password2
    }
    mainServer(config,customCommand)

def mainServer(config,customCommand):
    telemetryClient = ParallelSSHClient(config["hosts"],user=config["user"],password=config["pass"])

    try:
        output = telemetryClient.run_command(customCommand,sudo=True)
    except (AuthenticationException, UnknownHostException, ConnectionErrorException):
        print("Some error in the script!!!")

    # In case the command is interactive(you need to enter password, yes/no etc)
    # then push the parameters in stdin object followed by "\n"
    for host in output:
        output[host].stdin.write(password2+"\n")
        #output[host].stdin.write("yes"+"\n")
        output[host].stdin.flush()

    for host in output:
        print(" ")
        print(host)
        print("-------------------------")
        for line in output[host].stdout:
            print(line)


#telemetryServer('lsb_release -a')
#rabbitmqServer('cat /etc/centos-release')
