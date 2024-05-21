from argparse import ArgumentParser
from zipfile import ZipFile
from plistlib import loads
from colorama import Fore, Back, Style


HEADER = (
        '''
         ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░
         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░
         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░         ░▒▓█▓▒░
         ░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓█▓▒▒▓█▓▒░░▒▓██████▓▒░    ░▒▓█▓▒░
         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░         ░▒▓█▓▒░
         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░         ░▒▓█▓▒░
         ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓██▓▒░  ░▒▓████████▓▒░  ░▒▓█▓▒░
         by: @bsdrip
        '''
)


PERMISSIONS = [
    {
        'Bluetooth': [
            'NSBluetoothAlwaysUsageDescription',
            'NSBluetoothPeripheralUsageDescription',
        ],
    },
    {
        'Calendar and Reminders': [
            'NSCalendarsFullAccessUsageDescription',
            'NSCalendarsWriteOnlyAccessUsageDescription',
            'NSRemindersFullAccessUsageDescription',
        ],
    },
    {
        'Camera and Microphone': [
            'NSCameraUsageDescription',
            'NSMicrophoneUsageDescription',
        ],
    },
    {
        'Contacts': [
            'NSContactsUsageDescription',
        ],
    },
    {
        'Face ID': [
            'NSFaceIDUsageDescription',
        ],
    },
    {
        'Files and Folders': [
            'NSDesktopFolderUsageDescription',
            'NSDocumentsFolderUsageDescription',
            'NSDownloadsFolderUsageDescription',
            'NSNetworkVolumesUsageDescription',
            'NSRemovableVolumesUsageDescription',
            'NSFileProviderDomainUsageDescription',
        ],
    },
    {
        'Game Center': [
            'NSGKFriendListUsageDescription',
        ],
    },
    {
        'Health': [
            'NSHealthClinicalHealthRecordsShareUsageDescription',
            'NSHealthShareUsageDescription',
            'NSHealthUpdateUsageDescription',
            'NSHealthRequiredReadAuthorizationTypeIdentifiers',
        ],
    },
    {
        'Home': [
            'NSHomeKitUsageDescription',
        ],
    },
    {
        'Location': [
            'NSLocationAlwaysAndWhenInUseUsageDescription',
            'NSLocationUsageDescription',
            'NSLocationAlwaysUsageDescription',
            'NSLocationWhenInUseUsageDescription',
            'NSLocationTemporaryUsageDescription',
            'NSWidgetWantsLocation',
            'NSLocationDefaultAccuracyReduced',
        ],
    },
    {
        'Media Player': [
            'NSAppleMusicUsageDescription',
        ],
    },
    {
        'Motion': [
            'NSMotionUsageDescription',
            'NSFallDetectionUsageDescription',
        ],
    },
    {
        'Networking': [
            'NSLocalNetworkUsageDescription',
            'NSNearbyInteractionUsageDescription',
            'NSNearbyInteractionAllowOnceUsageDescription',
        ],
    },
    {
        'NFC': [
            'NFCTagReaderUsageDescription',
        ],
    },
    {
        'Photos': [
            'NSPhotoLibraryAddUsageDescription',
            'NSPhotoLibraryUsageDescription',
        ],
    },
    {
        'Scripting': [
            'NSAppleScriptEnabled',
        ],
    },
    {
        'Security': [
            'NSUpldateSecurityPolicy',
            'NSAppDataUsageDescription',
            'NSUserTrackingUsageDescription',
            'NSAppleEventsUsageDescription',
            'NSSystemAdministrationUsageDescription',
            'ITSAppUsesNonExemptEncryption',
            'ITSEncyptionExportComplianceCode',
        ],
    },
    {
        'Sensors': [
            'NSSensorKitUsageDescription',
            'NSSensorKitUsageDetail',
            'NSSensorKitPrivacyPolicyURL',
        ],
    },
    {
        'Siri': [
            'NSSiriUsageDescription',
        ],
    },
    {
        'Speech': [
            'NSSpeechRecognitionUsageDescription',
        ],
    },
    {
        'TV': [
            'NSVideoSubscriberAccountUsageDescription',
        ],
    },
    {
        'Vision': [
            'NSWorldSensingUsageDescription',
            'NSHandsTrackingUsageDescription',
        ],
    },
    {
        'Wallet': [
            'NSIdentityUsageDescription',
        ],
    },
    {
        'Wi-Fi': [
            'UIRequiresPersistentWiFi',
        ],
    },
    {
        'Deprecated Keys': [
            'NSCalendarsUsageDescription',
            'NSRemindersUsageDescription',
        ],
    },
]


