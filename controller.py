from locker import locker_system
from time import sleep


def useLockerTest():
    print("testing")

    locker = "qkMOyDPLnlNYSihFOVDT"

    # Data from QR Code 
    user = "manueldiaz@csus.edu"
    # TODO: Get Locker ID from User Document
    locker_network = locker_system()
    locker_network.useLocker(locker, user)
    res = locker_network.isLockerInUse(locker, user)
    print(res)
    # sleep(2)
    locker_network.closeLocker(locker)
    # sleep(2)
    locker_network.openLocker(locker)


def main():
    locker = "qkMOyDPLnlNYSihFOVDT"
    user = "manueldiaz@csus.edu"
    locker_network = locker_system()

    # When a code is scanned, it will take the ID from the QR code and through it in 'user'.
    locker_network.useLocker(locker, user)


def mainMock():
    locker = "qkMOyDPLnlNYSihFOVDT"
    user = "manueldiaz@csus.edu"
    locker_network = locker_system()

    # When a code is scanned, it will take the ID from the QR code and through it in 'user'.
    print(locker_network.useLocker(locker, user))


# main()
# useLockerTest()
mainMock()
