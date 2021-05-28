import argparse
import mcafee
import datetime
import getpass

def parseargs():
    parser = argparse.ArgumentParser(description= 'Consulta en el API de EPO una lista de usuarios y devuelve la lista de workstations en las que estos se loguean. By: Richard Arias Genao ;)', usage='%(prog)s [-h] [-i] [-o]')
    parser.add_argument('-i', help='-i <input file (user file)>')
    parser.add_argument('-o', help='-o <output file (workstations file)>, if not exist, create a new one')
    parseargs.args = parser.parse_args()



def EpoAuth():
    print('UserToPC, by Richard Arias Genao ;)')
    username = raw_input("Enter your EPO user: ")
    password = getpass.getpass(prompt='Password:', stream=None)

    #Authentication with McAfee EPO Api
    EpoAuth.mc = mcafee.client("co03vepo","8443",username,password,output='json')


def lookup():

    inputfile = open (parseargs.args.i,'r')
    outputfile = open (parseargs.args.o,'w')

    for line in inputfile:
        systems = EpoAuth.mc.system.find(line.rstrip('\n'))
        for system in systems:
            hostname = system['EPOComputerProperties.IPHostName']
            epotag = system['EPOLeafNode.Tags']

            if epotag != "Server":  # <-- If dont print servers
                print >> outputfile, hostname

    outputfile.close()
    inputfile.close()
    print('View your results at specified workstation list: '+parseargs.args.o)


parseargs()
EpoAuth()
lookup()

