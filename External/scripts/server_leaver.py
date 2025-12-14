import sys
import os
import threading

import curl_cffi.requests

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from Helper import (
    NexusColor,
    NexusLogging,
    Utils,
    HandleSetup,
    Discord,
    intro,
    fetch_session,
    pink_gradient,
)

class ServerLeaver():
    
    def __init__(self, useragent: str):
        self.session = curl_cffi.requests.Session(impersonate="chrome")
        self.useragent: str = useragent
        
        self.leave_count = 0
        self.error_count = 0
    
    def leave_server(self, token: str, guild_id: int) -> None:
        
        response = self.session.delete(
            f"https://discord.com/api/v9/users/@me/guilds/{guild_id}",
            json={"lurking": False},
            headers=Discord.fill_headers(token=token, user_agent=self.useragent)
        )
        
        if response.ok:
            NexusLogging.print_status(
                token=token,
                message=f"Left Server",
                color=NexusColor.GREEN
            )
            self.leave_count += 1
            return
        
        if response.status_code == 429:
            NexusLogging.print_status(
                token=token,
                message=f"Ratelimited",
                color=NexusColor.RED
            )
            self.error_count += 1
            return
        
        else:
            NexusLogging.print_error(
                token=token,
                message="Error while attempting to leave server",
                response=response
            )
            self.error_count += 1
            return
    
    def server_leaver(self, guild_id: int) -> None:
        threads = []
        for token in Utils.get_tokens(formatting=True):
            thread = threading.Thread(
                target=self.leave_server,
                args=(token, guild_id),
            )
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        print(
            f"\n{NexusLogging.LC} {NexusColor.LIGHTBLACK}Left Server: {NexusColor.GREEN}{self.leave_count}{NexusColor.LIGHTBLACK} | Error: {NexusColor.RED}{self.error_count}{NexusColor.RESET}"
        )
        input()
            
def main() -> None:    
    Utils.clear()
    Utils.new_title(
        "Server Leaver discord.gg/nexus-tools ┃ 1.0.0"
    )

    useragent = HandleSetup.fetch_user_agent()

    intro()
    
    guild_id = input(f"{NexusLogging.LC}{NexusColor.LIGHTBLACK} Guild ID: {NexusColor.NEXUS}")
    
    ServerLeaver(useragent=useragent).server_leaver(guild_id=guild_id)


if __name__ == "__main__":
    main()