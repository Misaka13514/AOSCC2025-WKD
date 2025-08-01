#! /usr/bin/env nix-shell
#! nix-shell -i python3 -p "python3.withPackages (ps: with ps; [ ])" -p gnupg

import sys
import json
import os

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        key_list = []
        data = json.load(f)
        print(data)
        for key, value in data.items():
            for fingerprint in value:
                key_list.append(fingerprint)
    
    key_string = " ".join(key_list)
    
    # 生成简化版本（只显示主UID）
    print("生成简化版本（只显示主UID）...")
    os.system(f"nix run github:cryolitia/nur-packages#pgp-sig2dot-graphviz --accept-flake-config -- -k {key_string} --online -p > wot.svg")
    
    # 生成完整版本（显示所有UID）
    print("生成完整版本（显示所有UID）...")
    os.system(f"nix run github:cryolitia/nur-packages#pgp-sig2dot-graphviz --accept-flake-config -- -k {key_string} --online > wot-full.svg")
