import tls_client
import time
import struct
import threading
from itertools import cycle
import ctypes

proxy = "http://infinix_admin:Exploit123$@infinixproxy.net:1337"

created = 0
deleted = 0
tags_found = 0

def title():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Exploit Guild Tag Creator | Created: {created} | Deleted: {deleted} | Tags Found: {tags_found}")


requests = tls_client.Session(client_identifier="chrome_120", random_tls_extension_order=True)


def get_headers(token):
    headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'deflate',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    'Authorization': token,
    # 'Content-Length': '57',
    'Content-Type': 'application/json',
    'Cookie': '__dcfduid=1b2aabd04ee611eeb0a30991a1bbba05; __sdcfduid=1b2aabd14ee611eeb0a30991a1bbba05c60f044166c2a47e3f39f190dc03a7e0280963208ce5b00182e92177369f8acf; _gcl_au=1.1.909415848.1697453399; __stripe_mid=ae87d2b5-0827-4ac5-bf9b-1ec2a49b5a363b20ee; __stripe_mid=7374c8a2-f321-48d4-8f8f-a249a3dbd76dff7890; _ga_Q149DFWHT7=GS1.1.1698078264.6.0.1698078264.0.0.0; _ga=GA1.2.1659610507.1697454578; OptanonConsent=isIABGlobal=false&datestamp=Fri+Nov+03+2023+10%3A40%3A56+GMT%2B0530+(India+Standard+Time)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; cf_clearance=DircLfF2pzD.eLsWsYSGTW5.t2jFuNsW0oqxxHUGwik-1701511014-0-1-7234bdef.20120ee1.2535e20f-0.2.1701511014; _cfuvid=kEOjr.SG95p9oXBbkwAzL5ngIV4e1lzxwBLO0BusEC4-1701612341161-0-604800000; __cfruid=89a1daa8d2263241e67b1b478426e02d4ba6b272-1701612345',
    'Dnt': '1',
    'Origin': 'https://discord.com',
    'Referer': 'https://discord.com/channels/@me',
    'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.309 Chrome/94.0.4606.81 Electron/13.5.1 Safari/537.36',
    'X-Debug-Options': 'bugReporterEnabled',
    'X-Discord-Locale': 'en-US',
    'X-Discord-Timezone': 'Asia/Calcutta',
    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE5LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjUwODMzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9'
}
    return headers


SERVER_NAME = "Tag server"
API_BASE = "https://discord.com/api/v9"


def murmurhash3_32(key, seed=0):
    key = bytearray(key.encode('utf-8'))
    c1 = 0xcc9e2d51
    c2 = 0x1b873593
    r1 = 15
    r2 = 13
    m = 5
    n = 0xe6546b64
    hash = seed
    length = len(key)
    rounded_end = (length & 0xfffffffc)  

    for i in range(0, rounded_end, 4):
        k = struct.unpack_from('<I', key, i)[0]
        k = (k * c1) & 0xffffffff
        k = ((k << r1) | (k >> (32 - r1))) & 0xffffffff
        k = (k * c2) & 0xffffffff

        hash ^= k
        hash = ((hash << r2) | (hash >> (32 - r2))) & 0xffffffff
        hash = (hash * m + n) & 0xffffffff

    k = 0
    val = length & 0x03
    if val == 3:
        k ^= key[rounded_end + 2] << 16
    if val in [2, 3]:
        k ^= key[rounded_end + 1] << 8
    if val in [1, 2, 3]:
        k ^= key[rounded_end]
        k = (k * c1) & 0xffffffff
        k = ((k << r1) | (k >> (32 - r1))) & 0xffffffff
        k = (k * c2) & 0xffffffff
        hash ^= k

    hash ^= length
    hash ^= (hash >> 16)
    hash = (hash * 0x85ebca6b) & 0xffffffff
    hash ^= (hash >> 13)
    hash = (hash * 0xc2b2ae35) & 0xffffffff
    hash ^= (hash >> 16)

    return hash

def create_guild(token):
    global created, deleted, tags_found
    print("Creating guild...")
    headers = get_headers(token)

    while True:
        try:
            res = requests.post(
                f"{API_BASE}/guilds",
                headers=headers,
                json={"name": SERVER_NAME}, proxy=proxy,
            )
            break

        except Exception as e:
            print(f"Error creating guild: {e}")

    if res.status_code != 201:
        print(f"Failed to create guild: {res.status_code} {res.text}")
    guild = res.json()
    guild_id = guild["id"]
    print(f"Guild created: {guild['name']} (ID: {guild_id})")
    created += 1
    title()


    tag = f"2025-02_skill_trees:{guild_id}"
    hash_value = murmurhash3_32(tag) % 10000

    if (10 <= hash_value < 20) or (60 <= hash_value < 100):
        print(f"🎉 FOUND GUILD WITH TAG! ID: {guild_id}")
        tags_found += 1
        title()
        with open("guilds.txt", "a") as f:
            f.write(f"{guild_id}:{token}\n")
    else:
        print(f"Guild (ID: {guild_id}) not in target experiment. Deleting ...")
        while True:
            try:
                del_res = requests.delete(f"{API_BASE}/guilds/{guild_id}", headers=headers, proxy=proxy)
                break
            except Exception as e:
                print(f"Error deleting guild: {e}")
        if del_res.status_code == 204:
            print(f"Guild {guild_id} deleted.")
            deleted += 1
            title()
        else:
            print(f"Failed to delete guild {guild_id}: {del_res.status_code} {del_res.text}")


tokens = cycle(open("tokens.txt").read().splitlines())
for _ in range(1000000):
    token = next(tokens)
    token = token.strip()
    if ":" in token:
        token = token.split(":")[-1]
    time.sleep(0.5)
    thread = threading.Thread(target=create_guild, args=(token,))
    thread.start()

