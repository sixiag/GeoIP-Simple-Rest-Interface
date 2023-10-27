import argparse
import ipaddress
import json
import requests
import sys


class IPLookup:

    def __init__(self, api_key):
        self.api_key = api_key
        self.timeout = 10

    def get_location(self, ip):
        """ Get geolocation
        :param ip: IP address to query
        :return: dictionary with latitude and longitude data
        """
        url = "http://api.ipstack.com/{ip}?access_key={api_key}".format(
            ip=ip, api_key=self.api_key
        )

        resp = self.process_response(requests.get(url, timeout=self.timeout))
        if not resp:
            raise Exception(f"No information found for IP {ip}")

        return json.dumps({
            "latitude": resp.get("latitude", None),
            "longitude": resp.get("longitude", None)
        }, indent=2)

    def process_response(self, response):
        if response.status_code == 200:
            resp_json = response.json()

            if "error" in resp_json.keys():
                raise Exception("IPStack Error: " + resp_json["error"]["info"])
            return resp_json

        return None


def check_ip(ip):
    """
    Check if IP address is valid
    :param ip: IP to check
    :return: valid IP or raise exception
    """
    try:
        # create an ip_address object
        ipaddress.ip_address(ip)
        return ip
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid IP address: {ip}")


def parse_args(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--ip", required=True, type=check_ip, help="IP address to query.")
    parser.add_argument("-k", "--key", required=True, help="Your API key.")

    return parser.parse_args(args=argv)


def main(argv=None):
    args = parse_args(argv)

    gl = IPLookup(args.key)
    print(gl.get_location(args.ip))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
