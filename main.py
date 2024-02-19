import requests

class Hostel:
    @staticmethod
    def login() -> None:
        pass

    @staticmethod
    def logout() -> None:
        pass

    @staticmethod
    def generate_headers() -> dict:
        # Too lazy to only include required headers
        return {
            "Host": "hfw.vitap.ac.in:8090",
            "Content-Length": "75",
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120"',
            "Sec-Ch-Ua-Platform": "Linux",
            "Sec-Ch-Ua-Mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Origin": "https://hfw.vitap.ac.in:8090",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://hfw.vitap.ac.in:8090/httpclient.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Priority": "u=1, i",
            "Connection": "close"
        }

class Campus:
    @staticmethod
    def login() -> None:
        pass

    @staticmethod
    def logout() -> None:
        pass

    @staticmethod
    def generate_headers() -> dict:
        pass

    @staticmethod
    def fetch_magic() -> str:
        pass

def main() -> None:
    pass

if __name__ == "__main__":
    main()