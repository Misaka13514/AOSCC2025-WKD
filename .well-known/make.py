#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p "python3.withPackages (ps: with ps; [ ])" -p gnupg

import sys
import json
import os

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = json.load(f)
        print(data)
        for key, value in data.items():
            for fingerprint in value:
                os.system(f"gpg --recv-keys --keyserver keyserver.ubuntu.com {fingerprint}")
                os.system(f"gpg --recv-keys --keyserver keys.openpgp.org {fingerprint}")
                os.system(f"gpg --list-options show-only-fpr-mbox -k {fingerprint} | gpg-wks-client -v --install-key")
