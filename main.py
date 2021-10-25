try:
  import os
  import discord
  import time
  from discord.ext import commands
except (ModuleNotFoundError):
  print("\u001b[38;5;45m-> \u001b[0mModules not installed.\n")
  input("\u001b[38;5;45m-> ");os._exit(0)

clear = lambda: os.system("cls; clear")

client = commands.Bot(
  command_prefix="Krypton#1337",
  intents=discord.Intents.all()
)

async def fetch(guild):
  x = client.get_guild(guild)
  try:
    os.remove("users.txt")

    with open("users.txt", "a") as i:
      for member in await x.chunk():
        i.write(f"{member.id}\n")
        print(f"\u001b[38;5;45m-> \u001b[0mFetched {member.id}.")
      i.close()
      print("\n\u001b[38;5;45m-> \u001b[0mFinished gathering IDs.")
    time.sleep(1.5)
    clear()
    await menu()
  except Exception:
    os._exit(0)
  

async def massdm(message): # <- Avoiding ratelimit is key.
  for x in open("users.txt"):
    member = await client.fetch_user(x)
    try:
      await member.send(message)
      print(f"\u001b[38;5;45m-> \u001b[0mSent the user {member} {message}.")
      print("\u001b[38;5;45m-> \u001b[0mSleeping for 2.5 seconds to avoid ratelimit.")
      time.sleep(2.5)
    except Exception as e:
      #print(f"\u001b[38;5;45m-> \u001b[0mException: {e}, press enter to continue.")
      #input()
      pass


async def menu():
  logo = """
\u001b[38;5;45m╔╦╗  ╔═╗  ╔═╗  ╔═╗  ╔╦╗  ╔╦╗
\u001b[38;5;51m║║║  ╠═╣  ╚═╗  ╚═╗   ║║  ║║║
\u001b[38;5;87m╩ ╩  ╩ ╩  ╚═╝  ╚═╝  ═╩╝  ╩ ╩"""
  for line in logo.split('\n'):
    print(line.center(100))
  print("""
\u001b[38;5;45m[ \u001b[38;5;87m-> \u001b[38;5;45m] \u001b[0mChoose a option below...
  \u001b[38;5;45m[ \u001b[38;5;87m1 \u001b[38;5;45m] \u001b[0m-> Gather Members
  \u001b[38;5;45m[ \u001b[38;5;87m2 \u001b[38;5;45m] \u001b[0m-> Mass DM
""")
  choice = int(input("\u001b[38;5;45m>> \u001b[0m"))

  if choice == 1:
    clear()
    guild = int(input("\u001b[38;5;45m-> \u001b[0mGuild ID?: "))
    await fetch(guild)
  elif choice == 2:
    clear()
    message = input("\u001b[38;5;45m-> \u001b[0mMessage To Send?: ")
    clear()
    await massdm(message)
    clear()
    await menu()
  else:
    clear()
    await menu()

@client.listen("on_connect")
async def ready():
  clear()
  await menu()

if __name__ == "__main__":
  clear()
  token = input("\u001b[38;5;45m-> \u001b[0mBot Token?: ")
  clear()
  try:
    client.run(
      token,
      bot=True
    )
    print("\u001b[38;5;45m-> \u001b[0mLoaded client.")
  except:
    print("\u001b[38;5;45m-> \u001b[0mSpecified invalid token.")
