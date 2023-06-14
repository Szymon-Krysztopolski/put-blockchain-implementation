from user import User
import manager
import random

def get_users() -> list:
    return Users

def get_public_keys() -> list:
     return [user.get_public_key() for user in Users]

def generate_blocks(size: int) -> None:
     for _ in range(size):
          current_user = random.choice(Users)
          manager.add_block_to_blockchain(current_user, [current_user.get_username() + ": ------ " + element for element in random.sample(LOREM_IPSUM, random.randint(1, min(5, len(LOREM_IPSUM))))])

def get_lorem() -> list:
     return LOREM_IPSUM

LOREM_IPSUM = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "The quick brown fox jumps over the lazy dog.",
    "A picture is worth a thousand words.",
    "Actions speak louder than words.",
    "Beauty is in the eye of the beholder.",
    "Don't count your chickens before they hatch.",
    "Every cloud has a silver lining.",
    "Fortune favors the bold.",
    "Haste makes waste.",
    "Ignorance is bliss.",
    "Knowledge is power.",
    "Laughter is the best medicine.",
    "No pain, no gain.",
    "Opportunity knocks only once.",
    "Practice makes perfect.",
    "Time flies when you're having fun."
]

Users = [
    User("JohnDoe",
         "qwerty123",
         """
-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgGzAhzVh/7EtiYBQuQHseNAu6nEc
iEmIJvqvK4p3ff5+1PUXbTlu1OLZkHwH/JgmHokxxvhaznB1raCj6zCRUf3PYYQF
lpFJgsP7+PTO+JY0Shv8rhmkVoTfa2NKt2elJbntFPTE0UZJcG+xj77f7it6zFqz
KzQKFqchitn89bshAgMBAAE=
-----END PUBLIC KEY-----
         """,
         """
-----BEGIN RSA PRIVATE KEY-----
MIICWgIBAAKBgGzAhzVh/7EtiYBQuQHseNAu6nEciEmIJvqvK4p3ff5+1PUXbTlu
1OLZkHwH/JgmHokxxvhaznB1raCj6zCRUf3PYYQFlpFJgsP7+PTO+JY0Shv8rhmk
VoTfa2NKt2elJbntFPTE0UZJcG+xj77f7it6zFqzKzQKFqchitn89bshAgMBAAEC
gYA0fr8FireVPAj6knyrrA0pWOw8C2zSKdG/Al1/Kmz8Mxby9Ar6RUCn/CNda7GH
dCcbTJbh/VtXN8bHGzkFKbCstZ819z28MqxLC6lVnjELJM/7K9IYU5LaxVqTklJk
58Yo+JLl72067WF9TPD03YuBiE/Ji9LjkKq23XIYxm2J/QJBAKc9KipHZiAo4s+D
g4BzWIN4p8JCyp5iAXUjF68UOtagDeG/twMRULnxVkTZTu+RrSTNK8QGDQ9cPDzH
gDDYSLMCQQCmeLmFLV0OLFSN2Ld6mhu6fMrfxF0AWH/BeWJEaSbAmEMa/h2J63HD
rBpqoX72VqiH2dSWNQraqgrinnK1k07bAkA8bA7V46H0MJFxo/RY7lOmfGsv9m26
N3KLXbhq2wY/EOizDU8T3qep5pXinhi02Y8S4sXTNtR1Hj/tPa8E9r+dAkA5KatK
t9EEVOST8J7QUqrC1qczP1JQFBOKdAvyQck0yRQB6NBr05U1A5vukZXvMMKeI4aE
LaKUg19Jge8RuouRAkAZDGgZVJxM2KIW3rAK5/rGrVUhX7EK5mneZyGSyPzYjvSM
QYmXL4l8eJAwCn/XGYjMiF61lHJ4eOhly0ynQBCf
-----END RSA PRIVATE KEY-----
         """
         ),
    # ===========================================================================================================
    User("AliceWonder",
         "p@ssw0rd1",
         """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArUMJzYe6HLByTXEiSKaI
I+6ozt6+ilnMEAvCcwHNLIryQroVvOkeLOLr/lbI4xeXMLKjNpkba23y4S9hnNSb
aIb+C8vbV+T7bkeZ+5rucbmVUmuaasT8SMb1FUeH0HkFYYEYxF61W17ucsakuNqQ
Q8YDNY9ncK/gHqlBz3UaEQg53mrmPL8HW5Up+dcBon3yTV/RE/DyDDoF2CxI3mEg
JS3hQ3olZgsCiHyDEhIZVdbToUxC4PTtElHz9iioMqPreLpCxfVyNS8THQI9sTQ5
VVEBqBBcNHPx6G8VhWxjXNpywMVLpidGJRMuQPe2Fi9bI/yE5nT+4guae1ed6G1z
iQIDAQAB
-----END PUBLIC KEY-----
""",
         """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCtQwnNh7ocsHJN
cSJIpogj7qjO3r6KWcwQC8JzAc0sivJCuhW86R4s4uv+VsjjF5cwsqM2mRtrbfLh
L2Gc1Jtohv4Ly9tX5PtuR5n7mu5xuZVSa5pqxPxIxvUVR4fQeQVhgRjEXrVbXu5y
xqS42pBDxgM1j2dwr+AeqUHPdRoRCDneauY8vwdblSn51wGiffJNX9ET8PIMOgXY
LEjeYSAlLeFDeiVmCwKIfIMSEhlV1tOhTELg9O0SUfP2KKgyo+t4ukLF9XI1LxMd
Aj2xNDlVUQGoEFw0c/HobxWFbGNc2nLAxUumJ0YlEy5A97YWL1sj/ITmdP7iC5p7
V53obXOJAgMBAAECggEAGAoWIRs02mgs48vPqu7YMswZReKn40BETPGkwBo+4nBA
3rs86uIZWrb9cWOPKdsLEimm9ZtWr5gou8+8JmtlSKJ6Ox7ExzQxIoLyvXMopETQ
kAf3+9pq+poIRTSQhn9UHMwxqIVPemb4hJpFHpTMsWqW5WaJPpxYZ0iqpeMkg7o6
+ctvG04SS+I9S6AG0T5ahgCzOr/epJmmWlt3JuVGzhF8Tb0Am68IcxMPAGKYUY9X
DuSpn4wH2uPMWpgMlXuGNgbj4z5NpoJBfShBhorSMxQD9ri75lUMOtaFS/RpG1zO
/vokaBBPdtdyN5tlPU0DjVr2CuZPf8G0u/ezFQOxUQKBgQDahCbSqeBL0hG0z9ar
nJzd8FQDhlbWlAM7sioPM6cWsc6YU5FQfgaecoIOxgaNiZmmoekdA42XPMXM3+mB
J3sbaR2Vt964zr0uEkmkpFkY7xp2Ybe7cQapgMzcj7LVDRNxFOnfjZYOMMFsPAOl
4AtDBTVSyoXS93g3n8Oj0ybczQKBgQDK+5osNyQOydRICawIK72rQZ5HeTAZJdQc
5DgRkO0PPZc+X47JdOhRcfhBlH7X1gvG7zwrPHzjuuyLIiwk1ShtXgt9nNJe1ehH
w8DT3l1fPaNFkvXgRp+woePt1Tc7Q97tS1CWH5Xgj8HrfO0rh2nAC6zyCR4mB8Ph
gGBl8oMxrQKBgGpsHjRPQ8vpfXIgHx7pYYS9vU0SKkzLPV/ff5hzwZbN9h495PHc
zwBwKGNlkl9weoKrLEtTJaxYjsUe8CxUvCI3aY83Q6OiHITJp1AmMrZwDOVG5iLG
A0aeUifBXIlimutiEh0sab5zhGBgQi6RFSsI6FVwCQkcOVJt3ux0s+KpAoGBALl5
Zcr5J62LprmcfOGKdmlCMErG5bhU5JjxwHnsn3DJqqWH04Upmg6xwVLLSYwXPfOt
LqGjR8sfRn1r4EJXs/Ubdgx1e5TEiNbqfAwcp90bCVHNk3Y3kjtn8kmkBi/VOKJD
q4NBoUXslhmDsYOQ3IRrJsCSrEW72rT3BR6illaRAoGBALNSxv6o18Tx6FHMI6F0
binrPMFQWBT6iEladloDhPZ73PaCYMsu07t3hsFQtSSXGnTfQLDztd74DTx8wSew
ey4Qp8D+OjS7TLIXqBp7+9NvIkV1VwSyKmACv3bl7XCYZRvpPdC3kDXOSH1qJgxK
wRB+OLZoBvwjsbwYW3hshwR7
-----END PRIVATE KEY-----
"""
         ),
    # ===========================================================================================================
    User("BobRoss",
         "p@inting123",
         """
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCn5vKhhfZGVW+GAZkL1UwZF9Ic
3WVSu5M8UCjQcQ0LK8OpduIJjttD6/uLkejBWayZk7UZMgR1DP6sdKjjaO7sK+7m
GisbRtgTr5539SMd+Xldh2csBorkxmF0mthXAC65j58Am+BvAMBo93JF0B2yWZul
fM5YKG+9mjLsTFii3wIDAQAB
-----END PUBLIC KEY-----
         """,
         """
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQCn5vKhhfZGVW+GAZkL1UwZF9Ic3WVSu5M8UCjQcQ0LK8OpduIJ
jttD6/uLkejBWayZk7UZMgR1DP6sdKjjaO7sK+7mGisbRtgTr5539SMd+Xldh2cs
BorkxmF0mthXAC65j58Am+BvAMBo93JF0B2yWZulfM5YKG+9mjLsTFii3wIDAQAB
AoGBAJLq0TBpSiAtLhLyXvstvxLN9zrut3R3UdSax7vs0F8QAnvM3OlEKbT7TvbH
zAUz9IXF69eKHsBViJta0VV8QmLRi7UEgyrl+M1SpfGe2t/3m3SzpgSRXtgUBSO1
8saGaiBc5GoFrUL82yun19uiXSN0wPB6pRUTbvchQcDnhWvhAkEA9s3slxUsBcYr
67sFwK3ge22yuTBQGpfHuUQuflDEs1z8CqmkMiFCr9hwAGz2qgZuP/6cTJOn6SQw
MPEfI8YsqQJBAK4ob6ijGhiHLmGZu7Lji5FecJILJTUjIdLw+RmwLxxYSSTVVMv/
HUV6Le6IOgF0bJ3yQnJ6mSN7wOiLFXZ4QEcCQQCcJA+ITfa5+HQVAQ9UpSyeKfqm
OrCTAm9zAHXBqGupZix2uniM1ooQIghJ3KX5T3Q0vGo58DiMwT5T2FhxE5FxAkEA
mGeMZw/sO0C5BvIofoB/14PEkRktw1VuORFle+RhJbXgtFn3rdkfvXgRD+eokzNW
BdZF7bZ5osKeayGjc5wB6wJAcVv/uKsaiUNJcJrhizHzMhOHcubKqzCYqNZnoieG
p9M12HgeZbGtmsgi48XvJnPzPu813iCnp8/zNnttGlxlkg==
-----END RSA PRIVATE KEY-----
         """
         )
    # ===========================================================================================================
]