DOMAIN_SETTINGS = [
    'NSIncludesSubdomains',
    'NSExceptionAllowsInsecureHTTPLoads',
    'NSExceptionRequiresForwardSecrecy',
    'NSExceptionMinimumTLSVersion',
    'NSExceptionRequiresForwardSecrecy',
    'NSExceptionAllowsInsecureHTTPLoads',
    'NSExceptionRequiresForwardSecrecy',
]


def print_red(text, header=False):
    if header:
        print(Back.WHITE)
    print(Fore.RED + text + Style.RESET_ALL)


def print_green(text, header=False):
    if header:
        print(Back.WHITE)
    print(Fore.GREEN + text + Style.RESET_ALL)


def print_blue(text, header=False):
    if header:
        print(Back.WHITE)
    print(Fore.BLUE + text + Style.RESET_ALL)


def print_yellow(text, header=False):
    if header:
        print(Back.WHITE)
    print(Fore.YELLOW + text + Style.RESET_ALL)


def extract_info_plist(ipa_file):
    with ZipFile(ipa_file) as ipa:
        info_plist = 'Payload/Info.plist'
        try:
            with ipa.open(info_plist) as plist_file:
                plist_data = plist_file.read()
                plist_dict = loads(plist_data)
                return plist_dict
        except KeyError:
            return None


def print_app_info(info_plist):
    print_blue('Application Information:', header=True)
    print_green(f'- Application Name: {info_plist.get("CFBundleDisplayName")}')
    print_green(f'- Bundle Name: {info_plist.get("CFBundleName")}')
    print_green(f'- Bundle Identifier: {info_plist.get("CFBundleIdentifier")}')
    print_green(f'- Bundle Version: {info_plist.get("CFBundleVersion")}')
    print_green(f'- Bundle Short Version String: {info_plist.get("CFBundleShortVersionString")}')
    print_green(f'- SDK Version: {info_plist.get("DTSDKBuild")}')
    print_green(f'- Minimum OS Version: {info_plist.get("MinimumOSVersion")}')
    print_green(f'- Architecture: {info_plist.get("UIRequiredDeviceCapabilities")[-1]}')
    print_green(f'- Associated Domains: {info_plist.get("ASSOCIATED_DOMAINS", "not set")}')
    print_green(f'- App Environment: {info_plist.get("ADJUST_ENV", "not set")}')

    print_red('Get \'Data Directory\' and \'Bundle Directory\' from \'igf\' logs')
    print()


def print_ats_settings(info_plist):
    print_blue('Application Transport Security (ATS) Settings:', header=True)
    if info_plist.get('NSAppTransportSecurity', {}).get('NSAllowsArbitraryLoads', False):
        print_green('- ATS Enabled: True')
    else:
        print_red('- ATS Enabled: False')
    if info_plist.get('NSAppTransportSecurity', {}).get('NSAllowsArbitraryLoads', False):
        print_blue('- ATS Exception Domains:')
        for domain, settings in info_plist.get('NSAppTransportSecurity', {}).get('NSExceptionDomains', {}).items():
            print_yellow(f'  - {domain}')
            for setting in DOMAIN_SETTINGS:
                if settings.get(setting, False):
                    print_green(f'    - {setting}: {settings.get(setting)}')
                elif settings.get(setting, True):
                    print_blue(f'    - {setting}: {settings.get(setting)}')
                else:
                    print_red(f'    - {setting}: {settings.get(setting)}')
    print()


def print_permissions(info_plist):
    print_blue('Application Permissions:', header=True)

    for permission in PERMISSIONS:
        for key, values in permission.items():
            print_yellow(f'- {key}')
            for value in values:
                if info_plist.get(value):
                    print_green(f'  - {value}: {info_plist.get(value)}')
                else:
                    print_blue(f'  - {value}: not set')
    print()


def main():
    parser = ArgumentParser(description='Extract values from an IPA file\'s Info.plist')
    parser.add_argument('ipa_file', help='Path to the IPA file')
    parser.add_argument('-i', '--info', help='Print application information', action='store_true')
    parser.add_argument('-a', '--ats', help='Print ATS settings', action='store_true')
    parser.add_argument('-p', '--permissions', help='Print permissions', action='store_true')
    parser.add_argument('-q', '--quiet', help='Do not print header', action='store_true')
    args = parser.parse_args()

    if not args.quiet:
        print(HEADER)

    info_plist = extract_info_plist(args.ipa_file)
    if info_plist:
        if args.info or not args.ats and not args.permissions:
            print_app_info(info_plist)
        if args.ats or not args.info and not args.permissions:
            print_ats_settings(info_plist)
        if args.permissions or not args.info and not args.ats:
            print_permissions(info_plist)
    else:
        print('No Info.plist found in the IPA file')


if __name__ == '__main__':
    main()
