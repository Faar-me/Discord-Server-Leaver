import discord
import asyncio
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class ServerLeaver(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = None

    async def on_ready(self):
        print(f"{Fore.GREEN}[INFO] Logged in as: {self.user}{Style.RESET_ALL}")
        await self.show_menu()

    async def show_menu(self):
        print(f"\n{Fore.CYAN}{Style.BRIGHT}")
        print(r"""
  _____                                  _                                 
 / ____|                                | |                                
| (___    ___  _ __ __   __  ___  _ __  | |  ___   __ _ __   __  ___  _ __ 
 \___ \  / _ \| '__|\ \ / / / _ \| '__| | | / _ \ / _` |\ \ / / / _ \| '__|
 ____) ||  __/| |    \ V / |  __/| |    | ||  __/| (_| | \ V / |  __/| |   
|_____/  \___||_|     \_/   \___||_|    |_| \___| \__,_|  \_/   \___||_|   
                                                                           
                                                                           
        """)
        print(f"{Fore.YELLOW}==================={Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}1.{Style.RESET_ALL} {Fore.WHITE}Leave all servers where the bot is not the owner{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}2.{Style.RESET_ALL} {Fore.WHITE}Leave a specific server by ID{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}3.{Style.RESET_ALL} {Fore.WHITE}Exit{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}==================={Style.RESET_ALL}")

        choice = input(f"{Fore.WHITE}Enter your choice (1, 2, or 3): {Style.RESET_ALL}")

        if choice == '1':
            await self.leave_all_non_owned_servers()
        elif choice == '2':
            try:
                guild_id = int(input(f"{Fore.WHITE}Enter the guild ID: {Style.RESET_ALL}"))
                await self.leave_specific_server(guild_id)
            except ValueError:
                print(f"{Fore.RED}Invalid guild ID format. Please enter a numeric ID.{Style.RESET_ALL}")
        elif choice == '3':
            print(f"{Fore.YELLOW}Exiting...{Style.RESET_ALL}")
            await self.close()
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option.{Style.RESET_ALL}")
            await self.show_menu()

    async def leave_all_non_owned_servers(self):
        print(f"\n{Fore.CYAN}Starting to leave all non-owned servers...{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}======================================={Style.RESET_ALL}")

        for guild in self.guilds:
            if guild.owner_id == self.user.id:
                print(f"{Fore.YELLOW}Skipping server: {guild.name} (ID: {guild.id}) - User is the owner.{Style.RESET_ALL}")
                continue

            while True:
                try:
                    await guild.leave()
                    print(f"{Fore.GREEN}Successfully left server: {guild.name} (ID: {guild.id}){Style.RESET_ALL}")
                    await asyncio.sleep(5)  # Delay to avoid rate limits
                    break
                except discord.HTTPException as e:
                    if e.status == 429:  # Rate limit error
                        data = await e.response.json()
                        retry_after = data.get('retry_after', 5)
                        print(f"{Fore.YELLOW}[WARN] Rate limited. Retrying after {retry_after} seconds...{Style.RESET_ALL}")
                        await asyncio.sleep(retry_after)
                    else:
                        print(f"{Fore.RED}[ERROR] Failed to leave server {guild.name} (ID: {guild.id}): {e}{Style.RESET_ALL}")
                        break

        print(f"\n{Fore.CYAN}Finished processing all servers.{Style.RESET_ALL}")

    async def leave_specific_server(self, guild_id):
        guild = self.get_guild(guild_id)

        if not guild:
            print(f"{Fore.RED}Guild with ID '{guild_id}' not found.{Style.RESET_ALL}")
            return

        if guild.owner_id == self.user.id:
            print(f"{Fore.YELLOW}Cannot leave server: {guild.name} (ID: {guild.id}) - Bot is the owner.{Style.RESET_ALL}")
            return

        try:
            await guild.leave()
            print(f"{Fore.GREEN}Successfully left server: {guild.name} (ID: {guild.id}){Style.RESET_ALL}")
        except discord.HTTPException as e:
            if e.status == 429:  # Rate limit error
                data = await e.response.json()
                retry_after = data.get('retry_after', 5)
                print(f"{Fore.YELLOW}[WARN] Rate limited. Retrying after {retry_after} seconds...{Style.RESET_ALL}")
                await asyncio.sleep(retry_after)
                await guild.leave()  # Retry after waiting
            else:
                print(f"{Fore.RED}[ERROR] Failed to leave server {guild.name} (ID: {guild.id}): {e}{Style.RESET_ALL}")

def main():
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print(r"""
  _____                                  _                                 
 / ____|                                | |                                
| (___    ___  _ __ __   __  ___  _ __  | |  ___   __ _ __   __  ___  _ __ 
 \___ \  / _ \| '__|\ \ / / / _ \| '__| | | / _ \ / _` |\ \ / / / _ \| '__|
 ____) ||  __/| |    \ V / |  __/| |    | ||  __/| (_| | \ V / |  __/| |   
|_____/  \___||_|     \_/   \___||_|    |_| \___| \__,_|  \_/   \___||_|   
                                                                           
                                                                           
    """)
    print(f"{Fore.MAGENTA}Made by FAAR{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}==================={Style.RESET_ALL}")
    print(f"{Fore.BLUE}Enter Your Account Token: {Style.RESET_ALL}")
    token = input(f"{Fore.WHITE}Token: {Style.RESET_ALL}").strip()
    if not token:
        print(f"{Fore.RED}Token cannot be empty. Exiting...{Style.RESET_ALL}")
        return

    bot = ServerLeaver()
    bot.token = token
    bot.run(token, bot=False)

if __name__ == "__main__":
    main()
